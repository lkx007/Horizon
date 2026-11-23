"""CLI entry point for Horizon."""

import argparse
import asyncio
import shlex
import sys
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console

from ._cli import add_data_dir_arguments, add_log_level_argument
from .console_icons import get_icons
from .digest_date import digest_date_str
from .logging_config import configure_logging
from .replay import ReplayRefusal, resolve_cli_action
from .storage.manager import ConfigError, StorageManager
from .orchestrator import HorizonOrchestrator
from .models import AIProvider


console = Console(stderr=True)


def print_banner():
    """Print the application banner."""
    banner = r"""
[bold blue]
  _    _            _
 | |  | |          (_)
 | |__| | ___  _ __ _ ___  ___  _ __
 |  __  |/ _ \| '__| |_  / / _ \| '_ \
 | |  | | (_) | |  | |/ / | (_) | | | |
 |_|  |_|\___/|_|  |_/___| \___/|_| |_|
[/bold blue]
[cyan]  AI-Driven Information Aggregation System[/cyan]
    """
    console.print(banner)


def main():
    """Main CLI entry point."""
    configure_logging(console)
    print_banner()
    icons = get_icons()

    parser = argparse.ArgumentParser(description="Horizon - AI-Driven Information Aggregation System")
    parser.add_argument("--hours", type=int, help="Force fetch from last N hours")
    parser.add_argument(
        "--digest-date",
        default=None,
        metavar="YYYY-MM-DD",
        help=(
            "Label the output with this Asia/Shanghai date. "
            "A date other than today requires --dry-run and --from-published."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not write docs/_posts, publish, or send mail or webhooks.",
    )
    parser.add_argument(
        "--from-published",
        default=None,
        metavar="PATH",
        help="Published HTML page to replay. Required for a past --digest-date.",
    )
    parser.add_argument(
        "--preview-out",
        default=None,
        metavar="PATH",
        help="Where a published-page replay writes its HTML preview.",
    )
    add_data_dir_arguments(parser)
    add_log_level_argument(parser)
    args = parser.parse_args()

    configure_logging(console, level=args.log_level)

    try:
        action = resolve_cli_action(
            requested_date=args.digest_date,
            dry_run=args.dry_run,
            from_published=args.from_published,
            shanghai_today=digest_date_str(),
        )
    except ReplayRefusal as exc:
        console.print(f"[bold red]{icons['error']} {exc}[/bold red]")
        sys.exit(2)

    if action == "published-replay":
        from scripts.render_ai_native_preview import write_replay_preview

        destination = Path(
            args.preview_out
            or f"previews/replay-{args.digest_date}-ai-native.html"
        )
        write_replay_preview(
            published_html=Path(args.from_published),
            digest_date=args.digest_date,
            destination=destination,
        )
        console.print(
            f"[bold cyan]Replay preview written to {destination}.[/bold cyan]\n"
            "This is the published page plus the approved AI Native section. "
            "It did not fetch sources, call the model, send mail, or write gh-pages."
        )
        return

    try:
        # Load environment variables from .env file
        load_dotenv()

        data_dir = Path(args.data_dir)

        # Initialize storage manager
        storage = StorageManager(data_dir=str(data_dir), config_path=args.config)

        # Load configuration
        try:
            config = storage.load_config()
        except FileNotFoundError:
            console.print(
                f"[bold red]{icons['error']} Configuration file not found![/bold red]\n"
            )
            console.print(f"Expected config: [cyan]{storage.config_path}[/cyan]\n")

            example_path = data_dir / "config.example.json"
            if not example_path.exists():
                example_path = Path("data/config.example.json")
            if example_path.exists():
                target_parent = storage.config_path.parent
                if target_parent != Path("."):
                    console.print(
                        f"Create the destination directory:\n"
                        f"  [cyan]mkdir -p {shlex.quote(str(target_parent))}[/cyan]\n"
                    )
                console.print(
                    f"Copy the example config and edit it:\n"
                    f"  [cyan]cp {shlex.quote(str(example_path))} "
                    f"{shlex.quote(str(storage.config_path))}[/cyan]\n"
                )
            if args.config is None and data_dir == Path("data"):
                console.print(
                    "Or run [bold cyan]uv run horizon-wizard[/bold cyan] to launch the interactive setup wizard.\n"
                )
            sys.exit(1)
        except ConfigError as e:
            console.print(
                f"[bold red]{icons['error']} Error loading configuration: {e}[/bold red]"
            )
            sys.exit(1)
        except Exception as e:
            console.print(
                f"[bold red]{icons['error']} Error loading configuration: {e}[/bold red]"
            )
            sys.exit(1)

        icons = get_icons(config.display.icon_style)
        if config.ai.provider == AIProvider.OPENAI_CHATGPT:
            from .ai.chatgpt_auth import MANAGE_USAGE_URL
            console.print(f"Using ChatGPT plan. Manage usage: {MANAGE_USAGE_URL}")

        # Create and run orchestrator
        orchestrator = HorizonOrchestrator(config, storage, console=console)
        asyncio.run(
            orchestrator.run(
                force_hours=args.hours,
                digest_date=args.digest_date,
                dry_run=action == "live-dry-run",
            )
        )

    except KeyboardInterrupt:
        console.print(f"\n[yellow]{icons['warning']} Interrupted by user[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[bold red]{icons['error']} Fatal error: {e}[/bold red]")
        console.print_exception()
        sys.exit(1)


if __name__ == "__main__":
    main()
