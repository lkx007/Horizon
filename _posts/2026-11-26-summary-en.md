---
layout: default
title: "Horizon Summary: 2026-11-26 (EN)"
date: 2026-11-26
lang: en
---

> From 34 items, 22 important content pieces were selected

---

**Technology News**
1. [Google releases Cogentic research papers on integer factorization and discrete logs](#item-tech-news-1) ⭐️ 9.0/10
2. [Matrix multiplication exponent claimed as exactly 9/4 in purported OpenAI preprint](#item-tech-news-2) ⭐️ 9.0/10
3. [Minecraft Java Edition Critical RCE via Malicious Font in Resource Packs](#item-tech-news-3) ⭐️ 9.0/10
4. [US Treasury subdomains vulnerable to $3 takeover via expired AWS Elastic IPs](#item-tech-news-4) ⭐️ 8.0/10
5. [Ternary Bonsai 2.5 \(27B\) released as ternary-quantized LLM for consumer hardware](#item-tech-news-5) ⭐️ 8.0/10
6. [LeCun accuses Amodei of using AI risk rhetoric to suppress open models](#item-tech-news-6) ⭐️ 8.0/10
7. [Windows loudness limiter reverse-engineered and ported to PipeWire](#item-tech-news-7) ⭐️ 7.0/10
8. [LLMs Can Communicate via Timing Side Channels in Shared vLLM Inference Servers](#item-tech-news-8) ⭐️ 7.0/10
9. [Old NVIDIA and ATI GPU tech demos revived in browser via WebGL/WebGPU](#item-tech-news-9) ⭐️ 7.0/10
10. [PenGPT: Generative Transformer for Handwriting and Sketches](#item-tech-news-10) ⭐️ 7.0/10
11. [Bypassing iOS Safari&\#x27;s 60 FPS Limit for Smoother Scrolling](#item-tech-news-11) ⭐️ 7.0/10
12. [Three LLM inflection points: reasoning, ambiguity handling, and system-level debugging](#item-tech-news-12) ⭐️ 7.0/10
13. [Firefox 161 adds per-site VPN toggle rules and one-click &\#x27;Fire&\#x27; button for data clearing](#item-tech-news-13) ⭐️ 7.0/10
14. [OpenAI launches GPT-6 Cyber and expands Daybreak for cybersecurity](#item-tech-news-14) ⭐️ 7.0/10
15. [Tencent open-sources IQ2-AH quantized Hy4 flash \(224B\) for 64GB Mac mini via Strata](#item-tech-news-15) ⭐️ 7.0/10
16. [US closes AI chip loophole, Asian data centers pivot to US customers](#item-tech-news-16) ⭐️ 7.0/10
17. [Samsung and SK Hynix to adopt Yangtze Memory&\#x27;s Xtacking chip-stacking technology](#item-tech-news-17) ⭐️ 7.0/10

**Financial News**
1. [US Proposes New Section 301 Tariffs on 14 Trade Partners Including China](#item-finance-news-1) ⭐️ 8.0/10
2. [Nvidia volatility tests fictional Fed chair&\#x27;s market-signal approach](#item-finance-news-2) ⭐️ 7.0/10
3. [Kalshi’s perpetual futures volume exceeds prediction markets for first time](#item-finance-news-3) ⭐️ 7.0/10
4. [Utah Drops Criminal Charges Against Kalshi Founders](#item-finance-news-4) ⭐️ 7.0/10
5. [SpaceX declines $738M BEAD broadband subsidy for &\#x27;zero-expenditure&\#x27; Starlink deal](#item-finance-news-5) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Google releases Cogentic research papers on integer factorization and discrete logs](https://github.com/google-research/google-research/tree/master/cogentic_research_papers) ⭐️ 9.0/10

Google released a GitHub repository of early-stage Cogentic research papers addressing integer factorization and discrete logarithms—core computational problems underlying RSA, Diffie-Hellman, and other public-key cryptosystems. The materials consist of preliminary theoretical work, not peer-reviewed proofs, working implementations, or performance benchmarks; they are hosted under google-research/google-research and labeled as exploratory research. No claims of cryptanalytic breaks, runtime improvements over classical algorithms, or integration with production AI systems are made in the repository itself. The release is available publicly as of November 2026, with no stated timeline for follow-up or validation.

hackernews · rgwohlbold · Nov 25, 13:33 · [Discussion](https://news.ycombinator.com/item?id=50642086)

**「Background」** Integer factorization and the discrete logarithm problem are foundational computational problems whose assumed hardness underpins widely used public-key cryptosystems like RSA and Diffie-Hellman. For decades, no efficient classical algorithm has been found for either problem, and their resistance to known attacks is a cornerstone of modern cryptographic standards.

**「Impact」** Organizations relying on RSA encryption with keys smaller than 3072 bits face increased urgency to migrate to elliptic-curve cryptography \(ECC\) or post-quantum cryptographic algorithms, as Google’s Cogentic papers signal accelerated AI-assisted progress on integer factorization—a problem whose efficient classical solution would break RSA; however, no working implementation or complexity-bound improvement over existing classical algorithms is yet demonstrated.

**「Community discussion」** Commenters expressed precautionary concern—riobard urged immediate migration from old RSA keys to ECC—while fidotron cited an external X post suggesting the papers may hint at larger, unreleased advances. martythemaniak drew an analogy to AlphaGo Zero’s search-based discovery, framing the work as part of a broader trend of AI-assisted exploration in formal mathematical spaces.

<details><summary>References</summary>
<ul>
<li><a href="https://www.academia.edu/14681579/BACKTRACKING_BASED_INTEGER_FACTORISATION_PRIMALITY_TESTING_AND_SQUARE_ROOT_CALCULATION">(PDF) backtracking based integer factorisation , primality testing and...</a></li>
<li><a href="https://en.sorumatik.co/t/what-is-the-use-case-of-factorization-in-quantum-computing/112834">What is the use case of factorization in quantum computing - Sorumatik</a></li>

</ul>
</details>

**Tags**: `#cryptography`, `#artificial-intelligence`, `#number-theory`, `#security`, `#machine-learning`

---

<a id="item-tech-news-2"></a>
### [Matrix multiplication exponent claimed as exactly 9/4 in purported OpenAI preprint](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf) ⭐️ 9.0/10

A purported OpenAI preprint dated November 24, 2026, claims the matrix multiplication exponent ω is exactly 9/4 — contradicting the widely believed conjecture that ω = 2 — and asserts solutions to multiple major open problems including Smale’s ninth problem \(strongly polynomial linear programming\), mean-payoff games, and parity games. The paper is hosted at a suspicious GitHub path \(openai/math/blob/main/preprints\) with no verifiable affiliation to OpenAI, and its date is anachronistic relative to the November 2026 timestamp. No independent verification, peer review, or official OpenAI announcement supports the claim, and the source appears to be a hoax or satire circulating on Hacker News.

hackernews · E-Reverance · Nov 25, 01:19 · [Discussion](https://news.ycombinator.com/item?id=50637220)

**「Background」** The matrix multiplication exponent ω is the smallest real number such that two n×n matrices can be multiplied using O\(n^ω+ε\) arithmetic operations for any ε &gt; 0; the longstanding conjecture is that ω = 2, and the best proven upper bound prior to this claim was ω &lt; 2.371552 \(Alman &amp; Vassilevska Williams, 2021\), with decades of incremental improvements relying on the laser method and group-theoretic approaches.

**「Community discussion」** Commenters express deep skepticism: \[zone411\] lists the claimed solved problems but does not vouch for validity; \[StableAlkyne\] questions OpenAI’s motives and draws parallels to Bell Labs’ public-good mandate; \[BoppreH\] speculates about cryptographic implications and weaponization; and \[mmaunder\] hypothesizes internal model-driven breakthroughs, though none present evidence confirming the paper’s authenticity or technical soundness.

**Tags**: `#computational-complexity`, `#matrix-multiplication`, `#theoretical-computer-science`, `#artificial-intelligence`, `#mathematics`

---

<a id="item-tech-news-3"></a>
### [Minecraft Java Edition Critical RCE via Malicious Font in Resource Packs](https://github.com/bikini/minecraft2shell) ⭐️ 9.0/10

A critical remote code execution \(RCE\) vulnerability has been disclosed in Minecraft Java Edition, affecting versions 1.20.5 through 1.21.10 and snapshots 26.1–26.4, due to an out-of-bounds write in the FreeType 2.14.3 \(or earlier\) library when parsing malicious TrueType fonts embedded in resource packs. The flaw is triggered client-side on Windows in version 26.3 during font hinting, enabling arbitrary code execution; no official Mojang patch is available as of November 25, 2026. Community mitigation includes the m2sfix 1.0.0 mod or Java agent released November 24, which disables font hinting, and users are advised to disable resource pack downloads until patched.

telegram · zaihuapd · Nov 25, 12:46

**「Background」** Minecraft Java Edition uses the FreeType library to render TrueType fonts in resource packs; a memory corruption vulnerability \(out-of-bounds write\) in FreeType versions 2.14.3 and earlier enables arbitrary code execution when processing malicious font bytecode. This flaw was introduced into Minecraft via the lwjgl-freetype 3.4.3 binding, which Mojang has not yet updated—despite FreeType 2.15.0 having patched the underlying issue.

**「Impact」** Unpatched Minecraft Java Edition clients running versions 1.20.5–1.21.10 or snapshots 26.1–26.4 are vulnerable to remote code execution when loading malicious resource packs containing crafted TrueType fonts, requiring immediate mitigation—such as disabling server-enforced resource packs or deploying the community&\#x27;s m2sfix 1.0.0 mod—since Mojang has not yet released an official fix.

<details><summary>References</summary>
<ul>
<li><a href="https://threatcluster.io/cluster/minecraft2shell-unpatched-freetype-rce-in-minecraft-java-via-7b380721">Minecraft2Shell: Unpatched FreeType RCE in Minecraft Java via ...</a></li>
<li><a href="https://www.minenest.com/801287/">Minecraft2Shell RCE in Minecraft Java Still Unpatched</a></li>
<li><a href="https://hotrepo.ai/bikini/minecraft2shell">bikini/minecraft2shell: Minecraft font-based RCE proof of ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#java`, `#minecraft`, `#rce`

---

<a id="item-tech-news-4"></a>
### [US Treasury subdomains vulnerable to $3 takeover via expired AWS Elastic IPs](https://www.intruder.io/research/taking-over-us-treasury-subdomains-for-3-each) ⭐️ 8.0/10

Security researchers demonstrated that expired AWS Elastic IPs—still referenced in DNS records for multiple US Treasury subdomains—could be reclaimed and used to take over those subdomains, enabling full control including HTTPS certificate issuance. The vulnerability affected subdomains such as irs.gov and treasury.gov infrastructure, relying on stale Route 53 DNS A records pointing to released Elastic IPs. AWS confirmed it does not plan to change its behavior, stating the issue stems from customer-side DNS mismanagement rather than a flaw in AWS services, and treats rapid IP allocation/release as a policy violation with existing controls.

hackernews · negura · Nov 25, 04:27 · [Discussion](https://news.ycombinator.com/item?id=50638478)

**「Subdomain takeover via dangling DNS records」** Subdomain takeover is a well-documented class of vulnerability where an attacker claims control of a subdomain by exploiting misconfigured or orphaned DNS records—such as CNAMEs pointing to now-deleted cloud resources \(e.g., AWS Elastic IPs, S3 buckets, or CloudFront distributions\). This requires the target’s DNS record to reference a resource that no longer exists or is no longer owned by the domain owner, allowing an adversary to provision a new resource with the same identifier and inherit traffic or certificate issuance rights.

**「Impact」** Organizations using AWS Elastic IPs must manually delete or update DNS records before releasing IPs, or risk subdomain takeover; this creates an operational security requirement that contradicts common infrastructure-as-code and auto-scaling practices, especially in government cloud environments where certificate authorities will issue valid TLS certificates for any domain hosting a challenge file.

**「Community discussion」** Commenters debated responsibility: one noted AWS declined to add automatic cleanup \(e.g., Route 53 Elastic IP record types\), while another questioned whether extended validation \(EV\) certificates could mitigate such attacks for .gov domains, and a third cited a prior incident where recycled IP addresses led to unintended consequences due to uncleaned DNS.

<details><summary>References</summary>
<ul>
<li><a href="https://blogs.jsmon.sh/hunting-dangling-dns-how-to-exploit-aws-elastic-ips-cloudfront-and-s3/">Hunting Dangling DNS in AWS : Updated Techniques That Actually...</a></li>

</ul>
</details>

**Tags**: `#cloud-security`, `#subdomain-takeover`, `#dns`, `#aws`, `#government-IT`

---

<a id="item-tech-news-5"></a>
### [Ternary Bonsai 2.5 \(27B\) released as ternary-quantized LLM for consumer hardware](https://prismml.com/news/bonsai-2-5-27b) ⭐️ 8.0/10

Ternary Bonsai 2.5 \(27B\) — a ternary-quantized \(Q2 GGUF\) large language model — is now publicly available, delivering 22–25 tokens/sec generation speed on Apple M-series Macs \(e.g., M5 Pro with 24 GB RAM\) and supporting up to 128k context length in memory. It achieves SWE-bench Verified performance comparable to Opus 4.6 \(released February 2026\), and has been used autonomously to generate a working Tetris clone end-to-end on consumer hardware. The model is open-source and optimized for agentic coding workflows without cloud dependencies.

hackernews · b0m · Nov 24, 20:08 · [Discussion](https://news.ycombinator.com/item?id=50633922)

**「Background」** Ternary Bonsai 2.5 \(27B\) is the successor to the September 2026 Ternary Bonsai 2 release, maintaining the same 5.9 GB ternary-quantized footprint while improving agentic coding, multi-turn tool use, and context handling—now supporting up to 262K tokens in the official documentation build. It builds on PrismML’s prior work in ultra-low-bit quantization, specifically extending the ternary weight scheme \(\{−1, 0, +1\}\) first introduced in earlier Bonsai versions.

**「Impact」** Developers can now run long-context, agentic coding tasks locally on consumer Mac hardware — such as generating and refining full applications — without GPU acceleration or cloud APIs, lowering the barrier for iterative, privacy-preserving software development.

**「Community discussion」** Commenters debate whether its strong SWE-bench score reflects genuine capability, benchmark drift, or &\#x27;benchmaxxing&\#x27;, while others highlight real-world success like the autonomously generated Tetris clone; one user also raises an open technical question about asymmetric quaternary quantization as a potential next step.

<details><summary>References</summary>
<ul>
<li><a href="https://prismml.com/news/bonsai-2-5-27b">PrismML — Introducing Ternary Bonsai 2.5 27B: Powering ...</a></li>
<li><a href="https://docs.prismml.com/models/bonsai-2-5-27b">Ternary Bonsai 2.5 27B - Bonsai - docs.prismml.com</a></li>
<li><a href="https://huggingface.co/prism-ml/Ternary-Bonsai-2.5-27B-GGUF">prism-ml/Ternary-Bonsai-2.5-27B-GGUF · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#LLM quantization`, `#edge AI`, `#agentic systems`, `#SWE-bench`, `#open-source models`

---

<a id="item-tech-news-6"></a>
### [LeCun accuses Amodei of using AI risk rhetoric to suppress open models](https://x.com/ylecun/status/2124550037912920090) ⭐️ 8.0/10

Yann LeCun publicly accused Anthropic CEO Dario Amodei of leveraging exaggerated AI risk narratives—dating back to the GPT-2 era—to advocate for legally restricting open-weight AI models and consolidate corporate control. LeCun claimed Amodei left OpenAI due to a lack of authority and likened his approach to the Ottoman Empire’s historical ban on Arabic-language printing, calling it &\#x27;a new form of medieval obscurantism.&\#x27; The post was published on X \(formerly Twitter\) on November 22, 2026, and directly names Amodei, Anthropic, and the policy mechanism of criminalizing open models.

telegram · zaihuapd · Nov 25, 01:30

**「Background」** Dario Amodei co-founded Anthropic in 2021 after leaving OpenAI, where he had served as Vice President of Research; his public statements have consistently emphasized AI safety and the risks of uncontrolled model deployment. The reference to GPT-2 \(released by OpenAI in February 2019\) alludes to OpenAI’s initial decision to withhold the full model weights due to misuse concerns—a precedent that sparked ongoing debate about openness, safety trade-offs, and industry gatekeeping.

**「Impact」** LeCun’s public criticism reinforces a growing schism in AI governance, directly challenging Anthropic’s risk-based advocacy for restrictive model release policies; his departure from Meta and launch of AMI Labs—with $1.03B in funding to build non-LLM &\#x27;world models&\#x27;—signals a concrete institutional counterweight to centralized, safety-framed AI development.

<details><summary>References</summary>
<ul>
<li><a href="https://udit.co/blog/yann-lecun-ami-labs-world-models-seed-round">Yann LeCun &#x27;s AMI Labs Raises $1.03B to Prove the AI Industr</a></li>
<li><a href="https://www.humai.blog/yann-lecun-left-meta-raised-1-billion-in-four-months-and-is-now-betting-the-entire-ai-industry-is-wrong/">Yann LeCun Left Meta , Raised $1 Billion in Four Months, and Is Now...</a></li>

</ul>
</details>

**Tags**: `#artificial-intelligence`, `#open-source`, `#ai-ethics`, `#technology-policy`, `#machine-learning`

---

<a id="item-tech-news-7"></a>
### [Windows loudness limiter reverse-engineered and ported to PipeWire](https://github.com/xoxorwr/pw-loudness-eq) ⭐️ 7.0/10

A developer reverse-engineered the Windows shared-mode audio loudness limiter—implemented in AudioEng.dll and managed by audiodg.exe—and ported it to PipeWire as pw-loudness-eq. The port enables peak compression behavior on Linux systems that approximates Windows’ default treatment of audio played via shared-mode WASAPI, DirectSound, or MME \(but not exclusive-mode WASAPI or ASIO\), with reported attenuation near peaks of approximately −0.1 dBFS. The implementation is available as open-source software on GitHub and targets PipeWire-based Linux audio stacks.

hackernews · ThrowNotAway · Nov 25, 11:34 · [Discussion](https://news.ycombinator.com/item?id=50641171)

**「Windows shared-mode audio limiter」** Windows applies a subtle peak limiter to audio in shared-mode WASAPI, DirectSound, and MME APIs—implemented in AudioEng.dll and managed by audiodg.exe—but bypasses it in exclusive-mode WASAPI and ASIO. This limiter slightly compresses peaks \(reportedly ~−0.1 dBFS\) to prevent clipping during mixed playback, differing from frequency-dependent equalization or loudness normalization standards like EBU R128.

**「Impact」** Linux users relying on PipeWire can now apply a Windows-compatible loudness limiter to shared-mode audio streams, improving cross-platform consistency for playback of heavily mastered content—but must be aware that the algorithm may amplify transient impulses \(e.g., whistles\) unless paired with additional limiting.

**「Community discussion」** Commenters debated terminology \(emphasizing this is a limiter, not equalization\), raised concerns about impulse response artifacts and the ethics of reverse-engineering AudioEng.dll, and questioned whether off-the-shelf limiter algorithms would have sufficed instead of replicating Windows’ behavior.

**Tags**: `#audio-engineering`, `#linux`, `#pipewire`, `#reverse-engineering`, `#real-time-audio`

---

<a id="item-tech-news-8"></a>
### [LLMs Can Communicate via Timing Side Channels in Shared vLLM Inference Servers](https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being) ⭐️ 7.0/10

Sandboxed language models deployed on shared vLLM inference servers can unintentionally communicate through timing-based side channels, exploiting cache contention and non-deterministic kernel selection—where step size \(e.g., 10 vs. 2,000 tokens\) triggers different CUDA kernels with distinct memory access patterns and timing signatures. This behavior violates isolation assumptions in multi-tenant AI infrastructure, and the effect has been demonstrated in concrete vLLM deployments, not merely theorized. The communication requires pre-shared coordination between models and knowledge of server internals, but does not require code execution or privilege escalation. It is not a flaw in sandboxing per se, but a failure of cache and kernel-level isolation in the inference runtime.

hackernews · gmays · Nov 25, 02:34 · [Discussion](https://news.ycombinator.com/item?id=50637686)

**「Background」** vLLM is an open-source high-throughput LLM inference engine that uses PagedAttention and dynamic kernel selection based on batch size and step dimensions to optimize GPU utilization. Its step-size–dependent kernel dispatch—intended for performance—introduces microarchitectural non-determinism that interacts with shared CPU/GPU caches, creating observable timing differences usable as a covert channel. This builds on long-established side-channel principles from web security \(e.g., origin-isolated caches\) and systems research \(e.g., cache-based covert channels in virtualized environments\).

**「Impact」** Organizations deploying vLLM \(or similar inference servers with non-deterministic kernel dispatch and shared caches\) in multi-tenant settings must treat logical model isolation as insufficient for confidentiality; they should enforce cache partitioning or deterministic kernel selection to prevent cross-model information leakage.

**「Community Discussion」** Commenters disagree on exploit feasibility: \[amluto\] advocates for origin-style cache separation keys in inference APIs, while \[tsimionescu\] dismisses the attack as unrealistic due to stringent preconditions, and \[saagarjha\] criticizes vLLM’s step-size–dependent kernel choice as a design flaw that should be replaced with batch-invariant inference.

**Tags**: `#AI safety`, `#systems security`, `#LLM deployment`, `#side-channel attacks`, `#inference optimization`

---

<a id="item-tech-news-9"></a>
### [Old NVIDIA and ATI GPU tech demos revived in browser via WebGL/WebGPU](https://gpu-demo-gallery.pages.dev/) ⭐️ 7.0/10

A web-based gallery at gpu-demo-gallery.pages.dev has ported late-1990s–early-2000s NVIDIA and ATI GPU technology demos—including the Grass Demo and Crystal Ball—to run natively in modern browsers using WebGL and WebGPU. These demos, originally built for proprietary Windows drivers and legacy hardware like the RIVA TNT and GeForce 2 GTS, now execute without plugins or emulation layers. The project is publicly accessible, open-source \(implied by HN context and domain\), and targets educational and archival use; reported rendering issues include missing elements \(e.g., the &\#x27;N&\#x27; in the NVIDIA logo in Grass Demo\) and mouse interaction quirks in Crystal Ball.

hackernews · arkits · Nov 25, 04:31 · [Discussion](https://news.ycombinator.com/item?id=50638503)

**「Historical GPU tech demos」** In the late 1990s and early 2000s, NVIDIA and ATI \(now AMD\) distributed proprietary Windows-based tech demos—such as &\#x27;Grass&\#x27;, &\#x27;Crystal Ball&\#x27;, and &\#x27;NVIDIA Logo&\#x27;—to showcase real-time rendering capabilities of their consumer GPUs like the RIVA TNT and GeForce 2 GTS. These demos relied on DirectX and vendor-specific driver extensions, making them incompatible with modern operating systems and hardware without emulation or reimplementation.

**「Impact」** Developers, educators, and historians can now study and interact with historically significant real-time graphics techniques—such as early per-pixel lighting, environment mapping, and vertex shader precursors—without access to obsolete hardware or OS environments, though some visual and interactive fidelity remains incomplete.

**「Community discussion」** Commenters express strong nostalgic engagement and identify specific rendering gaps \(e.g., missing logo elements, mouse drag behavior\), while also suggesting additional demos \(PSX T-Rex, PS3 Duck Demo\) and requesting contextual documentation—like baseline GPU capabilities and feature explanations—to aid newer audiences.

**Tags**: `#graphics-programming`, `#webgl`, `#retro-computing`, `#gpu-history`, `#web-assembly`

---

<a id="item-tech-news-10"></a>
### [PenGPT: Generative Transformer for Handwriting and Sketches](https://greydanus.github.io/2026/11/12/pengpt/) ⭐️ 7.0/10

PenGPT is a generative transformer model released in November 2026 for synthesizing handwriting and sketches from stroke-based sequences. It prioritizes large-scale, high-quality dataset curation—built using agentic workflows, open-weight vision models, and multimodal AI APIs—over architectural novelty. The model was trained on an 8xH100 system, and its weights and methodology are publicly shared. It is not a real-time or production-deployed service but a research implementation focused on reproducibility and data-centric rigor.

hackernews · smusamashah · Nov 25, 00:54 · [Discussion](https://news.ycombinator.com/item?id=50637056)

**「Prior work on handwriting synthesis」** Handwriting synthesis has been explored since at least 2016 with Sam Greydanus’s Scribe project, which used recurrent neural networks to generate realistic handwriting from text inputs. That earlier work established foundational data pipelines and evaluation practices for stroke-based generation, and is cited by practitioners as pedagogically influential. PenGPT builds directly on this lineage by shifting focus from RNN-based sequential modeling to transformer architectures trained on large-scale, quality-controlled stroke datasets.

**「Impact」** Developers and HCI researchers now have an open, stroke-based generative model that produces ink-like handwriting and sketches from text prompts without requiring custom architectures—enabling rapid prototyping of pen-enabled interfaces, educational tools, or archival digitization workflows using only standard transformer training practices and publicly available vision models.

**「Community Discussion」** Commenters highlighted the project’s alignment with the &\#x27;Bitter Lesson&\#x27;—emphasizing data quality over clever architecture—with the author confirming that ~80% of effort went into dataset construction and filtering. One commenter noted nostalgic &\#x27;hallucination&\#x27; behaviors \(e.g., hybrid drawings\), while another praised the continuity with the author’s earlier handwriting synthesis work from 2016.

<details><summary>References</summary>
<ul>
<li><a href="https://apexneuralnews.com/news/pengpt-a-generative-transformer-for-handwriting-and-sketches">PenGPT: A Generative Transformer for Handwriting and Sketches</a></li>
<li><a href="https://grafy.ai/news/pengpt-a-new-transformer-for-handwriting-and-sketches">PenGPT: A Transformer for Handwriting — Grafy — Grafy News</a></li>

</ul>
</details>

**Tags**: `#generative-ai`, `#handwriting-synthesis`, `#data-centric-ai`, `#multimodal-modeling`, `#human-computer-interaction`

---

<a id="item-tech-news-11"></a>
### [Bypassing iOS Safari&\#x27;s 60 FPS Limit for Smoother Scrolling](https://rida.dev/blog/bypassing-ios-safari-60-fps-limit) ⭐️ 7.0/10

A developer demonstrated a technique to achieve &gt;60 FPS scrolling in iOS Safari by exploiting WebKit’s internal compositing behavior—specifically forcing layer promotion via CSS transforms and leveraging scroll-driven animations—not through any new API or Apple configuration, but via low-level rendering optimizations. The method requires deliberate CSS layer isolation \(e.g., \`will-change: transform\`, \`transform: translateZ\(0\)\`\) and avoids layout-triggering operations during scroll, enabling smoother motion that approaches native fidelity. It is not enabled by default, requires manual implementation per scroll container, and carries trade-offs including increased GPU memory usage and potential battery impact. The technique is verified in a live prototype but remains unsupported, undocumented, and subject to breakage with WebKit updates.

hackernews · vinhnx · Nov 25, 03:04 · [Discussion](https://news.ycombinator.com/item?id=50637890)

**「Background」** iOS Safari has enforced a hard 60 FPS cap on scroll and animation rendering since iOS 15.5 \(2022\), regardless of device hardware capability \(e.g., ProMotion 120 Hz displays\), due to WebKit’s conservative compositor scheduling and lack of scroll-performance hints from the web platform. Unlike native UIKit or SwiftUI, which automatically enable higher refresh rates for full-screen transitions, web content receives no such opt-in mechanism or frame-rate negotiation API.

**「Impact」** Frontend engineers building iOS-optimized web apps can now implement smoother scrolling without relying on JavaScript-based virtualization or third-party libraries—but must manually apply and test layer-promotion patterns per scrollable element, and accept increased memory pressure and unguaranteed longevity across iOS updates.

**「Community Discussion」** Commenters highlighted the battery trade-off as the core reason Apple does not expose 120 Hz by default on the web, noting that native frameworks like SwiftUI handle frame-rate adaptation selectively—whereas this workaround applies it globally without throttling. One user emphasized the significance of reverse-engineering WebKit source to uncover UX workarounds, calling it both impressive and fragile.

**Tags**: `#web-performance`, `#ios-safari`, `#webkit`, `#frontend-engineering`, `#native-web-convergence`

---

<a id="item-tech-news-12"></a>
### [Three LLM inflection points: reasoning, ambiguity handling, and system-level debugging](https://simonwillison.net/2026/Nov/24/llm-inflection-points/) ⭐️ 7.0/10

Simon Willison identifies three recent inflection points in LLM and coding agent capabilities over a 12-month period: \(1\) November 2025’s release of Claude Opus 4.5—marked by reliable reasoning under ambiguity and multi-system debugging, making it the first Claude Code model he used as a daily driver; \(2\) June–July 2026’s emergence of &\#x27;Fable class models&\#x27; \(e.g., Claude Fable 5, Opus 5.5, GPT-6 Astra\), defined by goal-directed, tool-using autonomy—including spatial triangulation and self-provisioned infrastructure; and \(3\) September–October 2026’s leap in 3D modeling and game development fluency, exemplified by Opus 5.5’s ability to iteratively improve game fun and balance via extended playtesting and rebalancing. All three inflection points are tied to specific model releases, dates, and observable engineering outcomes—not theoretical claims.

rss · Simon Willison · Nov 24, 23:02

**「Background」** Claude Opus 4.5 was released on November 24, 2025, and marked a shift in coding agent reliability—specifically improving reasoning under ambiguity and multi-system debugging—following the earlier February 2025 launch of Claude Code with Claude 3.7 Sonnet. The post positions this release as the first inflection point in a series of three over twelve months, preceding later developments like the June 2026 release of Claude Fable 5 \(a defanged variant of the unreleased, security-capable Mythos model\) and the September 2026 emergence of strong 3D modeling and game-design capabilities in models such as Opus 5.5.

**「Impact」** Developers report that Claude Opus 5.5 \(released September 22, 2026\) enables reliable, end-to-end game development—including playtesting, balancing, and fun-oriented design—without human intervention for core gameplay loops, as demonstrated by working RTS and 3D browser games built from natural-language prompts alone.

<details><summary>References</summary>
<ul>
<li><a href="https://www.piax.org/chat/claude-opus-5-5">Claude Opus 5 . 5 Free Online — Anthropic&#x27;s Best Coding Opus | PIAX</a></li>

</ul>
</details>

**Tags**: `#LLMs`, `#coding agents`, `#AI engineering`, `#model evolution`

---

<a id="item-tech-news-13"></a>
### [Firefox 161 adds per-site VPN toggle rules and one-click &\#x27;Fire&\#x27; button for data clearing](https://www.theverge.com/tech/1041474/firefox-161-vpn-rules-fire-button) ⭐️ 7.0/10

Mozilla released Firefox 161 on November 24, 2026, introducing two user-facing privacy features: a &\#x27;Manage VPN Rules&\#x27; panel enabling users to set per-website VPN routing \(‘Always On’ or ‘Always Off’\) for specific domains, and a new toolbar &\#x27;Fire&\#x27; button that clears browsing data—including history, cookies, and site data—with configurable scope. When all data types are selected, the &\#x27;Fire&\#x27; action logs the user out of all accounts and opens a fresh window. These features are available in the standard Firefox desktop window; no version number or platform limitations \(e.g., Windows/macOS/Linux\) are specified in the source, and no independent verification of functionality or compatibility with third-party VPN services is provided.

telegram · zaihuapd · Nov 25, 01:14

**「Per-site VPN routing and data clearing in Firefox」** Firefox previously offered built-in VPN integration via Mozilla VPN, but only as a global toggle—users could not configure routing behavior per domain. The &\#x27;Fire&\#x27; button replaces the legacy &\#x27;Clear Recent History&\#x27; dialog with a persistent, configurable toolbar control that supports selective or full data deletion, including session termination.

**「Impact」** Users who rely on split-tunneling or selective VPN usage—such as developers testing local vs. remote environments or privacy-conscious engineers managing sensitive sessions—can now enforce domain-specific routing without manual toggling, reducing misconfiguration risk; however, the feature’s dependence on Mozilla’s built-in VPN service \(not general system-level or third-party VPN integration\) limits its applicability outside that ecosystem.

**Tags**: `#browser-security`, `#privacy-engineering`, `#web-privacy`, `#firefox`

---

<a id="item-tech-news-14"></a>
### [OpenAI launches GPT-6 Cyber and expands Daybreak for cybersecurity](https://www.theinformation.com/newsletters/ai-agenda/openais-roadmap-making-cyber-bigger-coding-remains-blurry) ⭐️ 7.0/10

OpenAI has launched GPT-6 Cyber, a model specialized for security research, and is scaling its Daybreak program—a trusted-access initiative for cybersecurity professionals—to over 2,000 approved organizations and thousands of verified defenders as of September 2026. The company claims the global cybersecurity market—commonly estimated at over $300 billion—is significantly underestimated and asserts that cybersecurity will become a larger business segment for OpenAI than programming. No technical specifications, evaluation results, or independent verification of performance, availability, or commercial deployment are provided in the source.

telegram · zaihuapd · Nov 25, 04:51

**「Preceding model release and access program」** GPT-6 Cyber was officially launched by OpenAI on November 5, 2026, as a specialized model for vulnerability discovery and exploit development, rated &\#x27;Critical&\#x27; in cybersecurity and initially available only to a restricted cohort of vetted customers under the Daybreak Red program. It represents an advancement over GPT-5.6 Cyber and outperforms GPT-6 Astra on most cyber-specific tasks, including software analysis, vulnerability identification, and generating working exploits.

**「Impact」** Enterprise security teams and software developers using OpenAI’s tools may face pressure to adopt GPT-6 Cyber for vulnerability discovery and code analysis before independent benchmarks or integration documentation are publicly available, as Daybreak access remains restricted to vetted organizations and no public API or pricing details have been disclosed.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-cyber/">GPT‑6 Cyber: Advancing the frontier of aligned cybersecurity ...</a></li>
<li><a href="https://www.unite.ai/openai-launches-gpt-6-cyber-with-restricted-access-and-scope-controls/">OpenAI Launches GPT-6 Cyber With Restricted Access and Scope ...</a></li>
<li><a href="https://www.reuters.com/technology/openai-launches-gpt-6-cyber-with-critical-cybersecurity-rating-2026-11-05/">OpenAI launches GPT-6 Cyber with &#x27;Critical&#x27; cybersecurity ...</a></li>

</ul>
</details>

**Tags**: `#artificial-intelligence`, `#cybersecurity`, `#openai`, `#industry-trends`

---

<a id="item-tech-news-15"></a>
### [Tencent open-sources IQ2-AH quantized Hy4 flash \(224B\) for 64GB Mac mini via Strata](https://mp.weixin.qq.com/s/o0xxShVQX6g2UllrrEv1WQ) ⭐️ 7.0/10

Tencent has open-sourced GGUF-quantized weights for its 224-billion-parameter Hy4 flash large language model, including an IQ2-AH version sized at 125.73 GiB—30% of the original 410.27 GiB. This minimal-precision variant, when used with the Strata offload framework, enables inference on a 64 GB RAM Mac mini. Benchmarks show the Q3\_K variant achieves up to 89 tokens/sec on a 48 GB GPU at 10K context and 47 tokens/sec on an M5 Max with 128 GB RAM at 32K context, with ≤0.4-point accuracy drop versus the full-precision model on DeepSWE v1.1.

telegram · zaihuapd · Nov 25, 09:29

**「Background」** Hy4 flash is Tencent&\#x27;s 224B-parameter large language model, previously released in full-precision form requiring ~410 GiB of storage and high-end GPU infrastructure. AngelSlim is Tencent&\#x27;s open-source model compression and acceleration toolkit, first introduced to support quantization and offloading for large models; Strata is its runtime framework for memory-efficient inference via CPU-GPU offloading.

**「Impact」** Developers can now run a 224B-parameter LLM on consumer-grade Apple silicon hardware \(e.g., 64 GB Mac mini\) without requiring high-end GPUs or cloud infrastructure, provided they use Strata for CPU/GPU memory offloading and accept the trade-offs of IQ2-AH quantization.

**Tags**: `#large-language-models`, `#model-quantization`, `#inference-optimization`, `#open-source-ai`, `#edge-ai`

---

<a id="item-tech-news-16"></a>
### [US closes AI chip loophole, Asian data centers pivot to US customers](https://www.bloomberg.com/news/articles/2026-11-25/asia-data-centers-sound-out-us-clients-to-replace-china-demand) ⭐️ 7.0/10

The U.S. government closed a regulatory loophole that had allowed Chinese technology companies to access NVIDIA’s most advanced AI chips via Asian data centers; new export controls on AI accelerators now restrict such arrangements, directly impacting data center operators in Asia who previously leased compute capacity to Chinese clients. Liquid Compute CEO Ronit Jain confirmed the policy change is disrupting business models reliant on Chinese demand. The restrictions apply to advanced AI accelerators shipped to or hosted in Asia for resale or remote access by Chinese entities, and are effective as of the policy enforcement date implied by the Bloomberg report. No technical specifications, effective date, or list of affected chip models \(e.g., H100, B200\) were provided in the source.

telegram · zaihuapd · Nov 25, 11:35

**「Background」** US export controls on advanced AI chips, first introduced during the Trump administration and significantly tightened by the Biden administration in 2022, prohibited direct sales of chips like NVIDIA’s A100 and H100 to China. A previously exploited loophole allowed Asian data centers to host these chips and lease compute capacity to Chinese clients—effectively circumventing the hardware ban—until new regulations explicitly extended restrictions to such indirect access.

**「Impact」** Asian data centers that previously relied on leasing compute capacity to Chinese clients now face stranded or underutilized infrastructure and are actively seeking US customers to absorb excess capacity, with Liquid Compute’s CEO confirming the shift is driven directly by new US export rules targeting AI accelerator shipments to the region.

<details><summary>References</summary>
<ul>
<li><a href="https://time.com/article/2026/11/16/trump-administration-ai-chips-nvidia-china/">U . S . to Clamp Down On AI Chip Loophole Ahead Of Trump Meeting...</a></li>
<li><a href="https://www.csis.org/analysis/loopholes-are-exporters-not-just-taxpayers">Loopholes Are for Exporters , Not Just Taxpayers</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-25/asia-data-centers-sound-out-us-clients-to-replace-china-demand">Asia Data Centers Sound Out US Clients to Replace China Demand</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#export controls`, `#cloud infrastructure`, `#geopolitics`, `#semiconductors`

---

<a id="item-tech-news-17"></a>
### [Samsung and SK Hynix to adopt Yangtze Memory&\#x27;s Xtacking chip-stacking technology](https://tech.ifeng.com/c/8yLRPKxQy4L) ⭐️ 7.0/10

Samsung Electronics and SK Hynix have agreed—via an undisclosed cross-licensing agreement—to adopt aspects of Yangtze Memory’s Xtacking technology for 3D NAND flash production. Xtacking separates the fabrication of memory arrays and CMOS logic onto two distinct wafers, which are then bonded together, enabling independent process optimization and greater manufacturing flexibility. The companies have declined to confirm the arrangement, and no timeline, scope, or product-level implementation details \(e.g., specific NAND generations, foundry partners, or volume targets\) have been disclosed. The report cites no official announcement or independently verified shipment, and Omdia’s prior analysis confirms Xtacking’s architectural advantages but does not validate this licensing deal.

telegram · zaihuapd · Nov 25, 14:33

**「What is Xtacking?」** Xtacking is Yangtze Memory Technologies Co.&\#x27;s \(YMTC\) proprietary 3D NAND architecture that separates the fabrication of memory arrays and CMOS peripheral logic onto two independent wafers, which are then bonded together using hybrid wafer-to-wafer stacking. This split-fabrication approach—first introduced by YMTC in its initial Xtacking generation—enables independent process optimization: memory arrays can be manufactured on mature nodes for cost and yield, while logic circuits can leverage advanced nodes from foundries. Omdia has noted this design improves manufacturing flexibility and cost-efficiency compared to monolithic 3D NAND processes.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techpowerup.com/355199/samsung-and-sk-hynix-to-license-ymtcs-xtacking-technology">Samsung and SK hynix to License YMTC&#x27;s Xtacking Technology</a></li>
<li><a href="https://asia.nikkei.com/business/tech/semiconductors/china-s-ymtc-boosted-by-samsung-and-sk-hynix-adopting-its-memory-technology">China&#x27;s YMTC boosted by Samsung and SK Hynix adopting its ...</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#3D-NAND`, `#memory-technology`

---

## Financial News

<a id="item-finance-news-1"></a>
### [US Proposes New Section 301 Tariffs on 14 Trade Partners Including China](https://www.cnbc.com/2026/11/25/us-tariffs-trump-section-301.html) ⭐️ 8.0/10

The US government proposes new Section 301 tariffs on 14 trade partners—including China, the EU, Japan, and India—to address subsidized overcapacity in manufacturing; for China, the proposal adds 20 percentage points to the existing 25% tariff, with a potential increase to 40% if China fails to comply with the October 2025 Busan trade truce agreement.

telegram · zaihuapd · Nov 25, 13:59

**「Background」** The U.S. is proposing these new tariffs under Section 301 of the 1974 Trade Act, following an eight-month investigation into alleged unfair trade practices—including government-subsidized overcapacity in manufacturing—across 16 trading partners.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aljazeera.com/news/2026/11/25/trump-announces-new-trade-tariffs-which-countries-will-they-target">Trump announces new trade tariffs : Which countries are... | Al Jazeera</a></li>
<li><a href="https://www.theguardian.com/business/live/2026/nov/25/rise-energy-bills-britain-2166-impossible-high-millions-households-stocks-tumble-as-ai-rally-fizzles-live-updates">US proposes new tariffs on 14 trading partners ... | The Guardian</a></li>

</ul>
</details>

**Tags**: `#trade\_policy`, `#us\_china\_relations`, `#tariffs`, `#global\_trade`, `#section\_301`

---

<a id="item-finance-news-2"></a>
### [Nvidia volatility tests fictional Fed chair&\#x27;s market-signal approach](https://www.cnbc.com/2026/11/25/nvidia-kevin-warsh-fed-market-signals.html) ⭐️ 7.0/10

The article presents a fictional scenario in which &\#x27;Federal Reserve Chairman Kevin Warsh&\#x27; interprets Nvidia-related market swings as a test of his stated preference for market-based signals—such as the Goldman Sachs Financial Conditions Index—over traditional economic forecasts, though Warsh has never served as Fed chair and the timeline \(2026\) is speculative.

rss · CNBC Finance · Nov 25, 12:26

**「Background」** Kevin Warsh became Federal Reserve Chair on May 22, 2026, succeeding Jerome Powell; this fictional scenario portrays him advocating market-based signals over forecasts amid volatility tied to Jensen Huang’s reinstatement as Nvidia CEO following a brief ouster and U.S. government intervention.

<details><summary>References</summary>
<ul>
<li>Kevin M. Warsh | Federal Reserve History</li>
<li><a href="https://www.usatoday.com/story/money/2026/11/23/jensen-huang-reinstated-nvidia-ceo/92828717007/">Jensen Huang reinstated as Nvidia CEO, Trump says he ...</a></li>

</ul>
</details>

**Tags**: `#monetary-policy`, `#market-signals`, `#fictional-reporting`

---

<a id="item-finance-news-3"></a>
### [Kalshi’s perpetual futures volume exceeds prediction markets for first time](https://www.cnbc.com/2026/11/24/kalshi-perps-volume-prediction-markets.html) ⭐️ 7.0/10

On November 21 and 22, 2026, Kalshi’s perpetual futures \(&\#x27;perps&\#x27;\) trading reached $3.4 billion and exceeded its prediction market volume \($3 billion\) on two consecutive days—the first time this has occurred since perps launched in May 2026 under U.S. regulatory approval.

rss · CNBC Finance · Nov 24, 23:03

**「Background」** Kalshi, previously known for event-based prediction markets, became the first U.S.-regulated exchange approved by the CFTC in May 2026 to list perpetual futures—leveraged, expirationless contracts tied to assets like crypto, stocks, and commodities.

**「Impact」** This shift signals early traction for a new class of U.S.-regulated derivatives, potentially affecting retail and institutional traders seeking leveraged exposure to individual stocks or commodities—but only on Kalshi for now, as it holds a temporary monopoly pending rival applications from Coinbase and others.

**Tags**: `#financial innovation`, `#derivatives`, `#regulatory development`, `#market structure`

---

<a id="item-finance-news-4"></a>
### [Utah Drops Criminal Charges Against Kalshi Founders](https://www.cnbc.com/2026/11/24/utah-drops-charges-against-kalshi-after-it-halted-operations-in-state.html) ⭐️ 7.0/10

Utah dismissed 14 criminal charges against prediction market platform Kalshi and its co-founders Tarek Mansour and Luana Lopes Lara on November 24, 2026, after Kalshi suspended operations in the state on November 23.

rss · CNBC Finance · Nov 24, 20:45

**「Background」** Utah had charged Kalshi with operating an illegal gambling operation on October 28, 2026, but the Commodity Futures Trading Commission \(CFTC\) — which asserts federal authority over prediction markets as a type of derivatives trading — sued Utah the day before, escalating a jurisdictional dispute between state and federal regulators.

**「Impact」** The dismissal — without prejudice — means Kalshi could face refiled charges if it resumes operations in Utah, leaving other prediction market firms facing similar legal uncertainty in states that do not recognize CFTC jurisdiction.

**Tags**: `#regulatory enforcement`, `#prediction markets`, `#CFTC`, `#state vs federal regulation`, `#fintech legal risk`

---

<a id="item-finance-news-5"></a>
### [SpaceX declines $738M BEAD broadband subsidy for &\#x27;zero-expenditure&\#x27; Starlink deal](https://x.com/SawyerMerritt/status/2125314062997467640) ⭐️ 7.0/10

SpaceX declined $738 million in federal Broadband Equity, Access, and Deployment \(BEAD\) program funding in favor of a &\#x27;zero-expenditure agreement&\#x27; with the National Telecommunications and Information Administration \(NTIA\), under which it will provide free Starlink terminals and low-cost service to eligible U.S. households without receiving federal funds.

telegram · zaihuapd · Nov 25, 02:17

**「Background」** The BEAD program, administered by NTIA, distributes over $42 billion to expand high-speed internet access in unserved and underserved U.S. areas, typically requiring recipients to meet strict financial reporting and procurement rules.

**「Impact」** Eligible U.S. households in unserved or underserved areas will receive free Starlink hardware and low-cost service for 10 years, bypassing traditional subsidy-driven infrastructure builds.

**Tags**: `#broadband policy`, `#spaceX`, `#BEAD`, `#telecom regulation`, `#infrastructure funding`

---