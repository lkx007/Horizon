# Daily briefing / 每日简报

GitHub Actions workflow: [`.github/workflows/daily-summary.yml`](.github/workflows/daily-summary.yml).

定时工作流：[`.github/workflows/daily-summary.yml`](.github/workflows/daily-summary.yml)。

## Schedule / 时间

Every day, including Saturday and Sunday / 每天（含周末）, `timezone: "Asia/Shanghai"`:

| Slot | Asia/Shanghai | UTC | Cron | What it does |
| --- | --- | --- | --- | --- |
| Overnight / 凌晨 | **00:17** | 16:17 previous day | `17 0 * * *` | Early slot for the 08:30 mail window. GitHub schedule dispatch on this repo is about 6.5–8 hours late, and the job then finishes in about 5 minutes. 00:17 + 6.5h ≈ 06:47; 00:17 + 8h ≈ 08:17. Minute 17 stays off :00. |
| Morning / 早间 | **08:52** | 00:52 | `52 8 * * *` | Same-day catch-up. Skips Horizon when today's Asia/Shanghai `_posts/YYYY-MM-DD-summary-<lang>.md` files are already on `gh-pages`. |
| Midday / 午间 | **12:17** | 04:17 | `17 12 * * *` | Same-day catch-up. Skips Horizon when today's posts already exist. |
| Afternoon / 午后 | **15:23** | 07:23 | `23 15 * * *` | Same-day catch-up. Skips Horizon when today's posts already exist. |

00:17 是给 08:30 邮件留出的凌晨槽：GitHub 在这个仓库上的定时触发大约晚 6.5–8 小时，任务本身大约 5 分钟跑完。00:17 加上 6.5 小时约 06:47，加上 8 小时约 08:17。08:52、12:17、15:23 是同一天的补跑，只有当天（Asia/Shanghai）各语言的 Pages 帖子还没齐时才会调用 Horizon。

Pages posts (`docs/_posts/YYYY-MM-DD-summary-<lang>.md`), the `data/summaries/` digest files, and the Pages deploy `DATE` use the Asia/Shanghai calendar date. An overnight run still writes today's filename. A schedule slot skips only when every configured language post for Shanghai today is already on `gh-pages`. A slot that starts after Shanghai midnight generates Shanghai today when those posts are missing, and skips when they exist.

页面文件、`data/summaries/` 日报和 Pages 部署用的 `DATE` 都按 Asia/Shanghai 取日期，所以凌晨运行写的仍是当天文件名。定时槽位只在当天各语言帖子都已在 `gh-pages` 上时跳过。上海午夜之后才启动的延迟槽位：当天帖子已在就跳过，不在就生成当天，不会写成或跳过错误的一天。

`timezone: "Asia/Shanghai"` is honored. The 2026-11-09 runs were created at 07:16Z and 07:52Z, before 08:52 UTC, so those crons were not read as UTC. Moving the minute inside 00:xx UTC did not help (`38 0` → 07:20Z on 2026-11-05 and 07:18Z on 2026-11-06). The same 6.5–8 hour dispatch delay is why the overnight slot is 00:17 rather than a morning-only schedule.

`timezone: "Asia/Shanghai"` 会生效，不是被忽略。把分钟挪到 UTC 00 点内并不能消掉这几小时的延迟，所以用 00:17 提前触发，让晚到的运行仍然通常赶在 08:30 之前。

Manual run / 手动运行: **Actions → Daily Horizon Summary → Run workflow**. A manual run with both inputs left empty still generates Asia/Shanghai today, even if today's page already exists. / 两个输入都留空时，手动运行仍生成上海今天的日报，即使当天页面已经存在。

A `digest_date` other than Asia/Shanghai today does not call Horizon or DashScope. The job downloads that day's already published HTML and writes `previews/replay/<date>-ai-native.html` on the runner. It does not deploy to `gh-pages`. Live RSS is not a reconstruction of that day. The same guard is `horizon --digest-date YYYY-MM-DD --dry-run --from-published page.html`.

填了不是上海今天的 `digest_date` 时，任务不会调用 Horizon 或 DashScope，只下载该日已经发布的页面并在运行器里写出预览，不会部署到 `gh-pages`。今天的 RSS 不能当成那天的采集结果。

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
