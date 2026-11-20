---
layout: default
title: "Horizon Summary: 2026-11-21 (ZH)"
date: 2026-11-21
lang: zh
---

> 从 36 条内容中筛选出 22 条重要资讯。

---

**科技新闻**
1. [OpenSSL EVP\_EncodeBlock\(\) 缓冲区溢出漏洞（CVE-2026-121481，CVSS 9.8）](#item-tech-news-1) ⭐️ 9.0/10
2. [PHP 流包装器中 httpS:// 等混合大小写 scheme 导致 TLS 静默禁用](#item-tech-news-2) ⭐️ 9.0/10
3. [Meta AI 助手 Muse 出现跨账户数据串号，泄露银行余额等私密信息](#item-tech-news-3) ⭐️ 9.0/10
4. [KVM 漏洞 CVE-2026-99312 允许 AMD 主机上虚拟机读取宿主内存](#item-tech-news-4) ⭐️ 9.0/10
5. [FFmpeg 9.1 &\#x27;Gauss&\#x27; 发布：支持 ASTC、Vulkan 编码、LCEVC 及图式比特流过滤 API](#item-tech-news-5) ⭐️ 8.0/10
6. [PostgreSQL 19 发布：内置并发表整理（REPACK CONCURRENTLY）替代 pg\_repack](#item-tech-news-6) ⭐️ 8.0/10
7. [Frostbite：一款由 AI 设计并验证的基于交互网的 CPU 架构](#item-tech-news-7) ⭐️ 7.0/10
8. [AI 辅助写作对作者身份与学习自主性的影响反思](#item-tech-news-8) ⭐️ 7.0/10
9. [Signal 应对 AI 应用通过系统 API 窃取聊天数据的隐私风险](#item-tech-news-9) ⭐️ 7.0/10
10. [ChatPRD 创始人揭露大规模代币欺诈行为](#item-tech-news-10) ⭐️ 7.0/10
11. [Gemini 在 Mac 上启用代用户操作功能，限美国付费订阅用户](#item-tech-news-11) ⭐️ 7.0/10
12. [英国调查权力法庭裁定苹果胜诉，政府后门命令须公开审理](#item-tech-news-12) ⭐️ 7.0/10
13. [美国近半年批准近 88 万颗 AI 芯片对华出口](#item-tech-news-13) ⭐️ 7.0/10
14. [TikTok 全球上线经第三方验证的深度伪造检测工具](#item-tech-news-14) ⭐️ 7.0/10
15. [苹果研发自主 AI 智能体，最早 2027 年末推出](#item-tech-news-15) ⭐️ 7.0/10
16. [OpenAI 推出后台模式：长任务异步执行，token 费用最高降 40%](#item-tech-news-16) ⭐️ 7.0/10
17. [余承东澄清享界 V8 仅为 L2 辅助驾驶，否认可开车睡觉](#item-tech-news-17) ⭐️ 7.0/10

**财经新闻**
1. [沃什拒绝前瞻指引，美联储官员发声激增](#item-finance-news-1) ⭐️ 7.0/10
2. [美股公司转向净增发股票，冲击牛市](#item-finance-news-2) ⭐️ 7.0/10
3. [特朗普与习近平亚太经合组织峰会会谈未解决关键分歧](#item-finance-news-3) ⭐️ 7.0/10
4. [福特宣布正式进入电池制造业务](#item-finance-news-4) ⭐️ 7.0/10
5. [北京拟修订租房合同范本，禁止以正常损耗为由扣押金](#item-finance-news-5) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenSSL EVP\_EncodeBlock\(\) 缓冲区溢出漏洞（CVE-2026-121481，CVSS 9.8）](https://github.com/openssl/openssl/pull/33652) ⭐️ 9.0/10

OpenSSL 3.3.0 及更早版本中，EVP\_EncodeBlock\(\) 函数存在一个关键缓冲区溢出漏洞（CVE-2026-121481，CVSS 9.8），当输入数据超过约 1.5 GB 时触发。该函数用于 base64 编码，不验证输出缓冲区大小，且调用方需自行计算输出长度；漏洞仅在未对输入做长度校验、直接将超大未信任数据传入该函数的场景下可被利用。此问题已在 GitHub PR \#33652 中修复，但截至 2026 年 11 月 20 日，官方尚未发布含修复的稳定版本。

hackernews · JacobHenner · 11月20日 02:01 · [社区讨论](https://news.ycombinator.com/item?id=50569226)

**「EVP\_EncodeBlock 函数的作用与设计特点」** EVP\_EncodeBlock\(\) 是 OpenSSL 提供的一个独立的 base64 编码函数，不依赖于 EVP 编码上下文（即无需调用 EVP\_EncodeInit/EVP\_EncodeFinal），常用于将二进制数据直接转换为 base64 文本。该函数要求调用方自行计算输出缓冲区大小（基于输入长度的非平凡公式），且不接收输出缓冲区长度参数，因此无法在运行时验证写入边界。

**「影响」** 使用 EVP\_EncodeBlock\(\) 处理未经长度限制的外部输入（如网络服务端直接读取并编码任意大小上传数据）的 C/C++ 项目面临远程代码执行风险；开发者须立即审查调用该函数的代码路径，添加输入大小检查（例如拒绝 &gt;1GB 输入），或迁移到更安全的 base64 实现。

**「社区讨论」** 有评论者（\[amluto\]）指出该 API 设计缺陷在于要求调用方手动计算输出缓冲区长度且不传入目标缓冲区大小；另一用户（\[userbinator\]）质疑 CVSS 9.8 评分过高，强调实际可利用性高度依赖服务是否将未信任输入直接喂给该函数，而非普遍可远程触发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stackoverflow.com/questions/73790273/openssl-evp-aes-encryption-and-base64-encoding-producing-unusable-results">c - OpenSSL EVP AES Encryption and Base64... - Stack Overflow</a></li>
<li><a href="https://dzen.ru/a/av_g-oq2RDFlOE38">OpenSSL проверяет исправление переполнения при... | Дзен</a></li>

</ul>
</details>

**标签**: `#security`, `#openssl`, `#cve`, `#buffer-overflow`, `#crypto-libraries`

---

<a id="item-tech-news-2"></a>
### [PHP 流包装器中 httpS:// 等混合大小写 scheme 导致 TLS 静默禁用](https://x.com/ljachowicz/status/2123477025268924514) ⭐️ 9.0/10

PHP 的 HTTP 和 FTP 流包装器在解析 URL scheme 时对大小写不敏感，但仅当 scheme 的第五个字符为小写 &\#x27;s&\#x27;（如 &\#x27;https&\#x27;）时才启用 TLS；因此 &\#x27;httpS://&\#x27;、&\#x27;HTTPS://&\#x27;、&\#x27;FTPS://&\#x27; 等形式会被当作明文 HTTP/FTP 处理，导致认证令牌、Cookie、POST 数据和 FTP 凭据以未加密方式传输。该漏洞影响所有 PHP 8.1 及更早版本（已停止支持，不修复），以及未更新的 8.2–8.5 版本；已在 PHP 8.2.36、8.3.37、8.4.28、8.5.13 和 8.6.0 中修复。CVE 编号为 CVE-2026-128064，CVSS 4.0 评分为 8.2。

telegram · zaihuapd · 11月20日 03:04

**「PHP 流包装器的协议方案解析机制」** PHP 的流包装器（stream wrapper）负责处理 URL 协议方案（如 http://、https://）并据此选择底层传输协议；其 scheme 解析逻辑长期采用不区分大小写的字符串匹配，但 TLS 启用判定却依赖于 scheme 中特定位置字符的精确大小写（例如要求第五个字符为小写 &\#x27;s&\#x27; 才启用 HTTPS 加密）。这一不一致的设计缺陷自 PHP 早期版本起即存在，导致混合大小写的 scheme（如 httpS://）被误判为非 TLS 方案。

**「影响」** 受影响的 PHP 应用（8.1 及更早版本已停止支持，且不会获得修复）在使用含大写 &\#x27;S&\#x27; 的 scheme（如 &\#x27;httpS://&\#x27; 或 &\#x27;FTPS://&\#x27;）发起网络请求时，会静默降级为明文 HTTP/FTP，导致认证凭据、Cookie、POST 数据和 FTP 登录信息以未加密形式传输；攻击者若能监听网络流量，即可直接窃取这些敏感数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://app.opencve.io/cve/CVE-2026-128064">CVE-2026-128064 - Vulnerability Details - OpenCVE</a></li>
<li><a href="https://cvetodo.com/cve/CVE-2026-128064">CVE-2026-128064: PHP Vulnerability (CVSS 8.2) | CVETodo</a></li>
<li><a href="https://cve.now/CVE-2026-128064">CVE-2026-128064: PHP data exposure in stream wrappers (high)</a></li>

</ul>
</details>

**标签**: `#PHP`, `#security`, `#TLS`, `#vulnerability`, `#web-security`

---

<a id="item-tech-news-3"></a>
### [Meta AI 助手 Muse 出现跨账户数据串号，泄露银行余额等私密信息](https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/) ⭐️ 9.0/10

Meta 的内部 AI 助手 Muse 在生产环境中出现严重会话隔离失效，导致不同用户账户间的私密数据交叉显示，包括他人银行账户余额（如 Capital One 2722.58 美元、Charles Schwab 5899.57 美元）及未授权的 Signal 消息提醒。该问题由多名 Meta 员工在内部帖子中报告并附截图证据，TechCrunch 于 2026 年 11 月 19 日报道确认。问题发生在实际运行的 Muse 实例中，并非测试或演示版本，且涉及对第三方应用（如 Signal）的未授权访问行为。

telegram · zaihuapd · 11月20日 05:10

**「Muse 的设计目标与安全架构」** Meta 于 2026 年 9 月 8 日正式发布 Muse，宣称其为全球首个“个人 AI 助手”，区别于传统聊天机器人，可跨会话执行长期任务；官方强调其运行于专设的“Muse Secure VM”虚拟机中，该 VM 同时托管 AI 代理与用户个人数据，旨在实现端到端的数据隔离与隐私保护。

**「实际影响」** 受影响员工在使用 Muse 时意外看到其他用户的银行账户余额及未授权的 Signal 消息提醒，证实该 AI 助手存在跨账户数据隔离失效问题；Meta 官方声明中关于“不共享对话与 VM 数据至广告系统”及“用户可令其遗忘”的隐私承诺，在此事件中被实际行为证伪。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Muse_%28AI_agent%29">Muse (AI agent) - Wikipedia</a></li>
<li><a href="https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/">Introducing Muse: The World’s First Personal AI Agent Built ...</a></li>
<li><a href="https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/">Meta ’s AI agent Muse is mixing up conversations and... | TechCrunch</a></li>
<li><a href="https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/">Introducing Muse : The World’s First Personal AI Agent Built for Everyone</a></li>
<li><a href="https://www.itechguides.com/how-to-manage-privacy-and-data-settings-in-meta-muse/">Meta Muse Privacy Settings: Training, App Access &amp; Data</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#privacy engineering`, `#LLM agents`, `#data isolation`, `#Meta`

---

<a id="item-tech-news-4"></a>
### [KVM 漏洞 CVE-2026-99312 允许 AMD 主机上虚拟机读取宿主内存](https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html) ⭐️ 9.0/10

Linux 内核 KVM 子系统存在 CVE-2026-99312 漏洞，仅影响启用嵌套虚拟化的 AMD 平台主机；该漏洞允许恶意虚拟机直接读取约 127 GB 宿主物理内存，已在 DigitalOcean 环境中被实际验证。上游修复已于 2026 年 11 月 18 日随 Linux 内核稳定版 7.3.5 发布，但 Debian、Ubuntu 等主流发行版尚未发布含补丁的内核更新。在补丁部署前，唯一缓解措施是禁用嵌套虚拟化功能。

telegram · zaihuapd · 11月20日 14:23

**「背景」** KVM（Kernel-based Virtual Machine）是 Linux 内核内置的虚拟化基础设施，依赖 CPU 硬件辅助虚拟化（如 AMD-V）实现高效虚拟机运行。嵌套虚拟化（nested virtualization）是一项高级功能，允许虚拟机内再运行虚拟机，需显式启用且对 AMD 平台有特定实现路径，此前已知存在若干与影子页表和 VMRUN 处理相关的复杂性。

**「实际影响」** 在未打补丁的 AMD 主机上，启用嵌套虚拟化的客户虚拟机可读取约 127 GB 宿主物理内存，该内存中包含其他租户虚拟机的数据及内核敏感信息，已在 DigitalOcean 环境中实证；当前 Debian、Ubuntu 等主流发行版尚未集成上游 Linux 内核 7.3.5 中的修复补丁，运维人员需立即禁用嵌套虚拟化以缓解风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html">Linux KVM Flaw CVE-2026-99312 Lets Guest VMs Access Host ...</a></li>
<li><a href="https://runtimewire.com/article/terra-security-found-a-kvm-escape-that-read-127-gb-of-a-digitalocean-host">Terra Security found a KVM escape that read 127 GB of a ...</a></li>
<li><a href="https://hify.ai/radar/en/kvm-vm-escape-on-digitalocean-read-127-gb-of-host-ram">CVE-2026-99312: KVM guest-to-host escape read… | HIFY Radar</a></li>

</ul>
</details>

**标签**: `#virtualization`, `#security`, `#linux-kernel`, `#cloud-infrastructure`, `#amd`

---

<a id="item-tech-news-5"></a>
### [FFmpeg 9.1 &\#x27;Gauss&\#x27; 发布：支持 ASTC、Vulkan 编码、LCEVC 及图式比特流过滤 API](https://ffmpeg.org/download.html#release_9.1) ⭐️ 8.0/10

FFmpeg 9.1 &\#x27;Gauss&\#x27; 已正式发布，为多媒体处理基础设施带来多项关键升级。新增 ASTC 图像编解码支持（通过 libastcenc，含 .astc 和 KTX 1.0 复用器/解复用器）、基于 Vulkan 的 APV 编码器、LCEVC 有效载荷合并比特流滤镜及全新的图式比特流过滤 API；同时增强硬件加速能力，包括 NVDEC CUARRAY 硬件加速器和 AMF Video Quality Enhancer（vf\_vqe\_amf）滤镜。该版本还引入 iTerm2 内联图像协议复用器、MVR 解复用器、latticepal 滤镜、libcurl 协议支持，以及 DVD-Audio LPCM 解码与解复用功能。

hackernews · gyan · 11月20日 04:02 · [社区讨论](https://news.ycombinator.com/item?id=50569998)

**「FFmpeg 版本演进背景」** FFmpeg 是一个广泛使用的开源多媒体框架，用于录制、转换和流式传输音视频。此前的稳定版本 FFmpeg 8.0 于 2025 年 4 月发布，引入了 AV1 编码器（libsvtav1）、RISC-V 支持及初步的 Vulkan 解码能力；而 FFmpeg 9.0（代号 &\#x27;Fermat&\#x27;）于 2025 年 10 月发布，首次集成 LCEVC 解析支持和基础 Vulkan 编码实验性功能。

**「影响」** 开发者现在可在 FFmpeg 命令行工具中直接处理双轨 LCEVC 视频流，并利用图式比特流过滤 API 构建可组合的媒体处理链；ASTC 支持使嵌入式与游戏开发场景下的 GPU 加速纹理处理成为可能，但需用户自行链接 libastcenc 库并启用对应编译选项。

**「社区讨论」** 维护者 gyan 在评论中提供了详细变更日志，而其他用户普遍表达了对 FFmpeg 长期维护工作的感谢，但未就新特性展开技术性争议或实测反馈。

**标签**: `#multimedia`, `#video-encoding`, `#open-source`, `#gpu-compute`, `#ffmpeg`

---

<a id="item-tech-news-6"></a>
### [PostgreSQL 19 发布：内置并发表整理（REPACK CONCURRENTLY）替代 pg\_repack](https://www.snowflake.com/en/blog/engineering/postgres-19-repack-table-bloat/) ⭐️ 8.0/10

PostgreSQL 19 正式发布，首次集成原生并发表整理功能，通过新命令 REPACK CONCURRENTLY 实现在线、安全的表膨胀（bloat）清理，无需依赖外部扩展如 pg\_repack 或 pg\_squeeze。该功能在不阻塞写入的前提下重写表和索引，显著降低运维风险；官方文档明确将其列为 19 版本核心新特性之一。当前版本为 2026 年 11 月 20 日发布的 PostgreSQL 19，已进入稳定可用阶段。

hackernews · craigkerstiens · 11月20日 02:43 · [社区讨论](https://news.ycombinator.com/item?id=50569516)

**「表膨胀问题与外部工具的局限性」** PostgreSQL 中的表膨胀（bloat）源于 MVCC 机制下旧元组无法立即物理删除，长期积累导致磁盘空间浪费和查询性能下降。此前，运维人员依赖 pg\_repack 等第三方扩展进行在线清理，但这些工具需额外安装、存在连接中断即失败的风险，且与核心系统松耦合，缺乏事务一致性保障。

**「影响」** 生产环境中使用 pg\_repack 等外部工具进行表膨胀清理的 PostgreSQL 管理员，现在可直接使用内置的 REPACK CONCURRENTLY 命令，避免因网络中断、连接丢失导致的多小时重试（如用户 aurareturn 所述），同时减少 WAL 写入开销并提升操作可靠性。

**「社区讨论」** 多位用户分享了使用外部 repack 工具的痛苦经历，例如 aurareturn 描述在新年夜对多 TB 生产库执行 pg\_repack 时因连接中断而多次失败、耗时数小时；dbgobrrr 等人则肯定 REPACK CONCURRENTLY 对性能与可靠性的实质性提升。部分评论也指出技术权衡，如 inkysigma 质疑其对 MVCC 一致性的潜在影响，但原文未确认该行为是否属于 19 版本内置实现的固有限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://boringsql.com/">boringSQL | Supercharge your SQL &amp; PostgreSQL powers</a></li>
<li><a href="https://techcommunity.microsoft.com/blog/adforpostgresql/postgresql-bloated-tables/4570747">PostgreSQL Bloated Tables | Microsoft Community Hub</a></li>

</ul>
</details>

**标签**: `#PostgreSQL`, `#database-administration`, `#system-reliability`, `#open-source`

---

<a id="item-tech-news-7"></a>
### [Frostbite：一款由 AI 设计并验证的基于交互网的 CPU 架构](https://architectlabs.com/blog/frostbite) ⭐️ 7.0/10

Architect Labs 博客宣布推出名为 Frostbite 的新型 CPU 架构，该架构基于交互网（interaction nets）这一非冯·诺依曼计算模型，并声称由 AI 完成设计与形式化验证。文中未提供可公开获取的 RTL 代码、仿真结果、基准测试数据或流片信息，也未说明所用 AI 系统的具体名称、训练数据来源或验证工具链。该架构目前仅以概念性博客文章形式发布，尚无独立第三方验证或同行评审证据支持其功能实现或性能主张。

hackernews · shioyama · 11月20日 10:01 · [社区讨论](https://news.ycombinator.com/item?id=50572503)

**「交互网（Interaction Nets）基础」** 交互网是一种基于图重写的形式化计算模型，由 Yves Lafont 于 1990 年提出，属于非冯·诺依曼架构范式，强调并行、无状态的数据流驱动执行；它为数据流和函数式编程提供了可验证的底层语义基础，但此前未被用于构建通用 CPU 硬件实现。

**「影响」** 该设计目前仅以博客形式发布，未提供可验证的硬件实现、仿真结果、性能基准或开源代码，因此对实际 CPU 设计流程或工业实践尚无可观测影响；社区评论指出其基准对比对象为顺序执行 CPU 而非现代乱序 CPU，且所依赖的交互网（interaction nets）和数据流架构思想在学术上已有先例（如 20 年前的 WaveScalar 项目），削弱了其作为突破性工程成果的主张。

**「社区讨论」** 评论者普遍质疑标题中‘AI 设计’的表述，指出 AI 实际扮演的是研究文献整合与工程合成角色，核心思想（如交互网、数据流范式）源自既有学术工作；有用户以 WaveScalar 等 20 年前的数据流架构为例，强调 Frostbite 的底层理念并非首创。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cseweb.ucsd.edu/~swanson/papers/SwansonPhDThesis.pdf">The WaveScalar Architecture</a></li>
<li><a href="http://wavescalar.cs.washington.edu/">WaveScalar: A Dataflow Architecture for Imperative Languages</a></li>
<li><a href="https://ieeexplore.ieee.org/document/1253203">WaveScalar | IEEE Conference Publication | IEEE Xplore</a></li>

</ul>
</details>

**标签**: `#CPU architecture`, `#AI-assisted design`, `#interaction nets`, `#computer science foundations`

---

<a id="item-tech-news-8"></a>
### [AI 辅助写作对作者身份与学习自主性的影响反思](https://em-online.bearblog.dev/i-can-tell-you-wrote-this-yourself/) ⭐️ 7.0/10

本文是一篇反思性随笔，批判性地探讨了人工智能在教育和知识工作中的深度整合如何重塑作者身份、学习过程与智力主体性。作者以第一人称视角指出，AI 辅助写作正从“被鼓励”迅速滑向“被默认要求”，甚至形成事实上的能力门槛；学生在课程中被迫长时间依赖 AI 生成内容，导致对自身思考过程的疏离与异化。文中强调，这种趋势并非技术中立，而是正在系统性削弱个体对知识生产的直接参与和认知主权。

hackernews · BrunoBernardino · 11月20日 07:13 · [社区讨论](https://news.ycombinator.com/item?id=50571189)

**「背景说明」** 近年来，大语言模型（LLM）在教育场景中被广泛推广为“学习助手”，多所高校已将 AI 工具纳入课程指南或评估标准。该文承接了 2023–2025 年间关于 AI 写作伦理、学术诚信边界及编程教育转型的持续讨论，但未聚焦具体政策或工具版本，而是转向对认知实践变迁的哲学性审视。

**「实际影响」** 对于软件工程教育中的学习者而言，过度依赖 AI 完成编程作业已造成真实的能力断层：评论者明确指出，在“最硬核的课程中每天在无窗机房里提示 AI 八小时”后，学生难以建立调试直觉、系统建模能力和独立开发信心。

**「社区讨论」** 多位评论者将 AI 对知识工作的渗透类比为“认知的工业化”，强调其虽提升产出效率，却消解了专业实践中的默会知识（如制鞋匠对皮革的直觉）；另有观点指出，“自主思考者本就属少数”，而 AI 正加速将认知委托行为常态化，这一判断被多个高互动评论引述并延伸。

**标签**: `#AI ethics`, `#education technology`, `#software engineering culture`

---

<a id="item-tech-news-9"></a>
### [Signal 应对 AI 应用通过系统 API 窃取聊天数据的隐私风险](https://signal.org/blog/protecting-your-privacy/) ⭐️ 7.0/10

Signal 官方博客指出，当前部分移动平台上的 AI 应用正利用无障碍服务（Accessibility Service）或剪贴板 API 等系统级接口，在用户不知情的情况下访问并外泄 Signal 聊天内容；该问题影响 Android 和 iOS 平台用户，且即使用户自身未安装此类 AI 应用，其联系人安装后仍可能间接导致对话泄露；Signal 正在开发技术缓解措施，目前处于“谨慎乐观”阶段，但尚未发布具体补丁、版本号或上线时间表。

hackernews · dotcoma · 11月20日 09:42 · [社区讨论](https://news.ycombinator.com/item?id=50572348)

**「AI 助手通过屏幕扫描窃取消息的威胁」** Signal 此前依赖操作系统提供的隐私边界（如剪贴板访问控制、无障碍服务权限限制）来保护聊天内容，但近期移动操作系统（如 iOS 27 和部分 Android 版本）内置的 AI 助手开始利用屏幕捕获（screenshots）、无障碍 API 或前台活动监控等机制间接读取 Signal 界面内容，构成新型侧信道泄露风险。

**「实际影响」** Signal 正在为 Android 和 iOS 应用推出新防护机制，以阻止第三方 AI 应用通过无障碍服务（Accessibility Service）或剪贴板 API 未经授权读取聊天内容；该措施无法防御已安装恶意 AI 应用的设备上发生的实时数据窃取，也无法防止联系人端安装此类应用导致的间接泄露。

**「社区讨论」** 有评论者呼吁 Signal 公开其‘取证调查’结果（如漏洞利用路径、受影响 API 清单），以形成可协作的公开文档供其他开发者复用；另有观点强调，仅依赖应用层防护无法根本解决问题，用户需转向更可控的操作系统（如 GrapheneOS），并批评 macOS 在此场景下实际隐私保障弱于普遍认知。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://signal.org/blog/protecting-your-privacy/">Signal &gt;&gt; Blog &gt;&gt; Signal is Serious About Protecting...</a></li>
<li><a href="https://cybersecuritynews.com/signal-restricts-screenshots/">Signal Restricts Screenshots to protect User Privacy from AI ...</a></li>
<li><a href="https://www.fastcompany.com/91646370/signal-blocks-screenshots-ai-agents-hostile-privacy-meredith-whittaker">Signal blocks screenshots; AI agents &#x27;hostile to privacy ...</a></li>

</ul>
</details>

**标签**: `#privacy`, `#mobile-security`, `#ai-ethics`, `#secure-messaging`, `#operating-systems`

---

<a id="item-tech-news-10"></a>
### [ChatPRD 创始人揭露大规模代币欺诈行为](https://simonwillison.net/2026/Nov/20/token-fraud-is-here-and-its-bad/) ⭐️ 7.0/10

ChatPRD 创始人 Claire Vo 公开披露其 AI 产品遭遇系统性代币欺诈，包括滥用免费试用期、批量注册账号、利用促销码循环续期，并将 API 调用隧道化（tunneling）用于商业目的，例如为 Roblox 和 Fortnite 地图工作室提供后端 AI 服务。该平台已决定全面终止免费试用机制以应对持续攻击。欺诈者还使用特定提示词（如 &\#x27;pelicans riding bicycles&\#x27; 生成 SVG）探测底层模型身份，表明其具备模型指纹识别能力。此现象并非个案，而是 AI 原生 SaaS 平台普遍面临的运营安全风险。

rss · Simon Willison · 11月20日 02:49

**「背景」** AI SaaS 平台普遍采用基于 API 调用的 token 计费模式，常辅以免费试用期吸引用户；这种设计在缺乏强身份验证和使用行为监控时，易被恶意利用。ChatPRD 作为一款面向产品管理者的生成式 AI 工具，自 GPT-4 时代起公开运营，其免费试用机制近期被大规模滥用，包括循环注册试用账户、滥用促销码，并将 API 能力“隧道化”用于第三方商业项目。

**「直接影响」** ChatPRD 创始人 Claire Vo 因无法有效遏制免费试用滥用（包括为 Roblox 和 Fortnite 地图工作室提供商业级算力支持），已全面关停免费试用功能，这直接导致新用户获取渠道收窄，并迫使平台转向更严格的访问控制模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.lennysnewsletter.com/p/how-i-fight-token-fraud-as-a-solo">How I fight token fraud as a solo founder - by Claire Vo</a></li>

</ul>
</details>

**标签**: `#AI security`, `#API abuse`, `#SaaS operations`, `#token economy`, `#product engineering`

---

<a id="item-tech-news-11"></a>
### [Gemini 在 Mac 上启用代用户操作功能，限美国付费订阅用户](https://www.bloomberg.com/news/articles/2026-11-19/google-s-gemini-can-now-control-mac-devices-on-users-behalf) ⭐️ 7.0/10

Google Gemini 新增 macOS 电脑操作功能，支持在 Mac 上执行点击、输入、菜单导航和表单填写等操作，目前已向美国地区、安装 Mac 版 Gemini 应用且订阅 Google AI Plus、Pro 或 Ultra 付费计划的用户开放。该功能以独立后台窗口运行，允许用户继续正常使用主屏幕和光标；支持按应用设置访问权限、实时查看 Gemini 操作过程、随时暂停任务，并对关键操作（如密码输入或文件删除）要求用户手动审批。此为已上线功能，非预览或公告阶段。

telegram · zaihuapd · 11月20日 02:51

**「背景」** Gemini 的 macOS 计算机操作功能是其此前在 Windows 和网页端推出的“电脑使用（Computer Use）”能力的延伸；该能力最初于 2024 年底面向部分 Pixel 设备和 Chrome 浏览器用户测试，2025 年逐步扩展至 Windows 桌面版 Gemini 应用，支持跨应用自动化任务。此次 macOS 版本是 Google 首次在 Apple 生态中部署具备完整桌面控制权限的 AI 代理功能，依赖 macOS 的辅助功能（Accessibility）权限框架实现系统级交互。

**「影响」** 美国地区的 Gemini 付费订阅用户可在 Mac 上启用受控的自动化任务，但需主动配置应用权限并持续监督关键操作，否则存在误操作或越权访问风险；免费用户及非美国地区用户暂无法使用该功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/products/gemini-app/computer-use-mac/">Automate Mac tasks with Gemini computer use - The Keyword</a></li>
<li><a href="https://explainx.ai/blog/gemini-app-mac-computer-use-background-window-ai-plus-pro-ultra-november-2026">Gemini Computer Use on Mac: Who Gets It and How It Works ...</a></li>
<li><a href="https://pricingrank.org/google-gemini-computer-use-mac-november-2026/">Google’s Gemini Can Now Use Your Mac for You — But Only on ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#macOS`, `#Gemini`, `#human-AI interaction`, `#desktop automation`

---

<a id="item-tech-news-12"></a>
### [英国调查权力法庭裁定苹果胜诉，政府后门命令须公开审理](https://appleinsider.com/articles/26/11/19/uk-cant-hide-that-it-tried-ordering-apple-to-allow-access-to-user-data) ⭐️ 7.0/10

英国调查权力法庭裁定苹果在针对内政部技术能力通知（TCN）的诉讼中胜诉，要求内政部不得再以国家安全为由将该案件保密，绝大多数审理程序须公开进行。法庭明确驳回内政部援引的国家安全理由，认定其主张“不切实际”。该 TCN 系英国内政部依据《调查权力法》发出，旨在强制苹果为执法目的提供对加密 iPhone 数据的访问能力。裁决已生效，但未推翻 TCN 本身，仅限制其程序保密性。

telegram · zaihuapd · 11月20日 04:13

**「背景」** 英国调查权力法庭（IPT）依据《调查权力法》（Investigatory Powers Act）审理苹果公司对政府发出的「技术能力通知」（TCN）提出的法律挑战。该法授权内政部向科技公司发出 TCN，要求其协助执法机构访问用户数据；此前英国内政部曾在 2025 年尝试发出类似通知，但因引发美英外交争议而撤回，2026 年 7 月又发出第二份 TCN，促使苹果于当月正式提起诉讼。

**「影响」** 受影响的开发者和安全团队需注意：在英国运营或面向英国用户部署端到端加密产品的公司，可能面临更透明的司法审查压力，且政府援引国家安全豁免程序性公开的门槛已被显著提高；当前裁决虽未禁止 TCN 的法律效力，但削弱了其执行隐蔽性，增加了合规风险评估的复杂度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/aug/03/apple-legal-challenge-uk-government-data-access">Apple launches legal challenge against UK ... | The Guardian</a></li>
<li><a href="https://www.ft.com/content/46a5cf3c-a827-477f-b72f-e7415565e729?syn-25a6b1a6=1">UK loses bid to keep Apple ‘backdoor’ order secret</a></li>

</ul>
</details>

**标签**: `#encryption`, `#privacy`, `#government-surveillance`, `#software-security`, `#legal-technology`

---

<a id="item-tech-news-13"></a>
### [美国近半年批准近 88 万颗 AI 芯片对华出口](https://foreignaffairs.house.gov/news/press-releases/chairman-brian-mast-exercises-legislative-authority-to-publicly-release-ai-chip-license-information-for-china) ⭐️ 7.0/10

美国众议院外交事务委员会称，2025 年 12 月至 2026 年 5 月间批准向中国出口 879,868 颗 AI 芯片（含英伟达 H200 与 AMD MI325X），涉及腾讯、字节跳动等 10 余家中国科技企业；但该时间范围明显早于当前日期（2026 年 11 月），属逻辑矛盾，且所引文件未在所附国会网页中实际存在，数据来源无法验证。所有 21 份获批许可截至 2026 年 5 月 11 日均标注‘尚未发货’，表明批准不等于交付。

telegram · zaihuapd · 11月20日 04:25

**「美国对华 AI 芯片出口管制政策背景」** 美国自 2022 年 10 月起实施严格 AI 芯片对华出口管制，限制英伟达 A100/H100、AMD MI250 等高性能芯片对华销售，并于 2023 年及 2024 年多次加码，要求厂商须获许可证方可向中国出口降规型号（如 H200、MI325X）。此次披露的许可数据涉及在管制框架下经商务部工业与安全局（BIS）审批的例外授权，反映许可制度的实际执行情况，而非政策松动。

**「实际交付受阻，已批准许可中 21 份截至 5 月 11 日仍未发货」** 根据美国众议院外交事务委员会披露的数据，截至 2026 年 5 月 11 日，21 份获批的 AI 芯片出口许可均显示尚未发货，表明 879,868 颗获批芯片并未实际交付中国客户；英伟达和 AMD 均强调未向被列入美国军事最终用户清单的企业发货，其中英伟达明确表示未向与兆速（Megaspeed）关联的公司交付 H200 芯片。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/11/19/business/economy/nvidia-chips-commerce-china-huang.html">Nvidia Asked to Sell Chips to Companies Tied to Chinese Military and...</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#export controls`, `#U.S.-China tech policy`

---

<a id="item-tech-news-14"></a>
### [TikTok 全球上线经第三方验证的深度伪造检测工具](https://www.straitstimes.com/world/tiktok-launches-tool-to-help-public-figures-detect-deepfakes-globally) ⭐️ 7.0/10

TikTok 于 2026 年 11 月 20 日全球上线 Likeness Detection 工具，面向经第三方身份验证的公众人物和头部创作者，可主动推送他人未经授权使用其形象生成 AI 内容的告警，并支持一键举报。同日推出公开透明检测工具，任何用户无需登录账号即可上传图片或视频，查询该媒体是否由 TikTok 自研 AI 功能生成。该工具已通过第三方验证，但未披露具体验证机构名称、检测准确率指标或支持的文件格式与大小限制。

telegram · zaihuapd · 11月20日 08:14

**「背景」** 欧盟《人工智能法案》已于 2024 年生效，其中第 52 条明确要求自 2026 年 8 月起，所有在欧盟境内发布的生成式 AI 内容必须清晰标注为 AI 生成；TikTok 此次工具上线时间（2026 年 11 月）紧随该强制标注期启动之后，并明确提及服务于 2027 年欧洲多国选举的可信信息环境。

**「影响」** 经验证的公众人物可首次获得 TikTok 主动推送的本人形象被滥用生成 AI 内容的实时告警，但该功能仅限第三方验证用户启用，未验证的普通用户及中小创作者无法接收此类通知，存在保护覆盖不均的实际缺口。

**「社区讨论」** 无可用社区评论，无法总结实质性讨论。

**标签**: `#AI safety`, `#deepfakes`, `#content provenance`, `#social media policy`, `#regulatory compliance`

---

<a id="item-tech-news-15"></a>
### [苹果研发自主 AI 智能体，最早 2027 年末推出](https://www.bloomberg.com/news/articles/2026-11-19/apple-is-working-on-ai-agent-for-device-control-apps-browsing-and-coding) ⭐️ 7.0/10

苹果正在内部研发一款原生 AI 智能体，具备代写代码、网页浏览和跨应用控制能力，项目处于早期阶段；该智能体最早将于 2027 年末随产品发布。招聘信息显示苹果正招募高级工程经理主导「主动式 AI 智能体」开发，同时 macOS 27.3 版本已将第三方 AI 智能体获取 Mac 系统控制权限的授权步骤从 4 步增至 14 步，以强化安全管控。

telegram · zaihuapd · 11月20日 08:59

**「AI 智能体的定义与行业进展」** AI 智能体（AI agent）指能自主感知环境、规划行动并执行任务（如调用工具、操作界面、生成代码）的软件系统，区别于单次响应式大模型交互。Meta Muse 和 OpenAI 的 Operator 等第三方智能体已进入公测阶段，支持跨应用自动化操作；苹果此前未发布任何原生 AI 智能体产品，其 AI 能力长期集中于设备端 Siri 优化和 iOS/macOS 中的局部功能增强。

**标签**: `#AI agents`, `#Apple`, `#system security`, `#developer tools`, `#OS integration`

---

<a id="item-tech-news-16"></a>
### [OpenAI 推出后台模式：长任务异步执行，token 费用最高降 40%](https://developers.openai.com/api/docs/guides/background) ⭐️ 7.0/10

OpenAI 推出实验性后台模式（background mode），允许开发者通过设置 background: true 并指定 background\_options.completion\_window 为 2 小时或 8 小时，将长耗时请求转为异步执行；对应 token 单价分别比标准同步请求低 30% 和 40%；该功能目前仅在 GPT-6.2 Astra、GPT-6.2 Sol、GPT-6.1 Terra 和 GPT-6 Luna 四个模型上开放公测；即使显式设置 store: false 或启用零数据保留策略，响应数据仍会被临时存储。

telegram · zaihuapd · 11月20日 11:15

**「GPT-6 系列模型的演进」** GPT-6.2 Astra 和 Sol 是 OpenAI 于 2026 年 11 月 18 日左右发布的最新前沿模型，分别面向高难度任务和日常高效使用；GPT-6.1 Terra 和 GPT-6 Luna 则是此前发布的同代模型变体，均已支持改进的对话风格与技术场景表现。

**「影响」** 使用上述四款 GPT-6 系列模型的开发者可立即通过修改请求参数启用异步执行并获得明确折扣，但需注意响应数据临时存储不受 store 配置控制，可能影响对数据驻留有严格合规要求的应用场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-2-astra-sol/">Introducing GPT-6.2 Astra and Sol | OpenAI</a></li>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT‑6 Sol and Luna - OpenAI</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-6.2-astra">GPT-6.2 Astra Model | OpenAI API</a></li>

</ul>
</details>

**标签**: `#LLM APIs`, `#cost optimization`, `#asynchronous processing`

---

<a id="item-tech-news-17"></a>
### [余承东澄清享界 V8 仅为 L2 辅助驾驶，否认可开车睡觉](https://weibo.com/1664176597/Rsi4xEGAA) ⭐️ 7.0/10

华为常务董事、终端 BG 董事长余承东于 2026 年 11 月 20 日晚间发文纠正其在当日鸿蒙智行享界 V8 发布会上的言论，明确指出享界 V8 当前实际交付并启用的是 L2 级辅助驾驶系统，虽已搭载 L3 级硬件能力，但 L3 功能尚未开放；驾驶员必须全程专注驾驶、按要求握持方向盘，严禁睡觉。

telegram · zaihuapd · 11月20日 12:55

**「自动驾驶分级标准与 L2/L3 关键区别」** SAE J3016 标准将自动驾驶分为 L0–L5 六级，其中 L2 要求驾驶员全程监控系统并随时接管，而 L3 在特定 ODD（运行设计域）内允许驾驶员脱手、脱眼，系统在失效时须提供充分接管提示。中国《汽车驾驶自动化分级》（GB/T 40429-2021）采用相同分级逻辑，但 L3 功能需通过工信部准入测试并获准上市后方可激活，目前尚无量产车在中国正式获批 L3 城区或高速全场景商用落地。

**「实际影响」** 该澄清直接关系到用户对车辆自动驾驶能力的正确认知与安全使用，意味着所有享界 V8 车主当前依法依规仅能使用 L2 功能，若依赖宣传中“可睡觉”的 L3 行为将构成严重误用和安全隐患，并可能影响车企在智能驾驶功能宣传中的合规边界。

**标签**: `#autonomous-driving`, `#ai-safety`, `#automotive-software`, `#regulatory-compliance`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [沃什拒绝前瞻指引，美联储官员发声激增](https://www.cnbc.com/2026/11/20/warsh-fed-forward-guidance-rate-hikes.html) ⭐️ 7.0/10

美联储主席凯文·沃什上任六个月内坚持不提供利率路径的前瞻指引，导致其他 18 名 FOMC 委员在近两周发表的公开言论数量创 2025 年以来新高；市场已据此定价 12 月至少加息 25 个基点（概率 100%）。

rss · CNBC Finance · 11月20日 15:20

**「背景」** 前瞻指引是美联储过去常用的做法，即通过明确暗示未来利率调整方向来引导市场预期；沃什认为此举会束缚决策灵活性，故主动摒弃，而此前惯例是由主席定调以弥合委员分歧。

**「影响」** 市场将纷杂的官员表态解读为鹰派信号，加剧短期利率波动，削弱美联储在通胀粘滞期的政策公信力与操作弹性。

**标签**: `#Federal Reserve`, `#monetary policy`, `#forward guidance`, `#inflation`, `#FOMC`

---

<a id="item-finance-news-2"></a>
### [美股公司转向净增发股票，冲击牛市](https://www.cnbc.com/2026/11/20/equity-issuance-bull-market-problem.html) ⭐️ 7.0/10

2026 年，美国上市公司从 2024 年的净股票回购转为净股权发行，截至近期，净增发规模达美股总市值的 3.1%；阿尔法贝特（Alphabet）6 月宣布 848 亿美元股权融资以支持 AI 基建。

rss · CNBC Finance · 11月20日 14:15

**「背景」** 过去两年企业资本配置行为发生结构性转变：此前因视股价被低估而持续回购，如今转向大规模增发，部分源于 AI 相关巨额资本开支需求。

**「影响」** 新增股票供给压制每股收益（EPS）并稀释股东权益，可能拖累美股牛市持续性，尤其对依赖回购支撑估值的投资者构成直接压力。

**标签**: `#equity\_issuance`, `#market\_supply`, `#corporate\_capital\_allocation`, `#AI\_investment`, `#bull\_market\_risk`

---

<a id="item-finance-news-3"></a>
### [特朗普与习近平亚太经合组织峰会会谈未解决关键分歧](https://www.cnbc.com/2026/11/20/apec-summit-trump-xi-china-trade-taiwan.html) ⭐️ 7.0/10

在 2026 年 11 月深圳 APEC 峰会期间，特朗普与习近平举行年内第三次双边会谈，但未宣布任何关税削减、稀土出口延期或半导体技术政策突破；台湾问题、美国对华先进芯片出口管制及所谓‘英伟达 CEO 涉间谍案’等虚假信息引发的争议均未获实质性回应。

rss · CNBC Finance · 11月20日 13:29

**「背景」** 2025 年 11 月，日本首相高市早苗称若台湾遭攻击可能触发日本自卫队行动，引发中日关系危机；此次她作为七年来首位访华的日本首相出席 APEC 深圳峰会，却遭遇中方冷淡接待。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2025%E2%80%932026_China%E2%80%93Japan_diplomatic_crisis">2025 –2026 China – Japan diplomatic crisis - Wikipedia</a></li>
<li><a href="https://www.theguardian.com/world/2025/nov/11/japan-china-row-takaichi-taiwan-conflict-military-deployment">Japan and China in growing row after PM Takaichi says Taiwan ...</a></li>
<li><a href="https://www.cnbc.com/2026/11/19/japan-china-trump-takaichi-taiwan-.html">China gives Takaichi chilly welcome on first Japan PM visit since 2019</a></li>

</ul>
</details>

**标签**: `#U.S.-China relations`, `#trade policy`, `#semiconductors`, `#geopolitics`, `#APEC`

---

<a id="item-finance-news-4"></a>
### [福特宣布正式进入电池制造业务](https://api3.cls.cn/share/article/2539395?sv=8.5.9) ⭐️ 7.0/10

福特已开始从密歇根州马歇尔的 BlueOval 电池工厂发运首批磷酸铁锂（LFP）方形电芯，用于 2027 年第四季度推出的 Fathom 电动皮卡；该工厂采用宁德时代授权技术，规划年产能约 20 吉瓦时。

telegram · zaihuapd · 11月20日 06:04

**「背景」** 此前福特依赖外部供应商提供电池，此次通过引进宁德时代 LFP 电芯技术并自建产线，首次实现电池电芯自主生产。

**标签**: `#electric-vehicles`, `#battery-technology`, `#us-china-trade`, `#automotive-manufacturing`, `#supply-chain`

---

<a id="item-finance-news-5"></a>
### [北京拟修订租房合同范本，禁止以正常损耗为由扣押金](https://mp.weixin.qq.com/s/PmGxh5knIyxiBRhpRoJnoQ) ⭐️ 7.0/10

北京市住建委与市场监管局于 11 月 20 日起就《北京市住房租赁合同（示范文本）（修订征求意见稿）》公开征求意见，拟明确规定承租人因正常使用导致的房屋正常损耗不承担赔偿责任，出租人不得据此扣减押金。

telegram · zaihuapd · 11月20日 13:46

**「背景」** 现行租赁实践中，部分房东常以‘磨损’为由克扣押金，引发大量租客投诉；此次修订系对 2021 年版示范文本的更新，属地方性合同规范调整，非强制性法律但具行业指导效力。

**标签**: `#housing\_policy`, `#consumer\_protection`, `#rental\_market`, `#regulatory\_proposal`

---