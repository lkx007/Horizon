# Daily briefing / 每日简报

GitHub Actions workflow: [`.github/workflows/daily-summary.yml`](.github/workflows/daily-summary.yml).

定时工作流：[`.github/workflows/daily-summary.yml`](.github/workflows/daily-summary.yml)。

## Schedule / 时间

- Cron: `38 0 * * 1-5` (UTC). That is **08:38 Asia/Shanghai on weekdays** (UTC 00:38 Mon–Fri).
- 工作日北京时间 **08:38**（UTC 周一至周五 00:38）。GitHub 定时任务按 UTC 计算，实际开始时间可能略有延迟。
- Manual run / 手动运行: **Actions → Daily Horizon Summary → Run workflow**.

The job copies `data/config.github.json` to `data/config.json`, then runs `uv run horizon --hours 24`, and publishes `docs/` to the `gh-pages` branch.

## Model / 模型

`data/config.github.json` uses DeepSeek, the provider originally shipped upstream:

- `provider`: `deepseek`
- `model`: `deepseek-v4-flash`
- `base_url`: `https://api.deepseek.com`
- `api_key_env`: `DEEPSEEK_API_KEY`

Cursor dashboard API keys (`crsr_…`) cannot drive Horizon's LLM. Store a real DeepSeek key as the `DEEPSEEK_API_KEY` Actions secret.

Cursor 控制台的 `crsr_…` 密钥不能当作 Horizon 的对话模型密钥。请使用 DeepSeek 的 API key。

## Secrets

Add these under **Settings → Secrets and variables → Actions**. Do not commit keys.

在 **Settings → Secrets and variables → Actions** 添加，不要把密钥写进仓库。

| Secret | Needed | Why |
| --- | --- | --- |
| `DEEPSEEK_API_KEY` | Required / 必填 | Current provider is `deepseek` (`api_key_env`). Must be a real DeepSeek key, not a `crsr_…` Cursor key. |
| `LWN_KEY` | Optional / 可选 | LWN full-text feed is enabled in `config.github.json`. |
| `OPENAI_API_KEY` | Unused / 未使用 | Mapped only so a later provider switch does not require a workflow edit. |
| `ANTHROPIC_API_KEY` | Unused / 未使用 | Same as OpenAI. |
| `GOOGLE_API_KEY` | Unused / 未使用 | Same as OpenAI. |

Feishu is off, so `HORIZON_WEBHOOK_URL` is not used. Do not add `EMAIL_PASSWORD`; this job does not send SMTP mail.

## Delivery / 投递

This Actions job only publishes the Markdown summary to GitHub Pages. `webhook.enabled` is `false` (no Feishu / 飞书). Horizon email is not configured.

Gmail and QQ delivery, in the style of the old Researchy 日报, is a separate Grok Bot routine. That bot reads the published Pages summary (or the Markdown on `gh-pages`) and sends it. Do not turn on Horizon SMTP in this workflow for the first version.

本工作流只把日报发到 GitHub Pages。飞书已关闭，也不在 Actions 里配 Horizon 的 SMTP。Gmail 与 QQ 双通道由单独的 Grok Bot 读取已发布页面后再发送。

## GitHub Pages

1. **Settings → Pages**.
2. **Source**: Deploy from a branch / 从分支部署.
3. **Branch**: `gh-pages`, folder `/ (root)`.
4. Site / 站点: `https://lkx007.github.io/Horizon/`

The first successful run creates `gh-pages`. `keep_files: true` keeps older summary pages.
