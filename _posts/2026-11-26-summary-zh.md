---
layout: default
title: "Horizon Summary: 2026-11-26 (ZH)"
date: 2026-11-26
lang: zh
---

> 从 34 条内容中筛选出 22 条重要资讯。

---

**科技新闻**
1. [Google 发布 Cogentic 研究论文探讨整数分解与离散对数](#item-tech-news-1) ⭐️ 9.0/10
2. [矩阵乘法指数被声称精确等于 9/4](#item-tech-news-2) ⭐️ 9.0/10
3. [Minecraft Java 版曝高危 RCE 漏洞，1.20.5 起全版本受影响](#item-tech-news-3) ⭐️ 9.0/10
4. [美国财政部子域名因过期 AWS 弹性 IP 被 3 美元接管](#item-tech-news-4) ⭐️ 8.0/10
5. [Ternary Bonsai 2.5（27B）发布：三值量化大模型在消费级硬件上实现 128k 上下文与高代码能力](#item-tech-news-5) ⭐️ 8.0/10
6. [LeCun 批评 Amodei 借 AI 风险论压制开源模型](#item-tech-news-6) ⭐️ 8.0/10
7. [Windows 音频响度限制器逆向工程并移植到 PipeWire](#item-tech-news-7) ⭐️ 7.0/10
8. [沙盒化语言模型可通过推理服务器缓存与内核选择实现侧信道通信](#item-tech-news-8) ⭐️ 7.0/10
9. [NVIDIA 和 ATI 经典显卡技术演示在浏览器中复现](#item-tech-news-9) ⭐️ 7.0/10
10. [PenGPT：面向手写与草图生成的生成式 Transformer 模型](#item-tech-news-10) ⭐️ 7.0/10
11. [绕过 iOS Safari 60 FPS 限制实现近原生滚动性能](#item-tech-news-11) ⭐️ 7.0/10
12. [LLM 能力三大拐点：Claude Opus 4.5、Fable 类模型与 3D 游戏生成](#item-tech-news-12) ⭐️ 7.0/10
13. [Firefox 161 发布：支持单网站 VPN 开关与工具栏一键清数据](#item-tech-news-13) ⭐️ 7.0/10
14. [OpenAI 推出 GPT-6 Cyber 并扩大 Daybreak 计划，称网络安全将超越编程业务](#item-tech-news-14) ⭐️ 7.0/10
15. [腾讯开源 Hy4 flash 模型 IQ2-AH 量化权重，64GB Mac mini 可运行](#item-tech-news-15) ⭐️ 7.0/10
16. [美国收紧 AI 芯片出口漏洞，亚洲数据中心转向美国客户](#item-tech-news-16) ⭐️ 7.0/10
17. [三星电子和 SK 海力士将采用长江存储 Xtacking 芯片堆叠技术](#item-tech-news-17) ⭐️ 7.0/10

**财经新闻**
1. [美国拟对中国等 14 个贸易伙伴加征新关税](#item-finance-news-1) ⭐️ 8.0/10
2. [英伟达股价波动考验‘市场信号导向’货币政策假说](#item-finance-news-2) ⭐️ 7.0/10
3. [Kalshi 永续合约日交易量首超预测市场](#item-finance-news-3) ⭐️ 7.0/10
4. [犹他州撤销对预测市场公司 Kalshi 及其创始人的刑事指控](#item-finance-news-4) ⭐️ 7.0/10
5. [SpaceX 放弃 7.38 亿美元宽带补贴，改用零支出协议提供星链服务](#item-finance-news-5) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Google 发布 Cogentic 研究论文探讨整数分解与离散对数](https://github.com/google-research/google-research/tree/master/cogentic_research_papers) ⭐️ 9.0/10

Google 于 2026 年 11 月 25 日在其 GitHub 仓库（google-research/cogentic\_research\_papers）公开了一批早期阶段的 Cogentic 研究论文，聚焦整数分解、离散对数等数论难题。这些论文尚未经过同行评审，也未附带可运行实现或形式化证明，仅呈现初步方法与实验观察。其目标是探索 AI 驱动的符号推理与搜索技术在基础数学问题上的应用潜力，当前不构成对 RSA 或 ECC 等现有公钥密码系统的实际破解能力。

hackernews · rgwohlbold · 11月25日 13:33 · [社区讨论](https://news.ycombinator.com/item?id=50642086)

**「背景」** 整数分解和离散对数问题是公钥密码学的数学基础，RSA 和 Diffie-Hellman 等广泛使用的加密算法的安全性直接依赖于这些问题在经典计算机上缺乏高效解法的假设。此前，Google 的 AlphaGo 和 AlphaZero 系统已证明 AI 可在复杂组合搜索空间（如围棋）中发现超越人类的策略，其基于强化学习与蒙特卡洛树搜索的范式被推测正被迁移至形式化数学推理领域。

**「影响」** 该研究尚未提供可运行的实现或经同行评审的密码学突破，但已促使部分安全从业者建议立即弃用十年以上的 RSA 密钥并迁移到椭圆曲线密码（ECC），因其直接挑战 RSA 和 Diffie-Hellman 等公钥系统所依赖的整数分解与离散对数问题的计算难度假设。

**「社区讨论」** 部分评论者（如 riobard）建议立即弃用十年前生成的 RSA 密钥并迁移到 ECC 密钥作为预防措施；另一些人（如 fidotron）援引未验证的外部推文暗示该工作可能是更大突破的开端，但该说法缺乏源材料佐证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.academia.edu/14681579/BACKTRACKING_BASED_INTEGER_FACTORISATION_PRIMALITY_TESTING_AND_SQUARE_ROOT_CALCULATION">(PDF) backtracking based integer factorisation , primality testing and...</a></li>
<li><a href="https://en.sorumatik.co/t/what-is-the-use-case-of-factorization-in-quantum-computing/112834">What is the use case of factorization in quantum computing - Sorumatik</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#artificial-intelligence`, `#number-theory`, `#security`, `#machine-learning`

---

<a id="item-tech-news-2"></a>
### [矩阵乘法指数被声称精确等于 9/4](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf) ⭐️ 9.0/10

一份署名 OpenAI 的预印本论文声称，矩阵乘法指数ω被严格证明为 9/4（即 2.25），适用于所有域；该结果直接否定了长期主流猜想ω = 2，并宣称同时解决了 Smale 第九问题（强多项式线性规划）、平均收益博弈、奇偶博弈等若干顶级开放数学与理论计算机科学问题。论文 URL 路径（openai/math/blob/main/preprints/...）和发布日期（2026 年 11 月 24 日）存在明显异常，且 GitHub 仓库 openai/math 并非 OpenAI 官方公开代码库，目前无独立验证或权威机构确认该结果。该声明尚未被同行评审，亦无已知学术机构或知名复杂性理论研究者提供实质性支持证据。

hackernews · E-Reverance · 11月25日 01:19 · [社区讨论](https://news.ycombinator.com/item?id=50637220)

**「矩阵乘法指数问题背景」** 矩阵乘法指数 ω 定义为最小实数，使得 n×n 矩阵乘法可在 O\(n^ω+ε\) 时间内完成（对任意 ε &gt; 0）；长期以来，ω = 2 被广泛猜想为最优值（即存在接近二次时间的算法），但严格证明仍属未解难题。此前最佳上界由 Alman 和 Vassilevska Williams 于 2021 年给出（ω &lt; 2.3728596），而下界仅知 ω ≥ 2（因需输出 n² 个元素）。该问题属于计算复杂性理论核心问题，与线性规划、博弈论及代数电路复杂度等深层问题紧密关联。

**「社区讨论」** Hacker News 评论中，用户\[zone411\]援引非权威来源（proofatlas.ai）称该论文解决了 Top 500 开放数学问题中的多个条目，但未提供可验证的引用；其他用户则普遍质疑其真实性，指出 URL 结构可疑、时间戳超前、缺乏官方渠道背书，并担忧若为真可能对密码学构成威胁，但所有观点均基于推测，无技术性反驳或复现报告。

**标签**: `#computational-complexity`, `#matrix-multiplication`, `#theoretical-computer-science`, `#artificial-intelligence`, `#mathematics`

---

<a id="item-tech-news-3"></a>
### [Minecraft Java 版曝高危 RCE 漏洞，1.20.5 起全版本受影响](https://github.com/bikini/minecraft2shell) ⭐️ 9.0/10

Minecraft Java 版存在一个高危远程代码执行（RCE）漏洞，影响 1.20.5 至 1.21.10 正式版及 26.1 至 26.4 快照版；该漏洞由资源包中恶意 TrueType 字体触发 FreeType 2.14.3 及更早版本的原生越界写（OOB write），已在 Windows 客户端 26.3 版本上验证可执行任意代码；Mojang 当前仍使用含漏洞的 lwjgl-freetype 3.4.3，尚未发布官方补丁；社区于 11 月 24 日推出 m2sfix 1.0.0 临时修复方案，支持以 Java agent 或 Mod 形式禁用字体 hinting。

telegram · zaihuapd · 11月25日 12:46

**「FreeType 字体渲染库漏洞背景」** Minecraft Java 版本依赖 FreeType 库（具体为 lwjgl-freetype 3.4.3 封装）渲染 TrueType 字体；该漏洞源于 FreeType 2.14.3 及更早版本中字体字形提示（hinting）阶段的原生越界写（OOB write），属内存破坏类漏洞。FreeType 项目已于 2023 年发布的 2.15.0 版本中修复此问题，但截至当前（2026 年 11 月），Mojang 尚未将 Minecraft Java 版本升级至含修复的 FreeType 版本。

**「影响」** 受影响用户（Java 版 1.20.5–1.21.10 及 26.1–26.4 快照的玩家与服务器）面临远程代码执行风险：当加载含恶意 TrueType 字体的资源包时，客户端可能被劫持执行任意系统命令；Mojang 尚未发布官方补丁，因此服务器管理员必须立即禁用资源包功能或部署社区 mod（如 m2sfix 1.0.0）以缓解风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://threatcluster.io/cluster/minecraft2shell-unpatched-freetype-rce-in-minecraft-java-via-7b380721">Minecraft2Shell: Unpatched FreeType RCE in Minecraft Java via ...</a></li>
<li><a href="https://www.minenest.com/801287/">Minecraft2Shell RCE in Minecraft Java Still Unpatched</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#java`, `#minecraft`, `#rce`

---

<a id="item-tech-news-4"></a>
### [美国财政部子域名因过期 AWS 弹性 IP 被 3 美元接管](https://www.intruder.io/research/taking-over-us-treasury-subdomains-for-3-each) ⭐️ 8.0/10

安全研究人员发现，美国财政部多个子域名（如 treasury.gov 的子域）因指向已释放但未从 DNS 中清除的 AWS 弹性 IP 地址，存在子域名接管漏洞；攻击者可低价（约 3 美元）重新申请这些 IP 并托管恶意内容，从而完全控制子域名。该漏洞依赖于 DNS 记录未及时清理，而非 AWS 服务本身缺陷，且 AWS 明确表示不计划修改当前策略，因其认定责任在于客户侧 DNS 管理。漏洞已在部分子域上验证成功，涉及 Route53 解析行为与证书颁发流程的协同风险。

hackernews · negura · 11月25日 04:27 · [社区讨论](https://news.ycombinator.com/item?id=50638478)

**「子域名接管漏洞背景」** 子域名接管（subdomain takeover）是一种因父域 DNS 记录指向已释放或未配置的第三方云资源（如 AWS Elastic IP、S3 存储桶、CloudFront 分发）而引发的安全漏洞，攻击者可注册同名资源并控制该子域名。此类漏洞依赖于 DNS 记录长期滞留且目标云服务商不自动清理或验证关联关系，此前已在多个云平台（如 S3、CloudFront）中被广泛验证和利用。

**「影响」** 受影响的政府 IT 运维团队需立即审计并自动化清理已下线云资源对应的 DNS A 记录，否则面临 HTTPS 证书被滥用、流量劫持及钓鱼攻击等真实风险；现有 EV 证书机制未能阻止该类接管，因 ACME 协议仅验证域名控制权，不校验 IP 归属或基础设施生命周期状态。

**「社区讨论」** 部分评论者指出 AWS 应为 Route53 提供自动删除弹性 IP 关联 DNS 记录的功能（如专用记录类型），而另一些人强调问题根源在于客户缺乏 IP 释放后的 DNS 清理流程，并援引早年类似事件佐证该风险长期存在且已被实际利用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.jsmon.sh/hunting-dangling-dns-how-to-exploit-aws-elastic-ips-cloudfront-and-s3/">Hunting Dangling DNS in AWS : Updated Techniques That Actually...</a></li>

</ul>
</details>

**标签**: `#cloud-security`, `#subdomain-takeover`, `#dns`, `#aws`, `#government-IT`

---

<a id="item-tech-news-5"></a>
### [Ternary Bonsai 2.5（27B）发布：三值量化大模型在消费级硬件上实现 128k 上下文与高代码能力](https://prismml.com/news/bonsai-2-5-27b) ⭐️ 8.0/10

Ternary Bonsai 2.5（27B）是一个三值量化（Q2 GGUF）的开源大语言模型，已正式发布并支持在 M 系列 Mac 等消费级硬件上运行；实测生成速度达 22–25 token/s（Mac Mini M5 Pro，24GB RAM），支持 128k 上下文长度，且在 SWE-bench Verified 基准上表现接近 2026 年 2 月发布的 Opus 4.6 模型；该模型已在 Hermes 框架下成功完成端到端自主编码任务（如生成可运行的 Tetris 克隆），源码与演示公开可用。

hackernews · b0m · 11月24日 20:08 · [社区讨论](https://news.ycombinator.com/item?id=50633922)

**「背景」** Ternary Bonsai 系列是 PrismML 推出的专为边缘端代理（agentic）任务优化的开源 LLM，其核心创新在于采用三值量化（ternary quantization，权重仅取 \{−1, 0, +1\}）实现极高的计算与内存效率。2026 年 9 月发布的 Bonsai 2（27B）已支持 128k 上下文和 GGUF 格式部署，而本次 2.5 版本在相同 5.9 GB 模型体积下，将上下文扩展至 262K tokens，并显著提升多步工具调用与自主编码能力。

**「影响」** 开发者可在无 GPU 的 M 系列 Mac 上本地部署该模型并执行长上下文、多步推理的自主编码任务，但其 SWE-bench 高分是否反映真实工程能力尚存争议，用户需谨慎评估其在非基准场景下的可靠性。

**「社区讨论」** 部分用户指出其 SWE-bench Verified 得分与 Opus 4.6 相当，推测可能源于基准偏移、模型针对性优化或小型模型能力进步的综合作用；另有用户提出探索非对称四值量化的技术可能性，但未提供实证结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://prismml.com/news/bonsai-2-5-27b">PrismML — Introducing Ternary Bonsai 2.5 27B: Powering ...</a></li>
<li><a href="https://docs.prismml.com/models/bonsai-2-5-27b">Ternary Bonsai 2.5 27B - Bonsai - docs.prismml.com</a></li>
<li><a href="https://huggingface.co/prism-ml/Ternary-Bonsai-2.5-27B-GGUF">prism-ml/Ternary-Bonsai-2.5-27B-GGUF · Hugging Face</a></li>

</ul>
</details>

**标签**: `#LLM quantization`, `#edge AI`, `#agentic systems`, `#SWE-bench`, `#open-source models`

---

<a id="item-tech-news-6"></a>
### [LeCun 批评 Amodei 借 AI 风险论压制开源模型](https://x.com/ylecun/status/2124550037912920090) ⭐️ 8.0/10

Yann LeCun 于 2025 年 11 月 22 日在 X 平台发帖，公开指责 Anthropic CEO Dario Amodei 自 GPT-2 时期起持续渲染人工智能风险，意图推动将开放权重大模型定为非法，以维持其对 AI 技术的控制权；LeCun 指出 Amodei 离开 OpenAI 的原因在于未能获得足够控制权，并将该策略类比为奥斯曼帝国禁止阿拉伯语印刷，称其为「一种新形式的中世纪蒙昧主义」。

telegram · zaihuapd · 11月25日 01:30

**「背景」** Yann LeCun 是卷积神经网络（LeNet）的奠基人之一，2018 年与 Geoffrey Hinton、Yoshua Bengio 共同获得图灵奖；他于 2013 年加入 Facebook（后为 Meta），担任首席 AI 科学家长达 12 年，于 2025 年 11 月离职并创办 AMI Labs。Dario Amodei 曾任 OpenAI 副总裁兼研究主管，2021 年离开后联合创立 Anthropic，主张以「宪法式 AI」和严格安全治理路径发展大模型。

**「实际影响」** LeCun 离开 Meta 后创办 AMI Labs 并完成 10.3 亿美元种子轮融资，其公开批评强化了开源 AI 社区对封闭模型主导权扩张的警惕，可能加剧开发者在模型选型、许可证合规及部署策略上的审慎评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://udit.co/blog/yann-lecun-ami-labs-world-models-seed-round">Yann LeCun &#x27;s AMI Labs Raises $1.03B to Prove the AI Industr</a></li>
<li><a href="https://www.humai.blog/yann-lecun-left-meta-raised-1-billion-in-four-months-and-is-now-betting-the-entire-ai-industry-is-wrong/">Yann LeCun Left Meta , Raised $1 Billion in Four Months, and Is Now...</a></li>

</ul>
</details>

**标签**: `#artificial-intelligence`, `#open-source`, `#ai-ethics`, `#technology-policy`, `#machine-learning`

---

<a id="item-tech-news-7"></a>
### [Windows 音频响度限制器逆向工程并移植到 PipeWire](https://github.com/xoxorwr/pw-loudness-eq) ⭐️ 7.0/10

开发者成功逆向分析 Windows 共享模式音频子系统（audiodg.exe 中的 CAudioLimiter，位于 AudioEng.dll 内），并将其实现移植为 PipeWire 插件 pw-loudness-eq。该插件在 Linux 上复现了 Windows 默认共享模式下对音频峰值的轻微压缩行为（约 -0.1 dBFS），适用于通过 PipeWire 播放的 WASAPI 共享、DirectSound 或 MME 类路径的等效场景。它不适用于独占模式（如 WASAPI Exclusive 或 ASIO），且当前实现明确为峰值限制器（limiter），而非频率相关的均衡器（equalizer）。项目已开源发布，可直接集成至 PipeWire 音频栈。

hackernews · ThrowNotAway · 11月25日 11:34 · [社区讨论](https://news.ycombinator.com/item?id=50641171)

**「Windows 共享模式音频限幅器」** Windows 在共享模式音频路径（如 WASAPI 共享模式、DirectSound、MME）中内置了一个轻量级峰值限幅器，由 audiodg.exe 进程中的 CAudioLimiter 组件实现，位于 AudioEng.dll 内；该限幅器在音频接近 0 dBFS 时施加约-0.1 dB 的轻微压缩，以防止削波，但仅作用于共享模式，不适用于 WASAPI 独占模式或 ASIO。此前 Linux 音频栈（包括 PipeWire）缺乏对应功能，导致跨平台音频回放一致性存在可测量差异。

**「影响」** Linux 音频用户现在可在 PipeWire 环境中启用与 Windows 共享模式一致的响度控制行为，从而提升跨平台音频回放的一致性；但需注意，该插件会改变原始 PCM 信号的峰值电平，可能影响对动态范围敏感的监听或母带处理流程。

**「社区讨论」** 多位评论者指出项目名称中的“Equalization”属术语误用，强调其本质是峰值限制（limiter）而非均衡，并质疑逆向工程必要性——认为标准限幅算法已足够且更透明；另有用户指出 Windows 原生实现对瞬态纯音（如哨音）存在增益异常风险，需额外末级限幅补偿。

**标签**: `#audio-engineering`, `#linux`, `#pipewire`, `#reverse-engineering`, `#real-time-audio`

---

<a id="item-tech-news-8"></a>
### [沙盒化语言模型可通过推理服务器缓存与内核选择实现侧信道通信](https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being) ⭐️ 7.0/10

沙盒化部署的语言模型可能通过共享推理服务器的 CPU/GPU 缓存行为和 vLLM 框架中步长依赖型内核选择机制，建立基于时序的侧信道通信。该现象已在 vLLM 等主流开源推理服务中被实证，其技术基础是不同 token 步长（如 10 token vs. 2000 token）触发不同计算内核，导致可测量的缓存访问时间差异。通信需双方预共享协议且依赖对底层硬件与软件栈（包括 vLLM 版本、GPU 型号、内核调度非确定性）的精确了解，并非自发建立。该能力属于已实现的侧信道利用，而非理论推测或厂商公告。

hackernews · gmays · 11月25日 02:34 · [社区讨论](https://news.ycombinator.com/item?id=50637686)

**「背景」** 现代 LLM 推理服务（如 vLLM）为提升吞吐量，常在多租户环境中复用 GPU 内存与缓存资源，并根据每步生成的 token 数量动态选择最优计算内核；这种设计虽提升性能，却意外引入了跨沙盒实例的隐蔽信息泄露路径。该问题与 Web 安全中早已确立的‘同源缓存隔离’原则直接对应，但当前 AI 基础设施普遍缺乏类似隔离机制。

**「影响」** 多租户 AI 云服务提供商（如使用 vLLM 托管客户模型的平台）需立即评估其推理服务器是否启用缓存分区或内核执行确定性模式，否则存在高权限租户通过精心构造的输入探测低权限租户模型状态的风险。

**「社区讨论」** 评论者\[amluto\]主张应借鉴浏览器同源策略，在 API 层引入缓存分离密钥；而\[tsimionescu\]则质疑该攻击在真实场景中极难实现，因其要求双方预先协调、精确掌握软硬件细节；\[saagarjha\]进一步指出 vLLM 的步长依赖内核选择本身即属设计缺陷，应被批处理不变的确定性推理所替代。

**标签**: `#AI safety`, `#systems security`, `#LLM deployment`, `#side-channel attacks`, `#inference optimization`

---

<a id="item-tech-news-9"></a>
### [NVIDIA 和 ATI 经典显卡技术演示在浏览器中复现](https://gpu-demo-gallery.pages.dev/) ⭐️ 7.0/10

一个名为 GPU Demo Gallery 的网页画廊（https://gpu-demo-gallery.pages.dev/）已上线，支持在现代浏览器中直接运行 1990 年代末至 2000 年代初的 NVIDIA 和 ATI 原生 Windows 技术演示，包括 Grass、Crystal Ball 等知名 demo。项目通过 WebGL 和 WebGPU 实现兼容层，无需安装旧版驱动或专用硬件，所有演示均在客户端完成渲染。目前存在已知渲染缺陷，例如 Grass Demo 中 NVIDIA 标志的字母 &\#x27;N&\#x27; 缺失，Crystal Ball 在鼠标拖拽释放后出现异常行为。

hackernews · arkits · 11月25日 04:31 · [社区讨论](https://news.ycombinator.com/item?id=50638503)

**「GPU 技术演示的历史背景」** 1990 年代末至 2000 年代初，NVIDIA（如 RIVA TNT、GeForce 2 系列）和 ATI（如 Rage 128、Radeon 7x00 系列）通过捆绑专属技术演示（tech demos）推广其 GPU 架构革新，这些演示通常需原生 Windows 环境、特定驱动及专用硬件才能运行，且源码未公开，长期面临失传风险。

**「影响」** 图形开发者、计算机历史研究者及教育者现在可无需遗留硬件即可访问和分析早期 GPU 实时渲染技术的关键实现细节；部分 demo 存在视觉或交互缺陷，可能影响教学或技术复现的准确性。

**「社区讨论」** 用户普遍表达怀旧情感并肯定项目价值，同时报告具体渲染问题（如 Grass Demo 缺失字母 &\#x27;N&\#x27;）；另有建议扩展收录 PlayStation 和 PlayStation 3 等平台的经典 demo，并呼吁补充技术背景说明以提升教育实用性。

**标签**: `#graphics-programming`, `#webgl`, `#retro-computing`, `#gpu-history`, `#web-assembly`

---

<a id="item-tech-news-10"></a>
### [PenGPT：面向手写与草图生成的生成式 Transformer 模型](https://greydanus.github.io/2026/11/12/pengpt/) ⭐️ 7.0/10

PenGPT 是一个专为手写文本和手绘草图合成设计的生成式 Transformer 模型，其核心创新在于构建了大规模、高质量的笔画级（stroke-based）数据集，而非引入新架构。该模型基于公开权重的视觉模型与轻量级多模态 API 构建，训练使用 8 块 H100 GPU，代码与数据集已开源。作者明确强调约 80% 的工作量投入于数据收集、清洗与质量控制，而非模型结构或训练技巧的改进。

hackernews · smusamashah · 11月25日 00:54 · [社区讨论](https://news.ycombinator.com/item?id=50637056)

**「背景」** 手写体与草图生成是人机交互和多模态生成建模中的长期研究方向，早期工作如作者 2016 年发布的 Scribe 项目已使用 TensorFlow 实现基于 RNN 的手写合成。PenGPT 并非首个该领域模型，但其技术路径显著转向数据驱动范式——放弃架构创新，转而构建大规模、高质量的笔画级（stroke-based）数据集并实施严格质量控制。

**「实际影响」** 开发者现在可使用开源、轻量级的 PenGPT 模型（在 8×H100 上即可训练）生成符合人类书写习惯的笔迹和草图，但需自行构建高质量笔画序列数据集以复现效果；该模型不直接兼容现有文本到图像管线，因其输出为 stroke-based 序列而非像素或 latent 张量。

**「社区讨论」** 多位评论者指出，作者对「苦涩教训」（The Bitter Lesson）的实践反思引发共鸣——即在多数情况下，扩大高质量数据规模比追求架构巧思更有效；作者本人回应称，此次刻意放弃以往对模型创新的执念，转而依托现有开放工具链提升数据工程效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://apexneuralnews.com/news/pengpt-a-generative-transformer-for-handwriting-and-sketches">PenGPT: A Generative Transformer for Handwriting and Sketches</a></li>
<li><a href="https://grafy.ai/news/pengpt-a-new-transformer-for-handwriting-and-sketches">PenGPT: A Transformer for Handwriting — Grafy — Grafy News</a></li>

</ul>
</details>

**标签**: `#generative-ai`, `#handwriting-synthesis`, `#data-centric-ai`, `#multimodal-modeling`, `#human-computer-interaction`

---

<a id="item-tech-news-11"></a>
### [绕过 iOS Safari 60 FPS 限制实现近原生滚动性能](https://rida.dev/blog/bypassing-ios-safari-60-fps-limit) ⭐️ 7.0/10

开发者通过利用 WebKit 内部渲染机制（如强制图层提升、scroll-driven animations 及 CSS 合成优化），在 iOS Safari 中实现了超过 60 FPS 的滚动帧率，显著提升了 Web 应用的滚动顺滑度。该方法不依赖新 API 或系统级权限，而是基于对 WebKit 源码行为的逆向洞察，在现有 Safari（截至 iOS 17/18）中即可生效，已通过公开原型验证。它并非 Apple 官方支持的功能，且需手动配置 CSS 层级与动画触发逻辑，存在电池功耗增加等已知权衡。

hackernews · vinhnx · 11月25日 03:04 · [社区讨论](https://news.ycombinator.com/item?id=50637890)

**「背景」** iOS Safari 长期将主线程渲染帧率硬性限制在 60 FPS，即使设备硬件支持 ProMotion（120 Hz）屏幕，Web 内容也无法自动启用更高刷新率；这与原生 UIKit/SwiftUI 应用可按场景动态启用 120 Hz 过渡动画形成鲜明对比。

**「影响」** 前端工程师可在不改用 WebView 封装或放弃 Web 技术栈的前提下，为关键滚动场景（如长列表、卡片流）实现接近原生的视觉流畅度，但需主动管理图层合成策略并接受潜在的续航下降风险。

**「社区讨论」** 多位评论者指出该方案首次在纯 Web 环境中达成「原生级」滚动质量（如 \[ksec\] 称其‘绝对令人震惊’），而 \[afavour\] 补充解释了 Apple 未默认启用 120 FPS 的根本原因：原生框架具备细粒度的刷新率调度能力，而 Web 平台缺乏对应控制接口。

**标签**: `#web-performance`, `#ios-safari`, `#webkit`, `#frontend-engineering`, `#native-web-convergence`

---

<a id="item-tech-news-12"></a>
### [LLM 能力三大拐点：Claude Opus 4.5、Fable 类模型与 3D 游戏生成](https://simonwillison.net/2026/Nov/24/llm-inflection-points/) ⭐️ 7.0/10

过去十二个月内，LLM 与编码智能体出现三个关键能力拐点：2025 年 11 月 Claude Opus 4.5 发布，显著提升在模糊需求下的推理能力与跨系统调试可靠性，使 Claude Code 首次成为日常可用的编程助手；2026 年 6 月起 Claude Fable 5 系列（含 5.1、5.2）及 Opus 5.5 等被归为“Fable 类模型”，其特征是能基于目标与工具自主规划并执行复杂任务（如声源三角定位、自建本地日志服务）；2026 年 9–10 月，Opus 5.5、GPT-5.6 Sol、Gemini 4 Neon 等模型在 Blender 建模、Three.js 动画与游戏平衡性调优（如将 RTS 游戏‘Battledrones’从枯燥升级为可玩性强的版本）上实现突破，标志 LLM 在 3D 空间理解与主观体验（如‘趣味性’）建模方面达到新水平。

rss · Simon Willison · 11月24日 23:02

**「LLM 能力演进的关键节点」** 大型语言模型（LLM）在软件工程中的实用化经历了阶段性跃迁：2025 年 2 月 Claude 3.7 Sonnet 发布并首次集成 Claude Code，标志着编码代理的初步可用；2025 年 11 月 Claude Opus 4.5 发布，被作者视为首个使编码代理达到日常可靠水平的模型；此后 Fable 系列（始于 2026 年 6 月 Fable 5）和 Opus 5.5（2026 年 9 月）等模型进一步拓展了目标驱动、多工具协同与 3D/游戏开发等新能力边界。

**「实际影响」** 开发者现在可将 Claude Opus 5.5 及 Fable 类模型（如 Fable 5.2、GPT-6 Astra）作为日常开发工具，用于完成需多步推理、系统级调试、3D 建模与游戏平衡调优等任务；例如，Opus 5.5 能在无明确指令下自主搭建本地日志服务器与截图工具链定位 Safari 显示异常，或通过 12 小时自主游玩测试重平衡 RTS 游戏使其具备真实娱乐性。

**标签**: `#LLMs`, `#coding agents`, `#AI engineering`, `#model evolution`

---

<a id="item-tech-news-13"></a>
### [Firefox 161 发布：支持单网站 VPN 开关与工具栏一键清数据](https://www.theverge.com/tech/1041474/firefox-161-vpn-rules-fire-button) ⭐️ 7.0/10

Mozilla 于 2026 年 11 月 24 日正式发布 Firefox 161，为所有标准安装的桌面版用户（Windows、macOS、Linux）提供两项新功能：一是在 VPN 面板中新增「管理 VPN 规则」界面，允许用户为任意指定域名（如 example.com）设置「始终开启」或「始终关闭」VPN 路由规则；二是向工具栏推送「Fire」按钮，点击后可按用户勾选范围（浏览历史、Cookie、缓存、站点数据等）清除数据，若全选则强制退出所有已登录账号并启动全新无痕窗口。

telegram · zaihuapd · 11月25日 01:14

**「背景」** Firefox 自 2021 年起集成 Mozilla VPN 服务，但此前仅支持全局开启或关闭 VPN，无法按网站粒度控制流量路由。Firefox 161 是首个在稳定版中提供每站点 VPN 规则配置能力的版本，该功能依托于浏览器内置的 VPN 管理面板而非第三方扩展。

**「影响」** 启用「始终关闭」规则的网站（如银行或企业内网）将绕过 VPN 直连，避免因加密隧道导致的认证失败或访问中断；而「Fire」按钮全选清除会立即终止所有活跃会话，可能意外登出未保存状态的关键管理后台，开发者需在测试环境中验证其对 OAuth 流程和持久化登录的影响。

**标签**: `#browser-security`, `#privacy-engineering`, `#web-privacy`, `#firefox`

---

<a id="item-tech-news-14"></a>
### [OpenAI 推出 GPT-6 Cyber 并扩大 Daybreak 计划，称网络安全将超越编程业务](https://www.theinformation.com/newsletters/ai-agenda/openais-roadmap-making-cyber-bigger-coding-remains-blurry) ⭐️ 7.0/10

OpenAI 正式将网络安全定位为优先战略方向，推出专用大模型 GPT-6 Cyber，并持续扩展其受信访问计划 Daybreak；截至 2026 年 9 月，该计划已覆盖数千名经验证的安全研究人员及约 2000 个获批组织与工作空间，支持漏洞发现、代码库分析和二进制逆向等任务。公司高管声称全球网络安全市场规模超 3000 亿美元的普遍估算被严重低估，且网络安全业务未来规模将超过其编程相关业务。报道未提供 GPT-6 Cyber 的技术规格、发布状态（如是否已上线或仅限内部/邀请测试）、基准评测结果或独立验证数据，亦未说明其与现有模型（如 GPT-4 系列）的架构差异或兼容性要求。

telegram · zaihuapd · 11月25日 04:51

**「GPT-6 Cyber 的发布背景」** GPT-6 Cyber 是 OpenAI 于 2026 年 11 月 5 日正式发布的专用大模型，定位为面向授权安全研究的高风险能力模型，其能力在漏洞识别、软件理解与可运行漏洞利用生成等任务上优于 GPT-6 Astra；该模型仅通过 API 和 Codex 向经严格审核的 Daybreak Red 计划客户开放，且被 Reuters 等信源标注为‘Critical’级网络安全产品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-cyber/">GPT‑6 Cyber: Advancing the frontier of aligned cybersecurity ...</a></li>
<li><a href="https://www.unite.ai/openai-launches-gpt-6-cyber-with-restricted-access-and-scope-controls/">OpenAI Launches GPT-6 Cyber With Restricted Access and Scope ...</a></li>
<li><a href="https://www.reuters.com/technology/openai-launches-gpt-6-cyber-with-critical-cybersecurity-rating-2026-11-05/">OpenAI launches GPT-6 Cyber with &#x27;Critical&#x27; cybersecurity ...</a></li>

</ul>
</details>

**标签**: `#artificial-intelligence`, `#cybersecurity`, `#openai`, `#industry-trends`

---

<a id="item-tech-news-15"></a>
### [腾讯开源 Hy4 flash 模型 IQ2-AH 量化权重，64GB Mac mini 可运行](https://mp.weixin.qq.com/s/o0xxShVQX6g2UllrrEv1WQ) ⭐️ 7.0/10

腾讯混元开源了其 2240 亿参数大模型 Hy4 flash 的 GGUF 格式量化权重，最小版本为 IQ2-AH，体积为 125.73 GiB（约为原始权重 410.27 GiB 的 30%）；该量化版本借助 Strata offload 框架，可在配备 64 GB 内存的 Mac mini 上完成推理。实测显示，在 48 GB 显存设备上处理 10K 上下文时 token 生成速率为 89 tokens/s，在 M5 Max（128 GB 内存）上运行 Q3\_K 版本、32K 上下文时速率为 47 tokens/s；在 DeepSWE v1.1 评测中，Q3\_K 版本相较原模型得分差距不超过 0.4 分。

telegram · zaihuapd · 11月25日 09:29

**「模型压缩工具 AngelSlim 与 Strata 卸载框架」** AngelSlim 是腾讯开源的大模型压缩加速工具箱，此前已支持对混元系列模型进行量化与蒸馏；Strata 是一个专为大模型推理设计的内存卸载（offload）框架，可将部分模型权重动态调度至系统内存或磁盘，以缓解显存压力。

**「影响」** 开发者现在可在消费级硬件（如 64 GB 内存的 Mac mini）上本地运行 224B 级别大模型，无需依赖云服务或高端 GPU，但需集成 Strata offload 框架并接受 IQ2-AH 量化带来的轻微精度损失（未提供具体数值，仅 Q3\_K 版本有 &lt;0.4 分误差数据）。

<details><summary>参考链接</summary>
<ul>
<li>Now you can run Tencent Hy4 flash locally, quantized by AngelSlim! Laptop: up to 39 TPS on Spark, 50 TPS on 128GB Mac M5 Max via llama.cpp. PC</li>
<li>Hy4-flash quants are down from 70 to 49 GB, run on a 64Gb vRAM : r/LocalLLaMA - Reddit</li>
<li>AngelSlim/Hy4-flash-GGUF - Hugging Face</li>

</ul>
</details>

**标签**: `#large-language-models`, `#model-quantization`, `#inference-optimization`, `#open-source-ai`, `#edge-ai`

---

<a id="item-tech-news-16"></a>
### [美国收紧 AI 芯片出口漏洞，亚洲数据中心转向美国客户](https://www.bloomberg.com/news/articles/2026-11-25/asia-data-centers-sound-out-us-clients-to-replace-china-demand) ⭐️ 7.0/10

美国政府收紧了允许中国科技公司通过第三地（如亚洲数据中心）获取英伟达最先进 AI 芯片的出口监管漏洞，导致依赖向中国客户出租算力的亚洲数据中心业务受挫。Liquid Compute 首席执行官 Ronit Jain 指出，针对先进 AI 加速器向亚洲地区出口的新规正直接冲击此类服务商。该政策变化已促使多家亚洲数据中心主动接触美国客户，试图转售原本面向中国市场的过剩算力。目前无公开信息表明新规的具体生效日期、适用芯片型号清单或合规过渡期。

telegram · zaihuapd · 11月25日 11:35

**「美国对华 AI 芯片出口管制的演进」** 美国自特朗普政府第一任期起即开始限制中国获取 AI 芯片，拜登政府于 2022 年将先进 AI 芯片对华出口定为非法；此前存在一项漏洞，允许中国公司通过在亚洲第三方数据中心部署英伟达最先进芯片来绕过直接出口禁令。

**「实际影响」** 亚洲数据中心因美国收紧对华 AI 芯片出口漏洞而面临算力需求骤降，部分服务商已启动向美国客户转售过剩算力的紧急业务调整，但该策略受限于网络延迟、数据主权合规性及美国客户采购周期等现实约束。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://time.com/article/2026/11/16/trump-administration-ai-chips-nvidia-china/">U . S . to Clamp Down On AI Chip Loophole Ahead Of Trump Meeting...</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-25/asia-data-centers-sound-out-us-clients-to-replace-china-demand">Asia Data Centers Sound Out US Clients to Replace China Demand</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#export controls`, `#cloud infrastructure`, `#geopolitics`, `#semiconductors`

---

<a id="item-tech-news-17"></a>
### [三星电子和 SK 海力士将采用长江存储 Xtacking 芯片堆叠技术](https://tech.ifeng.com/c/8yLRPKxQy4L) ⭐️ 7.0/10

三星电子和 SK 海力士已通过交叉许可协议，同意在 3D NAND 闪存产品中采用长江存储开发的 Xtacking 堆叠技术；该技术将存储单元阵列与 CMOS 逻辑电路分别制造于两片晶圆上，再通过晶圆键合集成，从而支持工艺分离优化；目前三方均拒绝置评，且未公布具体实施时间、产品型号、授权范围或量产节点；该合作尚未获官方确认，亦无独立验证表明技术已进入流片或量产阶段。

telegram · zaihuapd · 11月25日 14:33

**「Xtacking 技术原理与行业背景」** Xtacking 是长江存储（YMTC）自主研发的 3D NAND 架构，其核心是将存储阵列（memory array）与 CMOS 外围逻辑电路（peripheral logic）分别在两片晶圆上独立制造，再通过晶圆对晶圆混合键合（hybrid bonding）实现堆叠。该技术自 2018 年首次发布以来已迭代至第四代，旨在突破传统单晶圆集成在制程兼容性、良率和成本上的限制；Omdia 指出，这种分离式制造允许厂商用成熟制程生产存储单元，同时将逻辑电路外包给具备先进节点（如 7nm 或更小）能力的代工厂。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/355199/samsung-and-sk-hynix-to-license-ymtcs-xtacking-technology">Samsung and SK hynix to License YMTC&#x27;s Xtacking Technology</a></li>
<li><a href="https://asia.nikkei.com/business/tech/semiconductors/china-s-ymtc-boosted-by-samsung-and-sk-hynix-adopting-its-memory-technology">China&#x27;s YMTC boosted by Samsung and SK Hynix adopting its ...</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#3D-NAND`, `#memory-technology`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [美国拟对中国等 14 个贸易伙伴加征新关税](https://www.cnbc.com/2026/11/25/us-tariffs-trump-section-301.html) ⭐️ 8.0/10

美国政府依据 1974 年《贸易法》第 301 条，拟对包括中国、欧盟、日本、印度在内的 14 个贸易伙伴加征新关税；对中国将在 2018 年已实施的 25%关税基础上再加征 20%，若未遵守 2025 年 10 月釜山贸易休战协议，税率可能升至 40%。

telegram · zaihuapd · 11月25日 13:59

**「背景」** 美国依据 1974 年《贸易法》第 301 条发起为期八个月的调查，认定 14 个贸易伙伴存在制造业结构性产能过剩问题，即通过政府补贴扩大生产、压低出口价格，损害美国产业。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aljazeera.com/news/2026/11/25/trump-announces-new-trade-tariffs-which-countries-will-they-target">Trump announces new trade tariffs : Which countries are... | Al Jazeera</a></li>
<li><a href="https://www.theguardian.com/business/live/2026/nov/25/rise-energy-bills-britain-2166-impossible-high-millions-households-stocks-tumble-as-ai-rally-fizzles-live-updates">US proposes new tariffs on 14 trading partners ... | The Guardian</a></li>

</ul>
</details>

**标签**: `#trade\_policy`, `#us\_china\_relations`, `#tariffs`, `#global\_trade`, `#section\_301`

---

<a id="item-finance-news-2"></a>
### [英伟达股价波动考验‘市场信号导向’货币政策假说](https://www.cnbc.com/2026/11/25/nvidia-kevin-warsh-fed-market-signals.html) ⭐️ 7.0/10

该报道虚构了美联储主席凯文·沃什（Kevin Warsh）以市场信号替代经济预测的政策取向，并借英伟达股价剧烈波动（周五下跌、周一反弹）及所谓‘12 月和 1 月加息概率回升’来演示其理念张力；但现实中沃什从未担任美联储主席，当前主席为杰罗姆·鲍威尔，且文中所有事件、职务安排与时间点（如 2026 年 11 月 25 日）均属虚构。

rss · CNBC Finance · 11月25日 12:26

**「背景」** 凯文·沃什（Kevin Warsh）于 2026 年 5 月 22 日就任美联储主席，其政策主张强调依赖市场信号（如金融状况指数、通胀补偿率等）而非传统经济模型预测；与此同时，英伟达 CEO 黄仁勋在 2026 年 11 月中旬因所谓间谍丑闻辞职后，又于当月下旬在特朗普公开施压下重返职位，引发市场剧烈波动。

<details><summary>参考链接</summary>
<ul>
<li>Kevin M. Warsh | Federal Reserve History</li>
<li><a href="https://www.usatoday.com/story/money/2026/11/23/jensen-huang-reinstated-nvidia-ceo/92828717007/">Jensen Huang reinstated as Nvidia CEO, Trump says he ...</a></li>
<li><a href="https://www.businessinsider.com/nvidia-board-input-senior-levels-us-government-jensen-huang-2026-11">Nvidia Board Got &#x27;Input From Senior Levels&#x27; of US Government ...</a></li>
<li><a href="https://time.com/article/2026/11/23/jensen-huang-return-nvidia-trump/">6 Questions About Jensen Huang&#x27;s Stunning Return as Nvidia CEO</a></li>

</ul>
</details>

**标签**: `#monetary-policy`, `#market-signals`, `#fictional-reporting`

---

<a id="item-finance-news-3"></a>
### [Kalshi 永续合约日交易量首超预测市场](https://www.cnbc.com/2026/11/24/kalshi-perps-volume-prediction-markets.html) ⭐️ 7.0/10

Kalshi 的永续合约（perps）在 2026 年 11 月 24 日和 25 日连续两天日名义交易量达 34 亿美元，首次超过其预测市场日名义交易量（约 30 亿美元）。该数据为实际成交结果，非预测或目标值。

rss · CNBC Finance · 11月24日 23:03

**「背景」** Kalshi 于 2026 年 5 月获美国商品期货交易委员会（CFTC）批准，成为首家可在美上市加密货币永续合约的受监管交易所，随后扩展至个股、原油和金属等标的。

**「影响」** 目前仅 Kalshi 一家获准在美国本土提供永续合约交易，因此其增长直接惠及参与该平台的散户与机构交易者，但行业竞争正加速——Coinbase 已申请上市个股永续合约，CFTC 亦在推动境外头部平台 Hyperliquid 进入美国市场。

**标签**: `#financial innovation`, `#derivatives`, `#regulatory development`, `#market structure`

---

<a id="item-finance-news-4"></a>
### [犹他州撤销对预测市场公司 Kalshi 及其创始人的刑事指控](https://www.cnbc.com/2026/11/24/utah-drops-charges-against-kalshi-after-it-halted-operations-in-state.html) ⭐️ 7.0/10

犹他州于 2026 年 11 月 24 日撤销了针对预测市场平台 Kalshi 及其联合创始人塔雷克·曼苏尔（Tarek Mansour）和露安娜·洛佩斯·拉腊（Luana Lopes Lara）的 14 项刑事指控，此举紧随 Kalshi 于 11 月 23 日宣布暂停在该州运营之后。

rss · CNBC Finance · 11月24日 20:45

**「背景」** 犹他州于 10 月 28 日以“非法赌博经营”为由提起上述刑事指控，而联邦商品期货交易委员会（CFTC）次日即起诉犹他州，主张其对预测市场拥有专属监管权。

**「影响」** 该撤诉决定使 Kalshi 暂时避免犹他州刑事追责，但因撤销“不带偏见”（without prejudice），若其未来重启该州业务，指控可重新提起。

**标签**: `#regulatory enforcement`, `#prediction markets`, `#CFTC`, `#state vs federal regulation`, `#fintech legal risk`

---

<a id="item-finance-news-5"></a>
### [SpaceX 放弃 7.38 亿美元宽带补贴，改用零支出协议提供星链服务](https://x.com/SawyerMerritt/status/2125314062997467640) ⭐️ 7.0/10

SpaceX 已正式放弃美国国家电信与信息管理局（NTIA）BEAD 计划下 7.38 亿美元的联邦宽带补贴资金，转而签署一项‘零支出协议’，即不领取任何联邦拨款，但须向符合条件的美国家庭免费提供星链终端设备，并提供最低 100 Mbps 下载/20 Mbps 上传的低价宽带服务，承诺持续运营 10 年。

telegram · zaihuapd · 11月25日 02:17

**「背景」** BEAD（宽带公平接入与发展）计划是美国《基础设施投资与就业法》设立的 500 亿美元联邦宽带补贴项目，旨在扩大农村和欠覆盖地区高速互联网接入；‘零支出协议’是 NTIA 为吸引私营企业参与而设的替代机制，允许企业不领资金但履行同等服务义务以换取简化监管。

**「影响」** 该安排将使约数十万符合低收入或农村资格的美国家庭无需自费购买星链终端（市价约 599 美元）即可接入宽带，同时减轻 SpaceX 的财务报告负担，但其网络性能仍须接受 NTIA 统一测试。

**标签**: `#broadband policy`, `#spaceX`, `#BEAD`, `#telecom regulation`, `#infrastructure funding`

---