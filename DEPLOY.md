# Daily briefing / 每日简报

GitHub Actions workflow: [`.github/workflows/daily-summary.yml`](.github/workflows/daily-summary.yml).

定时工作流：[`.github/workflows/daily-summary.yml`](.github/workflows/daily-summary.yml)。

## Schedule / 时间

Weekdays / 工作日, `timezone: "Asia/Shanghai"`:

| Slot | Asia/Shanghai | UTC | Cron | What it does |
| --- | --- | --- | --- | --- |
| Primary / 主槽 | **08:52** | 00:52 Mon–Fri | `52 8 * * 1-5` | First attempt. Minute 52 avoids the top of the hour. A full run takes about 5 minutes, so an on-time start finishes near 08:57, before the ~09:15 mail routine. |
| Fallback / 补跑 | **09:07** | 01:07 Mon–Fri | `7 9 * * 1-5` | Runs only when today's `_posts/YYYY-MM-DD-summary-<lang>.md` files are not all already on `gh-pages`. 01:07 UTC is outside the overloaded midnight-UTC hour. An on-time start finishes near 09:12. |

08:52 是第一次尝试，分钟设在 52，躲开每小时开头；正常大约 5 分钟跑完，09:00 前结束。09:07 是补跑，只有当天各语言的 Pages 帖子还没齐时才会真正调用 Horizon，从而避开 DashScope 一天两次。01:07 UTC 不在最拥堵的午夜 UTC 小时里，正常大约 09:12 结束。

GitHub may still start a slot late. The earlier cron (`38 0 * * 1-5`, 08:38 Shanghai / 00:38 UTC) often never created a run: the 2026-11-05 schedule appeared 6h42m late, and the 2026-11-06 00:38 UTC slot created none. Do not move the trigger earlier than 08:00 Shanghai. Horizon names the page with the UTC date, so 07:xx Shanghai would publish the previous day's filename.

GitHub 仍可能晚点启动。原先的 `38 0 * * 1-5`（北京时间 08:38 / UTC 00:38）经常根本不创建 run。不要把触发改到北京时间 08:00 以前：Horizon 用 UTC 日期给页面命名，07:xx 会写成前一天。

Manual run / 手动运行: **Actions → Daily Horizon Summary → Run workflow**. A manual run always generates, even if today's page already exists. / 手动运行总会重新生成，即使当天页面已经存在。

The job copies `data/config.github.json` to `data/config.json`, then runs `uv run horizon --hours 24`, and publishes `docs/` to the `gh-pages` branch.

## Model / 模型

`data/config.github.json` uses Alibaba DashScope (通义, provider `ali`) through Horizon's OpenAI-compatible client. Model and endpoint match `AI_PROVIDER_DEFAULTS` for `ali`:

- `provider`: `ali`
- `model`: `qwen-plus`
- `base_url`: `https://dashscope.aliyuncs.com/compatible-mode/v1`
- `api_key_env`: `DASHSCOPE_API_KEY`

Cursor dashboard API keys (`crsr_…`) cannot drive Horizon's LLM. Store a DashScope API key from Alibaba Cloud / 百炼 as the `DASHSCOPE_API_KEY` Actions secret.

Cursor 控制台的 `crsr_…` 密钥不能当作 Horizon 的对话模型密钥。请使用阿里云百炼（DashScope）的 API key。

## Secrets

Add these under **Settings → Secrets and variables → Actions**. Do not commit keys.

在 **Settings → Secrets and variables → Actions** 添加，不要把密钥写进仓库。

| Secret | Needed | Why |
| --- | --- | --- |
| `DASHSCOPE_API_KEY` | Required / 必填 | Current provider is `ali` (`api_key_env`). DashScope API key from Alibaba Cloud / 百炼, not a `crsr_…` Cursor key. |
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
