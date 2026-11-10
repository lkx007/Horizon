# Daily briefing / 每日简报

GitHub Actions workflow: [`.github/workflows/daily-summary.yml`](.github/workflows/daily-summary.yml).

定时工作流：[`.github/workflows/daily-summary.yml`](.github/workflows/daily-summary.yml)。

## Schedule / 时间

Weekdays / 工作日, `timezone: "Asia/Shanghai"`:

| Slot | Asia/Shanghai | UTC | Cron | What it does |
| --- | --- | --- | --- | --- |
| Morning / 早间 | **08:52** | 00:52 Mon–Fri | `52 8 * * 1-5` | First attempt. Minute 52 avoids the top of the hour. A full run takes about 5 minutes, so an on-time start finishes near 08:57, before the ~09:15 mail routine. This UTC hour has been ~6.5h late on this repo. |
| Midday / 午间 | **12:17** | 04:17 Mon–Fri | `17 12 * * 1-5` | Catch-up outside the 00:xx and 01:xx UTC hours. Skips Horizon when today's `_posts/YYYY-MM-DD-summary-<lang>.md` files are already on `gh-pages`. |
| Afternoon / 午后 | **15:23** | 07:23 Mon–Fri | `23 15 * * 1-5` | Same-day catch-up in a later UTC hour, so a dropped morning slot can still publish by mid-afternoon. Skips Horizon when today's posts already exist. |

08:52 是早间第一次尝试，分钟设在 52；正常大约 5 分钟跑完，赶在约 09:15 的邮件检查之前。12:17 和 15:23 是同一天的补跑，只有当天各语言的 Pages 帖子还没齐时才会调用 Horizon。15:23（07:23 UTC）离开已经测到会晚约 6.5 小时的 00 点和 01 点 UTC。

`timezone: "Asia/Shanghai"` is honored. The 2026-11-09 runs were created at 07:16Z and 07:52Z, before 08:52 UTC, so those crons were not read as UTC. Moving the minute inside 00:xx UTC did not help (`38 0` → 07:20Z on 2026-11-05 and 07:18Z on 2026-11-06). The 09:07 Shanghai slot is 01:07 UTC; the second 2026-11-09 run was 07:52Z, still about six hours late, so that slot is gone. Do not move any trigger earlier than 08:00 Shanghai. Horizon names the page with the UTC date, so an on-time 07:xx Shanghai start would publish the previous day's filename.

`timezone: "Asia/Shanghai"` 会生效，不是被忽略。不要把触发改到北京时间 08:00 以前：Horizon 用 UTC 日期给页面命名，07:xx 会写成前一天。

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
