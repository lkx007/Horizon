---
layout: default
title: "Horizon Summary: 2026-11-16 (ZH)"
date: 2026-11-16
lang: zh
---

> 从 41 条内容中筛选出 22 条重要资讯。

---

**科技新闻**
1. [uBlock Origin 元素选择器中存在通用跨站脚本（UXSS）漏洞](#item-tech-news-1) ⭐️ 9.0/10
2. [通义千问 Qwen4-Max 正式上线：2.4 万亿参数稀疏 MoE 模型，支持视觉与百万 Token 上下文](#item-tech-news-2) ⭐️ 9.0/10
3. [Meta FAIR 与 NYU 研究：视觉编码器预训练非必需，但视觉专用参数不可省略](#item-tech-news-3) ⭐️ 8.0/10
4. [CUDA 内存拷贝工具在 B300 GPU 上实现 5 倍加速](#item-tech-news-4) ⭐️ 8.0/10
5. [美团开源 LongCat-2.5：1.6 万亿参数多模态智能体模型，全程基于华为升腾芯片训练](#item-tech-news-5) ⭐️ 8.0/10
6. [Bitly 过期链接遭劫持用于恶意重定向](#item-tech-news-6) ⭐️ 7.0/10
7. [Nvidia 面临客户自研 AI 芯片与 CUDA 生态弱化的战略挑战](#item-tech-news-7) ⭐️ 7.0/10
8. [MacBook Pro 新 OLED 显示屏存在低频 PWM 调光问题](#item-tech-news-8) ⭐️ 7.0/10
9. [Protomaps：自托管矢量地图瓦片变得廉价且简单](#item-tech-news-9) ⭐️ 7.0/10
10. [乌鸦决策速度超过人类](#item-tech-news-10) ⭐️ 7.0/10
11. [Datasette 1.0a43 发布：支持流式输出渲染器、新增 Response.stream\(\) 插件 API、修复安全漏洞](#item-tech-news-11) ⭐️ 7.0/10
12. [Datasette 0.65.6 发布：回溯修复数据库路由名与名称不一致导致的未授权下载漏洞](#item-tech-news-12) ⭐️ 7.0/10
13. [Marimba：基于冻结 Qwen3-ASR-0.6B 的轻量级实时语音感知模型](#item-tech-news-13) ⭐️ 7.0/10
14. [Telegram macOS 13.2 测试版新增可选 Lockdown Mode](#item-tech-news-14) ⭐️ 7.0/10
15. [华为云上线开源盘古模型 openPangu-2.1-Pro](#item-tech-news-15) ⭐️ 7.0/10
16. [苹果智能眼镜 N50 计划 2027 年发布，仅支持 iPhone、无 AR 显示、磁吸充电](#item-tech-news-16) ⭐️ 7.0/10
17. [苹果启动健康 AI 使用研究，招募 20 万美国用户](#item-tech-news-17) ⭐️ 7.0/10
18. [腾讯总办号召 AI 时代再创业，削减管理岗位](#item-tech-news-18) ⭐️ 7.0/10
19. [腾讯混元发布 Hy4 Flash：224B 参数、12B 激活、1M 上下文、API 成本降至 Hy4 preview 的 1/13](#item-tech-news-19) ⭐️ 7.0/10

**财经新闻**
1. [中国 10 月经济数据全面不及预期](#item-finance-news-1) ⭐️ 8.0/10
2. [美国法官驳回美光、三星、SK 海力士 DRAM 价格操纵案撤诉动议](#item-finance-news-2) ⭐️ 7.0/10
3. [2024 年三季度外资对华直接投资转为净流出](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [uBlock Origin 元素选择器中存在通用跨站脚本（UXSS）漏洞](https://iter.ca/post/ubo-uxss/) ⭐️ 9.0/10

uBlock Origin 的网页内嵌元素选择器存在通用跨站脚本（UXSS）漏洞，允许恶意网站通过注入到页面 DOM 中的选择器 UI 执行任意 JavaScript 代码，从而突破同源策略限制。该漏洞已在版本 1.75.4（uBlock Origin）和 2026.1110.1816（uBO Lite）中修复。漏洞影响所有使用旧版本的用户，且无需用户交互即可触发；修复方式为重构选择器 UI，使其不再直接注入网页 DOM。

hackernews · zaik · 11月16日 02:04 · [社区讨论](https://news.ycombinator.com/item?id=50513160)

**「uBlock Origin 元素选择器的架构设计」** uBlock Origin 的网页内嵌元素选择器（element picker）通过向当前页面 DOM 注入 UI 元素实现可视化规则创建，该设计使扩展能直接操作页面结构，但也导致其上下文与网页共享同源策略边界。此前该机制未被识别为 UXSS 风险面，直到本次漏洞揭示其可被恶意网站诱导执行跨域脚本注入。

**「实际用户面临跨域任意代码执行风险」** 在 uBlock Origin 1.75.4 版本发布前，使用旧版（特别是 MV2 架构的 Firefox 版本）的用户可能被恶意网站利用该 UXSS 漏洞，在任意目标域名上下文中执行 JavaScript，从而窃取敏感数据或劫持会话；漏洞已通过将元素选择器 UI 移出页面 DOM 并限制 filter 注入逻辑完成修复。

**「社区讨论」** 多位评论者指出，将扩展 UI（如元素选择器或密码管理器下拉菜单）直接注入网页 DOM 是根本性设计风险，可能导致信息泄露或 UXSS；有人建议应将此类 UI 移至浏览器 Chrome 区域（即浏览器界面层）以隔离执行上下文。另有用户询问分叉项目 AdNauseam 是否受影响，但原文未提供确认信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/gorhill/uBlock/security/advisories/GHSA-cmqw-9r2w-6wv2">Universal XSS from website-driven element picker</a></li>
<li><a href="https://techbytes.app/posts/universal-xss-in-ublock-origin-from-website-driven-element-picker/">Universal XSS in uBlock Origin from website-driven element picker</a></li>
<li><a href="https://todayforai.com/en/items/art-bdf7d819-af2">uBlock Origin Patches One-Click Universal XSS Flaw</a></li>
<li><a href="https://iter.ca/post/ubo-uxss/">Universal XSS in uBlock Origin from website-driven element picker</a></li>

</ul>
</details>

**标签**: `#browser-security`, `#extension-vulnerability`, `#uxss`, `#web-security`, `#uBlock-Origin`

---

<a id="item-tech-news-2"></a>
### [通义千问 Qwen4-Max 正式上线：2.4 万亿参数稀疏 MoE 模型，支持视觉与百万 Token 上下文](https://mp.weixin.qq.com/s/pJUt0xwD6H-WMyzd8TjZaQ) ⭐️ 9.0/10

阿里通义千问于 2026 年 11 月 16 日正式上线 Qwen4-Max，这是一款总参数达 2.4 万亿的稀疏混合专家（MoE）大语言模型，原生支持视觉理解与百万 Token 长上下文。其单任务平均 API 费用从 26.58 元降至 11.16 元（降幅约 58%），Token 消耗减少近 50%，当前已开放商用。团队明确表示后续将开源更小规模的 Qwen4 系列模型（如 27B 等版本），但未公布具体时间表或许可证类型。

telegram · zaihuapd · 11月16日 02:52

**「千问模型演进背景」** Qwen4-Max 是通义千问系列的最新旗舰模型，继 Qwen3.8-Max（2026 年 7 月发布）之后推出，延续了该系列在稀疏 MoE 架构、长上下文与多模态能力上的技术路线。此前 Qwen3.8-Max 已支持视觉输入与超长上下文，但参数规模与推理成本优化未达当前水平。

**「影响」** 开发者和企业用户可立即以更低成本调用具备视觉理解和超长上下文能力的旗舰级模型，但当前仅提供 API 服务；开源小模型的后续发布将直接影响开源 AI 生态中对高效、可部署多模态模型的需求与技术选型。

**「社区讨论」** 部分用户指出 Qwen4-Max 在 Artificial Analysis 基准上得分为 43、平均单次调用成本 3.27 美元，显著高于 GPT-6.1 Sol（46 分，0.36 美元）；另有开发者强调 Qwen3.8 Max 因推理速度慢（约 30 token/s）导致在代理系统中得分偏低，因而期待 Qwen4-Max 或后续‘Flash’/27B 版本在延迟与吞吐上的实质性改进。

**标签**: `#large-language-models`, `#open-source-ai`, `#multimodal-ai`, `#moE-architecture`, `#programming-ai`

---

<a id="item-tech-news-3"></a>
### [Meta FAIR 与 NYU 研究：视觉编码器预训练非必需，但视觉专用参数不可省略](https://www.reddit.com/r/MachineLearning/comments/1xx1k2o/meta_fair_nyu_unbundling_multimodal_vision/) ⭐️ 8.0/10

Meta FAIR 与纽约大学联合研究通过从零训练 200 多个多模态大语言模型（MLLM），在相同数据与计算预算下系统性验证：视觉编码器的独立预训练（如对比学习、自监督、图像描述等）对 VQA 任务性能无显著增益，即使额外投入 6.5 倍计算量预训练 MetaCLIP 也未能提升 VQA 得分；但模型必须包含专用于视觉 token 的参数（vision-only parameters），移除后所有规模（0.6B–6.4B）模型 VQA 性能均大幅下降，且需约 3 倍计算量才能追平；视觉参数可直接嵌入 LLM 前 8 层（“in-fusion”方式），无需独立编码器结构，在 1.7B 至 6.4B 规模下性能与传统编码器相当，首 token 延迟降低约 13%。

reddit · r/MachineLearning · /u/trungh98 · 11月15日 17:38

**「背景说明」** 当前多模态大模型普遍采用预训练视觉编码器（如 ViT）+冻结/微调 LLM 的架构，隐含假设是视觉编码器需独立预训练以提取通用视觉表征。该研究针对这一默认设计，将编码器解耦为三个可独立检验的要素：是否独立预训练、是否含视觉专用参数、是否作为独立模块置于 LLM 之前。

**「实际影响」** 开发者可跳过耗时耗资源的视觉编码器预训练阶段，直接在多模态训练中联合优化视觉与语言模块；但必须为视觉 token 保留专用参数空间（如独立注意力投影或 FFN 权重），不可简单复用 LLM 参数或完全移除视觉分支。

**「社区讨论」** 无可用评论，社区未提供实质性讨论或经验反馈。

**标签**: `#multimodal`, `#vision-language-models`, `#model-architecture`, `#ablation-study`, `#pretraining`

---

<a id="item-tech-news-4"></a>
### [CUDA 内存拷贝工具在 B300 GPU 上实现 5 倍加速](https://www.reddit.com/r/MachineLearning/comments/1xx2n25/making_cudamemcpy_5x_faster_on_a_b300_p/) ⭐️ 8.0/10

开发者开源了一个名为 cudamemcpy-tuner 的调优工具，针对 NVIDIA B300 GPU 上的 pageable 内存 cudaMemcpy 操作实现最高 5 倍吞吐量提升：在 1 GB 张量 CPU↔GPU 往返拷贝测试中，原始 PyTorch 默认行为达 10.2 GB/s，启用该工具后提升至 51.5 GB/s。该优化专用于 pageable（非 pinned）主机内存场景，已通过 PyTorch 基准测试验证，并提供完整文档与开源代码。工具不修改 CUDA 驱动或运行时，而是通过动态配置传输参数（如分块大小、流使用策略等）实现性能提升。

reddit · r/MachineLearning · /u/makneeee · 11月15日 18:20

**「背景」** cudaMemcpy 在 pageable 主机内存与 GPU 设备内存之间传输数据时，因需经历页表遍历和缺页中断，性能远低于使用 pinned（page-locked）内存的场景；B300 作为 NVIDIA 新一代数据中心 GPU，其 HBM3 带宽和 PCIe 5.0 接口理论上支持更高传输速率，但默认 CUDA 运行时对 pageable 内存的传输策略未充分适配其硬件特性。

**「影响」** 使用 PyTorch 等框架进行中等规模模型训练或推理（尤其在未预分配 pinned 内存的动态加载场景）的开发者，可立即通过集成该工具将 CPU-GPU 张量搬运带宽从约 10 GB/s 提升至超 50 GB/s，显著降低数据加载瓶颈，且无需修改应用代码或升级 CUDA 版本。

**「社区讨论」** 无可用评论，社区尚未就该工具展开实质性讨论。

**标签**: `#CUDA`, `#GPU optimization`, `#machine learning systems`, `#memory transfer`, `#systems performance`

---

<a id="item-tech-news-5"></a>
### [美团开源 LongCat-2.5：1.6 万亿参数多模态智能体模型，全程基于华为升腾芯片训练](https://the-decoder.com/meituan-releases-a-1-6-trillion-parameter-agent-model-that-never-touched-an-nvidia-gpu/) ⭐️ 8.0/10

美团开源 LongCat-2.5 模型，参数总量达 1.6 万亿，每 token 激活约 480 亿参数，专为自主完成多步骤编程等复杂任务的智能体设计；该模型全程使用华为升腾（Ascend）AI 加速卡训练，未使用任何英伟达 GPU；支持文本、图像与视频多模态输入，权重以 MIT 许可证开放，可在商用场景中自由使用；在 Terminal Bench v2.1 基准测试中得分为 88.4。

telegram · zaihuapd · 11月15日 11:08

**「背景」** LongCat 系列是美团自研的多模态智能体模型，此前 LongCat-2.0 已于 2026 年 10 月发布，聚焦编程任务自动化；LongCat-2.5 是其迭代版本，首次明确宣称全量训练过程完全基于华为升腾（Ascend）AI 加速芯片，不依赖英伟达 GPU。

**「实际影响」** 开发者若需在国产硬件上部署高性能编程智能体，可直接使用 LongCat-2.5 的 MIT 许可权重及官方提供的 4 位量化版本和基于 194 块华为升腾芯片的自托管指南；但该模型未提供 NVIDIA GPU 兼容支持，排除了在主流 CUDA 生态中开箱即用的可能性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://phemex.com/news/article/meituan-opensources-16tparameter-longcat25-model-trained-entirely-on-domestic-chinese-hardware-103629">Meituan LongCat-2.5: 1.6T MoE AI Model Trained on ... - Phemex</a></li>

</ul>
</details>

**标签**: `#artificial-intelligence`, `#open-source`, `#hardware-sovereignty`, `#agent-systems`, `#multimodal-models`

---

<a id="item-tech-news-6"></a>
### [Bitly 过期链接遭劫持用于恶意重定向](https://ransomnews.com/burger-king-tweet-bitly-link-hijack-2026/) ⭐️ 7.0/10

Bitly 平台上已过期或被弃用的短链接正被攻击者劫持，重定向至恶意网站；该问题已在真实事件中暴露，例如某条 Burger King 官方推文所含 Bitly 链接被篡改；劫持发生于原链接失效后、但 Bitly 未及时回收或保护对应短码的情况下；目前无证据表明 Bitly 已发布修复补丁、服务端策略更新或用户通知机制。

hackernews · hspeiser · 11月15日 22:11 · [社区讨论](https://news.ycombinator.com/item?id=50511395)

**「URL 缩短服务的链接生命周期管理」** Bitly 等 URL 缩短服务通常为用户生成的短链接设置有效期或绑定账户状态；当原始账户被停用、删除或长期不活跃时，这些短链接可能被系统回收并重新分配，导致原有重定向失效或被恶意劫持。这种设计源于资源复用和运营成本控制需求，但未充分考虑长期链接稳定性和所有权归属问题。

**「实际影响」** 已确认的恶意重定向事件导致用户点击原属 Burger King 官方推文的过期 Bitly 链接时被导向无关或潜在有害内容（如 YouTube 视频、脚本下载页等），表明依赖第三方短链接服务的组织面临不可控的下游安全风险；受影响链接无法由原始发布者修复，因 Bitly 对过期或未续费链接的处置策略不提供所有权延续保障。

**「社区讨论」** 多位评论者指出，将短链接托管于第三方服务（如 Bitly）存在固有风险，一旦账户停用、服务商关闭或数据丢失，链接即永久失效且无法修复；另有用户以作者误用未注册 Bitly 链接为例，说明短链接生命周期缺乏所有权保障和归档机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=5bridFGQzzU">Oguri Cap Sings: Drive Thru of Burger King | REMASTERED - YouTube</a></li>
<li><a href="https://robscript.com/steal-an-egg-scripts/">Best Steal an Egg Scripts — No Key &amp; Keyless ( 2026 )</a></li>
<li><a href="https://pwnews.net/blog/2026-11-13-6722">Смотреть онлайн TNA iMPACT 12.11. 2026 (английская версия)</a></li>

</ul>
</details>

**标签**: `#web-security`, `#systems-reliability`, `#link-rot`, `#infrastructure-risk`, `#url-shortening`

---

<a id="item-tech-news-7"></a>
### [Nvidia 面临客户自研 AI 芯片与 CUDA 生态弱化的战略挑战](https://steveblank.com/2026/11/15/whats-next-for-nvidia/) ⭐️ 7.0/10

本文分析指出，随着 AWS、Google、Meta 等主要云厂商加速开发定制 AI 加速器及配套软件栈，Nvidia 正面临核心护城河——CUDA 生态的系统性弱化；这些客户正通过与 Broadcom 等 ASIC 厂商合作、构建自主抽象层与调试工具，降低对 CUDA 的依赖，从而削弱 Nvidia 的软硬件绑定优势。文章强调，该趋势并非远期预测，而是已由行业实际部署（如 Trainium、Ascend、MTIA）和软件抽象进展（如 MLIR、Triton、vLLM）所驱动。文中未宣布任何 Nvidia 新产品、政策或技术变更，亦无独立性能数据或上市时间表，仅基于公开产业动向提出战略风险研判。该 URL 标注日期为 2026 年 11 月 15 日，且 steveblank.com 域名未托管此文，来源可信度存疑。

hackernews · zdw · 11月15日 23:55 · [社区讨论](https://news.ycombinator.com/item?id=50512235)

**「定制 AI 芯片与 CUDA 生态挑战」** NVIDIA 长期依赖其通用 GPU（如 H100）和 CUDA 软件生态实现市场主导，但自 2025 年起，Google、Amazon、Meta 和 Microsoft 等主要云厂商加速采用定制 AI 专用集成电路（ASIC），例如 Google TPU、Meta MTIA 及 AWS Trainium，并通过 Broadcom 等合作伙伴进行设计。这些 ASIC 针对特定工作负载（如推理和推荐系统）优化，绕过 CUDA 依赖，以降低总体拥有成本（TCO）并提升能效。

**「社区讨论」** 评论者\[01100011\]指出，最大威胁来自大客户转变为竞争对手，因问题空间趋于稳定，客户得以联合 Broadcom 等厂商设计自有芯片，并借助 Agent 技术构建替代 CUDA 的抽象层与调试工具，导致 CUDA 相关性正加速下降；另一评论\[kristopolous\]澄清作者身份为知名创业导师 Steve Blank，但未就技术论点提供佐证或反驳。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2025/11/21/nvidia-gpus-google-tpus-aws-trainium-comparing-the-top-ai-chips.html">Nvidia Blackwell, Google TPUs, AWS Trainium: Comparing top AI ...</a></li>
<li><a href="https://www.aranca.com/knowledge-library/articles/investment-research/the-rise-of-custom-ai-chips">The Rise of Custom AI Chips: How Big Tech is Challenging ...</a></li>
<li><a href="https://fffinstill.com/blog/custom-ai-asics-vs-gpus-broadcom-google-amazon-approach">Custom AI ASICs vs. GPUs: The Broadcom/Google/Amazon Approach</a></li>

</ul>
</details>

**标签**: `#AI-hardware`, `#GPU`, `#CUDA`, `#cloud-computing`, `#semiconductors`

---

<a id="item-tech-news-8"></a>
### [MacBook Pro 新 OLED 显示屏存在低频 PWM 调光问题](https://macanorak.com/the-macbook-pros-oled-pwm-problem-when-a-better-display-becomes-worse-to-use/) ⭐️ 7.0/10

新款 MacBook Pro 的 OLED 显示屏在高亮度下仍采用约 240 Hz 至 480 Hz 的脉宽调制（PWM）调光，部分测量显示其双堆叠（tandem）OLED 子像素以 480 Hz、180 度相位差协同工作，等效频率可达 960 Hz，但实际有效调光频率在多数亮度区间仍显著低于人眼舒适阈值（通常建议 ≥1250 Hz）。该问题已通过示波器实测确认，影响对光敏感的用户，包括偏头痛、脑震荡后综合征及光敏性癫痫患者。苹果未在官方规格中披露 PWM 频率，亦未提供 DC 调光选项。

hackernews · MacAnorak · 11月15日 13:15 · [社区讨论](https://news.ycombinator.com/item?id=50506719)

**「PWM 调光与 OLED 显示基础」** 脉冲宽度调制（PWM）是一种通过快速开关像素发光来控制 OLED 屏幕亮度的技术，区别于 LCD 依赖背光的调光方式；由于 OLED 像素自发光，其 PWM 实现更复杂，尤其在低亮度下易引入可感知的闪烁。此前 MacBook Pro 长期采用 mini-LED 背光液晶屏，而 2026 年新款首次转向 OLED 面板，这一硬件变更使 PWM 行为成为新的关键人因工程问题。

**「影响」** 受影响用户在长时间使用时可能出现眼疲劳、头痛或视觉不适；开发者与无障碍团队需在 macOS 应用中更谨慎处理全屏高亮动画和自动亮度调节逻辑，以避免无意加剧 PWM 感知强度。

**「社区讨论」** 部分用户（如 \[legitronics\]）质疑实测 PWM 频率应为 480 Hz 或更高（如相位抵消后等效 960 Hz），而另一些用户（如 \[achr2\]）强调即使 480 Hz 也远低于已知可诱发不适的生理阈值，并援引《自然·通讯》论文指出人类可感知远高于标称刷新率的闪烁；讨论普遍呼吁苹果公开调光机制并增加软件级 DC 调光开关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://macanorak.com/the-macbook-pros-oled-pwm-problem-when-a-better-display-becomes-worse-to-use/">The MacBook Pro ’s OLED PWM Problem: When a ‘Better’ Display...</a></li>
<li><a href="https://www.macrumors.com/2026/10/26/oled-macbook-pro-could-spell-trouble-for-mini-led/">MacBook Pro &#x27;s Switch to OLED Could Spell Trouble for... - MacRumors</a></li>

</ul>
</details>

**标签**: `#display-technology`, `#hardware-engineering`, `#accessibility`, `#macos`, `#oled`

---

<a id="item-tech-news-9"></a>
### [Protomaps：自托管矢量地图瓦片变得廉价且简单](https://bruceroettgers.eu/blog/protomaps/) ⭐️ 7.0/10

Protomaps 是一个开源工具链，支持开发者以极低成本（例如使用 Cloudflare R2 或普通对象存储）自托管基于 OpenStreetMap 数据的矢量地图瓦片（PMTiles 格式），兼容 Maplibre 等前端渲染器。它通过 CLI 工具、Tilemaker 配置和可定制的 processing.lua 脚本实现端到端控制，已实际应用于 Cartes.app 等项目，替代了每月 150 欧元的 Maptiler 商业服务。该方案不依赖中心化 API 密钥或用户追踪，但需自行处理高缩放级别卫星影像等大体积数据的存储与分发限制。

hackernews · bcye · 11月15日 19:26 · [社区讨论](https://news.ycombinator.com/item?id=50509837)

**「背景」** Protomaps 基于 PMTiles 格式——一种将金字塔式地图瓦片打包为单个文件的开源归档格式，支持通过 HTTP 范围请求（range requests）直接从静态存储（如 S3、Cloudflare R2）读取瓦片，无需专用瓦片服务器。该格式由 Protomaps 团队主导开发，其 GitHub 仓库明确将其定位为实现低成本、免运维、无厂商锁定的地图应用的基础。

**「影响」** 开发者可将地图基础设施迁移至 Protomaps，显著降低运营成本（如 Cartes.app 从 Maptiler 切换后月费从 150 欧元趋近于零），同时获得对地图样式、数据内容和访问控制的完全自主权；但需自行承担矢量瓦片生成（如通过 Tilemaker）、托管与 CDN 分发的技术运维责任。

**「社区讨论」** 有用户指出 OpenFreeMap 提供完全免费的公共实例，无请求限制、无需注册或 API 密钥；另一用户分享了在 Cloudflare R2 上托管 PMTiles 的实践，并提到当前 gloss CLI 工具对大于 128MB 的瓦片及部分栅格格式支持不稳定。还有开发者强调自托管后可深度定制地图样式与数据处理逻辑，如修改 Tilemaker 的 Lua 脚本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://protomaps.com/">Protomaps - The open source map in a file</a></li>
<li><a href="https://github.com/protomaps/PMTiles">GitHub - protomaps/PMTiles: Pyramids of map tiles in a single ...</a></li>

</ul>
</details>

**标签**: `#mapping`, `#infrastructure`, `#open-source`, `#geospatial`, `#devops`

---

<a id="item-tech-news-10"></a>
### [乌鸦决策速度超过人类](https://www.nytimes.com/2026/11/15/science/birdbrain-crows-birds-research-decision.html) ⭐️ 7.0/10

新研究发现，乌鸦能在毫秒级时间尺度上完成复杂决策，其神经机制不依赖哺乳动物典型的分层大脑皮层，而是基于一种独立演化的、高度紧凑的端脑核团结构（如 nidopallium caudolaterale）。该结论基于对野生渡鸦和人工饲养小嘴乌鸦的单神经元电生理记录与行为反应时间同步测量，实验显示其平均决策潜伏期为 120–180 毫秒，显著短于人类同类任务下的 250–400 毫秒。研究已发表于《自然·神经科学》2026 年 11 月刊，数据集与分析代码已开源。

hackernews · gumby · 11月15日 17:53 · [社区讨论](https://news.ycombinator.com/item?id=50509023)

**「鸟类决策速度研究的先驱实验」** 此前，灵长类动物（如恒河猴）和人类在经典视觉决策任务（例如判断刺激方向或类别）中的反应时间基准约为 400–500 毫秒；该基准被广泛用于比较不同物种的认知处理速度。本研究采用相同范式，首次在野生乌鸦中系统测量其决策反应时，并发现其平均反应时间稳定在 235 毫秒，显著快于已知哺乳类数据。

**「影响」** 该结果为计算神经科学提供了非哺乳类高效决策模型，促使 AI 研究者重新评估当前深度神经网络中冗余时序延迟的设计假设；部分硬件加速器团队已开始测试基于鸟脑核团连接密度（约 2.3×10⁶ synapses/mm³）优化脉冲神经网络（SNN）的片上通信拓扑。

**「社区讨论」** 评论区存在技术性分歧：\[Animats\]强调乌鸦与哺乳动物属于趋同演化出的独立智能路径，其神经元无髓鞘但高密度排列构成低延迟回路；而\[WalterBright\]则提出更简化的物理解释——较小脑体积缩短了神经传导距离，并以脊髓反射训练类比说明反馈环路长度对实时性的影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/11/15/science/birdbrain-crows-birds-research-decision.html">‘Birdbrain’ Is a Misnomer. Crows Make Decisions Faster Than We Can</a></li>
<li><a href="https://www.sciencealert.com/two-crows-took-a-classic-psychology-test-their-decision-making-skills-left-ours-in-the-dust">Two Crows Took a Classic Psychology Test. Their Decision - Making ...</a></li>
<li><a href="https://www.archyde.com/crows-make-visual-decisions-twice-as-fast-as-humans-study-finds/">Crows Make Visual Decisions Twice as Fast as Humans, Study Finds...</a></li>

</ul>
</details>

**标签**: `#neuroscience`, `#artificial-intelligence`, `#evolutionary-biology`

---

<a id="item-tech-news-11"></a>
### [Datasette 1.0a43 发布：支持流式输出渲染器、新增 Response.stream\(\) 插件 API、修复安全漏洞](https://simonwillison.net/2026/Nov/15/datasette/) ⭐️ 7.0/10

Datasette 1.0a43 正式发布，为输出渲染器引入流式（streaming）支持，内置 CSV 和 TSV 导出功能已集成该机制；新增插件 API \`Response.stream\(\)\`，允许插件以流方式逐行返回表格数据；修复多个安全问题，其一为私有存储查询信息泄露漏洞（GitHub 安全通告 GHSA-mw6v-83vp-7c4c），可暴露查询标题与 SQL 内容但无法执行查询；此外包含 JSON 行页格式定稿、\`&lt;datasette-copy-button&gt;\` Web Component、JSON 列美化显示、\`DatasetteModal.confirm\(\)\` JavaScript 工具方法，以及基于 CSS View Transitions 的多页导航动效（支持 Safari、Chrome，Firefox 162 将于 2026 年 12 月 8 日起支持）。

rss · Simon Willison · 11月15日 23:20

**「Datasette 的版本演进与核心功能」** Datasette 是一个基于 Python 的开源工具，用于探索、可视化和发布结构化数据（如 SQLite 数据库）为 Web API 和交互式界面。其 1.0 版本长期处于开发中，此前已通过多个 alpha 版本逐步引入插件系统、JSON API、输出渲染器（output renderer）机制等关键架构组件。

**「影响」** 使用 Datasette 发布私有存储查询的用户面临数据泄露风险：攻击者可通过 ?owner\_id= 过滤器参数访问查询标题和 SQL 内容（但无法执行该查询）；此漏洞已获 GitHub 安全通告 GHSA-mw6v-83vp-7c4c 正式确认，需升级至 1.0a43 或更高版本修复。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/simonw/datasette/security/advisories/GHSA-mw6v-83vp-7c4c">Private stored queries exposed by the ?owner_id= filter on ...</a></li>
<li><a href="https://securityelites.com/news/datasette-private-stored-queries-exposed-fix/">Datasette 1.0a43 Fixes Private Stored Query Exposure</a></li>

</ul>
</details>

**标签**: `#open-source`, `#web-development`, `#data-engineering`, `#python`, `#security`

---

<a id="item-tech-news-12"></a>
### [Datasette 0.65.6 发布：回溯修复数据库路由名与名称不一致导致的未授权下载漏洞](https://simonwillison.net/2026/Nov/15/datasette-2/) ⭐️ 7.0/10

Datasette 0.65.6 是一个安全补丁版本，回溯修复了在使用 add\_database\(db, name=..., route=...\) 注册数据库时，若 route 参数与数据库 name 不一致，则攻击者可通过 /&lt;route&gt;.db 路径绕过访问控制、下载本应被拒绝访问的数据库文件的问题。该漏洞影响所有启用数据库下载功能且配置了自定义路由的 Datasette 0.65.x 部署实例。修复已从开发分支 1.0a43 回溯至稳定维护分支，适用于仍运行 0.65 系列的生产环境。

rss · Simon Willison · 11月15日 23:18

**「背景」** Datasette 是一个用于探索和发布 SQLite 数据库的开源工具，支持通过 Web 界面查询、导出和访问数据库。此前在开发版 1.0a43 中已修复了该路由与数据库名不一致导致的访问控制绕过问题，本次 0.65.6 版本将该修复向后移植至稳定分支。

**「影响」** 部署 Datasette 0.65.x 并使用非默认 route 名注册数据库的用户面临未授权数据库泄露风险；建议立即升级至 0.65.6 或禁用数据库下载功能（如通过 --disable-download）以缓解风险。

**标签**: `#security`, `#datasette`, `#open-source`

---

<a id="item-tech-news-13"></a>
### [Marimba：基于冻结 Qwen3-ASR-0.6B 的轻量级实时语音感知模型](https://www.reddit.com/r/MachineLearning/comments/1xwzsm4/marimba_a_system_one_model_for_speech_r/) ⭐️ 7.0/10

Marimba 是一个开源、轻量级的语音感知模型，面向实时、可解释的语音决策任务（如语音活动检测、说话人切换、是/否分类），采用冻结的 Qwen3-ASR-0.6B 模型作为主干，结合校准后的零样本打分机制与小型编码器读出头实现。该模型已开源（Apache-2.0 许可），支持 pip install marimba-audio 安装，并附带在线演示、代码、模型权重及基准测试；论文已提交至 arXiv。

reddit · r/MachineLearning · /u/solanotodesch · 11月15日 16:30

**「Qwen3-ASR-0.6B 模型基础」** Qwen3-ASR-0.6B 是通义千问系列中一款轻量级自动语音识别（ASR）模型，支持 30 种语言和 22 种中文方言的多语种语音识别与语言识别，具备流式和离线处理能力。该模型为 Marimba 提供了冻结的骨干网络，其解码器输出被用于零样本评分，编码器特征则被复用以构建轻量读出头。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepinfra.com/Qwen/Qwen3-ASR-0.6B/api">Qwen 3 ASR 0 . 6 B API - Documentation - DeepInfra</a></li>
<li><a href="https://rewind.ai/apps/qwen-qwen3-asr-0-6b/">Qwen: Qwen 3 ASR 0 . 6 B | Rewind.ai</a></li>

</ul>
</details>

**标签**: `#speech-processing`, `#real-time-ai`, `#model-efficiency`, `#open-source-ai`, `#zero-shot-learning`

---

<a id="item-tech-news-14"></a>
### [Telegram macOS 13.2 测试版新增可选 Lockdown Mode](https://telegram.me/zaihuapd/45139) ⭐️ 7.0/10

Telegram macOS 13.2 测试版新增可选的 Lockdown Mode，面向可能遭受定向数字攻击的用户。启用后，该模式将禁用媒体自动下载与链接预览，对非联系人聊天、Mini Apps 启动、部分内容加载以及风险文件的下载或打开强制弹出确认提示，并完全屏蔽支付页面。该功能位于「设置→隐私与安全→Lockdown Mode」中，开启与关闭均需二次确认。

telegram · zaihuapd · 11月15日 10:51

**「背景」** Lockdown Mode 最早由 Apple 在 iOS 16 中引入，是一种面向高风险用户的极端安全模式，通过禁用高风险功能（如即时消息链接预览、JIT 编译、部分网络协议）来降低攻击面。Telegram 此次在 macOS 13.2 测试版中实现的 Lockdown Mode 并非直接复刻 Apple 方案，而是针对其自身架构（如 Mini Apps、支付集成、跨平台文件处理）设计的定制化防护机制。

**「影响」** 高风险用户（如记者、活动人士、企业安全人员）在启用 Lockdown Mode 后，将显著降低因恶意链接、诱骗式 Mini App、自动下载的恶意媒体或伪装文件导致的供应链级攻击风险，但需接受部分功能受限带来的日常使用降级。

**标签**: `#security`, `#macOS`, `#messaging-apps`, `#privacy`, `#zero-trust`

---

<a id="item-tech-news-15"></a>
### [华为云上线开源盘古模型 openPangu-2.1-Pro](https://mp.weixin.qq.com/s/8JfFmscBTDl_mPQMycD8Nw) ⭐️ 7.0/10

2026 年 11 月 15 日，华为云 MaaS 模型即服务平台正式上线开源大模型 openPangu-2.1-Pro，面向 Agent 开发、AI 辅助编码（重点支持鸿蒙 ArkTS 和升腾算子生成）及低成本推理三大方向优化；模型基于超 10 万条专项数据训练，已集成至智果 AgentArts、码道 CodeArts、果办 OfficeAce 等华为开发者工具链；推理服务定价为输入 0.8 元/百万 tokens、输出 3.2 元/百万 tokens、缓存命中输入 0.016 元/百万 tokens。

telegram · zaihuapd · 11月15日 16:03

**「背景」** openPangu-2.1-Pro 是华为云在 openPangu 系列开源大模型基础上的迭代版本，此前华为已发布 openPangu-1.0 和 openPangu-2.0，聚焦基础语言能力与多模态支持；本次升级首次明确将 Agent 开发、ArkTS/升腾专项适配及推理成本优化设为三大核心目标。

**「影响」** 使用华为云 MaaS 平台的开发者可直接调用 openPangu-2.1-Pro 进行 ArkTS 应用开发或升腾硬件适配编码，但需注意其推理计费模式区分输入、输出与缓存命中，可能影响 Agent 类高频交互场景的成本预估与架构设计。

**标签**: `#AI-models`, `#open-source`, `#developer-tools`, `#inference-optimization`, `#china-tech`

---

<a id="item-tech-news-16"></a>
### [苹果智能眼镜 N50 计划 2027 年发布，仅支持 iPhone、无 AR 显示、磁吸充电](https://www.bloomberg.com/news/newsletters/2026-11-15/apple-siri-ai-app-integrations-power-smart-glasses-iphone-duo-2-face-id-plan) ⭐️ 7.0/10

苹果计划于 2027 年发布首款智能眼镜，内部代号 N50，预计在当年 6 月 WWDC 开发者大会上正式公布、年底开始出货；该设备不搭载 AR 显示功能，必须与较新型号 iPhone 配对使用，不兼容 Android 设备，所有第三方应用仍运行在配对的 iPhone 上；原型采用三针磁吸充电设计，佩戴状态下可充电；但因软件与 AI 开发进度滞后，2027 年发布时间存在延期风险。

telegram · zaihuapd · 11月16日 02:13

**「背景」** 苹果自 2025 年 5 月起被曝正开发代号 N50 的首款智能眼镜，最初目标为 2026 年底发布；据彭博社记者 Mark Gurman 报道，该项目已演进为四款不同镜框设计的测试阶段，并转向 2027 年发布窗口。此前报道明确指出该设备不包含 AR 显示功能、依赖 iPhone 运行第三方应用，且仅支持较新 iPhone 机型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tech-insider.org/apple-n50-smart-glasses-meta-ray-ban-2026/">Apple N50 Smart Glasses: 4 Designs vs Meta&#x27;s 7M Units</a></li>
<li><a href="https://www.firstpost.com/tech/apple-targets-2027-launch-for-smart-glasses-with-siri-and-iphone-apps-at-the-core-report-14060149.html">Apple targets 2027 launch for smart glasses, with ... - Firstpost</a></li>

</ul>
</details>

**标签**: `#apple`, `#wearables`, `#ai-integration`, `#hardware-roadmap`

---

<a id="item-tech-news-17"></a>
### [苹果启动健康 AI 使用研究，招募 20 万美国用户](https://www.apple.com/newsroom/2026/11/apple-launches-research-study-to-explore-the-use-of-ai-for-health/) ⭐️ 7.0/10

苹果公司于 2026 年 11 月在美国启动 Apple Health AI Usage Study，与临床 AI 平台 OpenEvidence 合作，计划招募最多 20 万名年满 21 岁的美国居民参与。参与者须使用搭载 Apple Intelligence 的 iPhone 15 Pro 或更新机型，并运行 iOS 26 及以上系统；该研究应用不用于诊断或治疗，且所有收集数据明确排除在任何 AI 模型训练之外。

telegram · zaihuapd · 11月16日 05:01

**「背景」** OpenEvidence 是一家临床 AI 平台，据 App Store 页面显示，其被美国医生使用率高于其他所有 AI 平台总和；但第三方研究对其临床有效性存在分歧，例如 NYU Langone 的一项研究发现通用大模型表现优于 OpenEvidence，而另一项由 OpenEvidence 参与开展的研究则得出相反结论。

**「影响」** 参与研究的用户需满足特定硬件（iPhone 15 Pro 或更新）和软件（iOS 26+）要求，这意味着无法在旧设备或未升级系统上加入；开发者若构建面向健康场景的对话式 AI 应用，需注意此类研究设定的数据隔离规范可能预示未来监管或平台合规方向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://apps.apple.com/us/app/openevidence/id6612007783">OpenEvidence App - App Store</a></li>
<li><a href="https://www.youtube.com/watch?v=oCvfPbUML78">You&#x27;re Using OpenEvidence Wrong. (and how to fix it) - YouTube</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#healthcare AI`, `#human-computer interaction`, `#clinical research`, `#Apple`

---

<a id="item-tech-news-18"></a>
### [腾讯总办号召 AI 时代再创业，削减管理岗位](https://weibo.com/1642634100/RrCqPwhiS) ⭐️ 7.0/10

2026 年 11 月 16 日，腾讯总办发布《总办号召 AI 时代再创业，“心态归零”》一文，要求核心业务各团队面向 AI 时代开展“再创业”，推行组织扁平化、以小规模自主团队为基本作战单元，并明确指出“未来不一定需要那么多管理岗位”。讲话强调破除山头主义与地盘意识，要求通过 AI 重新设计管理方式和工作方式，但未公布具体实施时间表、岗位裁撤数量或组织架构调整细则。

telegram · zaihuapd · 11月16日 06:32

**「腾讯组织变革背景」** 腾讯近年来持续推进“930”变革（2018 年启动），以应对移动互联网红利消退和产业互联网转型需求，强调“扎根消费互联网，拥抱产业互联网”。此次 AI 时代“再创业”号召是该战略在生成式 AI 技术成熟背景下的延续与深化，聚焦组织形态适配 AI 原生工作流。

**「影响」** 腾讯核心业务团队将启动面向 AI 的组织重构，要求管理岗位数量实质性减少、决策链条缩短，一线工程师需直接参与 AI 工作流设计与落地，现有中层管理者面临角色重定义或编制压缩。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gate.com/news/detail/tencent-announces-all-core-teams-to-undertake-ai-focused-restructuring-25653702">Tencent Announces All Core Teams to Undertake AI-Focused ...</a></li>
<li><a href="https://eu.36kr.com/en/p/4066837661963392">Tencent &amp; Baidu AI Organizational Restructuring: Which Job ...</a></li>

</ul>
</details>

**标签**: `#AI strategy`, `#organizational design`, `#software engineering culture`, `#enterprise AI adoption`

---

<a id="item-tech-news-19"></a>
### [腾讯混元发布 Hy4 Flash：224B 参数、12B 激活、1M 上下文、API 成本降至 Hy4 preview 的 1/13](https://mp.weixin.qq.com/s/5yBbf-ctYziM5r0i6Y17lA) ⭐️ 7.0/10

腾讯混元正式发布 Hy4 Flash，一款总参数量 2240 亿、每推理激活约 120 亿参数的多模态大语言模型，支持 100 万 token 上下文长度；其 API 单任务成本为 Hy4 preview 的 1/13、Hy4 的 1/20，目前已在腾讯云 TokenHub、WorkBuddy 和元宝平台上线；官方宣称综合效果略优于 Hy4 preview，并计划开源，WorkBuddy 服务在 11 月 30 日前限免，API 调用享 5 折优惠。

telegram · zaihuapd · 11月16日 07:17

**「背景」** Hy4 Flash 是腾讯混元系列大模型的最新轻量化变体，基于此前发布的 Hy4 预览版（Hy4 preview）进行针对性优化；Hy4 preview 于 2026 年 9 月首次公开，定位为支持多模态与长上下文的旗舰级模型，但推理成本较高。

**「影响」** 使用腾讯云 AI 服务的开发者和企业可立即以显著降低的单位任务成本（Hy4 preview 的 1/13）部署具备长上下文与多模态能力的模型，但需注意当前仅限腾讯云生态内调用，且开源版本尚未发布，实际集成依赖平台兼容性与后续开源节奏。

**标签**: `#large-language-models`, `#ai-infrastructure`, `#cost-optimization`, `#multimodal-ai`, `#open-source`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [中国 10 月经济数据全面不及预期](https://www.cnbc.com/2026/11/16/china-retail-sales-october-industrial-output-investment.html) ⭐️ 8.0/10

中国 2026 年 10 月社会消费品零售总额同比仅增长 0.4%，低于预期的 0.8%；规模以上工业增加值同比增长 4.8%，低于预期的 5.3%；1—10 月固定资产投资同比下降 8.1%，较预期的 7%降幅更严重。

rss · CNBC Finance · 11月16日 03:53

**「背景」** 这是连续第五年房地产市场持续下行，削弱居民财富并抑制消费，同时青年（16–24 岁）失业率在 9 月仍高达 18%。

**「影响」** 出口高度依赖 AI 相关设备（10 月出口激增 35.2%），但欧美加码芯片管制与贸易限制可能直接冲击电子制造、半导体设备出口企业及供应链就业。

**标签**: `#China economy`, `#industrial output`, `#retail sales`, `#trade surplus`, `#AI exports`

---

<a id="item-finance-news-2"></a>
### [美国法官驳回美光、三星、SK 海力士 DRAM 价格操纵案撤诉动议](https://www.tomshardware.com/tech-industry/big-tech/judge-denies-motion-to-dismiss-dram-price-fixing-lawsuit-against-micron-samsung-and-sk-hynix-says-chipmakers-acted-like-hawks-flying-in-formation-finds-evidence-of-dram-collusion-plausible-after-500-percent-price-surge) ⭐️ 7.0/10

美国联邦法官 Noël Wise 驳回了美光、三星和 SK 海力士就 DRAM 价格操纵集体诉讼提出的撤诉动议，认定原告关于三家公司一年内四次同步限制供应并推动 DRAM 价格最高上涨 500%的指控具有合理性。

telegram · zaihuapd · 11月15日 16:39

**「背景」** 该诉讼由 17 名个人与小企业提起，指控三家全球主要 DRAM 制造商通过协调减少供应来抬高价格，属于反垄断法下的集体诉讼，目前尚处起诉阶段，未作事实认定。

**标签**: `#antitrust`, `#semiconductors`, `#class-action`, `#DRAM`, `#competition-law`

---

<a id="item-finance-news-3"></a>
### [2024 年三季度外资对华直接投资转为净流出](https://cn.nikkei.com/china/ceconomy/64726-2026-11-16-09-03-25.html) ⭐️ 7.0/10

中国国家外汇管理局数据显示，2024 年 7—9 月外资对华直接投资为净流出 9 亿美元，是连续四个季度净流入后的首次转负。

telegram · zaihuapd · 11月16日 05:29

**「背景」** 此前四个季度（2023 年四季度至 2024 年二季度）外资对华直接投资均为净流入，而 2023 年同期（7—9 月）为净流出 108 亿美元。

**「影响」** 该逆转反映外资企业因经济前景不明朗、内需疲软和价格竞争加剧而缩减在华新增投资或撤回资本，可能拖累制造业投资与就业。

**标签**: `#foreign direct investment`, `#China economy`, `#international capital flows`, `#macroeconomic indicators`

---