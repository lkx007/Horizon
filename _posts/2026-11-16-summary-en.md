---
layout: default
title: "Horizon Summary: 2026-11-16 (EN)"
date: 2026-11-16
lang: en
---

> From 41 items, 22 important content pieces were selected

---

**Technology News**
1. [Universal XSS vulnerability patched in uBlock Origin 1.75.4](#item-tech-news-1) ⭐️ 9.0/10
2. [Qwen4-Max launches with 2.4T-parameter sparse MoE, vision, million-token context, and 58% lower task cost](#item-tech-news-2) ⭐️ 9.0/10
3. [Meta FAIR and NYU find vision-only parameters essential but encoder pretraining optional in MLLMs](#item-tech-news-3) ⭐️ 8.0/10
4. [CUDA memcpy tuner achieves 5x speedup for pageable transfers on NVIDIA B300](#item-tech-news-4) ⭐️ 8.0/10
5. [Meituan open-sources LongCat-2.5, a 1.6-trillion-parameter multimodal agent model trained exclusively on Huawei Ascend chips](#item-tech-news-5) ⭐️ 8.0/10
6. [Expired Bitly links hijacked for malicious redirects](#item-tech-news-6) ⭐️ 7.0/10
7. [Nvidia&\#x27;s Ecosystem Lock-in Erodes as Cloud Providers Build Custom AI Chips](#item-tech-news-7) ⭐️ 7.0/10
8. [MacBook Pro OLED display exhibits low-frequency PWM flicker at high brightness](#item-tech-news-8) ⭐️ 7.0/10
9. [Protomaps enables affordable, self-hosted vector map tile infrastructure](#item-tech-news-9) ⭐️ 7.0/10
10. [Crows make decisions faster than humans using non-mammalian brain architecture](#item-tech-news-10) ⭐️ 7.0/10
11. [Datasette 1.0a43 adds streaming output renderers, Response.stream\(\) API, and security fixes](#item-tech-news-11) ⭐️ 7.0/10
12. [Datasette 0.65.6 backports security fix for unauthorized database download](#item-tech-news-12) ⭐️ 7.0/10
13. [Marimba: open-source lightweight speech perception model using frozen Qwen3-ASR-0.6B](#item-tech-news-13) ⭐️ 7.0/10
14. [Telegram macOS 13.2 beta adds opt-in Lockdown Mode](#item-tech-news-14) ⭐️ 7.0/10
15. [Huawei Cloud launches openPangu-2.1-Pro for Agent development and ArkTS/Ascend-aware AI coding](#item-tech-news-15) ⭐️ 7.0/10
16. [Apple N50 smart glasses target 2027 release with iPhone-only Siri integration](#item-tech-news-16) ⭐️ 7.0/10
17. [Apple Launches Health AI Usage Study with 200,000 Participants](#item-tech-news-17) ⭐️ 7.0/10
18. [Tencent Executive Committee Calls for AI-Era Re-entrepreneurship and Fewer Management Roles](#item-tech-news-18) ⭐️ 7.0/10
19. [Tencent Hunyuan Releases Hy4 Flash: 224B-Parameter Multimodal LLM with 1M Context and 1/13 Per-Task Cost of Hy4 Preview](#item-tech-news-19) ⭐️ 7.0/10

**Financial News**
1. [China&\#x27;s October 2026 Economic Data Misses Forecasts Amid Deepening Slowdown](#item-finance-news-1) ⭐️ 8.0/10
2. [US Judge Rejects Motion to Dismiss DRAM Price-Fixing Lawsuit](#item-finance-news-2) ⭐️ 7.0/10
3. [Q3 2024 Foreign Direct Investment in China Turns Net Negative](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Universal XSS vulnerability patched in uBlock Origin 1.75.4](https://iter.ca/post/ubo-uxss/) ⭐️ 9.0/10

A universal cross-site scripting \(UXSS\) vulnerability in uBlock Origin’s website-embedded element picker allowed malicious websites to inject and execute arbitrary JavaScript across any origin. The flaw stemmed from the picker injecting UI elements directly into the page’s DOM, breaking same-origin policy isolation. It was patched in version 1.75.4 \(released November 10, 2026\), with uBO Lite updated to version 2026.1110.1816. The vulnerability affected all users running versions prior to those patches.

hackernews · zaik · Nov 16, 02:04 · [Discussion](https://news.ycombinator.com/item?id=50513160)

**「Background」** uBlock Origin’s element picker is a feature that injects a UI overlay directly into the webpage’s DOM to let users select elements for filtering rules; this design requires the extension to run script in the page context, which—when combined with insufficient isolation—enabled universal XSS. The vulnerability exploited the fact that the picker’s injected elements could be manipulated by malicious websites to execute arbitrary JavaScript across origins, a risk inherent to DOM-injected UIs in browser extensions.

**「Impact」** Users running uBlock Origin versions prior to 1.75.4 \(MV2\) or uBO Lite prior to 2026.1110.1816 were exposed to universal XSS, enabling malicious websites to execute arbitrary JavaScript in the context of any other domain — including sensitive sites like banking or email — via the element picker UI injected into the page DOM.

**「Community discussion」** Commenters highlighted architectural concerns about extensions embedding UI in the page DOM—ByteOfWood noted risks like credential leakage in password managers, and akersten argued the picker UI should reside in browser chrome instead of the webpage’s DOM. renehsz asked whether the AdNauseam fork is also affected, but no confirmation or denial was provided in the comments.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/gorhill/uBlock/security/advisories/GHSA-cmqw-9r2w-6wv2">Universal XSS from website-driven element picker</a></li>
<li><a href="https://techbytes.app/posts/universal-xss-in-ublock-origin-from-website-driven-element-picker/">Universal XSS in uBlock Origin from website-driven element picker</a></li>
<li><a href="https://todayforai.com/en/items/art-bdf7d819-af2">uBlock Origin Patches One-Click Universal XSS Flaw</a></li>
<li><a href="https://iter.ca/post/ubo-uxss/">Universal XSS in uBlock Origin from website-driven element picker</a></li>

</ul>
</details>

**Tags**: `#browser-security`, `#extension-vulnerability`, `#uxss`, `#web-security`, `#uBlock-Origin`

---

<a id="item-tech-news-2"></a>
### [Qwen4-Max launches with 2.4T-parameter sparse MoE, vision, million-token context, and 58% lower task cost](https://mp.weixin.qq.com/s/pJUt0xwD6H-WMyzd8TjZaQ) ⭐️ 9.0/10

Alibaba has officially launched Qwen4-Max, a 2.4-trillion-parameter sparse Mixture-of-Experts \(MoE\) large language model with native multimodal vision support and million-token context length. It is now available via API, with per-task pricing reduced from ¥26.58 to ¥11.16 \(a 58% decrease\) and token consumption cut by nearly 50%. The team announced plans to open-source smaller variants of the Qwen4 series, though no release date, model sizes, or license terms were specified.

telegram · zaihuapd · Nov 16, 02:52

**「Background」** Qwen4-Max succeeds the Qwen3.8 series, which included models such as Qwen3.8-Max and variants like &\#x27;prime&\#x27; and &\#x27;0902&\#x27;—previously benchmarked for speed and cost trade-offs on platforms like OpenRouter. The Qwen series has evolved from earlier open-weight versions \(e.g., Qwen2, Qwen2.5\) toward increasingly large, multimodal, and MoE-based architectures, with Qwen3.8 already supporting vision and long-context capabilities but at higher latency and cost.

**「Impact」** Developers using Qwen APIs will immediately benefit from significantly lower inference costs and improved multimodal and long-context capabilities, but must adapt integrations to the new model’s interface and behavior; the promised open-sourcing of smaller Qwen4 models—if delivered—could accelerate adoption in resource-constrained or privacy-sensitive deployments.

**「Community discussion」** Commenters noted Qwen4-Max’s high cost per task relative to competitors \(e.g., $3.27 vs. $0.36 for GPT-6.1 Sol on Artificial Analysis\), while expressing cautious optimism about future smaller, faster variants like &\#x27;Flash&\#x27; or 27B models; one developer attributed Qwen3.8’s poor arena performance primarily to low inference speed \(30 tokens/sec vs. ~80 for Opus\), not capability.

**Tags**: `#large-language-models`, `#open-source-ai`, `#multimodal-ai`, `#moE-architecture`, `#programming-ai`

---

<a id="item-tech-news-3"></a>
### [Meta FAIR and NYU find vision-only parameters essential but encoder pretraining optional in MLLMs](https://www.reddit.com/r/MachineLearning/comments/1xx1k2o/meta_fair_nyu_unbundling_multimodal_vision/) ⭐️ 8.0/10

Meta FAIR and NYU researchers trained over 200 multimodal LLMs from scratch—including both vision encoder and LLM components—under identical data, compute, and evaluation conditions to isolate the role of vision encoders. They found that separate encoder pretraining \(e.g., contrastive or captioning objectives\) provides no VQA performance benefit over joint training, even when pretraining is computationally &\#x27;free&\#x27;; however, vision-specific parameters—whether in a standalone encoder or injected as zero-initialized vision-only branches into early LLM layers—are strictly necessary for strong multimodal performance. Models without dedicated vision parameters underperformed across all backbone sizes \(0.6B–6.4B\), requiring ~3× more compute to match encoder-equipped models, while &\#x27;in-fusion&\#x27; architectures placing vision-only attention and FFN weights in the first 8 layers of Qwen3-1.7B–6.4B matched or slightly exceeded standard encoder performance with 13% lower time-to-first-token.

reddit · r/MachineLearning · /u/trungh98 · Nov 15, 17:38

**「Background」** Multimodal LLMs \(MLLMs\) typically use a pretrained vision encoder \(e.g., ViT\) to process images before fusing features with an LLM, assuming such pretraining improves downstream multimodal understanding. Recent conflicting model releases—like Gemma 4 12B omitting an encoder, Kimi K3 training one from scratch, and Inkling 2 Small reintroducing it—highlight unresolved design trade-offs around encoder necessity, pretraining value, and parameter allocation.

**「Impact」** MLLM developers can eliminate costly, separate vision encoder pretraining steps without sacrificing VQA performance—but must retain dedicated vision-only parameters, either in a conventional encoder or via in-fusion into early LLM layers, to avoid severe performance degradation and inefficient compute scaling.

**「Community discussion」** No community comments were available for this submission.

**Tags**: `#multimodal`, `#vision-language-models`, `#model-architecture`, `#ablation-study`, `#pretraining`

---

<a id="item-tech-news-4"></a>
### [CUDA memcpy tuner achieves 5x speedup for pageable transfers on NVIDIA B300](https://www.reddit.com/r/MachineLearning/comments/1xx2n25/making_cudamemcpy_5x_faster_on_a_b300_p/) ⭐️ 8.0/10

A user-developed open-source CUDA memory transfer tuner tool improves cudaMemcpy throughput for pageable memory transfers by 5× on NVIDIA B300 GPUs, raising CPU→GPU transfer speed from 10.2 GB/s to 51.5 GB/s for a 1 GiB tensor, as measured using PyTorch&\#x27;s .to\(&\#x27;cuda&\#x27;\) and .cpu\(\) calls with synchronization. The optimization targets pageable \(non-pinned\) host memory transfers—a common but suboptimal pattern—and requires running the benchmark under the cmt tune wrapper. The tool is documented in a technical blog and released on GitHub with reproducible benchmarks.

reddit · r/MachineLearning · /u/makneeee · Nov 15, 18:20

**「Background」** cudaMemcpy between pageable host memory and GPU device memory is inherently slower than with pinned \(page-locked\) memory because it requires OS-mediated page faults and temporary staging buffers; NVIDIA’s documentation and prior performance guides recommend pinning host memory for high-throughput transfers, but many frameworks and user code still rely on pageable transfers for convenience or compatibility.

**「Impact」** ML engineers and HPC practitioners using PyTorch or raw CUDA with pageable memory transfers on B300 GPUs can immediately gain ~5× memcpy bandwidth without modifying application code—by wrapping execution with the cmt tool—though this introduces a dependency on an external, community-maintained tuner and does not eliminate the underlying inefficiency of pageable transfers.

**「Community discussion」** No substantive community comments were available in the source item.

**Tags**: `#CUDA`, `#GPU optimization`, `#machine learning systems`, `#memory transfer`, `#systems performance`

---

<a id="item-tech-news-5"></a>
### [Meituan open-sources LongCat-2.5, a 1.6-trillion-parameter multimodal agent model trained exclusively on Huawei Ascend chips](https://the-decoder.com/meituan-releases-a-1-6-trillion-parameter-agent-model-that-never-touched-an-nvidia-gpu/) ⭐️ 8.0/10

Meituan has open-sourced LongCat-2.5, a 1.6-trillion-parameter multimodal agent model designed for autonomous, multi-step programming tasks. The model was trained entirely on Huawei Ascend AI accelerators—no NVIDIA GPUs were used—and activates approximately 48 billion parameters per token. It supports text, image, and video inputs, and its weights are released under the MIT license for commercial use. On Terminal Bench v2.1, it scores 88.4, slightly below Claude Opus 5’s 89.1.

telegram · zaihuapd · Nov 15, 11:08

**「Background」** LongCat-2.5 is the latest iteration of Meituan’s LongCat series of multimodal agent models, following earlier versions such as LongCat-1 and LongCat-2, which were also designed for autonomous programming and terminal-based task execution. Unlike prior releases, LongCat-2.5 is distinguished by its scale \(1.6 trillion total parameters\) and its explicit training exclusively on Huawei Ascend AI accelerators—marking a deliberate departure from the NVIDIA GPU-dominated training infrastructure common in large-model development.

**「Impact」** Developers seeking to deploy large multimodal agent models on domestic Chinese hardware now have a production-ready, MIT-licensed option—LongCat-2.5—that achieves competitive performance \(88.4 on Terminal Bench v2.1\) without requiring NVIDIA GPUs, and includes a documented 4-bit quantized self-hosting setup for Huawei Ascend chips.

<details><summary>References</summary>
<ul>
<li><a href="https://phemex.com/news/article/meituan-opensources-16tparameter-longcat25-model-trained-entirely-on-domestic-chinese-hardware-103629">Meituan LongCat-2.5: 1.6T MoE AI Model Trained on ... - Phemex</a></li>

</ul>
</details>

**Tags**: `#artificial-intelligence`, `#open-source`, `#hardware-sovereignty`, `#agent-systems`, `#multimodal-models`

---

<a id="item-tech-news-6"></a>
### [Expired Bitly links hijacked for malicious redirects](https://ransomnews.com/burger-king-tweet-bitly-link-hijack-2026/) ⭐️ 7.0/10

Expired Bitly links are being hijacked to redirect users to malicious destinations, as demonstrated by a compromised Burger King tweet that pointed to an expired Bitly URL now serving malware. Bitly does not retain ownership or control of shortened URLs after account deactivation or link expiration, enabling attackers to register and repurpose those short paths. This behavior affects any user or organization that relied on Bitly for long-term linking without active account maintenance, and it is not limited to deprecated or legacy accounts—active but inactive links are vulnerable. The issue reflects Bitly’s architectural decision to treat short links as ephemeral identifiers rather than persistent, owned resources.

hackernews · hspeiser · Nov 15, 22:11 · [Discussion](https://news.ycombinator.com/item?id=50511395)

**「URL shortening and link expiration」** URL shortening services like Bitly assign persistent, opaque identifiers to long URLs and store the mapping server-side; when a shortened link is no longer actively maintained—due to account deactivation, service discontinuation, or policy changes—the underlying redirect can become unmanaged and vulnerable to reuse or hijacking. This architectural pattern inherently delegates long-term link integrity to a third-party service, contradicting the web’s original design principle of persistent, owner-controlled identifiers.

**「Impact」** Users clicking on previously legitimate Bitly links—such as the compromised Burger King tweet—may now be redirected to malicious or unrelated content, including spam, phishing pages, or unrelated commercial sites, because Bitly does not retain ownership or enforce redirect continuity after link expiration or account deactivation.

**「Community discussion」** Multiple commenters argue that outsourced URL shorteners introduce systemic reliability and security risks due to their transient nature and lack of long-term ownership guarantees, with one noting that such services are &\#x27;an order of magnitude worse for the internet&\#x27; than in-house alternatives. Another user shared a real-world example where an unregistered Bit.ly link embedded in a published book was later hijacked—not maliciously, but illustratively—highlighting how easily unmonitored short links become uncontrolled assets.

**Tags**: `#web-security`, `#systems-reliability`, `#link-rot`, `#infrastructure-risk`, `#url-shortening`

---

<a id="item-tech-news-7"></a>
### [Nvidia&\#x27;s Ecosystem Lock-in Erodes as Cloud Providers Build Custom AI Chips](https://steveblank.com/2026/11/15/whats-next-for-nvidia/) ⭐️ 7.0/10

Major cloud providers and AI companies—including AWS, Google, and Meta—are developing custom AI accelerators and software stacks that reduce reliance on Nvidia GPUs and the CUDA programming model. This shift undermines Nvidia’s ecosystem lock-in, as customers vertically integrate hardware and software to optimize for specific workloads and cost. The trend is accelerating due to maturing AI workloads, improved ASIC design capabilities \(e.g., via partnerships with Broadcom\), and rising adoption of hardware-agnostic abstractions like Triton and MLIR. While Nvidia continues to innovate, its historically high margins face structural pressure from this commoditization and bypass of CUDA.

hackernews · zdw · Nov 15, 23:55 · [Discussion](https://news.ycombinator.com/item?id=50512235)

**「Custom AI chips erode Nvidia&\#x27;s CUDA moat」** Nvidia&\#x27;s dominance in AI acceleration has long rested on its general-purpose GPUs and the CUDA software ecosystem, which locks developers into its hardware. However, major cloud providers—including Google \(TPUs\), Amazon \(Trainium\), Meta \(MTIA\), and Microsoft—have increasingly designed and deployed custom AI ASICs, often in partnership with Broadcom, to optimize for specific workloads like inference and recommendation systems. These efforts reduce reliance on CUDA by building alternative software stacks and abstraction layers, accelerating a structural shift away from GPU-centric AI infrastructure.

**「Community Discussion」** Commenters highlight CUDA’s declining relevance, with one noting that &\#x27;CUDA is becoming less relevant, and the rate at which that is happening is about to go parabolic&\#x27; due to customer-built abstraction layers and debug tools. Another commenter contextualizes Steve Blank as a respected startup methodology author—but no technical analysis or consensus on Nvidia’s strategic response emerges from the thread.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2025/11/21/nvidia-gpus-google-tpus-aws-trainium-comparing-the-top-ai-chips.html">Nvidia Blackwell, Google TPUs, AWS Trainium: Comparing top AI ...</a></li>
<li><a href="https://www.aranca.com/knowledge-library/articles/investment-research/the-rise-of-custom-ai-chips">The Rise of Custom AI Chips: How Big Tech is Challenging ...</a></li>
<li><a href="https://fffinstill.com/blog/custom-ai-asics-vs-gpus-broadcom-google-amazon-approach">Custom AI ASICs vs. GPUs: The Broadcom/Google/Amazon Approach</a></li>

</ul>
</details>

**Tags**: `#AI-hardware`, `#GPU`, `#CUDA`, `#cloud-computing`, `#semiconductors`

---

<a id="item-tech-news-8"></a>
### [MacBook Pro OLED display exhibits low-frequency PWM flicker at high brightness](https://macanorak.com/the-macbook-pros-oled-pwm-problem-when-a-better-display-becomes-worse-to-use/) ⭐️ 7.0/10

The new MacBook Pro’s OLED display uses pulse-width modulation \(PWM\) for brightness control at frequencies as low as ~240 Hz—even at high brightness levels—contrary to expectations for modern OLEDs. Oscilloscope measurements confirm the presence of this low-frequency flicker, which persists across much of the usable brightness range due to phase-offset PWM behavior in its tandem OLED subpixels. This affects users with photosensitivity, migraine disorders, or post-concussion syndrome, potentially causing eye strain and discomfort. The issue is present in shipped hardware, not a pre-release prototype or vendor claim.

hackernews · MacAnorak · Nov 15, 13:15 · [Discussion](https://news.ycombinator.com/item?id=50506719)

**「PWM dimming in OLED displays」** Pulse Width Modulation \(PWM\) is a brightness control method used in OLED displays where the light-emitting pixels are rapidly switched on and off; the perceived brightness depends on the duty cycle of that switching. Unlike LCDs with separate backlights, OLEDs modulate the pixels themselves, making PWM a common—but not universal—approach, especially when DC dimming is unavailable or insufficient across the full brightness range.

**「Impact」** Users with flicker sensitivity may experience increased eye strain, headaches, or difficulty concentrating when using the MacBook Pro OLED display at typical brightness settings, and no built-in OS-level DC dimming toggle or firmware update has been confirmed to mitigate the behavior.

**「Community discussion」** Commenters debate the measured PWM frequency—some argue the effective flicker rate is higher \(e.g., ~960 Hz\) due to out-of-phase PWM on tandem OLED subpixels—while others express concern that Apple shipped a display with perceptible flicker despite known physiological sensitivity thresholds cited in peer-reviewed literature.

<details><summary>References</summary>
<ul>
<li><a href="https://macanorak.com/the-macbook-pros-oled-pwm-problem-when-a-better-display-becomes-worse-to-use/">The MacBook Pro ’s OLED PWM Problem: When a ‘Better’ Display...</a></li>

</ul>
</details>

**Tags**: `#display-technology`, `#hardware-engineering`, `#accessibility`, `#macos`, `#oled`

---

<a id="item-tech-news-9"></a>
### [Protomaps enables affordable, self-hosted vector map tile infrastructure](https://bruceroettgers.eu/blog/protomaps/) ⭐️ 7.0/10

Protomaps is an open-source toolkit that simplifies and reduces the cost of self-hosting vector map tiles, using PMTiles format and CLI tools built around Tilemaker and Maplibre. It enables developers to replace commercial providers like Maptiler—Cartes.app migrated from Maptiler to Protomaps after exceeding free-tier limits and facing €150/month bills. Hosting costs are minimal, and customization is supported via editable Lua processing scripts and dynamic Maplibre styles. The solution targets privacy-conscious, cost-sensitive, or highly customized mapping use cases, and works with infrastructure like Cloudflare R2.

hackernews · bcye · Nov 15, 19:26 · [Discussion](https://news.ycombinator.com/item?id=50509837)

**「Background」** Protomaps builds on the PMTiles specification—a single-file, HTTP-range-request–enabled archive format for tiled geospatial data—which enables serving vector map tiles from static storage \(e.g., S3, Cloudflare R2\) without a dedicated tile server. The PMTiles format, developed by Protomaps and open-sourced in 2022, replaces traditional tile directory structures with a compact, seekable binary layout, making self-hosting feasible for small teams and privacy-sensitive applications.

**「Impact」** Developers migrating from commercial map tile providers like Maptiler to Protomaps can reduce monthly infrastructure costs from ~€150 to near-zero, as demonstrated by Cartes.app’s switch; however, self-hosting requires operational investment in tile generation \(e.g., customizing Tilemaker’s processing.lua\) and does not scale to high-resolution satellite imagery beyond zoom level 17 without multi-terabyte storage.

**「Community discussion」** Commenters highlight related tools—OpenFreeMap \(a free public instance with no API keys or tracking\), PMTiles viewers like &\#x27;gloss&\#x27;, and ntmaps \(a Go library\)—while noting practical limitations such as large-tile handling failures in gloss and storage scalability challenges for high-resolution satellite imagery beyond zoom level 17.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/protomaps/PMTiles">GitHub - protomaps/PMTiles: Pyramids of map tiles in a single ...</a></li>
<li><a href="https://openfreemap.org/">OpenFreeMap</a></li>

</ul>
</details>

**Tags**: `#mapping`, `#infrastructure`, `#open-source`, `#geospatial`, `#devops`

---

<a id="item-tech-news-10"></a>
### [Crows make decisions faster than humans using non-mammalian brain architecture](https://www.nytimes.com/2026/11/15/science/birdbrain-crows-birds-research-decision.html) ⭐️ 7.0/10

New research shows crows make rapid, flexible decisions despite lacking a layered cerebral cortex—the mammalian brain’s highest integration center. Their decision-making speed and behavioral flexibility arise from a distinct neural architecture involving densely packed neurons in the pallium, not cortical layers. This finding is based on controlled behavioral assays and neuroanatomical imaging of corvids, not theoretical models or anecdotal observation. The work challenges the assumption that mammalian-style cortical organization is necessary for advanced cognition.

hackernews · gumby · Nov 15, 17:53 · [Discussion](https://news.ycombinator.com/item?id=50509023)

**「Background」** Crows lack a layered cerebral cortex—the mammalian brain structure long considered essential for high-level cognition—but possess densely packed pallial neurons organized differently. Earlier research established that corvids exhibit advanced cognitive abilities such as tool use, future planning, and social reasoning despite this divergent neuroanatomy, suggesting intelligence can arise via multiple evolutionary pathways.

**「Impact」** AI and computational neuroscience researchers may revisit assumptions about neural efficiency and minimal architectures for real-time decision-making, as crow brains achieve high-speed processing with lower neuron counts and no cortex—suggesting alternative design principles for edge AI or neuromorphic hardware.

**「Community discussion」** Commenters highlight convergent evolution across mammals, corvids, and octopuses as evidence that intelligence can emerge from radically different neural substrates; one user notes that shorter neural conduction distances in smaller brains may contribute to speed, while another emphasizes birds’ quantum-enabled magnetoreception and decentralized timekeeping as underappreciated facets of avian cognition.

**Tags**: `#neuroscience`, `#artificial-intelligence`, `#evolutionary-biology`

---

<a id="item-tech-news-11"></a>
### [Datasette 1.0a43 adds streaming output renderers, Response.stream\(\) API, and security fixes](https://simonwillison.net/2026/Nov/15/datasette/) ⭐️ 7.0/10

Datasette 1.0a43 introduces streaming support for output renderers, enabling the built-in CSV and TSV export mechanisms to stream results row-by-row instead of buffering entirely in memory. It adds a new \`Response.stream\(\)\` plugin API for developers to implement streaming renderers, and includes security fixes—one of which is documented in GitHub Security Advisory GHSA-mw6v-83vp-7c4c—addressing unauthorized exposure of private stored query titles and SQL \(though not execution\). The release also delivers dozens of smaller improvements, including CSS view transitions for smoother multi-page navigation in Safari, Chrome, and upcoming Firefox 162.

rss · Simon Willison · Nov 15, 23:20

**「Datasette&\#x27;s output renderer architecture」** Datasette has long supported plugin-defined output renderers—functions that convert database query results into HTTP responses in formats like HTML, JSON, CSV, or TSV. Prior to 1.0a43, these renderers operated on fully materialized result sets, loading all rows into memory before generating the response.

**「Impact」** Users exporting large datasets via CSV or TSV will experience reduced memory pressure and faster response times due to the new streaming renderer implementation, which leverages Python 3 asyncio and efficient pagination; additionally, operators running Datasette with private stored queries must upgrade to 1.0a43 to prevent unauthorized disclosure of query titles and SQL \(though not execution\), as documented in GitHub Security Advisory GHSA-mw6v-83vp-7c4c.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.datasette.io/en/stable/csv_export.html">CSV export - Datasette documentation</a></li>
<li><a href="https://github.com/simonw/datasette/security/advisories/GHSA-mw6v-83vp-7c4c">Private stored queries exposed by the ?owner_id= filter on ...</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#web-development`, `#data-engineering`, `#python`, `#security`

---

<a id="item-tech-news-12"></a>
### [Datasette 0.65.6 backports security fix for unauthorized database download](https://simonwillison.net/2026/Nov/15/datasette-2/) ⭐️ 7.0/10

Datasette 0.65.6 backports a security fix from version 1.0a43 that prevents unauthorized download of databases when a custom route name is used via \`add\_database\(db, name=..., route=...\)\`. Specifically, if the route differs from the database name, attackers could previously access the database file directly at \`/&lt;route&gt;.db\` even when denied permission to the database. This patch applies to the stable 0.65.x series and addresses an access control bypass vulnerability in multi-tenant or permissioned deployments.

rss · Simon Willison · Nov 15, 23:18

**「Background」** Datasette is an open-source Python tool for exploring, publishing, and sharing data from SQLite databases via a web interface. It supports fine-grained access control, including per-database permissions, and allows programmatic registration of databases with custom names and URL routes using the \`add\_database\(\)\` API.

**「Impact」** Users running Datasette 0.65.x with custom database routes must upgrade to 0.65.6 to prevent unauthorized \`.db\` file downloads; deployments relying on Datasette’s access controls for database confidentiality are otherwise vulnerable.

**Tags**: `#security`, `#datasette`, `#open-source`

---

<a id="item-tech-news-13"></a>
### [Marimba: open-source lightweight speech perception model using frozen Qwen3-ASR-0.6B](https://www.reddit.com/r/MachineLearning/comments/1xwzsm4/marimba_a_system_one_model_for_speech_r/) ⭐️ 7.0/10

Marimba is an open-source, Apache-2.0-licensed speech perception model that performs real-time, typed decisions—including voice activity detection, speaker change detection, turn-ending identification, speaker count estimation, and yes/no classification—using a frozen Qwen3-ASR-0.6B backbone. It employs calibrated zero-shot scoring over ASR decoder hypotheses for word- and language-level tasks, and small trainable encoder readout heads for low-level audio decisions. The model is pip-installable as \`marimba-audio\`, with weights, code, and benchmarks publicly available; a paper was submitted to arXiv the week of November 15, 2026.

reddit · r/MachineLearning · /u/solanotodesch · Nov 15, 16:30

**「Background」** Qwen3-ASR-0.6B is a compact, multilingual automatic speech recognition model supporting 30 languages and 22 Chinese dialects, designed for both streaming and offline use. Marimba builds upon this frozen ASR backbone—using its decoder hypotheses for zero-shot scoring and adding small encoder readouts—rather than fine-tuning or replacing it.

**「Impact」** Developers building edge or low-latency speech interfaces can deploy Marimba without fine-tuning large models, as it requires only lightweight readouts atop a frozen 0.6B-parameter ASR model and supports real-time inference with typed, interpretable outputs.

<details><summary>References</summary>
<ul>
<li><a href="https://deepinfra.com/Qwen/Qwen3-ASR-0.6B/api">Qwen 3 ASR 0 . 6 B API - Documentation - DeepInfra</a></li>
<li><a href="https://rewind.ai/apps/qwen-qwen3-asr-0-6b/">Qwen: Qwen 3 ASR 0 . 6 B | Rewind.ai</a></li>

</ul>
</details>

**Tags**: `#speech-processing`, `#real-time-ai`, `#model-efficiency`, `#open-source-ai`, `#zero-shot-learning`

---

<a id="item-tech-news-14"></a>
### [Telegram macOS 13.2 beta adds opt-in Lockdown Mode](https://telegram.me/zaihuapd/45139) ⭐️ 7.0/10

Telegram macOS 13.2 beta introduces an opt-in Lockdown Mode, accessible via Settings → Privacy &amp; Security, that restricts media auto-download, link previews, non-contact chats, Mini Apps, risky file handling, and payment UI to mitigate targeted digital attacks. The mode requires explicit confirmation to enable or disable, and when active, prompts for confirmation before loading certain content or opening potentially unsafe files. This is a shipped capability in the beta version—not merely announced—and applies only to macOS users running Telegram 13.2 beta; no iOS, Android, or web versions are mentioned as supporting it.

telegram · zaihuapd · Nov 15, 10:51

**「Background」** Lockdown Mode is a security-hardening feature first introduced by Apple in iOS 16 and macOS Ventura to protect high-risk users from sophisticated cyberattacks by disabling or restricting high-risk functionality. Telegram’s implementation adapts this concept to its cross-platform messaging architecture, targeting threats like zero-click exploits, malicious Mini Apps, and weaponized file handling.

**「Impact」** High-risk users—such as journalists, activists, or government personnel—gain a concrete, user-controlled hardening option that reduces attack surface by disabling high-risk features like Mini Apps and automatic media downloads, but at the cost of reduced convenience and some core functionality \(e.g., payments become inaccessible\). Developers integrating Telegram Mini Apps or payment flows must now account for their unavailability under this mode.

**Tags**: `#security`, `#macOS`, `#messaging-apps`, `#privacy`, `#zero-trust`

---

<a id="item-tech-news-15"></a>
### [Huawei Cloud launches openPangu-2.1-Pro for Agent development and ArkTS/Ascend-aware AI coding](https://mp.weixin.qq.com/s/8JfFmscBTDl_mPQMycD8Nw) ⭐️ 7.0/10

On November 15, 2026, Huawei Cloud launched openPangu-2.1-Pro, an updated open-source large language model on its MaaS \(Model-as-a-Service\) platform. The model is optimized for three specific capabilities: Agent development \(with improved Skills triggering and tool calling trained on over 100,000 domain-specific samples\), AI-assisted coding for ArkTS and Ascend operator generation, and cost-efficient inference with tiered pricing—¥0.80 per million input tokens, ¥3.20 per million output tokens, and ¥0.016 per million cached-input tokens. It is integrated with Huawei’s developer tools including AgentArts, CodeArts, and OfficeAce. The announcement does not specify whether model weights are publicly available, nor does it provide architectural details, benchmark results, or independent verification of performance claims.

telegram · zaihuapd · Nov 15, 16:03

**「Background」** The openPangu series is Huawei&\#x27;s open-source large language model initiative, first launched in 2023 with openPangu-1.0; subsequent versions such as openPangu-2.0 \(released in mid-2024\) introduced support for multimodal tasks and improved tool integration. This release builds on that lineage by focusing specifically on agent orchestration, ArkTS/Ascend-aware code generation, and inference cost reduction.

**「Impact」** Developers building Agents or ArkTS applications on Huawei’s ecosystem face a new, commercially priced inference option with claimed optimizations—but must verify whether openPangu-2.1-Pro’s weights are actually downloadable and usable offline, as the term &\#x27;open source&\#x27; is not substantiated in the source with license, repository, or weight availability details.

**Tags**: `#AI-models`, `#open-source`, `#developer-tools`, `#inference-optimization`, `#china-tech`

---

<a id="item-tech-news-16"></a>
### [Apple N50 smart glasses target 2027 release with iPhone-only Siri integration](https://www.bloomberg.com/news/newsletters/2026-11-15/apple-siri-ai-app-integrations-power-smart-glasses-iphone-duo-2-face-id-plan) ⭐️ 7.0/10

Apple is targeting a 2027 release for its first smart glasses, codenamed N50, with an expected announcement at WWDC in June and initial shipments by year-end. The device will rely entirely on pairing with a recent iPhone model—no Android support—and will not include AR display capabilities in its first version; instead, it emphasizes deep Siri and iPhone app integration, with third-party apps continuing to run on the paired iPhone. It features a three-pin magnetic charging system that allows charging while worn, and its form factor is reportedly slightly thinner than Meta’s second-generation Ray-Ban smart glasses. However, delays in software and AI development cast uncertainty on the 2027 timeline.

telegram · zaihuapd · Nov 16, 02:13

**「Background」** Apple has been developing smart glasses under the internal codename N50 since at least May 2025, when Bloomberg first reported plans for two models targeting an end-of-2026 launch; subsequent reporting in April 2026 confirmed Apple was testing four frame designs and characterizing the project as its most ambitious wearable initiative since the Apple Watch. The current report revises the timeline to a 2027 target, citing software and AI delays not present in earlier public accounts.

<details><summary>References</summary>
<ul>
<li><a href="https://tech-insider.org/apple-n50-smart-glasses-meta-ray-ban-2026/">Apple N50 Smart Glasses: 4 Designs vs Meta&#x27;s 7M Units</a></li>
<li><a href="https://www.firstpost.com/tech/apple-targets-2027-launch-for-smart-glasses-with-siri-and-iphone-apps-at-the-core-report-14060149.html">Apple targets 2027 launch for smart glasses, with ... - Firstpost</a></li>

</ul>
</details>

**Tags**: `#apple`, `#wearables`, `#ai-integration`, `#hardware-roadmap`

---

<a id="item-tech-news-17"></a>
### [Apple Launches Health AI Usage Study with 200,000 Participants](https://www.apple.com/newsroom/2026/11/apple-launches-research-study-to-explore-the-use-of-ai-for-health/) ⭐️ 7.0/10

Apple has launched the Apple Health AI Usage Study in the U.S., recruiting up to 200,000 adults aged 21 and older to investigate real-world interaction with and comprehension of conversational AI for health. Participation requires an iPhone 15 Pro or newer running iOS 26 or later with Apple Intelligence enabled; the study app is explicitly not intended for diagnosis or treatment. The study is conducted in collaboration with OpenEvidence, and all collected data is excluded from AI model training. It is currently open only to U.S. residents and does not represent a product release or feature update.

telegram · zaihuapd · Nov 16, 05:01

**「Background」** OpenEvidence is a clinical AI platform used by U.S. physicians to access evidence-based medical information, and according to its App Store listing, it is used by more physicians in the U.S. than all other AI platforms combined. The Apple Health AI Usage Study builds on prior industry efforts to assess real-world AI use in healthcare but differs by focusing specifically on conversational AI interaction, trust, and comprehension among general users—not clinicians—and explicitly excluding participant data from AI model training.

**「Impact」** Developers and AI practitioners building health-facing applications must account for growing regulatory and ethical expectations around transparency, user comprehension, and strict separation of research data from model training—standards now being operationalized by Apple at scale.

<details><summary>References</summary>
<ul>
<li><a href="https://apps.apple.com/us/app/openevidence/id6612007783">OpenEvidence App - App Store</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#healthcare AI`, `#human-computer interaction`, `#clinical research`, `#Apple`

---

<a id="item-tech-news-18"></a>
### [Tencent Executive Committee Calls for AI-Era Re-entrepreneurship and Fewer Management Roles](https://weibo.com/1642634100/RrCqPwhiS) ⭐️ 7.0/10

On November 16, 2026, Tencent&\#x27;s Executive Committee issued a call for &\#x27;re-entrepreneurship&\#x27; across core business teams to adapt to the AI era, mandating organizational flattening and operation via small, autonomous units. It stated that &\#x27;there is no need for so many management positions,&\#x27; explicitly targeting bureaucratic inertia, &\#x27;mountain-top-ism&\#x27; \(fiefdom mentality\), and territorial behavior among managers. The directive requires redesigning both management practices and workflows using AI, though no specific implementation timeline, structural metrics, or policy documentation was provided in the source material.

telegram · zaihuapd · Nov 16, 06:32

**「Organizational restructuring in response to AI adoption」** Large technology companies have increasingly restructured internal operations to accelerate AI integration, often emphasizing autonomy, speed, and reduced hierarchy—practices seen in earlier shifts like Spotify’s &\#x27;squad&\#x27; model or Microsoft’s post-2014 engineering reorganization. Tencent’s 2024–2025 internal initiatives—including the &\#x27;AI First&\#x27; strategy announced at its 2024 Tech Summit and subsequent pilot deployments of AI copilots across product teams—set the stage for this call to organizational &\#x27;re-entrepreneurship&\#x27;.

**「Impact」** Tencent&\#x27;s directive to eliminate redundant management layers and restructure all core teams around AI-native, autonomous small units requires existing middle managers—particularly those overseeing non-AI-aligned workflows—to either reskill for AI-integrated roles or face role elimination, as confirmed by the company&\#x27;s official culture account and corroborated by its July 2026 foundational-model team merger.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gate.com/news/detail/tencent-announces-all-core-teams-to-undertake-ai-focused-restructuring-25653702">Tencent Announces All Core Teams to Undertake AI-Focused ...</a></li>
<li><a href="https://china-gateway360.com/tencent-ai-restructuring-multimodal-china-2026/">Tencent Restructures AI Teams — 4 Signals for China’s ...</a></li>

</ul>
</details>

**Tags**: `#AI strategy`, `#organizational design`, `#software engineering culture`, `#enterprise AI adoption`

---

<a id="item-tech-news-19"></a>
### [Tencent Hunyuan Releases Hy4 Flash: 224B-Parameter Multimodal LLM with 1M Context and 1/13 Per-Task Cost of Hy4 Preview](https://mp.weixin.qq.com/s/5yBbf-ctYziM5r0i6Y17lA) ⭐️ 7.0/10

Tencent Hunyuan released Hy4 Flash, a 224-billion-parameter multimodal large language model with only 12 billion parameters activated per inference, supporting up to 1 million tokens of context. It is immediately available on Tencent Cloud’s TokenHub, WorkBuddy, and Yuanbao platforms, with WorkBuddy offering free access until November 30, 2026, and all API calls discounted by 50% until then. The model’s per-task cost—measured via Tencent’s internal WorkIndex metric—is claimed to be 1/13 that of Hy4 preview and 1/20 that of the full Hy4 model; Tencent states its overall effectiveness is slightly better than Hy4 preview. A plan to open-source Hy4 Flash is announced, but no release date or license is specified.

telegram · zaihuapd · Nov 16, 07:17

**「Background」** Hy4 Flash is a new variant of Tencent&\#x27;s Hy4 series of multimodal large language models; the original Hy4 preview was released earlier in 2026 and served as the baseline for cost and capability comparisons. Unlike the full Hy4 model, Hy4 Flash uses a mixture-of-experts \(MoE\) architecture with 224 billion total parameters but only 12 billion activated per token, enabling high throughput and lower inference costs while retaining 1M context length and multimodal support.

**「Impact」** Developers deploying daily AI workloads on Tencent Cloud can now reduce per-task inference costs by up to 92% compared to Hy4 preview while retaining multimodal input support and 1M-context capability—though actual performance and compatibility must be validated against specific task pipelines, as WorkIndex is an internal metric not independently benchmarked.

**Tags**: `#large-language-models`, `#ai-infrastructure`, `#cost-optimization`, `#multimodal-ai`, `#open-source`

---

## Financial News

<a id="item-finance-news-1"></a>
### [China&\#x27;s October 2026 Economic Data Misses Forecasts Amid Deepening Slowdown](https://www.cnbc.com/2026/11/16/china-retail-sales-october-industrial-output-investment.html) ⭐️ 8.0/10

China’s October 2026 retail sales rose 0.4% year-on-year—missing the 0.8% forecast and slowing from 1.1% in September—while industrial output grew 4.8%, below the 5.3% estimate and down from 5.5% in September; fixed-asset investment fell 8.1% year-to-date, worse than the expected 7% decline.

rss · CNBC Finance · Nov 16, 03:53

**「Background」** This follows a broader slowdown driven by a five-year property market downturn eroding household wealth and weakening domestic demand, alongside rising reliance on AI-related exports vulnerable to global tech restrictions.

**「Impact」** Households face stagnant consumption and elevated youth unemployment \(18% for ages 16–24 in September\), while exporters and AI equipment manufacturers face heightened risk from potential EU trade restrictions and U.S. chip controls.

**Tags**: `#China economy`, `#industrial output`, `#retail sales`, `#trade surplus`, `#AI exports`

---

<a id="item-finance-news-2"></a>
### [US Judge Rejects Motion to Dismiss DRAM Price-Fixing Lawsuit](https://www.tomshardware.com/tech-industry/big-tech/judge-denies-motion-to-dismiss-dram-price-fixing-lawsuit-against-micron-samsung-and-sk-hynix-says-chipmakers-acted-like-hawks-flying-in-formation-finds-evidence-of-dram-collusion-plausible-after-500-percent-price-surge) ⭐️ 7.0/10

A U.S. federal judge denied Micron, Samsung, and SK Hynix’s motion to dismiss a class-action antitrust lawsuit alleging coordinated DRAM supply restraint that led to price increases of up to 500% over one year; the ruling allows the case to proceed to the next stage.

telegram · zaihuapd · Nov 15, 16:39

**「Background」** DRAM is a type of memory chip used in computers and servers, and the three defendants collectively control over 90% of the global market, giving them substantial pricing influence.

**Tags**: `#antitrust`, `#semiconductors`, `#class-action`, `#DRAM`, `#competition-law`

---

<a id="item-finance-news-3"></a>
### [Q3 2024 Foreign Direct Investment in China Turns Net Negative](https://cn.nikkei.com/china/ceconomy/64726-2026-11-16-09-03-25.html) ⭐️ 7.0/10

China recorded a $900 million net outflow of foreign direct investment \(FDI\) in Q3 2024 — the first quarterly net outflow in four quarters — according to official data from China’s State Administration of Foreign Exchange.

telegram · zaihuapd · Nov 16, 05:29

**「Background」** FDI had been in net inflow for the previous three quarters, and the Q3 2024 reversal marks the first such shift since Q2 2024, driven by weakening growth expectations, soft domestic demand, and intensified price competition.

**「Impact」** The net outflow signals declining foreign investor confidence and may delay or reduce new manufacturing investments and job creation in export- and foreign-invested sectors.

**Tags**: `#foreign direct investment`, `#China economy`, `#international capital flows`, `#macroeconomic indicators`

---