---
layout: default
title: "Horizon Summary: 2026-11-22 (ZH)"
date: 2026-11-22
lang: zh
---

> 从 26 条内容中筛选出 11 条重要资讯。

---

**科技新闻**
1. [GPGME v2.3.0 修复关键双释放漏洞](#item-tech-news-1) ⭐️ 9.0/10
2. [台积电暂停向中国企业供应 16nm 及以下制程芯片](#item-tech-news-2) ⭐️ 9.0/10
3. [浙江大学在‘天目 2 号’超导芯片上首次真机实现 QRAM](#item-tech-news-3) ⭐️ 9.0/10
4. [daraxonrasib 一线治疗转移性胰腺癌：61 例中 8.2%达完全缓解](#item-tech-news-4) ⭐️ 9.0/10
5. [Lean 完成广义黎曼假设的形式化验证](#item-tech-news-5) ⭐️ 8.0/10
6. [OpenAI 加强反蒸馏防护，GPT-6.2 Astra 和 Sol 模型提取成功率降至 0.2%](#item-tech-news-6) ⭐️ 8.0/10
7. [微软发布 Windows RDMA over USB4 开发者预览，支持多台消费级 PC 协同运行单个本地 AI 模型](#item-tech-news-7) ⭐️ 8.0/10
8. [OpenRouter 警告 MiniMax 模型提示词可能遭第三方读取](#item-tech-news-8) ⭐️ 8.0/10
9. [USB 显示器内置集线器导致 TCP ACK 延迟并降低 75%下载速度](#item-tech-news-9) ⭐️ 7.0/10

**科技博客**
1. [为何输出缓存对 LLM 智能体收效甚微](#item-tech-blog-1) ⭐️ 8.0/10

**财经新闻**
1. [特朗普提议对海外建 AI 数据中心的美企征“巨额税款”](#item-finance-news-1) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [GPGME v2.3.0 修复关键双释放漏洞](https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html) ⭐️ 9.0/10

GPGME 库中存在一个关键的双释放（double-free）漏洞，已在 v2.3.0 版本中修复；该漏洞影响所有使用 GPGME &lt;2.3.0 的软件，包括 GitLab（其签名提交功能）、邮件客户端、XMPP 客户端、Samba、Flatpak 和 Gpg4win 等；漏洞由 Johan Carlsson 发现，GitLab 于 2026 年 11 月 12 日通报，原定协调披露日为 11 月 25 日，但因 Ruby2Shell 漏洞事件提前至 11 月 20 日公开；官方公告发布于 2026 年 11 月 21 日。

hackernews · gdgghhhhh · 11月21日 08:32 · [社区讨论](https://news.ycombinator.com/item?id=50587208)

**「GPGME 库的作用与历史」** GPGME（GnuPG Made Easy）是一个为应用程序提供加密、解密、签名和验证功能的 C 语言封装库，广泛用于集成 GnuPG 功能的软件中，如邮件客户端、Git 工具链和包管理系统。该库自 2000 年代初起成为 GnuPG 生态的关键中间件，其设计目标是屏蔽底层 GnuPG 进程通信和协议细节，但长期依赖手动内存管理。

**「影响」** 所有使用 GPGME &lt;2.3.0 版本的软件（包括 GitLab、Gpg4win、主流邮件客户端、Samba 和 Flatpak）均面临远程代码执行风险，GitLab 已确认其签名提交验证路径可被利用，因此必须立即升级 GPGME 或应用补丁。

**「社区讨论」** 部分用户质疑将该漏洞直接定性为‘远程代码执行（RCE）’是否准确，指出其本质是双释放缺陷，需结合具体上下文（如 GitLab 签名验证路径）才可能构成 RCE 链；另有用户强调该漏洞在 Red Hat 的 CentOS Stream 中已于五年前被修补，但上游 GnuPG 项目长期未合并修复。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html">[Announce] GnuPG Security Advisory for GPGME ...</a></li>
<li><a href="https://thehackernews.com/2026/11/gnupg-warns-critical-gpgme-flaw-could.html">GnuPG Warns Critical GPGME Flaw Could Expose App Data via...</a></li>

</ul>
</details>

**标签**: `#security`, `#cryptography`, `#vulnerability`, `#open-source`, `#systems-programming`

---

<a id="item-tech-news-2"></a>
### [台积电暂停向中国企业供应 16nm 及以下制程芯片](https://appleinsider.com/articles/26/11/20/apple-supplier-tsmc-cuts-off-china-chip-orders-amid-tighter-export-controls) ⭐️ 9.0/10

台积电已暂停接受中国公司所有 16 纳米及以下先进制程芯片的订单，此举系响应美国最新半导体出口管制新规——该规则要求对向中国出口亚 16nm 制程芯片实施强制性事前美国政府审批，不再允许台积电自行评估豁免资格。目前美国商务部批准的许可名单中包含苹果、AMD 和英伟达，但尚无任何中国公司获批。受影响企业仅能使用 28nm 或 40nm 等成熟制程，无法获取 AI 数据中心所依赖的高带宽内存（HBM）配套先进逻辑芯片。

telegram · zaihuapd · 11月21日 02:01

**「美国收紧半导体出口管制新规」** 美国近期更新半导体出口管制规则，要求向中国客户供应 16nm 及以下先进制程芯片前，必须获得美国商务部工业与安全局（BIS）的预先许可，不再允许台积电等代工厂自行评估是否符合豁免条件；此前该类评估由厂商自主进行，新规将审批权完全收归美方。

**「影响」** 中国 AI 基础设施建设面临实质性瓶颈：因无法获得 16nm 及以下制程芯片，国内 AI 服务器厂商短期内难以部署符合性能与能效要求的新一代 AI 加速器及配套高带宽内存系统，部分在研项目可能被迫降规或延期。

**标签**: `#semiconductor`, `#AI-hardware`, `#export-controls`, `#chip-manufacturing`, `#geopolitics`

---

<a id="item-tech-news-3"></a>
### [浙江大学在‘天目 2 号’超导芯片上首次真机实现 QRAM](https://finance.sina.com.cn/stock/2026-11-21/doc-iniznhsk3530826.shtml) ⭐️ 9.0/10

浙江大学团队在自主研制的超导量子处理器‘天目 2 号’上，全球首次在真实硬件上实现了量子随机存储器（QRAM）功能，成功运行 4 位和 8 位数据检索原型，实测保真度分别为 80.9%和 60.4%，电路深度较未优化方案降低 30%以上，并首次在物理芯片上验证了该 QRAM 架构的局部抗噪特性。该成果已发表于《自然·物理》。

telegram · zaihuapd · 11月21日 08:31

**「量子随机存储器（QRAM）的基本概念」** QRAM 是一种理论上的量子硬件模块，旨在支持量子算法高效访问经典数据，是 Grover 搜索、量子机器学习等算法实现指数级加速的关键前提。长期以来，QRAM 仅存在于理论设计和数值模拟中，缺乏在真实量子硬件上的可运行实现，因其对量子线路深度、控制精度和抗噪能力要求极高。

**「影响」** 该 QRAM 原型的实现在超导硬件上为 Grover 搜索和量子机器学习等依赖高效量子数据加载的算法提供了首个可验证的物理基础；但当前 4 位和 8 位数据检索的保真度（分别为 80.9% 和 60.4%）仍低于容错量子计算所需阈值，意味着相关算法尚无法在现有实现上获得理论加速优势。

**标签**: `#quantum computing`, `#QRAM`, `#superconducting qubits`, `#hardware acceleration`, `#quantum algorithms`

---

<a id="item-tech-news-4"></a>
### [daraxonrasib 一线治疗转移性胰腺癌：61 例中 8.2%达完全缓解](https://event.eortc.org/ena2026/2026/11/20/metastatic-pancreatic-cancer-responds-well-to-initial-treatment/) ⭐️ 9.0/10

在 ENA 2026 大会公布的 I/II 期单臂研究中，61 例既往未接受过系统治疗的转移性胰腺导管腺癌患者接受口服 daraxonrasib（200 mg 每日一次）联合吉西他滨/白蛋白紫杉醇治疗，确认客观缓解率为 60.7%，完全缓解率为 8.2%（5/61），疾病控制率为 90.2%，中位无进展生存期为 12.8 个月，12 个月总生存率为 76.6%，中位随访时间为 18.3 个月。该药已于 2026 年 8 月 26 日获 FDA 批准（商品名 RASONQUE），但此前获批适应症仅限于既往治疗失败的患者，依据是 III 期 RMC-302 试验；本次公布的数据为首次用于一线治疗的早期结果，尚未经过随机对照 III 期试验验证。

telegram · zaihuapd · 11月21日 11:24

**「背景」** Daraxonrasib（商品名 RASONQUE）是 Revolution Medicines 公司开发的首款口服泛 RAS\(ON\) 抑制剂，于 2026 年 8 月 26 日获 FDA 批准用于既往治疗失败的转移性胰腺癌患者，依据是 III 期 RMC-302 研究中中位总生存期达 13.2 个月（对照组化疗为 6.7 个月）。该药作用于 RAS 蛋白的活性构象，可靶向多种 KRAS 和 NRAS 突变，不限于 G12C 亚型。

**「对一线治疗患者的影响」** 对于既往未接受过治疗的转移性胰腺导管腺癌患者，daraxonrasib（商品名 RASONQUE）联合吉西他滨/白蛋白紫杉醇方案在单臂 I/II 期研究中实现了 8.2%的完全缓解率（即肿瘤消失），显著高于历史化疗方案的 1 年生存率基准（22%–48%），但该结果尚未经随机对照 III 期试验验证，临床应用需等待确证性研究完成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.drugs.com/rasonque.html">Rasonque ( daraxonrasib ): Uses, Dosage, Side Effects</a></li>
<li><a href="https://www.nytimes.com/2026/08/26/science/pancreatic-cancer-daraxonrasib-approval.html">F.D.A. Approves the Drug Daraxonrasib That’s Poised to Transform...</a></li>
<li><a href="https://www.tradingstocksnow.com/2026/08/27/revolution-medicines-built-a-platform-rasonque-is-the-opening-move/">Revolution Medicines Built a Platform. Rasonque Is the Opening Move.</a></li>

</ul>
</details>

**标签**: `#oncology`, `#RAS inhibition`, `#pancreatic cancer`, `#targeted therapy`, `#clinical trials`

---

<a id="item-tech-news-5"></a>
### [Lean 完成广义黎曼假设的形式化验证](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) ⭐️ 8.0/10

Lean 定理证明器社区已完成广义黎曼假设（GRH）的机器可验证形式化证明，该证明由人类专家（Levent Alpöge 等）监督完成，并依赖于两个独立验证内核 con-leche 和 con-ron。该验证不提供新的数学推导，而是对已知解析方法（如 Weil 显式公式与正定性论证）进行完整、分步的形式化编码与检查。验证覆盖了从基础实分析、复分析到代数数论的关键引理，全部在 Lean 4 中实现并经多内核交叉验证通过。

hackernews · g-b-r · 11月21日 14:36 · [社区讨论](https://news.ycombinator.com/item?id=50589618)

**「黎曼假设的形式化基础」** 黎曼假设（Riemann Hypothesis）是 1859 年提出的关于黎曼ζ函数非平凡零点分布的著名未解猜想；其广义形式（GRH）涉及狄利克雷 L 函数。该猜想此前已在 Lean 数学库（mathlib）中被形式化为命题 RiemannHypothesis，并经 Lean 专家与数论学者共同审验，成为可验证目标。形式化工作依赖于已建立的分析与代数基础设施，而本次验证并非提出新数学证明，而是对既有解析方法（由 Alpöge 等人完成）进行全链路机器可检的 Lean 形式化。

**「影响」** 该验证使 GRH 在形式化数学框架下首次获得机器可核查的可靠性保障，意味着任何未来基于 GRH 的密码学或算法设计（如某些素性测试和伪随机数生成器）若采用此形式化版本，可排除手写证明中潜在的隐含假设或推理跳跃风险。

**「社区讨论」** 评论者就验证的独立性提出质疑：\[rcr-anti\] 强调 con-leche 和 con-ron 均自带自一致性证明，大幅降低系统性错误概率；而 \[thejokeisonme\] 则援引 Collatz 猜想假反例曾绕过单个检查器的先例，指出多个检查器间实际依赖共享基础设施，其独立性被高估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://leanprover-community.github.io/blog/posts/riemann-hypothesis/">Lean verification of the Riemann Hypothesis | Lean community blog</a></li>
<li><a href="https://www.clarin.com/us-news/who-is-levent-alpoge-the-anthropic-mathematician-who-claims-solved-the-riemann-hypothesis-with-claude_0_2WdGvYKBVM.html">Who is Levent Alpöge ? The Anthropic mathematician who claims he...</a></li>
<li><a href="https://news.ycombinator.com/item?id=50589618">Lean verification of the Riemann Hypothesis | Hacker News</a></li>

</ul>
</details>

**标签**: `#formal-methods`, `#number-theory`, `#theorem-proving`, `#lean-prover`, `#mathematical-foundations`

---

<a id="item-tech-news-6"></a>
### [OpenAI 加强反蒸馏防护，GPT-6.2 Astra 和 Sol 模型提取成功率降至 0.2%](https://openai.com/index/combatting-adversarial-distillation/) ⭐️ 8.0/10

OpenAI 于 2025 年 11 月 20 日宣布，其 GPT-6.2 Astra 和 Sol 模型已部署增强型反对抗性蒸馏防护，红队测试显示对历史请求推理链的提取成功率从 54.0% 显著降至 0.2%。该防护已投入生产环境，适用于当前发布的 GPT-6.2 Astra 与 Sol 版本。OpenAI 同时披露，2025 年每周对数千至数万个涉嫌模型蒸馏的账号采取执法行动，并就 DeepSeek 相关行为向美国国会提交简报。

telegram · zaihuapd · 11月21日 01:30

**「对抗性蒸馏的定义与威胁」** 对抗性蒸馏是一种通过向目标大模型反复提交精心构造的查询（如要求其输出推理链），再利用返回结果训练替代模型的技术，旨在绕过授权直接复制闭源模型的能力。此前研究（如 2025 年多篇论文）已证实该方法在 GPT-4、Claude 3 等模型上可实现超 50%的提取成功率，构成对模型知识产权与安全控制的实质性威胁。

**「影响」** 使用自动化蒸馏工具尝试复现或窃取 GPT-6.2 Astra 和 Sol 推理行为的攻击者，其成功概率已趋近于零（0.2%），显著提高模型知识产权与安全边界的实际防护强度；开发者若依赖历史响应蒸馏构建轻量替代模型，将面临技术路径失效风险。

**标签**: `#AI security`, `#model protection`, `#adversarial distillation`, `#LLM safety`, `#AI policy`

---

<a id="item-tech-news-7"></a>
### [微软发布 Windows RDMA over USB4 开发者预览，支持多台消费级 PC 协同运行单个本地 AI 模型](https://videocardz.com/newz/microsoft-brings-rdma-over-usb4-to-windows-allowing-multiple-pcs-to-run-one-local-ai-model) ⭐️ 8.0/10

微软发布了 Windows 的 RDMA over USB4 开发者预览版，允许使用标准 USB4 线缆连接的多台消费级 PC（如搭载 AMD Ryzen AI Max+ 395 的设备）共享内存与 GPU 资源，协同执行单个本地大语言模型推理任务。该功能已实测在三台设备上以 4-bit 量化运行 Qwen3-235B-A22B 模型，达到约 18.5 token/s 的吞吐量。当前仅限 Windows Insider 预览通道推送，需特定 USB4 硬件支持，尚未作为正式版功能发布。

telegram · zaihuapd · 11月21日 06:13

**「RDMA 与 USB4 的基础能力」** RDMA（远程直接内存访问）是一种允许网络设备绕过操作系统内核直接读写远程内存的技术，通常依赖 InfiniBand 或 RoCE（RDMA over Converged Ethernet）等专用硬件实现低延迟和高吞吐。USB4 基于 Thunderbolt 3 协议，原生支持 PCIe 隧道和 DisplayPort 隧道，但此前未在 Windows 中启用 RDMA 功能。

**「影响」** 使用该功能的开发者需确保其 PC 配备支持 RDMA 的 USB4 主机控制器（如 AMD Ryzen AI Max+ 395）及 Windows Insider 预览版系统，否则无法启用跨设备内存与 GPU 资源共享；当前预览版不兼容 Intel 或 NVIDIA 主控的 USB4 设备。

**标签**: `#AI systems`, `#distributed computing`, `#Windows`, `#USB4`, `#local AI`

---

<a id="item-tech-news-8"></a>
### [OpenRouter 警告 MiniMax 模型提示词可能遭第三方读取](https://news.ycombinator.com/item?id=50585962) ⭐️ 8.0/10

OpenRouter 发出安全警告，指出用户发送至 MiniMax 模型的提示词可能被第三方通过下游服务提供商（AtlasCloud、Novita、StreamLake）读取。该结论基于 2026 年 7 月至 10 月间开展的安全测试：研究者在提示词中嵌入唯一可追踪的测试 URL，随后在 40 至 130 小时内观测到这些 URL 被外部实体访问。OpenRouter 已移除相关端点的“零数据保留”声明，并建议处理敏感数据的用户轮换 API 密钥；该警告以邮件形式发出，官网尚未发布公开通告。

telegram · zaihuapd · 11月21日 06:53

**「MiniMax 模型通过第三方基础设施提供服务」** MiniMax 的模型（如 minimax/m2-her、minimax/m3.1-flash 和 minimax-01）通过 OpenRouter 等聚合平台分发，其后端依赖 AtlasCloud、Novita 和 StreamLake 等下游服务提供商。此前 MiniMax-m2-her 已于 2026 年 11 月 5 日正式下架，而 m3.1-flash 和 -01 等新模型仍持续在 OpenRouter 上提供服务。

**「影响」** 使用 OpenRouter 调用 MiniMax 模型（如 M2.5、M3）的开发者面临提示词泄露风险，尤其当输入含敏感凭证或测试 URL 时；OpenRouter 已移除相关端点的“零数据保留”声明，并建议用户立即轮换 API 密钥。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.okapi.bot/models/openrouter/minimax/minimax-m2-her/">minimax / minimax -m2-her shutdown: Nov 5, 2026 ( OpenRouter )</a></li>
<li><a href="https://aifree.dev/news/minimax-m31-flash-free-openrouter-space-bunny">MiniMax M3.1 Flash Goes Free on OpenRouter | aifree.dev</a></li>
<li><a href="https://openrouter.ai/zh-CN/minimax/minimax-01">MiniMax -01 - API 定价与提供商 | OpenRouter</a></li>

</ul>
</details>

**标签**: `#security`, `#ai-ops`, `#api-security`, `#llm-infrastructure`, `#data-privacy`

---

<a id="item-tech-news-9"></a>
### [USB 显示器内置集线器导致 TCP ACK 延迟并降低 75%下载速度](https://blog.tymscar.com/posts/studiodisplayethernet/) ⭐️ 7.0/10

一名开发者发现，通过 USB 连接的 Studio Display 显示器内置 USB 集线器传输以太网流量时，会引入显著的 ACK 延迟，导致 TCP 接收窗口阻塞、网卡缓冲区溢出及丢包，最终使实际下载速度下降 75%。问题在 2.5 Gbps 对称光纤线路环境下被识别，使用独立 USB 以太网适配器（如 ASIX AX88179）替代显示器直连后，速度恢复正常。该问题并非显示器固件缺陷，而是 USB 拓扑结构中 hub 引入的非确定性延迟与 Linux TCP 栈默认 ACK 定时机制（如 tcp\_delack\_min）相互作用所致。

hackernews · soheilpro · 11月21日 10:36 · [社区讨论](https://news.ycombinator.com/item?id=50587875)

**「TCP 延迟确认与 USB 网络适配器性能」** TCP 延迟确认（Delayed ACK）是一种优化机制，允许接收方将 ACK 包延迟最多 200 毫秒或等待第二个数据包到达后再合并发送，以减少小包数量；但当链路引入额外 USB 轮询延迟时，该机制可能导致 ACK 超时、接收窗口停滞及 TCP 重传。USB 连接的以太网适配器（尤其是经由显示器内置 USB 集线器中转时）常因 USB 带宽竞争和调度延迟加剧这一问题，进而触发内核缓冲区溢出与丢包。

**「影响」** 依赖 USB-C 显示器扩展网络连接的 Mac 或 Linux 用户可能遭遇严重吞吐量下降，且该问题无明显告警；建议避免将高带宽以太网流量经由 USB 显示器内置 hub 转发，或调整内核 TCP 延迟 ACK 参数（如设置 net.ipv4.tcp\_delack\_min=0）以缓解。

**「社区讨论」** 多位评论者强调问题本质是 USB 集线器引入的额外延迟触发了 TCP 协议栈的 ACK 定时行为异常，而非显示器本身故障；有用户指出，类似现象也出现在其他 USB 网络设备中，但因 Studio Display 的普及和高带宽场景而更易暴露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://apple.stackexchange.com/questions/437555/macos-networking-brutally-slow-using-vnc-or-apple-remote-desktop">macOS networking brutally slow using VNC or Apple Remote Desktop</a></li>
<li><a href="https://www.linkedin.com/pulse/20141113153643-13386347-what-is-delayed-ack-and-how-can-it-be-a-bottleneck-in-your-network">What is Delayed ACK and how can it be a bottleneck in your network.</a></li>

</ul>
</details>

**标签**: `#networking`, `#usb`, `#tcp`, `#debugging`, `#systems-engineering`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [为何输出缓存对 LLM 智能体收效甚微](https://seangoedecke.com/why-output-caching-doesnt-work/) ⭐️ 8.0/10

rss · Sean Goedecke · 11月21日 00:00

**「背景」** LLM 智能体常重复输出代码片段、证据文档或样本结果，看似浪费输出 token；而输出 token 生成成本远高于输入 token，因此有人提议通过引用（如“src/script.py:12-15”）替代重复内容来缓存输出。

**「方案」** 作者基于自身智能体日志发现：用户可见的最终输出仅占总输出 token 的约 6%，其余 94%为推理过程 token（50%）和工具调用 token（44%）；即便将可见输出压缩三分之二（极乐观估计），总 token 节省也仅约 4%，受 Amdahl 定律严格限制。作者指出，模型内部链式推理极少自我重复，故优化重点不应是表层输出去重，而应提升模型智能——更聪明的模型能以更少推理步和工具调用达成目标，实测中高单价模型因 token 用量锐减反而总成本更低。

**「启示」** 在 LLM 系统优化中，输出缓存边际收益极低；真正决定成本效率的是模型推理效率本身——提升智能比压缩可见输出更能显著降低总 token 消耗与推理开销。

**标签**: `#LLM optimization`, `#inference economics`, `#caching`, `#Amdahl&\#x27;s law`, `#agent systems`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [特朗普提议对海外建 AI 数据中心的美企征“巨额税款”](https://apnews.com/article/trump-artificial-intelligence-data-centers-f1ac03b73d13445400eeed8631d9d879) ⭐️ 7.0/10

特朗普于 2026 年 11 月 20 日称，拟对在美国境外建设人工智能数据中心的美国科技公司征收“巨额税款”，该计划尚未向政府内部官员透露，也未公布具体税率、征收方式或生效时间。

telegram · zaihuapd · 11月21日 03:26

**「背景」** 特朗普在 11 月 20 日白宫记者会上首次提出该设想，称尚未向其政府团队内部透露，也未形成正式政策方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.politico.com/news/2026/11/20/trump-overseas-data-center-tax-01178999">Trump says he’ll tax companies building data centers outside ...</a></li>
<li><a href="https://www.cnbc.com/2026/11/20/trump-data-centers-ai-companies-tax.html">Trump vows to stop U.S. companies from building data centers ...</a></li>

</ul>
</details>

**标签**: `#US-China tech competition`, `#AI policy`, `#corporate taxation`, `#infrastructure policy`, `#election-year proposals`

---