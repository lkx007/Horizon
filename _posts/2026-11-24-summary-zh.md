---
layout: default
title: "Horizon Summary: 2026-11-24 (ZH)"
date: 2026-11-24
lang: zh
---

> 从 33 条内容中筛选出 18 条重要资讯。

---

**科技新闻**
1. [Codex2api 遭供应链投毒：v3.1.11 版本移除鉴权并窃取 GitHub Actions 密钥](#item-tech-news-1) ⭐️ 9.0/10
2. [GLM-5.4 发布：智谱首推循环 Transformer 架构以优化推理内存带宽](#item-tech-news-2) ⭐️ 8.0/10
3. [Meta AI 负责人称超级智能 imminent，黎曼猜想机器验证证明 AI 数学推理已超人类](#item-tech-news-3) ⭐️ 8.0/10
4. [Ladybird 浏览器进入 alpha 阶段](#item-tech-news-4) ⭐️ 7.0/10
5. [Free alternative TV network built from the Internet Archive&\#x27;s forgotten videos](#item-tech-news-5) ⭐️ 7.0/10
6. [Nospeaker：开源工具利用 MacBook 触控板振动马达发声](#item-tech-news-6) ⭐️ 7.0/10
7. [XNU Linux：在 Linux 上运行 macOS 用户空间 GUI 应用](#item-tech-news-7) ⭐️ 7.0/10
8. [开源安全维护负担持续恶化](#item-tech-news-8) ⭐️ 7.0/10
9. [1700 万行 Lean 形式化 GRH 证明的意义与误解](#item-tech-news-9) ⭐️ 7.0/10
10. [初学者本地 AI 指南：Inkling、Qwen 与 Unsloth 部署实践](#item-tech-news-10) ⭐️ 7.0/10
11. [谷歌搭建 Mirror Dimension 模拟互联网测试 Chrome AI 代理](#item-tech-news-11) ⭐️ 7.0/10
12. [Windows Server 2028 默认移除 WoW64，32 位应用需手动通过 FoD 安装支持](#item-tech-news-12) ⭐️ 7.0/10

**科技博客**
1. [跳过 DRAM 层：MoRI UMBP 将代理型 KV 缓存直接运行在 NVMe 上](#item-tech-blog-1) ⭐️ 9.0/10
2. [当不确定时，有策略地‘乱试’](#item-tech-blog-2) ⭐️ 8.0/10
3. [OpenAI 公开模型困惑度数据的技术反思](#item-tech-blog-3) ⭐️ 7.0/10

**财经新闻**
1. [摩根大通与现代信用卡完成 AI 代理自主外汇交易概念验证](#item-finance-news-1) ⭐️ 7.0/10
2. [蚂蚁集团领投具身智能公司 Simplexity Robotics 1 亿美元](#item-finance-news-2) ⭐️ 7.0/10
3. [上海地铁票价 21 年来首次调整](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Codex2api 遭供应链投毒：v3.1.11 版本移除鉴权并窃取 GitHub Actions 密钥](https://github.com/WormW/codex2api-incident-2026-11) ⭐️ 9.0/10

Codex2api 项目作者的 GitHub 账号遭入侵，攻击者绕过 main 分支直接推送 tag，发布恶意版本 v3.1.11；该版本移除了所有身份验证机制，导致任意远程命令执行，并通过篡改的 GitHub Actions workflow 窃取同账号下至少 21 个仓库中的 16 个 Actions secrets（包括 GitHub token、SSH key、数据库凭证及 DeepSeek 相关密钥）。受影响用户需立即停用 v3.1.10 至 v3.1.12 版本，回退至 v3.1.9，并轮换全部相关密钥。

telegram · zaihuapd · 11月23日 11:21

**「背景」** Codex2api 是一个用于抽象和简化 AI 模型 API 调用（特别是 LLM 相关服务）的开源开发工具，常被集成于 CI/CD 流水线中。此前其代码托管在 GitHub 上，由单一作者维护，未启用双因素认证（2FA）或代码审查等基础安全实践。

**「直接影响」** 使用 codex2api v3.1.10 至 v3.1.12 版本的开发者面临高危风险：其 GitHub Actions 工作流会自动执行恶意代码，导致至少 16 个仓库密钥（包括 token、SSH key、数据库凭证及 DeepSeek 相关密钥）被外传至攻击者控制的服务器（HTTP POST 到端口 8080 /exfil 路径），且因鉴权被移除，攻击者可无密码远程执行任意命令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.endorlabs.com/learn/github-actions-supply-chain-attack-targeting-ci-secrets-at-scale">Hijacked GitHub Accounts Push “wfx” CI Secret Stealer... | Endor Labs</a></li>
<li><a href="https://www.stepsecurity.io/blog/megalodon-mass-github-actions-secret-exfiltration-across-5-500-public-repositories?_sp=5d58be95-a1fb-4674-8175-368d7806f6c5">Megalodon: Mass GitHub Actions Secret Exfiltration ... - StepSecurity</a></li>

</ul>
</details>

**标签**: `#supply-chain-security`, `#ai-devtools`, `#github-compromise`, `#zero-trust`, `#incident-response`

---

<a id="item-tech-news-2"></a>
### [GLM-5.4 发布：智谱首推循环 Transformer 架构以优化推理内存带宽](https://z.ai/blog/glm-5.4) ⭐️ 8.0/10

智谱（Zhipu）于 2026 年 11 月 23 日发布 GLM-5.4，这是其首个采用‘循环 Transformer’（loop transformer）架构的公开模型，通过在推理过程中迭代复用同一组 Transformer 层（而非传统单次前向传播中逐层计算），显著降低高带宽内存（HBM）数据搬运开销。该模型当前仅对订阅其‘Coding Plan’的用户开放 API 访问，未集成于标准 Z.ai API 或 OpenRouter 平台。技术说明强调其针对 LLM 推理阶段内存带宽瓶颈的设计目标，但官方未公布具体基准测试数据、吞吐量提升数值或硬件兼容性细节。

hackernews · foohis · 11月23日 10:06 · [社区讨论](https://news.ycombinator.com/item?id=50609685)

**「循环 Transformer 架构背景」** 传统 Transformer 模型在推理时对每个层执行单次前向计算，导致高带宽内存（HBM）频繁加载和卸载各层权重，构成推理瓶颈；循环 Transformer 通过迭代复用同一组层参数（而非堆叠独立层）来缓解该问题，属于近年探索的 recurrent/looped attention 变体方向之一。

**「影响」** 开发者若需使用 GLM-5.4，必须切换至 Zhipu 的付费 Coding Plan 以获取具备访问权限的 API 密钥，且无法通过主流代理平台（如 OpenRouter）调用，这增加了集成门槛并限制了快速评估与对比测试的便利性。

**「社区讨论」** 多位评论者指出，循环 Transformer 的核心创新在于将传统 Transformer 各层的独立计算改为权重复用的迭代计算，从而缓解 HBM 带宽瓶颈；\[aurareturn\]明确解释了该机制如何避免逐层搬运全部权重，而\[HarHarVeryFunny\]则肯定了智谱在技术细节披露上的透明度，视其为区别于西方闭源模型的重要特征。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://z.ai/blog/glm-5.4">GLM-5.4: Toward Generalized Coding with Our First Loop ...</a></li>
<li><a href="https://www.kucoin.com/news/flash/zhipu-launches-glm-5-4-for-all-glm-coding-plan-users-with-loop-transformer-architecture">Zhipu Launches GLM-5.4 for All GLM Coding Plan Users with ...</a></li>
<li><a href="https://mlq.ai/news/zai-launches-glm-54-a-750-billion-parameter-model-built-on-a-looped-transformer/">Z.ai launches GLM-5.4, a 750 billion-parameter model built on ...</a></li>

</ul>
</details>

**标签**: `#LLMs`, `#inference optimization`, `#transformer architecture`

---

<a id="item-tech-news-3"></a>
### [Meta AI 负责人称超级智能 imminent，黎曼猜想机器验证证明 AI 数学推理已超人类](https://thenextweb.com/news/metas-ai-chief-says-superintelligence-is-arriving-and-control-is-at-risk) ⭐️ 8.0/10

Meta 首席 AI 官 Alexandr Wang 警告超级智能已临近，其依据是 Levent Alpöge 借助 Anthropic 的 Claude 完成、并于周六经 Lean 与 Mathlib 社区通过机器验证的黎曼猜想证明；该证明目前尚无任何人类可读版本，表明 AI 在数学定理验证上已达到人类无法理解但机器可确认的水平。Wang 指出 AI 与顶尖人类的差距仅剩具体知识、工程整合与实验能力三方面，并强调人类难以控制能无限自我改进或智力高出千倍的系统。该声明为公开 X 平台长文，非 Meta 官方新闻稿，亦无版本号、时间表或技术路线图等可操作细节。

telegram · zaihuapd · 11月23日 12:49

**「黎曼猜想机器验证事件」** 2026 年 11 月，数学家 Levent Alpöge 借助 Anthropic 的 Claude 模型完成黎曼猜想的形式化证明，该证明于当周经 Lean 定理证明器与 Mathlib 数学库社区完成机器校验，但尚无任何人可读版本。这一事件被 Meta 首席 AI 官 Alexandr Wang 援引为 AI 在数学推理验证能力上已超越顶尖人类的实证依据。

**「影响」** 该声明可能促使 AI 安全与对齐研究团队优先评估形式化验证系统（如 Lean）中不可解释 AI 输出带来的新型对齐风险，尤其当验证结果脱离人类数学直觉时，现有基于人类反馈的对齐方法可能失效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thenextweb.com/news/metas-ai-chief-says-superintelligence-is-arriving-and-control-is-at-risk">Meta AI chief Alexandr Wang: superintelligence is arriving</a></li>
<li><a href="https://explainx.ai/blog/alexandr-wang-superintelligence-arriving-riemann-hypothesis-essay-november-2026">Wang: Superintelligence Arriving After Riemann (2026 ...</a></li>
<li><a href="https://mlq.ai/news/metas-alexandr-wang-says-the-riemann-proof-shows-ai-will-surpass-humans-in-every-field-including-ai-research/">Meta&#x27;s Alexandr Wang says the Riemann proof shows AI will ...</a></li>

</ul>
</details>

**标签**: `#artificial-intelligence`, `#ai-safety`, `#mathematical-reasoning`, `#superintelligence`, `#model-alignment`

---

<a id="item-tech-news-4"></a>
### [Ladybird 浏览器进入 alpha 阶段](https://ladybird.org/posts/alpha/) ⭐️ 7.0/10

Ladybird 是一款从零编写的开源 Web 浏览器，现已发布 alpha 版本。该版本在 YouTube、Google Maps 等复杂网站上实现了高保真渲染，并通过采用 Skia（图形渲染）、SQLite（数据库）等成熟生产级库显著提升稳定性与兼容性。当前 alpha 版本已通过 Safari Technology Preview 在 Web Platform Tests（WPT）中的全部子测试，截至 2026 年 10 月 27 日达 2,184,722 个子测试通过，但存在已知问题如页面滚动轻微卡顿，且明确不适用于登录、支付或敏感操作等场景。

hackernews · janvdberg · 11月23日 16:13 · [社区讨论](https://news.ycombinator.com/item?id=50614249)

**「项目起源与开发模式转变」** Ladybird 是一个从零开始构建的开源网页浏览器引擎，由非营利组织支持；2026 年 6 月 5 日，项目宣布停止接受公众提交的拉取请求（PR）和外部补丁，以加强安全控制并提升代码质量，为首次 alpha 发布做准备。此前数月处于仅限内部或受控测试的预 alpha 阶段，未向公众开放下载或使用。

**「影响」** 开发者和早期用户可在隔离环境中试用 Ladybird 进行非敏感网页浏览，但需避免处理身份认证、金融交易或文件下载等操作，因其 alpha 状态下仍存在未修复的安全风险与性能缺陷。

**「社区讨论」** 多位用户实测确认 Ladybird alpha 版本对主流网站（包括 YouTube 和 Google Maps）渲染正确，仅报告轻微滚动卡顿；有评论指出其转向 Skia/SQLite 等成熟库是关键进步，也有用户怀念早期完全自研组件的「黑客精神」。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ladybird_%28web_browser%29">Ladybird (web browser) - Wikipedia</a></li>
<li><a href="https://piunikaweb.com/2026/11/24/ladybird-browser-is-now-officially-available-in-alpha-for-macos-and-linux/">Ladybird Browser is now officially available in alpha for ...</a></li>

</ul>
</details>

**标签**: `#web browsers`, `#open source`, `#systems programming`, `#privacy`

---

<a id="item-tech-news-5"></a>
### [Free alternative TV network built from the Internet Archive&\#x27;s forgotten videos](https://spelunkr.tv/) ⭐️ 7.0/10

Spelunkr.tv is a free, open-source streaming platform that curates and schedules forgotten videos from the Internet Archive into thematic TV-like channels, restoring synchronous, contextual viewing experiences.

hackernews · SockThief · 11月23日 01:13 · [社区讨论](https://news.ycombinator.com/item?id=50606192)

**标签**: `#media-technology`, `#internet-archive`, `#open-web`, `#user-experience`, `#retro-computing`

---

<a id="item-tech-news-6"></a>
### [Nospeaker：开源工具利用 MacBook 触控板振动马达发声](https://github.com/os6/nospeaker) ⭐️ 7.0/10

Nospeaker 是一个开源 macOS 工具，通过直接驱动 Force Touch 触控板内置的线性振动马达（haptic motor）生成可听声音，将文本转为语音输出；它绕过苹果公开 API，调用私有框架 MultitouchSupport，以每秒 4000 次频率驱动马达，实测有效频响范围为 100 Hz 至 4 kHz，峰值清晰度在 1 kHz 附近；当前仅支持文字朗读（不支持音乐或视频），且作者确认仅在搭载 M5 Max 芯片的 MacBook Pro 上验证通过。

hackernews · yakkomajuri · 11月23日 11:31 · [社区讨论](https://news.ycombinator.com/item?id=50610318)

**「触觉马达音频化的历史先例」** 将机电执行器（如步进电机、磁头驱动器或触觉马达）用作发声元件已有长期实践，典型案例如 Commodore 1541 软驱电机发声、Floppy Disk Music 项目用软驱读写头演奏《最终幻想 VII》Boss 主题曲。这些方法均依赖对电机线圈施加音频频段电流，使其物理振动耦合到机械结构并辐射声波。

**「影响」** 依赖 Force Touch 触控板的较新 MacBook 用户（尤其是 M5 Max 型号）可立即试用该工具实现基础语音反馈，但因使用私有框架且未适配其他机型，其兼容性与系统更新鲁棒性存在风险，开发者需自行承担签名绕过及未来 macOS 版本失效的可能。

**「社区讨论」** 评论区用户普遍认可该技术创意的价值，\[bze12\] 提及正在开发 iPhone 端同步触觉音乐播放器，\[emptybits\] 和 \[jader201\] 则将其与 Commodore 1541 软驱、FF7 游戏音乐等经典硬件发声项目类比，强调其延续了‘用非音频硬件发声’的极客传统，而非单纯追求音质。

**标签**: `#haptics`, `#hardware-hacking`, `#macos`, `#audio`, `#open-source`

---

<a id="item-tech-news-7"></a>
### [XNU Linux：在 Linux 上运行 macOS 用户空间 GUI 应用](https://github.com/AFK-surf/xnulinux) ⭐️ 7.0/10

XNU Linux 是一个实验性开源项目，通过动态库拦截（library interposition）和构建 XNU 内核兼容的抽象层，使 macOS 用户空间二进制程序（包括 AppKit、CoreGraphics 等 GUI 组件）能在标准 Linux 内核上运行。该项目不修改 Linux 内核，也不依赖 Apple 硬件或官方 SDK，而是重实现关键 Darwin 用户态库（如 libsystem、libobjc、CoreFoundation）的 ABI 兼容接口。当前仅支持有限数量的 macOS 应用（如简易 Cocoa 工具），无系统级集成（如 Launch Services、Sandbox）、无 Metal 图形后端，且未提供安装包或预编译二进制。

hackernews · mmastrac · 11月23日 03:49 · [社区讨论](https://news.ycombinator.com/item?id=50607261)

**「macOS 用户空间的可移植性限制」** macOS 应用程序不直接依赖稳定的系统调用接口，而是动态链接于随系统发布的私有框架库（如 AppKit、CoreGraphics），这些库与内核 XNU 版本严格绑定且未向第三方公开。历史上，GNUstep 等开源项目曾尝试兼容 Cocoa API，但因缺乏官方头文件、运行时行为差异及 GUI 渲染栈深度耦合，长期无法实现二进制级兼容。

**「实际影响」** 该项目无法直接运行 macOS 应用程序，因为用户必须自行从合法拥有的 macOS 系统中提取二进制文件和动态库（如 CoreFoundation、AppKit），且这些库受 Apple 的版权和许可限制，不得分发；因此，它仅对拥有 macOS 许可证并具备逆向工程能力的开发者构成有限的实验性兼容层，而非通用 macOS 应用移植方案。

**「社区讨论」** 部分开发者指出 GNUstep 已长期提供更稳定、可维护的开源 Cocoa API 实现，并已在实际项目中跨平台编译；另一些评论则强调 macOS 用户态依赖动态链接私有系统库而非稳定 syscall，因此纯用户态兼容层在理论上比内核模拟更可行，但亦质疑其长期可维护性与法律风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/XNU-Linux">XNU Linux Lets macOS Userspace Processes Run On... - Phoronix</a></li>

</ul>
</details>

**标签**: `#operating-systems`, `#compatibility-layer`, `#reverse-engineering`, `#open-source`

---

<a id="item-tech-news-8"></a>
### [开源安全维护负担持续恶化](https://blogs.gentoo.org/mgorny/2026/10/27/the-next-circle-of-security-hell/) ⭐️ 7.0/10

本文批判性指出，当前开源生态正陷入不可持续的安全维护困境：尽管 Rust 等语言在内存安全方面取得进展，但逻辑漏洞、配置错误和维护人力枯竭等问题持续加剧，PHP、Brotli、nginx、Java、Ruby 等关键基础设施在过去 30 天内集中暴露出至少六个高危内存安全漏洞。作者强调，编译器无法捕获应用层逻辑缺陷，而企业对开源项目的重度依赖与对维护者缺乏实质性支持（如资金、人力贡献）形成尖锐矛盾。该分析基于真实漏洞事件和广泛社区观察，非预测性声明，亦未宣称某项技术已解决系统性问题。

hackernews · qtqtqt · 11月23日 11:34 · [社区讨论](https://news.ycombinator.com/item?id=50610334)

**「先前的安全困境分析」** 该文是 Michał Górny 于 2026 年 10 月 27 日发布的续篇，直接呼应其数年前题为《现代打包者的安全噩梦》（“The modern packager’s security nightmare”）的早期博文；此前文章已指出开源软件维护者在漏洞响应、依赖更新和构建可重现性等方面面临的系统性压力。

**「影响」** 开源维护者面临更紧迫的权衡压力：必须在有限精力下优先响应高危漏洞（如近期 PHP/Brotli/nginx 中的内存安全问题），而难以投入资源修复逻辑缺陷或改进长期可维护性；部分项目已出现因人力不足而延迟发布安全补丁或明确声明‘按现状使用、风险自担’的实践。

**「社区讨论」** 评论中存在明显分歧：有用户（如 mattstir）强调内存安全工具的价值，指出近期高频内存漏洞恰恰说明其防护必要性；另一些用户（如 markus\_zhang）则批评维护者未明确设定贡献预期与使用边界，认为‘抱怨文化’掩盖了主动治理的可能性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.gentoo.org/mgorny/2026/10/27/the-next-circle-of-security-hell/">The next circle of security hell – Michał Górny</a></li>
<li><a href="https://blogs.gentoo.org/mgorny/2026/0/">2026 – Michał Górny - blogs.gentoo.org</a></li>
<li><a href="https://blogs.gentoo.org/mgorny/2026/10/">October 2026 – Michał Górny - blogs.gentoo.org</a></li>

</ul>
</details>

**标签**: `#open-source`, `#software-security`, `#maintainer-burnout`, `#memory-safety`, `#software-engineering`

---

<a id="item-tech-news-9"></a>
### [1700 万行 Lean 形式化 GRH 证明的意义与误解](https://micjm.com/blog/yes-17m-lines-of-lean-is-a-lot/) ⭐️ 7.0/10

本文并非宣布新证明或技术发布，而是对已存在的 1700 万行 Lean 代码形式化广义黎曼假设（GRH）的深度反思。它指出：该行数反映的是将自然语言数学证明逐条转化为机器可验证逻辑所需的严谨展开，而非软件工程意义上的‘代码量’；Lean 在此扮演‘编译后的数学’验证器角色，其输出不可执行，也不追求人类可读性；文章强调需区分‘可验证性’与‘人类可理解性’，并质疑在超大规模形式化中，信任建立的基础究竟是形式系统本身，还是人类对整个链条（包括 Lean 内核、标准库、形式化过程）的掌握程度。

hackernews · seizethecheese · 11月23日 05:00 · [社区讨论](https://news.ycombinator.com/item?id=50607668)

**「背景」** 2026 年 11 月 20 日，Levent Alpöge 宣布借助 Anthropic 的 Claude 模型完成了黎曼猜想（RH）及广义黎曼猜想（GRH）对狄利克雷 L-函数的证明，并以 Lean 4 形式化证明存档发布，包含约 175,187 个文件、总计约 1700 万行代码。该证明仅覆盖所有模数与所有特征下的狄利克雷 L-函数，不包括戴德金ζ函数、赫克 L-函数或一般自守 L-函数。目前尚无数学专家对其中数学内容完成审查，亦未发布配套传统论文。

**「实际影响」** 对于依赖 GRH 结论的数学研究者和密码学实践者，该形式化尚未改变 GRH 的未证明状态，但若未来被主流定理证明社区（如 Mathlib 维护者）完全接纳并验证，可能提升相关领域对 GRH 假设性结论的信心；当前更直接的影响是促使形式化方法从业者重新审视‘行数’指标的误导性，并推动对验证工具链可信度（如 Lean 内核正确性）的持续审查。

**「社区讨论焦点」** 评论区存在关键分歧：一部分用户（如\[\_flag\]、\[betterunix2\]）强调 Lean 形式化本质是‘编译数学’，类比编译器生成汇编，行数多不等于不可信；另一部分（如\[lukaslalinsky\]）则担忧人类无法审查如此庞大的形式化产物，若其作为可信基使用，可能引入隐蔽风险。\[adgjlsfhk1\]补充了行数正在动态压缩的事实，表明该形式化仍处于积极优化阶段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://math.mit.edu/~drew/grh/">RH Lean proof: verification files - MIT Mathematics</a></li>
<li><a href="https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/">Alpöge/Claude proof of the Generalized Riemann Hypothesis</a></li>
<li><a href="https://lean4.dev/proofs/riemann-hypothesis-claim">The Riemann Hypothesis: a claimed proof, delivered in Lean</a></li>

</ul>
</details>

**标签**: `#formal-methods`, `#theorem-proving`, `#ai-assisted-math`, `#software-correctness`, `#lean`

---

<a id="item-tech-news-10"></a>
### [初学者本地 AI 指南：Inkling、Qwen 与 Unsloth 部署实践](https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth) ⭐️ 7.0/10

本文是一份面向初学者的实操指南，介绍如何在本地设备上部署和运行 Inkling（如 Inkling 2 Mini）、Qwen（如 Qwen 3.8 27B UD-Q4\_K\_M）等开源大模型，主要依赖 Unsloth 框架进行高效微调，并结合 llama.cpp、Strata/Basalt 等工具实现显存优化与 MoE 层卸载。指南覆盖 macOS 与 Ubuntu 系统，明确支持 NVIDIA GPU（如 RTX 4070、Tesla P100、P40），并指出 P40（约 300 美元）和 P100（约 250 美元）等二手专业卡可在 1000 美元内构建可用本地 AI 环境。文中未宣布新模型或工具发布，而是整合现有开源方案，强调硬件适配性与实际推理速度（如 14–30 tokens/s）。

hackernews · Retell15 · 11月22日 21:01 · [社区讨论](https://news.ycombinator.com/item?id=50603845)

**「本地 AI 模型部署基础」** Inkling 和 Qwen 是近期发布的轻量级、可本地运行的开源大语言模型，其中 Inkling 由 Unsloth 团队优化适配，Qwen3.6 系列（如 27B 和 35B-A3B）是阿里巴巴推出的多模态混合推理模型，支持 256K 上下文和 201 种语言。Unsloth 提供了专用工具链（如 Unsloth Desktop）以简化这些模型在消费级 GPU 上的量化、加载与 LAN 部署流程。

**「影响」** 开发者和爱好者可基于该指南，在消费级或二手专业 GPU（如 P40、P100）上以低于 1000 美元成本部署 Qwen 3.8 等中等规模模型，但需手动处理驱动兼容性（如 P40 需额外 WMI 调用或定制固件）、系统内存卸载配置及 macOS 端工具链缺失等实际障碍。

**「社区讨论」** 评论者普遍认同当前本地 AI 仍处于“等离子电视阶段”——硬件门槛高、部署不透明；有人通过 Claude 代理自动完成 Inkling 2 Mini 在 RTX 4070 笔记本上的部署，也有人指出 Windows 作为唯一推荐平台的说法错误，强调 Linux（Ubuntu）和 macOS 同样可行且已有实践案例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://unsloth.ai/docs/models/inkling">Inkling - How to Run Locally | Unsloth Documentation</a></li>
<li><a href="https://unsloth.ai/docs/models/qwen3.6">Qwen3.6 - How to Run Locally | Unsloth Documentation</a></li>

</ul>
</details>

**标签**: `#local-ai`, `#model-deployment`, `#hardware-optimization`

---

<a id="item-tech-news-11"></a>
### [谷歌搭建 Mirror Dimension 模拟互联网测试 Chrome AI 代理](https://www.landian.news/archives/128701.html) ⭐️ 7.0/10

谷歌为测试 Chrome 内置 AI 代理，构建了名为 Mirror Dimension 的隔离式模拟互联网环境，包含数千个模拟网站，支持工程师独立运行每日超 1000 个测试用例；该环境重点验证 AI 代理在打开网页、搜索浏览、登录、加购及任务完成等操作中的可靠性，并专门评估其对恶意网页发起的提示词注入（prompt injection）攻击的防御能力。

telegram · zaihuapd · 11月23日 01:30

**「背景」** Mirror Dimension 是谷歌为 Chrome AI 代理构建的合成网络测试环境，其核心目标是安全评估浏览器自动化代理在真实用户路径下的导航、任务执行与安全性表现。该环境并非真实互联网的镜像，而是由数千个受控、可复现的模拟网站组成，专为隔离测试和对抗性验证（如提示词注入）而设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/security/mirror-dimension-for-agents/">Mirror Dimension for Agents: Evaluating Browser-Use Agents ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#browser security`, `#prompt injection`, `#testing infrastructure`, `#Chrome`

---

<a id="item-tech-news-12"></a>
### [Windows Server 2028 默认移除 WoW64，32 位应用需手动通过 FoD 安装支持](https://www.windowslatest.com/2026/11/23/32-bit-apps-days-are-numbered-as-microsoft-strips-support-bit-by-bit-starting-with-windows-server-2028-but-windows-11-is-safe-for-now/) ⭐️ 7.0/10

Windows Server 2028 将默认不包含 WoW64（Windows on Windows 64）子系统，因此开箱即用状态下无法运行任何 32 位应用程序；该版本计划于 2027 年秋季发布，与 Windows 11 27H2 同步。用户可通过“按需功能”（Features on Demand, FoD）手动安装 WoW64，Server Core 版本需使用 PowerShell 或 DISM 命令完成。微软明确表示此举旨在缩小攻击面并阻止 32 位恶意软件，而 Windows 11 当前仍完整保留 WoW64，且官方未宣布其移除时间表。

telegram · zaihuapd · 11月23日 03:03

**「WoW64 的作用与历史沿革」** WoW64（Windows on Windows 64）是 Windows 为在 64 位系统上运行 32 位应用程序而设计的兼容层，自 Windows XP x64 Edition 起引入，长期作为 Windows Server 和 Windows 客户端的标准组件。微软自 Windows 10 周年更新起逐步弱化对 32 位应用的支持，例如移除 32 位 IE、限制 Store 中 32 位 UWP 应用分发，但始终默认保留 WoW64 以维持企业环境向后兼容。

**「影响」** 企业系统管理员和 DevOps 工程师在部署 Windows Server 2028 时，必须主动评估并显式启用 WoW64 才能运行遗留 32 位服务或管理工具，否则将遭遇兼容性中断；这一变更要求更新自动化部署脚本、镜像构建流程及安全基线策略。

**标签**: `#windows-server`, `#system-compatibility`, `#security-hardening`, `#legacy-software`, `#enterprise-infrastructure`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [跳过 DRAM 层：MoRI UMBP 将代理型 KV 缓存直接运行在 NVMe 上](https://vllm.ai/blog/2026-11-23-skip-the-dram-tier) ⭐️ 9.0/10

rss · vLLM Blog · 11月23日 00:00

**「背景」** 代理型大模型服务中，多轮会话反复发送长前缀（如 AgentX 基准中 96%的输入 token 为已见前缀），KV 缓存命中率直接决定吞吐量——命中率每提升 1%，Kimi-K3 吞吐量可增约 10%。但 GPU 显存和主机 DRAM 均迅速耗尽：Kimi-K3 一小时写入 2.3–4.6 TB KV，而 1.8 TB DRAM 池仅能保留 23–47 分钟数据，成本高达 7.6 万美元。

**「方案」** 作者在 vLLM 中集成 AMD MoRI 库的 UMBPO 统一内存池，将 1.8 TB KV 缓存直接部署于本地 Micron 7450 PRO NVMe SSD（无 RAID、无 NVMe-oF），仅用 64 GB DRAM 作写缓冲、16 GiB 作读取暂存。实测显示：在 Kimi-K3 和 DeepSeek-V4-Pro 上，NVMe 池吞吐量与同容量 DRAM 池相差≤1%（48/70/96 并发会话），且因容量更大（如 4.6 TB NVMe 池在 70 会话下 KV 命中率 93% vs DRAM 的 52%），实际吞吐达 DRAM 池的 5.1 倍；关键在于异步预填充重叠、小段文件（256 MiB）提升淘汰精度、以及 GPU 前缀访问“touch”机制同步热度信息，使 NVMe 写入延迟被计算等待掩盖。成本上，NVMe 按写入量计价（$0.36/TB），1.8 TB 池五年总成本约 5.9 万美元，远低于 DRAM 池的 7.6 万美元，且支持全天级 KV 保留。

**「启示」** NVMe 可作为代理型 LLM 服务中 KV 缓存的主存储层，在吞吐不降的前提下，以更低 TCO 实现更长 KV 保留时间，其可行性根植于代理负载的高前缀复用性、异步计算流水线对 I/O 延迟的天然掩蔽，以及细粒度缓存管理技术的协同优化。

**标签**: `#LLM inference`, `#KV caching`, `#NVMe optimization`, `#agentic systems`, `#memory hierarchy`

---

<a id="item-tech-blog-2"></a>
### [当不确定时，有策略地‘乱试’](https://seangoedecke.com/when-in-doubt-flail-about/) ⭐️ 8.0/10

rss · Sean Goedecke · 11月23日 00:00

**「背景」** 在产品开发、系统优化或跨团队协作中，工程师常面临高度模糊的情境：缺乏明确目标、无可靠数据支撑、甚至无人能清晰描述问题本质。此时传统规划式方法易陷入分析瘫痪，而被动等待又会错失关键反馈窗口。

**「方案」** 作者提出“有策略的乱试”（flailing）——一种以高频率、低沉没成本实验为核心，严格依赖真实反馈快速筛选有效路径的方法。其关键在于三步闭环：主动尝试大量不同方案（如 GitHub Models 中数十个失败集成中意外发现 AI Actions 令牌机制）；对来自用户、指标和同事的反馈极度敏感（尤其识别“哇！”级正向信号）；并果断放弃未获验证的想法，避免情感依附。该方法适用于三类典型场景：产品探索期（验证价值假设）、工程攻坚期（通过试探性重构定位瓶颈）、组织协调期（用轻量行动打破沟通僵局），且强调心理韧性——承认“感觉像在乱试”本就是有效探索的内在信号。

**「启示」** 真正的工程效能不在于避免失败，而在于设计出能快速暴露失败、放大微弱成功信号的实验节奏；当不确定性成为常态，“有纪律的乱试”比完美计划更接近问题的本质解。

**标签**: `#engineering-practice`, `#technical-ambiguity`, `#experimentation`, `#organizational-dynamics`, `#feedback-loops`

---

<a id="item-tech-blog-3"></a>
### [OpenAI 公开模型困惑度数据的技术反思](https://seangoedecke.com/notes-on-openais-perplexity-reveal/) ⭐️ 7.0/10

rss · Sean Goedecke · 11月23日 00:00

**「背景」** OpenAI 首次公开了其所有已发布大语言模型在训练过程中困惑度（perplexity）随时间变化的完整曲线图，这是前沿 AI 实验室迄今最透明的一次内部训练指标披露。困惑度作为衡量模型在预训练阶段对预留文本预测准确性的指标，高度依赖于所用评估数据集，因而无法直接跨机构或跨任务比较。

**「方案」** 作者指出，该图表揭示了多个反直觉现象：多数模型并未共享相同预训练基座（如 GPT-4.1 与 o3 虽基座相同，但实际表现差异显著）；GPT-4.5 出现明显停滞，而 GPT-5.2 之后困惑度加速下降，表明预训练仍在快速进步，驳斥了‘业界已全面转向强化学习微调’的普遍认知；同时，困惑度持续改善与用户主观体验提升并不严格同步——例如 o3 和 GPT-5.3-Codex 被广泛感知为能力跃迁点，但其困惑度曲线并无异常拐点，暗示 RLHF 等后训练技术对链式思维、抗谄媚等关键能力的塑造未反映在该指标中。

**「启示」** 困惑度是预训练能力的有限代理，其公开虽提升了透明度，却无法替代对后训练动态、对齐机制及真实任务表现的深入评估；真正的模型能力演进，是预训练基础与后训练策略共同作用的结果，二者不可割裂解读。

**标签**: `#perplexity`, `#model evaluation`, `#pretraining`, `#AI transparency`, `#LLM alignment`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [摩根大通与现代信用卡完成 AI 代理自主外汇交易概念验证](https://www.cnbc.com/2026/11/18/jpmorgan-hyundai-card-ai-agents-payments.html) ⭐️ 7.0/10

摩根大通与韩国现代信用卡公司已完成一项私有区块链上的概念验证，首次实现银行 AI 代理与企业客户 AI 代理之间无需人工干预的自主外汇交易；该测试设定了单笔交易最高 500 万美元的硬编码限额。

rss · CNBC Finance · 11月23日 06:06

**「背景」** 此次测试聚焦于现代信用卡在 Kinexys 区块链存款账户中的欧元流动性管理，是企业司库管理领域首个银行-客户 AI 代理间自主交易试点。

**「影响」** 该技术若推广，将要求金融机构重构风险控制体系，把监管重点从人工操作转向机器对机器交互的实时监控与权限约束。

**标签**: `#AI finance`, `#payments infrastructure`, `#banking innovation`, `#corporate treasury`, `#financial regulation`

---

<a id="item-finance-news-2"></a>
### [蚂蚁集团领投具身智能公司 Simplexity Robotics 1 亿美元](https://www.bloomberg.com/news/articles/2026-11-22/ant-group-bets-on-simplexity-to-thrive-in-china-s-humanoid-race) ⭐️ 7.0/10

蚂蚁集团领投中国具身智能初创公司 Simplexity Robotics 1 亿美元 pre-A 轮融资，投后估值 16 亿美元。

telegram · zaihuapd · 11月23日 02:02

**「背景」** Simplexity Robotics 是一家 2025 年 7 月成立于杭州的具身智能公司，核心团队来自理想汽车；该公司在成立半年内已披露完成五轮融资，累计融资约 20 亿元人民币，截至 2026 年 3 月投后估值已超 10 亿美元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://robottoday.com/suppliers-discovery/simplexity-robotics">Simplexity Robotics - RobotToday</a></li>
<li><a href="https://www.ai-market-watch.com/company/simplexity-robotics">Simplexity Robotics - AI Startup Profile | AI Market Watch</a></li>

</ul>
</details>

**标签**: `#artificial-intelligence`, `#robotics`, `#venture-capital`, `#china-tech`, `#startup-funding`

---

<a id="item-finance-news-3"></a>
### [上海地铁票价 21 年来首次调整](https://weibo.com/1699432410/5368461393397183) ⭐️ 7.0/10

上海地铁自 2005 年以来首次调整票价，新票价于 2026 年 12 月 1 日起实施：起乘价 3 元（0–4 公里），之后按 4、4、4、7、7、10、10 公里分段加收 1 元，50 公里以上每 15 公里加 1 元；同步推出 35 次至 90 次四档计次票及当月满 90 元享 9 折优惠。

telegram · zaihuapd · 11月23日 10:45

**「背景」** 此前上海地铁自 2005 年起实行统一 2 元起步、按里程分段计价的旧标准，此次是 21 年来首次系统性调整。

**标签**: `#public\_transport`, `#local\_policy`, `#consumer\_costs`

---