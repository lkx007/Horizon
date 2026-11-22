---
layout: default
title: "Horizon Summary: 2026-11-23 (ZH)"
date: 2026-11-23
lang: zh
---

> 从 27 条内容中筛选出 13 条重要资讯。

---

**科技新闻**
1. [硅谷重心从信息导航转向 AI 驱动增长](#item-tech-news-1) ⭐️ 7.0/10
2. [Perplexity 作为 AI 智能评估指标引发 Hacker News 技术讨论](#item-tech-news-2) ⭐️ 7.0/10
3. [游戏《Worker755》：用户扮演大语言模型的子代理](#item-tech-news-3) ⭐️ 7.0/10
4. [Anthropic 2028 数据中心电力结构：87%天然气、11%煤炭](#item-tech-news-4) ⭐️ 7.0/10
5. [Muru：由 mod\_wsgi 创建者开发的 AI 辅助 Rust 版 Python Web 服务器](#item-tech-news-5) ⭐️ 7.0/10
6. [特斯拉开始推送全自动驾驶 FSD v15 版本](#item-tech-news-6) ⭐️ 7.0/10
7. [Google Gemini 新增独立开关：关闭训练数据留存但保留聊天历史](#item-tech-news-7) ⭐️ 7.0/10
8. [Phison 发布面向太空的 Pascari SSD 系列，488 TB 版本将用于 2027 年 StarVault-001 轨道数据中心](#item-tech-news-8) ⭐️ 7.0/10

**科技博客**
1. [写好代码的关键在于避免致命错误](#item-tech-blog-1) ⭐️ 8.0/10

**财经新闻**
1. [Eric Trump 支持的机器人初创公司停缴员工医保](#item-finance-news-1) ⭐️ 7.0/10
2. [英媒曝光英伟达芯片走私指控：柬埔寨太子集团人员被指涉对华走私](#item-finance-news-2) ⭐️ 7.0/10
3. [美股科技股暴跌引发亚洲多国紧急干预](#item-finance-news-3) ⭐️ 7.0/10
4. [超级厄尔尼诺海温破纪录，粮食援助承压](#item-finance-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [硅谷重心从信息导航转向 AI 驱动增长](https://www.oreilly.com/radar/what-happened-to-silicon-valley/) ⭐️ 7.0/10

本文是一篇反思性评论文章，追溯硅谷战略重心的历史演变：从 2000 年代初帮助用户应对信息爆炸、构建网络效应（如 Web 2.0 时期），转向当前以人工智能为杠杆、追求增长至上的商业模式。作者指出，零利率政策（ZIRP）时期助长了企业盲目扩张和初创公司回避成熟市场而追逐‘绿地’机会的倾向；如今利率回升，科技公司正以 AI 为名侵蚀自身核心能力。文章强调，这一转变根植于对资本主义本质的误读——将市场视为自然现象而非人类设计的机制，并质疑当前技术治理与注意力经济的设计前提。

hackernews · greenyouse · 11月22日 19:20 · [社区讨论](https://news.ycombinator.com/item?id=50602947)

**「背景」** 本文作者 Tim O&\#x27;Reilly 在 2005 年发表的《什么是 Web 2.0？》一文中，首次系统提出 Web 2.0 的核心特征，强调幸存于 dotcom 泡沫破裂的公司均通过帮助用户规模化应对信息爆炸而立足；该文援引赫伯特·西蒙 1971 年关于“信息丰富导致注意力稀缺”的论断，为后续注意力经济与平台设计逻辑奠定基础。

**「影响」** 对技术从业者和 AI 系统设计者而言，该文促使重新审视产品目标函数：若系统持续被优化以最大化短期股东价值或用户停留时长，而非人类注意力质量或长期福祉，则可能加剧现有平台失灵问题，例如内容同质化、决策代理弱化及组织能力空心化。

**「社区讨论」** 多位评论者认同文章对机制设计责任的强调，如\[Animats\]主张应将资本市场视为可重编程的人造系统，而非不可干预的自然力；\[CoolestBeans\]则补充指出 ZIRP 是导致当前 AI 滥用的直接诱因，而利率正常化正暴露其不可持续性。

**标签**: `#technology-industry`, `#capitalism-and-tech`, `#AI-strategy`, `#Web-2.0`, `#attention-economy`

---

<a id="item-tech-news-2"></a>
### [Perplexity 作为 AI 智能评估指标引发 Hacker News 技术讨论](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 7.0/10

一篇在 Hacker News 上被广泛讨论、题为《Perplexity and Intelligence》的文章（来源 URL 已失效，无法验证原文内容）提出困惑度（perplexity）应被更严肃地用作评估 AI 模型智能水平的指标。文章未明确定义困惑度，也未说明其报告的困惑度值所基于的具体数据集或任务分布，仅泛称其为‘内部指标’。社区评论指出，困惑度本质上是语言模型在给定序列上预测下一个 token 时的交叉熵损失指数化形式，理论取值范围为 1（完美预测）至词表大小（完全随机），但其解释力高度依赖于测试数据的代表性与任务相关性。

hackernews · acossta · 11月22日 17:06 · [社区讨论](https://news.ycombinator.com/item?id=50601525)

**「困惑度的定义与信息论基础」** 困惑度（perplexity）是信息论中用于衡量概率分布不确定性的指标，定义为分布熵的指数函数，数值越低表示模型对序列的预测越确定；在语言建模中，它等价于模型在给定训练数据上对下一个词元的平均预测难度。该指标长期作为评估语言模型拟合能力的核心指标，与交叉熵损失直接相关。

**「社区讨论」** 多位评论者质疑该提议的可操作性：有人指出文章未定义困惑度，有人强调‘困惑度在什么数据上计算’这一前提缺失即导致指标不可比；还有人观察到 GPT-4.5 在困惑度-能力关系图中呈现异常断点，但该现象未获原文解释，亦无独立数据佐证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.m.wikipedia.org/wiki/Perplexity">Perplexity - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI evaluation`, `#language modeling`, `#perplexity`, `#benchmarking`, `#Hacker News`

---

<a id="item-tech-news-3"></a>
### [游戏《Worker755》：用户扮演大语言模型的子代理](https://github.com/gulivan/worker755) ⭐️ 7.0/10

开发者 ivantgam 发布了开源浏览器游戏《Worker755》，玩家在游戏中作为受控于大语言模型（LLM）‘管理者’的子代理，通过执行命令、调用工具并观察 LLM 如何分配任务、解释输入和响应结果来互动。该游戏基于前端 JavaScript 实现，无需后端或远程 API，所有逻辑在本地浏览器中运行，当前版本为 GitHub 仓库 worker755 的初始公开发布。它不依赖外部 LLM 服务，也不支持接入本地运行的 LLM，其‘管理者’行为由预设规则与模拟逻辑驱动，而非真实推理模型。

hackernews · ivantgam · 11月22日 13:56 · [社区讨论](https://news.ycombinator.com/item?id=50599762)

**「背景」** 近年来，LLM 智能体（agent）架构研究兴起，其中‘分层代理’（hierarchical agents）和‘子代理’（subagents）概念被用于分解复杂任务，例如让主 LLM 调度多个专用子代理执行搜索、代码生成或文件操作。此前并无面向公众的交互式演示将人类置于子代理位置以直观体验该范式。

**「影响」** 教育者和初学者可借助该游戏快速建立对 LLM 代理系统中角色分工、指令歧义、工具调用边界及失败归因的具身认知，但因其完全模拟 LLM 行为，不能用于测试真实模型能力或部署实际自动化流程。

**「社区讨论」** 部分用户指出游戏中的‘管理者’倾向于直接给出完整命令（如 Seb0927 所提），削弱了自主决策挑战性；另有用户（boricj）明确表示希望支持本地 LLM 接入，当前设计未满足该需求。

**标签**: `#AI agents`, `#LLM architecture`, `#interactive learning`, `#AI safety`, `#prompt engineering`

---

<a id="item-tech-news-4"></a>
### [Anthropic 2028 数据中心电力结构：87%天然气、11%煤炭](https://betterdatacenterproject.com/2026/11/16/how-ai-is-powered-a-breakdown-of-byop-and-grid-power/) ⭐️ 7.0/10

根据 Better Data Center Project 于 2026 年 11 月发布的分析，Anthropic 公司预计其 2028 年数据中心电力供应中 87%将来自天然气、11%来自煤炭，仅约 2%来自可再生能源。该预测基于 Anthropic 已签约或规划中的数据中心（如田纳西州孟菲斯的 Colossus 1）所在电网的能源构成及购电协议现状，并非企业自主披露的官方承诺目标。数据反映的是实际供电结构而非企业宣称的‘碳中和’时间表，且未包含未兑现的长期可再生能源采购承诺。

hackernews · happosai · 11月22日 08:57 · [社区讨论](https://news.ycombinator.com/item?id=50597612)

**「背景」** Anthropic 的数据中心电力供应依赖外部电网，其 2028 年电力结构预测基于美国中南部电网（如田纳西河流域管理局 TV A 覆盖区）当前以化石燃料为主的发电组合；该预测并非 Anthropic 自建电厂（BYOP）的实测数据，而是对其所接入电网电力来源的建模估算。

**「影响」** 该电力结构意味着 Anthropic 的 AI 基础设施在 2028 年仍将高度依赖化石燃料，直接加剧本地空气污染（如孟菲斯社区报告的健康影响）和温室气体排放，使工程师与运维团队在设计高吞吐 AI 系统时面临真实且未被内部定价的环境外部性成本。

**「社区讨论」** 多位评论者指出 Anthropic 未在美国作出具约束力的可再生能源采购承诺，对比 Alphabet 等同行形成鲜明反差；\[contemporary343\]强调其租赁 Colossus 1 数据中心已导致孟菲斯当地污染恶化，而\[sollewitt\]则主张必须通过监管强制内化环境成本，否则负外部性将持续转嫁给远离决策中心的弱势社区。

**标签**: `#AI infrastructure`, `#sustainable computing`, `#energy policy`, `#corporate accountability`

---

<a id="item-tech-news-5"></a>
### [Muru：由 mod\_wsgi 创建者开发的 AI 辅助 Rust 版 Python Web 服务器](https://simonwillison.net/2026/Nov/21/muru/) ⭐️ 7.0/10

Graham Dumpleton（mod\_wsgi 的创建者）发布了 Muru，一个用 Rust 编写的新型 AI 辅助服务器，专为运行 Python WSGI 和 ASGI 应用程序设计，支持开发与生产环境。该项目于 2026 年 11 月 4 日起密集发布技术博文，涵盖工作进程模型、HTTPS 开发支持、WSGI/ASGI 共存、容器与 Kubernetes 集成、零扩缩（scaling to zero）、运行时热更新（releases not restarts）、灰度发布（canaries）、自动追踪与页面调试工具栏等特性。截至 2026 年 11 月 22 日，Muru 尚未发布可下载的稳定版本或公开的源码仓库（GitHub 页面仅显示占位符），所有信息均来自作者持续发布的开发日志，属于早期预研阶段项目。

rss · Simon Willison · 11月21日 23:56

**「背景」** mod\_wsgi 是由 Graham Dumpleton 于 2006 年开发的 Apache 模块，用于在生产环境中部署 Python WSGI 应用程序，已成为 Python Web 部署的长期事实标准之一。ASGI（Asynchronous Server Gateway Interface）是继 WSGI 之后为支持异步 Python Web 框架（如 FastAPI、Starlette）而提出的现代接口规范，但现有 ASGI 服务器（如 Uvicorn、Hypercorn）与传统 WSGI 生态的集成及运维体验仍存在割裂。

**标签**: `#Python`, `#Rust`, `#Web Servers`, `#ASGI`, `#Systems Engineering`

---

<a id="item-tech-news-6"></a>
### [特斯拉开始推送全自动驾驶 FSD v15 版本](https://x.com/Tesla/status/2124222447855743019) ⭐️ 7.0/10

特斯拉已在全球范围内向符合条件的海外用户推送全自动驾驶（FSD）v15 软件更新。该版本宣称将安全关键场景（如突发障碍物、复杂路口）的处理能力提升至 v14.4.x 的 25 倍，新增‘Tesla Reality View’增强现实界面，支持在车机屏幕实时叠加摄像头画面与车辆行驶路径规划，提供全屏、地图或分屏三种视图及可选的安静模式；同时优化了坑洼与路面碎片识别、学校区域及雨雪天气下的速度控制逻辑，并调整导航转向提示音与转向灯提示音为更轻柔且渐弱式播放。

telegram · zaihuapd · 11月22日 00:03

**「FSD v15 的技术基础」** FSD v15 是特斯拉基于端到端神经网络架构的全自动驾驶软件重大迭代，取代了此前依赖模块化感知-规划-控制流水线的 v12–v14 版本；该架构自 2024 年底起在部分北美车辆上进行有限测试，并于 2025 年初通过监管备案确认其作为 L2+ 系统的合规性。

**「影响」** 已订阅 FSD Beta 服务且车辆满足硬件要求（HW4 或部分 HW3+）的海外用户将逐步收到 v15 推送，但该版本仍属 L2 级辅助驾驶系统，不改变法定驾驶责任归属，用户须持续监控并随时接管；部分用户可能因区域监管限制（如欧盟尚未批准 Reality View 实时叠加功能）或车载硬件差异导致功能降级或延迟启用。

**标签**: `#autonomous-driving`, `#AI-systems`, `#human-computer-interface`, `#real-time-systems`

---

<a id="item-tech-news-7"></a>
### [Google Gemini 新增独立开关：关闭训练数据留存但保留聊天历史](https://blog.google/innovation-and-ai/products/gemini-app/updated-controls/) ⭐️ 7.0/10

Google Gemini 应用将在未来几周内推出两项独立设置：一项控制聊天历史的保存时长（默认约 2 个月），另一项单独控制用户对话内容（文字及附件）是否用于生成式 AI 模型训练；用户可选择关闭训练数据留存，同时继续保存聊天记录。该变更不适用于音频输入和 Gemini Live 功能，其录音默认不用于改进 Google 服务。变更生效时，新设置将根据用户当前“保留活动记录”开关状态自动同步初始化。

telegram · zaihuapd · 11月22日 01:24

**「背景」** 此前 Gemini 仅提供单一的“保留活动记录”开关，统一控制聊天历史保存与模型训练数据使用，缺乏对二者用途的区分授权。这一设计不符合 GDPR 等隐私法规对“目的限定”和“数据最小化”的要求，也难以满足用户对训练数据使用的明确知情与选择权。

**「影响」** 用户现在可依法行使更精细的数据权利——例如在保留个人对话历史用于自身回顾的同时，拒绝其被用于模型再训练，这直接支持了 GDPR 第 22 条关于自动化决策透明度及第 6 条关于合法处理依据的要求。

**标签**: `#AI ethics`, `#privacy engineering`, `#LLM deployment`, `#user consent`

---

<a id="item-tech-news-8"></a>
### [Phison 发布面向太空的 Pascari SSD 系列，488 TB 版本将用于 2027 年 StarVault-001 轨道数据中心](https://videocardz.com/newz/phison-announces-488tb-of-ssd-storage-for-space-data-centers-pricing-expected-to-be-astronomical) ⭐️ 7.0/10

Phison 已正式发布专为航天器、卫星及在轨数据中心设计的 Pascari Space SSD 系列，其中 488 TB 配置将集成于 Lonestar Data Holdings 的 StarVault-001 轨道数据中心，并计划于 2027 年上半年发射入低地球轨道；该配置标称容量 488 TB，入轨后可用容量约 370 TB；系列分 Flight Critical、Main Storage 和 Orbital Data Center 三类，单设备最高容量为 128 TB，部分型号采用 pSLC 模式，宣称写入寿命提升最高达 60 倍；产品已上市。

telegram · zaihuapd · 11月22日 10:31

**「背景」** Phison 此前已推出面向企业级数据中心的 Pascari 系列 SSD，主打高写入强度与大容量（如 Pascari Performance X-Series），但未专为太空环境设计；Lonestar Data Holdings 是一家专注轨道数据基础设施的美国初创公司，其 StarVault-001 是首个明确宣布将部署商用 SSD 存储的在轨数据中心项目，此前该公司曾通过 SpaceX Falcon 9 执行月球着陆任务（Lonestar Freedom Mission），并搭载了 Phison Pascari SSD 进行验证。

**「影响」** Lonestar 的 StarVault-001 成为首个公开确认部署商用固态硬盘的轨道数据中心，其依赖 Phison Pascari SSD 实现 370 TB 可用存储，意味着低轨边缘 AI/ML 数据处理对高可靠性、辐射硬化存储的实际需求已进入硬件交付阶段，但未披露具体耐辐射等级、温度适应范围或 MTBF 等关键可靠性指标，可能影响用户对长期在轨稳定性的评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phisonenterprise.com/">PASCARI by Phison : Redefining Enterprise Data Storage</a></li>
<li><a href="https://www.tweaktown.com/news/103564/phisons-new-pascari-enterprise-grade-ssd-launches-on-rocket-lands-the-moon-march-4/index.html">Phison &#x27;s new Pascari enterprise-grade SSD launches on a rocket...</a></li>

</ul>
</details>

**标签**: `#space computing`, `#SSD`, `#edge AI`, `#hardware reliability`, `#orbital infrastructure`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [写好代码的关键在于避免致命错误](https://seangoedecke.com/to-code-well-avoid-blunders/) ⭐️ 8.0/10

rss · Sean Goedecke · 11月22日 00:00

**「背景」** 在大型商业代码库中，代码质量的可持续性不取决于技术上的 brilliance，而在于系统性规避破坏一致性和引入冗余需求的致命错误——这类错误会迅速侵蚀团队信任与系统可维护性。

**「方案」** 作者提出核心策略：始终优先识别任务在现有代码库中最自然的落点，并将实现压缩至最小必要需求集；典型致命错误包括并行系统、多源真相、同步转异步的不当变更、新增隐性故障点及接口复杂化，其共性是制造不一致性或叠加不必要的约束；尤其强调‘不必要的需求’具有强粘性与组合爆炸效应——一旦存在，后续每个新功能都需考虑与其交互，显著抬高认知负荷；因此，工程师应将心智资源聚焦于防错而非炫技，警惕‘我可以用这个巧妙模式实现’这类念头，因其常预示注意力已偏离一致性与精简性这一主线。

**「启示」** 真正决定大型代码库长期健康度的，不是抽象的优雅或技术的巧妙，而是对一致性的严守和对冗余需求的持续剔除——这是一种可训练、可实践、且比‘聪明’更稀缺的工程纪律。

**标签**: `#software-engineering`, `#code-quality`, `#system-design`, `#engineering-culture`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [Eric Trump 支持的机器人初创公司停缴员工医保](https://www.cnbc.com/2026/11/22/foundation-future-industries-health-benefits-payroll-base-group.html) ⭐️ 7.0/10

Foundation Future Industries 因现金短缺，自 2026 年 10 月起停缴员工健康保险，并已连续三次未发放工资（最近一次发薪日为 10 月 15 日）；公司称将报销员工自行支付的 COBRA 保费，但未兑现。

rss · CNBC Finance · 11月22日 18:55

**「背景」** Foundation Future Industries 是一家由埃里克·特朗普支持并担任首席战略顾问的人形机器人初创公司，其联合创始人桑卡特·帕塔克此前创办的公司已于 2024 年倒闭。

**标签**: `#startup-failure`, `#employee-compensation`, `#corporate-governance`, `#venture-capital`, `#health-benefits`

---

<a id="item-finance-news-2"></a>
### [英媒曝光英伟达芯片走私指控：柬埔寨太子集团人员被指涉对华走私](https://www.ft.com/content/f3ad8a81-3890-4a8a-8853-ff0a94b08ba9?syn-25a6b1a6=1) ⭐️ 7.0/10

英国《金融时报》援引知情人士称，被美方列为制裁对象的柬埔寨太子集团“二号人物”胡小伟涉嫌参与将英伟达芯片经空壳公司和私人飞机走私至中国；报道称 2024 年 12 月至 2025 年 12 月，该集团关联的马来西亚子公司 Megaspeed 申报进口货物价值约 46 亿美元，部分芯片据称流入中国黑市，太子集团否认相关指控。

telegram · zaihuapd · 11月22日 04:34

**「背景」** 美国自 2022 年起严格限制向中国出口高端 AI 芯片（如英伟达 A100/H100），要求企业须获许可证，违者可能面临制裁。

**「影响」** 若指控属实，可能加剧美国对第三方国家中转半导体贸易的审查，并影响依赖非正规渠道获取先进芯片的中国 AI 企业和数据中心。

**标签**: `#semiconductors`, `#export-controls`, `#US-China-technology-rivalry`

---

<a id="item-finance-news-3"></a>
### [美股科技股暴跌引发亚洲多国紧急干预](https://news.bjd.com.cn/2026/11/22/12039852.shtml) ⭐️ 7.0/10

美国纳斯达克指数周五单日下跌 5.28%，费城半导体指数下跌近 11%；中国、韩国和中国台湾地区随即出台多项市场稳定措施。

telegram · zaihuapd · 11月22日 13:24

**「背景」** 此次暴跌由 AI 相关科技股大规模抛售引发，触发亚洲主要市场对系统性风险的快速响应。

**「影响」** 措施直接影响 A 股、韩股及台股的融资融券交易者、做市商、上市公司及衍生品发行人。

**标签**: `#US stock market`, `#Asian financial regulation`, `#tech sector volatility`, `#short-selling policy`, `#market intervention`

---

<a id="item-finance-news-4"></a>
### [超级厄尔尼诺海温破纪录，粮食援助承压](https://www.wired.com/story/how-this-years-super-el-nino-will-worsen-global-hunger/) ⭐️ 7.0/10

截至 2026 年 10 月，中热带太平洋海表温度较常年平均高 3.5℃，创历史纪录；世界粮食计划署（WFP）预计该超级厄尔尼诺将在 2027 年底前导致额外 4900 万人陷入急性粮食不安全。

telegram · zaihuapd · 11月22日 14:09

**「背景」** 厄尔尼诺是赤道太平洋海温异常升高的自然气候现象，强度通常以该区域海表温度距平（即偏离长期平均值的度数）衡量。

**「影响」** 全球粮食援助资金较 2022 年峰值下降 30%，已导致索马里等重灾国受援人数从 1000 万骤降至不足 100 万。

**标签**: `#climate-risk`, `#food-security`, `#humanitarian-aid`, `#macroeconomic-impact`, `#El-Nino`

---