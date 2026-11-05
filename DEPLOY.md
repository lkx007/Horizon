# Daily briefing / 每日简报

GitHub Actions workflow: [`.github/workflows/daily-summary.yml`](.github/workflows/daily-summary.yml).

定时工作流：[`.github/workflows/daily-summary.yml`](.github/workflows/daily-summary.yml)。

## Schedule / 时间

- Cron: `38 0 * * 1-5` (UTC). That is **08:38 Asia/Shanghai on weekdays** (UTC 00:38 Mon–Fri).
- 工作日北京时间 **08:38**（UTC 周一至周五 00:38）。GitHub 定时任务按 UTC 计算，实际开始时间可能略有延迟。
- Manual run / 手动运行: **Actions → Daily Horizon Summary → Run workflow**.

The job copies `data/config.github.json` to `data/config.json`, then runs `uv run horizon --hours 24`, and publishes `docs/` to the `gh-pages` branch.

## Secrets

Add these under **Settings → Secrets and variables → Actions**. Do not commit keys.

在 **Settings → Secrets and variables → Actions** 添加，不要把密钥写进仓库。

| Secret | Needed | Why |
| --- | --- | --- |
| `DEEPSEEK_API_KEY` | Required / 必填 | `data/config.github.json` uses the DeepSeek provider (`api_key_env`). |
| `HORIZON_WEBHOOK_URL` | Optional / 可选 | Feishu / 飞书 webhook. Omit it to publish Pages only. |
| `LWN_KEY` | Optional / 可选 | LWN full-text feed is enabled in `config.github.json`. |

`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, and `GOOGLE_API_KEY` are mapped by the workflow and are unused by the current GitHub config.

## GitHub Pages

1. **Settings → Pages**.
2. **Source**: Deploy from a branch / 从分支部署.
3. **Branch**: `gh-pages`, folder `/ (root)`.
4. Site / 站点: `https://lkx007.github.io/Horizon/`

The first successful run creates `gh-pages`. `keep_files: true` keeps older summary pages.
