# 2026-11-23 AI Native 补充阅读来源

检索日期：2026-11-23。方式：对每篇原文做公开 HTTP GET。三篇都不是当天 24 小时窗口里的新闻，也没有调用 DashScope，没有编造评分或日期。

## 预览里的三篇

### AI Native 产品设计

- 原文标题：Bitter lessons building AI products
- 作者：Olivia Koshy
- 页面日期：October 9, 2025
- URL：https://hex.tech/blog/bitter-lessons-building-ai-in-hex-product-management/
- 用了什么：2023 年 Notebook Agent 为了绕开模型缺陷而做的模板流程失败；后来改成围绕工具调用重做。
- 原文没有给出的：独立复现、“10 倍”和 Threads 工期的测量方法、Sonnet 3.5 的评测表。这些在预览里写成作者判断。

### 团队工作流与人机协作

- 原文标题：Our first outage from LLM-written code
- 作者：Josh Bleecher Snyder、Sean McCullough
- 页面日期：2025-07-31。文中故障发生在 7 月 15 日。
- URL：https://sketch.dev/blog/our-first-outage-from-llm-written-code
- 用了什么：人审过的智能体补丁把 Go 的 `break` 写成 `continue`，造成死循环和全表扫描。
- 原文没有给出的：剪贴板方案的量化结果。作者写的是还没有多少实际里程，初步看起来有希望。

### 落地案例、方法与失败教训

- 原文标题：Dead Ends or Data Goldmines? Investment Insights from Two Years of AI-Powered Postmortem Analysis
- 作者：Dmitry Kolesnikov，Senior Principal Engineer
- 页面日期：Posted on Sep 25, 2025
- URL：https://engineering.zalando.com/posts/2025/09/dead-ends-or-data-goldmines-ai-powered-postmortem-analysis.html
- 用了什么：摘要、分类、分析、模式、机会五段流水线和 map-fold；人工抽查从 100% 降到每批 10–20%。
- 原文给出、但是内部观察：3B–12B 幻觉最高约 40%，人工筛选后低于 15%；Claude Sonnet 4 上表面归因仍约 10%；S3 相关洞察“能够挡住后续 25% 的数据存储事故”没有对照实验设计。预览把后者标成作者对内部回报的说法。

## 当天没有 RSS 的页面

探测于 2026-11-23：

- Hex 的 `/blog/rss.xml`、`/rss.xml`、`/blog/feed` 返回 404。
- `https://sketch.dev/feed.xml` 返回 HTML，不是 feed。
- Anthropic engineering 页面没有可用的 RSS。

所以这三篇只出现在本地预览，不会被当天的采集任务自动抓到。

## 已接入、并在 2026-11-23 用 feedparser 打开的订阅

这些源使用 `ai-native` profile，阈值 7.0，不做话题去重。栏目由分析标签决定，不把整份订阅锁死在一个栏目里。只有发布落在 24 小时窗口、并且通过评分的文章，才会出现在以后的日报里。

| 订阅 | URL | 抽查时看到的最新一条 |
| --- | --- | --- |
| Eugene Yan | https://eugeneyan.com/rss/ | How Public Evals Work and Fail, and What Should Change，Thu, 19 Nov 2026 |
| Hamel Husain | https://hamel.dev/index.xml | How To Use Decision Models for Evals，Tue, 20 Oct 2026 |
| Phil Calçado | https://philcalcado.com/feed.xml | Building AI Products—Part II，Fri, 14 Mar 2025 |
| Zalando Engineering | https://engineering.zalando.com/atom.xml | Upgrading MLflow Pipelines Across a Python Version Boundary，2026-10-30 |
| Chip Huyen | https://huyenchip.com/feed.xml | Common pitfalls when building generative AI applications，Thu, 16 Jan 2025 |
