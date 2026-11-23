---
layout: default
title: "Horizon Summary: 2026-11-24 (EN)"
date: 2026-11-24
lang: en
---

> From 33 items, 18 important content pieces were selected

---

**Technology News**
1. [Codex2api遭供应链投毒：v3.1.11移除鉴权并窃取16个GitHub Actions secrets](#item-tech-news-1) ⭐️ 9.0/10
2. [GLM-5.4 introduces loop transformer for memory-bandwidth-efficient LLM inference](#item-tech-news-2) ⭐️ 8.0/10
3. [Meta AI Chief Warns Superintelligence Is Imminent Amid Unreadable Riemann Proof](#item-tech-news-3) ⭐️ 8.0/10
4. [Ladybird browser enters alpha with high Web Platform Test scores](#item-tech-news-4) ⭐️ 7.0/10
5. [Free alternative TV network built from the Internet Archive&\#x27;s forgotten videos](#item-tech-news-5) ⭐️ 7.0/10
6. [Nospeaker repurposes MacBook trackpad haptic motor as audio transducer](#item-tech-news-6) ⭐️ 7.0/10
7. [XNU Linux: Run macOS GUI apps on Linux via userspace compatibility layer](#item-tech-news-7) ⭐️ 7.0/10
8. [The Next Circle of Security Hell: Open Source Maintainer Burden and Security Trade-offs](#item-tech-news-8) ⭐️ 7.0/10
9. [17M Lines of Lean Formalization of GRH Highlights Formal Verification vs. Readability](#item-tech-news-9) ⭐️ 7.0/10
10. [Beginner&\#x27;s Guide to Local AI with Inkling, Qwen, and Unsloth](#item-tech-news-10) ⭐️ 7.0/10
11. [Google builds Mirror Dimension simulation to test Chrome AI agent](#item-tech-news-11) ⭐️ 7.0/10
12. [Windows Server 2028 ships without WoW64 by default, blocking 32-bit apps out of the box](#item-tech-news-12) ⭐️ 7.0/10

**Technology Blog**
1. [Skip the DRAM Tier: MoRI UMBP Runs Agentic KV Cache on NVMe](#item-tech-blog-1) ⭐️ 9.0/10
2. [Flailing Well: A Feedback-Driven Approach to Ambiguity](#item-tech-blog-2) ⭐️ 8.0/10
3. [OpenAI’s Perplexity Graph: Transparency, Limits, and Pretraining Revival](#item-tech-blog-3) ⭐️ 7.0/10

**Financial News**
1. [JPMorgan and Hyundai Card test AI agents for autonomous FX transactions](#item-finance-news-1) ⭐️ 7.0/10
2. [Ant Group Leads $100M Funding for Simplexity Robotics](#item-finance-news-2) ⭐️ 7.0/10
3. [Shanghai Metro Fares Rise After 21 Years](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Codex2api遭供应链投毒：v3.1.11移除鉴权并窃取16个GitHub Actions secrets](https://github.com/WormW/codex2api-incident-2026-11) ⭐️ 9.0/10

The codex2api project suffered a confirmed supply chain compromise when attackers hijacked the author&\#x27;s GitHub account and pushed malicious release tags—including v3.1.11—bypassing the main branch. This version disables authentication, enabling unauthenticated remote command execution, and includes a compromised GitHub Actions workflow that exfiltrates 16 GitHub Actions secrets. The attack affects at least 21 repositories under the same GitHub account, and users who installed or updated to versions 3.1.10–3.1.12 are instructed to immediately downgrade to v3.1.9 and rotate all related credentials, including GitHub tokens, SSH keys, database passwords, and DeepSeek API keys.

telegram · zaihuapd · Nov 23, 11:21

**「Background」** Codex2api is an open-source tool that abstracts and routes API calls to multiple LLM providers \(e.g., DeepSeek, OpenAI\), commonly used in AI development workflows for protocol translation and provider-agnostic client integration. It relies on GitHub Actions for CI/CD and stores sensitive credentials—such as GitHub tokens, SSH keys, and API keys—as repository secrets.

**「Immediate credential compromise risk for developers using codex2api v3.1.10–v3.1.12」** Developers who installed or updated to codex2api versions 3.1.10 through 3.1.12 are at immediate risk of having their GitHub tokens, SSH keys, database credentials, and DeepSeek API keys exfiltrated—via malicious GitHub Actions workflows that harvest and HTTP POST 16 exposed secrets to an attacker-controlled server on port 8080.

<details><summary>References</summary>
<ul>
<li><a href="https://www.endorlabs.com/learn/github-actions-supply-chain-attack-targeting-ci-secrets-at-scale">Hijacked GitHub Accounts Push “wfx” CI Secret Stealer... | Endor Labs</a></li>

</ul>
</details>

**Tags**: `#supply-chain-security`, `#ai-devtools`, `#github-compromise`, `#zero-trust`, `#incident-response`

---

<a id="item-tech-news-2"></a>
### [GLM-5.4 introduces loop transformer for memory-bandwidth-efficient LLM inference](https://z.ai/blog/glm-5.4) ⭐️ 8.0/10

Zhipu AI released GLM-5.4, its first &\#x27;loop transformer&\#x27; model, which iteratively reuses transformer layers during inference instead of computing each layer once. This architecture targets memory bandwidth bottlenecks—specifically the repeated movement of layer weights between high-bandwidth memory \(HBM\) and compute units—by reducing the number of distinct weight transfers per token. The model is available exclusively via Zhipu’s new Coding Plan API tier, not the standard Z.ai API plan or OpenRouter. No benchmark numbers, latency measurements, or open weights are provided in the announcement.

hackernews · foohis · Nov 23, 10:06 · [Discussion](https://news.ycombinator.com/item?id=50609685)

**「Loop transformer architecture」** The loop transformer is an architectural variant where a subset of transformer layers is reused iteratively—executing the same layer multiple times with updated hidden states—rather than applying each layer once in a fixed-depth stack. This design aims to reduce memory bandwidth pressure during inference by limiting the number of distinct weight matrices that must be fetched from high-bandwidth memory \(HBM\), addressing a well-documented bottleneck in large language model deployment.

**「Impact」** Developers requiring GLM-5.4 must subscribe to Zhipu’s paid Coding Plan to access the model via API, as it is unavailable through the standard API tier or third-party aggregators like OpenRouter.

**「Community discussion」** Commenters highlight the novelty of iterative layer reuse as a response to memory bandwidth constraints, with one explaining that conventional transformers move each layer’s weights into the chip once per token, whereas loop transformers aim to amortize that cost. Another user notes frustration with GLM models’ high latency \(&\#x27;marathon thinking&\#x27;\) in practice despite competitive benchmark scores.

<details><summary>References</summary>
<ul>
<li><a href="https://z.ai/blog/glm-5.4">GLM-5.4: Toward Generalized Coding with Our First Loop ...</a></li>
<li><a href="https://www.kucoin.com/news/flash/zhipu-launches-glm-5-4-for-all-glm-coding-plan-users-with-loop-transformer-architecture">Zhipu Launches GLM-5.4 for All GLM Coding Plan Users with ...</a></li>
<li><a href="https://mlq.ai/news/zai-launches-glm-54-a-750-billion-parameter-model-built-on-a-looped-transformer/">Z.ai launches GLM-5.4, a 750 billion-parameter model built on ...</a></li>

</ul>
</details>

**Tags**: `#LLMs`, `#inference optimization`, `#transformer architecture`

---

<a id="item-tech-news-3"></a>
### [Meta AI Chief Warns Superintelligence Is Imminent Amid Unreadable Riemann Proof](https://thenextweb.com/news/metas-ai-chief-says-superintelligence-is-arriving-and-control-is-at-risk) ⭐️ 8.0/10

Meta&\#x27;s Chief AI Officer and head of its Superintelligence Lab, Alexandr Wang, stated that superintelligence is no longer a distant prospect but an imminent reality. He cited the machine-verified proof of the Riemann hypothesis—completed by mathematician Levent Alpöge using Anthropic&\#x27;s Claude and validated by the Lean theorem prover and Mathlib community—as evidence that AI has surpassed top human mathematicians in formal verification, though the proof remains unreadable by humans. Wang emphasized that the remaining gaps between AI and elite humans are limited to domain-specific knowledge, engineering integration, and experimental capability—not reasoning or verification—and warned that systems capable of recursive self-improvement or 1000× greater intelligence pose acute control and alignment risks.

telegram · zaihuapd · Nov 23, 12:49

**「Riemann hypothesis proof formalized with Claude and machine-verified」** The Riemann hypothesis is a century-old unsolved problem in mathematics concerning the distribution of prime numbers; its proof would be a landmark achievement. In late 2024, mathematician Levent Alpöge used Anthropic’s Claude to assist in formalizing a proof, which was later machine-verified using the Lean theorem prover and the Mathlib library—a rigorous, community-vetted process that confirms logical correctness without requiring human-readable exposition. As of November 2026, no human-readable version of the proof exists, making it a concrete example of AI-assisted reasoning that exceeds current human verification capacity.

**「Impact」** Researchers and developers working on AI safety, formal verification, and alignment must now treat unreadable yet machine-validated proofs as concrete evidence of capability divergence, prompting urgent reassessment of current evaluation frameworks and containment assumptions for advanced AI systems.

<details><summary>References</summary>
<ul>
<li><a href="https://thenextweb.com/news/metas-ai-chief-says-superintelligence-is-arriving-and-control-is-at-risk">Meta AI chief Alexandr Wang: superintelligence is arriving</a></li>
<li><a href="https://explainx.ai/blog/alexandr-wang-superintelligence-arriving-riemann-hypothesis-essay-november-2026">Wang: Superintelligence Arriving After Riemann (2026 ...</a></li>
<li><a href="https://mlq.ai/news/metas-alexandr-wang-says-the-riemann-proof-shows-ai-will-surpass-humans-in-every-field-including-ai-research/">Meta&#x27;s Alexandr Wang says the Riemann proof shows AI will ...</a></li>

</ul>
</details>

**Tags**: `#artificial-intelligence`, `#ai-safety`, `#mathematical-reasoning`, `#superintelligence`, `#model-alignment`

---

<a id="item-tech-news-4"></a>
### [Ladybird browser enters alpha with high Web Platform Test scores](https://ladybird.org/posts/alpha/) ⭐️ 7.0/10

Ladybird, a from-scratch web browser, has entered alpha release as of November 23, 2026. It achieves high rendering fidelity across complex sites including YouTube and Google Maps, and passed Safari Technology Preview on the Web Platform Tests \(WPT\) suite on October 26, 2026, reaching 2,184,722 passing subtests. The project pragmatically adopted mature libraries like Skia for graphics and SQLite for storage, replacing earlier self-developed components. It remains pre-beta, with known limitations including jerky scrolling and explicit security caveats for alpha-stage use.

hackernews · janvdberg · Nov 23, 16:13 · [Discussion](https://news.ycombinator.com/item?id=50614249)

**「Background」** Ladybird is a new web browser engine built from scratch and developed by a non-profit organization; it was previously in pre-alpha with no public availability and had restricted external contributions since June 2026, when the project halted public pull requests to prioritize security and code quality ahead of its alpha release.

**「Impact」** Users should avoid using Ladybird for authenticated sessions, payments, or sensitive data entry due to its alpha status and documented security caveats; developers may adopt it for compatibility testing or systems programming exploration, but not production workloads.

**「Community discussion」** Commenters widely praise Ladybird’s functional correctness—reporting near-perfect rendering on major sites—but note minor performance issues like jerky scrolling; one user explicitly asks about safe usage boundaries, reflecting community awareness of the alpha risk.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ladybird_%28web_browser%29">Ladybird (web browser) - Wikipedia</a></li>
<li><a href="https://ladybird.org/">Ladybird</a></li>
<li><a href="https://piunikaweb.com/2026/11/24/ladybird-browser-is-now-officially-available-in-alpha-for-macos-and-linux/">Ladybird Browser is now officially available in alpha for ...</a></li>

</ul>
</details>

**Tags**: `#web browsers`, `#open source`, `#systems programming`, `#privacy`

---

<a id="item-tech-news-5"></a>
### [Free alternative TV network built from the Internet Archive&\#x27;s forgotten videos](https://spelunkr.tv/) ⭐️ 7.0/10

Spelunkr.tv is a free, open-source streaming platform that curates and schedules forgotten videos from the Internet Archive into thematic TV-like channels, restoring synchronous, contextual viewing experiences.

hackernews · SockThief · Nov 23, 01:13 · [Discussion](https://news.ycombinator.com/item?id=50606192)

**Tags**: `#media-technology`, `#internet-archive`, `#open-web`, `#user-experience`, `#retro-computing`

---

<a id="item-tech-news-6"></a>
### [Nospeaker repurposes MacBook trackpad haptic motor as audio transducer](https://github.com/os6/nospeaker) ⭐️ 7.0/10

Nospeaker is an open-source macOS tool that drives the Force Touch trackpad’s haptic motor with audio waveforms to produce audible sound, achieving a usable frequency range of 100 Hz to 4 kHz—with peak clarity near 1 kHz. It converts text to speech using macOS’s built-in voice synthesis, samples formants \(two per 10 ms frame\), and replays them with dynamic pitch and loudness; output sounds robotic and is limited to text-to-speech only—not music or video playback. The tool bypasses Apple’s public haptic APIs and instead uses the private MultitouchSupport framework, and has been confirmed to work only on M5 Max–equipped MacBook Pro models with Force Touch trackpads.

hackernews · yakkomajuri · Nov 23, 11:31 · [Discussion](https://news.ycombinator.com/item?id=50610318)

**「Haptic motors as audio transducers」** Haptic feedback motors—originally designed for tactile cues, not sound—have been repurposed as crude audio transducers in prior hardware-hacking projects, such as generating tones from floppy drive stepper motors \(e.g., Commodore 1541\) and synthesizing music via iPhone vibration actuators. Nospeaker builds on this lineage by targeting the MacBook’s Force Touch trackpad haptic motor, which uses a linear resonant actuator \(LRA\) capable of higher-frequency vibration than typical eccentric rotating mass \(ERM\) motors.

**「Impact」** Developers and accessibility researchers can now experiment with low-bandwidth, hardware-constrained audio output on supported MacBooks—but must accept reliance on undocumented APIs, lack of official support, and incompatibility with non-Force Touch or non-M5 Max systems.

**「Community discussion」** Commenters draw parallels to historical hardware-hacking audio projects—such as Commodore 1541 floppy drive music—and express enthusiasm for haptics as an underused sensory channel, with one contributor sharing a haptic-synced iPhone music player prototype.

**Tags**: `#haptics`, `#hardware-hacking`, `#macos`, `#audio`, `#open-source`

---

<a id="item-tech-news-7"></a>
### [XNU Linux: Run macOS GUI apps on Linux via userspace compatibility layer](https://github.com/AFK-surf/xnulinux) ⭐️ 7.0/10

XNU Linux is an experimental open-source project that enables macOS userspace applications—including GUI components built with Cocoa and other Apple frameworks—to run on Linux by intercepting dynamic library calls and providing XNU-compatible abstractions. It does not emulate the XNU kernel or require Apple hardware, instead relying on shared library interposition and reverse-engineered API compatibility. The project is hosted on GitHub \(AFK-surf/xnulinux\) and remains in early, proof-of-concept stage with no official Apple toolchain integration or syscall-level kernel emulation.

hackernews · mmastrac · Nov 23, 03:49 · [Discussion](https://news.ycombinator.com/item?id=50607261)

**「Background」** XNU is the hybrid kernel developed by Apple and used in macOS, iOS, and other Apple operating systems; it combines Mach microkernel components with BSD Unix elements. macOS userspace applications depend on Darwin’s system libraries \(e.g., libSystem, CoreFoundation, AppKit\) and are not designed to run outside Apple’s tightly integrated stack—unlike Linux binaries, which rely on stable kernel ABIs and widely portable userspace toolchains.

**「Impact」** Developers attempting to run macOS GUI applications on Linux must supply their own macOS binaries \(e.g., from a licensed macOS installation\), as XNU Linux does not redistribute Apple&\#x27;s libraries or frameworks; this creates legal and practical constraints for deployment and testing.

**「Community discussion」** Commenters debate technical feasibility and alternatives: one contributor prefers improving GNUstep for cross-platform Cocoa compatibility, citing successful compilation of the same IUP driver on both macOS and GNUstep; another notes macOS’s lack of stable syscalls makes userspace porting plausible without kernel changes, while a third speculates about future hardware-enforced OS execution restrictions preventing such efforts.

<details><summary>References</summary>
<ul>
<li><a href="https://www.phoronix.com/news/XNU-Linux">XNU Linux Lets macOS Userspace Processes Run On... - Phoronix</a></li>

</ul>
</details>

**Tags**: `#operating-systems`, `#compatibility-layer`, `#reverse-engineering`, `#open-source`

---

<a id="item-tech-news-8"></a>
### [The Next Circle of Security Hell: Open Source Maintainer Burden and Security Trade-offs](https://blogs.gentoo.org/mgorny/2026/10/27/the-next-circle-of-security-hell/) ⭐️ 7.0/10

This reflective essay critiques the unsustainable security maintenance burden on open source maintainers, arguing that advances in memory safety \(e.g., Rust\) have not reduced systemic vulnerability exposure because logic flaws, misconfigurations, and under-resourced maintenance remain pervasive. It cites recent high-profile memory-safety bugs in PHP, Brotli, nginx, Java, and Ruby—not as evidence against Rust, but to underscore that eliminating one class of bugs does not resolve the broader crisis of scale, incentive misalignment, and corporate dependency on volunteer-maintained infrastructure. The piece explicitly distinguishes compiler-enforced memory safety from application-level and operational vulnerabilities, rejecting the notion that language choice alone solves security debt.

hackernews · qtqtqt · Nov 23, 11:34 · [Discussion](https://news.ycombinator.com/item?id=50610334)

**「Preceding critique of open source security maintenance」** This post is a follow-up to Michał Górny’s earlier essay &quot;The modern packager’s security nightmare&quot;, which documented the growing burden on open source maintainers in responding to security vulnerabilities. That earlier work established the tension between increasing vulnerability disclosures and limited maintainer capacity, particularly in distribution-facing roles like Gentoo package maintainers.

**「Impact」** Projects relying on volunteer maintainers—especially widely used infrastructure like nginx or PHP—are increasingly exposed to unpatched vulnerabilities not due to technical ignorance, but because maintainers lack capacity to triage, verify, and backport fixes across dozens of versions while balancing day jobs and burnout; this forces downstream users to either accept risk or divert engineering effort toward internal patching and monitoring.

**「Community Discussion」** Commenters debate responsibility: one argues maintainers should explicitly set boundaries and shift liability to users \(&\#x27;use at your own risk&\#x27;\), while another contends blame is collective—rooted in society’s fundamental misunderstanding of computational risk—and a third predicts AI-assisted code review will become mandatory for security-critical projects, as human-only review is no longer scalable.

<details><summary>References</summary>
<ul>
<li><a href="https://blogs.gentoo.org/mgorny/2026/10/27/the-next-circle-of-security-hell/">The next circle of security hell – Michał Górny</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#software-security`, `#maintainer-burnout`, `#memory-safety`, `#software-engineering`

---

<a id="item-tech-news-9"></a>
### [17M Lines of Lean Formalization of GRH Highlights Formal Verification vs. Readability](https://micjm.com/blog/yes-17m-lines-of-lean-is-a-lot/) ⭐️ 7.0/10

The blog post reflects on the 17-million-line Lean formalization of the Generalized Riemann Hypothesis \(GRH\), clarifying that the line count reflects the granularity required for machine-checkable rigor—not code bloat or poor design. It emphasizes that Lean serves as a &\#x27;compiled math&\#x27; verifier: natural-language mathematical arguments expand dramatically when fully formalized with definitions, lemmas, and type-checking infrastructure. The post distinguishes this from executable software, noting that Lean proofs are not run but verified, and stresses that human comprehension of the full formalization is neither expected nor necessary for trust in the result. The formalization remains an ongoing effort, with community reports indicating reductions to ~13 million lines and projected further shrinkage.

hackernews · seizethecheese · Nov 23, 05:00 · [Discussion](https://news.ycombinator.com/item?id=50607668)

**「Background」** The Generalized Riemann Hypothesis \(GRH\) for Dirichlet L-functions was claimed to be proven by Levent Alpöge using Anthropic&\#x27;s Claude, and the proof was formalized in Lean and released on 20 November 2026 as a 17-million-line archive comprising 175,187 files; it covers all moduli and characters for Dirichlet L-functions but excludes Dedekind zeta functions, Hecke L-functions, and automorphic L-functions. Unlike traditional mathematical publications, this proof has no accompanying human-written paper and has not yet undergone expert review of its underlying mathematics.

**「Impact」** For mathematicians and formal methods practitioners, this reinforces that reliance on verified formalizations does not require full human understanding of every line—just confidence in the trusted kernel, definitions, and logical structure—enabling safer use of GRH as a lemma across fields without circularity or informal gaps.

**「Community Discussion」** Commenters debate whether understanding the Lean formalization itself matters more than trusting its verification \(\_flag\_ and \_betterunix2\_\), while others express unease about the scale and auditability of such large formal artifacts \(lukaslalinsky\), and one notes active size reduction efforts \(adgjlsfhk1\).

<details><summary>References</summary>
<ul>
<li><a href="https://math.mit.edu/~drew/grh/">RH Lean proof: verification files - MIT Mathematics</a></li>
<li><a href="https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/">Alpöge/Claude proof of the Generalized Riemann Hypothesis</a></li>
<li><a href="https://lean4.dev/proofs/riemann-hypothesis-claim">The Riemann Hypothesis: a claimed proof, delivered in Lean</a></li>

</ul>
</details>

**Tags**: `#formal-methods`, `#theorem-proving`, `#ai-assisted-math`, `#software-correctness`, `#lean`

---

<a id="item-tech-news-10"></a>
### [Beginner&\#x27;s Guide to Local AI with Inkling, Qwen, and Unsloth](https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth) ⭐️ 7.0/10

The article is a hands-on beginner&\#x27;s guide to deploying local AI models—including Inkling \(a small, fast inference-optimized model\), Qwen \(specifically Qwen3.8 variants like 27B UD-Q4\_K\_M\), and optimization tools like Unsloth—on consumer hardware. It covers practical setup steps, VRAM-conscious quantization \(e.g., Q4\_K\_M\), and cross-platform considerations, notably highlighting macOS tooling efforts and Linux-based llama.cpp deployments. The guide targets users with mid-tier GPUs \(e.g., RTX 4070, Tesla P100, or P40\) and emphasizes affordability and accessibility over cutting-edge hardware, though it does not announce new software releases, model versions, or official support milestones.

hackernews · Retell15 · Nov 22, 21:01 · [Discussion](https://news.ycombinator.com/item?id=50603845)

**「Background」** Inkling is a family of compact, open-weight language models developed by Unsloth, designed for efficient local inference; Qwen is Alibaba&\#x27;s series of open multimodal models, with recent versions like Qwen3.6 and Qwen3.8 supporting long context \(up to 256K tokens\) and multilingual tasks. Unsloth Desktop is a recently released GUI tool \(November 2026\) that simplifies local deployment of these models on consumer hardware, abstracting CUDA setup, quantization selection, and LAN serving.

**「Impact」** Developers and hobbyists with older or budget GPUs \(e.g., Tesla P40, P100, or RTX 4070\) can now deploy performant local models like Qwen3.8-Flash-Next or Inkling 2 Mini at usable speeds \(e.g., 14–30 tokens/sec\) using publicly available tooling \(llama.cpp, Unsloth\) and community-maintained setup guides—reducing the hardware barrier to entry for local AI experimentation.

**「Community Discussion」** Commenters debate hardware pragmatism: one notes local AI is still in its &\#x27;plasma TV phase&\#x27;—early and expensive—while others highlight accessible paths using used Tesla cards \(P40, P100\) and open tooling; another corrects the guide’s Windows-only hardware assumption, stressing Linux and macOS viability.

<details><summary>References</summary>
<ul>
<li><a href="https://www.explainx.ai/blog/unsloth-qwen-inkling-beginners-local-ai-lan-guide-november-2026">Unsloth Desktop Local AI: Qwen &amp; Inkling LAN Guide | explainx ...</a></li>
<li><a href="https://unsloth.ai/docs/models/inkling">Inkling - How to Run Locally | Unsloth Documentation</a></li>
<li><a href="https://unsloth.ai/docs/models/qwen3.6">Qwen3.6 - How to Run Locally | Unsloth Documentation</a></li>

</ul>
</details>

**Tags**: `#local-ai`, `#model-deployment`, `#hardware-optimization`

---

<a id="item-tech-news-11"></a>
### [Google builds Mirror Dimension simulation to test Chrome AI agent](https://www.landian.news/archives/128701.html) ⭐️ 7.0/10

Google has built an internal sandboxed testing environment called &\#x27;Mirror Dimension&\#x27;—a simulated internet with thousands of fake websites—to evaluate Chrome&\#x27;s AI agent&\#x27;s web navigation, task completion \(e.g., logging in, adding items to cart\), and resilience against prompt injection attacks. The environment isolates tests per engineer and runs over 1,000 test cases daily. This is an internal infrastructure effort, not a public release or user-facing feature, and no version, timeline, or compatibility details for the AI agent itself are provided.

telegram · zaihuapd · Nov 23, 01:30

**「Background」** The Mirror Dimension is Google&\#x27;s internally developed synthetic web environment for evaluating AI agents in Chrome, first publicly described in a November 2026 Google Security Blog post; it replaces risky real-web testing with a controllable, scalable, and adversarially designed sandbox featuring thousands of simulated websites modeled on real user journeys.

**「Impact」** Developers and security researchers cannot access or use Mirror Dimension, limiting its immediate impact to Google’s internal AI agent development and validation; however, its design—emphasizing adversarial testing at scale—signals a concrete shift toward rigorous, safety-focused evaluation of browser-based AI agents before deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/security/mirror-dimension-for-agents/">Mirror Dimension for Agents: Evaluating Browser-Use Agents ...</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#browser security`, `#prompt injection`, `#testing infrastructure`, `#Chrome`

---

<a id="item-tech-news-12"></a>
### [Windows Server 2028 ships without WoW64 by default, blocking 32-bit apps out of the box](https://www.windowslatest.com/2026/11/23/32-bit-apps-days-are-numbered-as-microsoft-strips-support-bit-by-bit-starting-with-windows-server-2028-but-windows-11-is-safe-for-now/) ⭐️ 7.0/10

Windows Server 2028, scheduled for release in fall 2027, will ship without the WoW64 \(Windows on Windows 64-bit\) subsystem enabled by default, preventing execution of 32-bit applications immediately after installation. Administrators can manually reinstall WoW64 via Features on Demand \(FoD\) using PowerShell or DISM—supported on both Server Core and Desktop Experience editions. This change applies only to Windows Server 2028; Windows 11 retains WoW64 with no announced removal timeline.

telegram · zaihuapd · Nov 23, 03:03

**「What is WoW64?」** WoW64 \(Windows on Windows 64-bit\) is the compatibility layer that enables 32-bit x86 applications to run on 64-bit versions of Windows by translating 32-bit system calls and handling architectural differences such as pointer size and registry redirection. It has been included by default in all 64-bit Windows Server editions since Windows Server 2003, and its presence has been a foundational assumption for enterprise deployments relying on legacy 32-bit binaries.

**「Impact」** Enterprise system administrators deploying Windows Server 2028 must explicitly install WoW64 via FoD to run legacy 32-bit applications, adding a mandatory compatibility step during OS deployment and potentially breaking automated provisioning pipelines that assume default 32-bit support.

**Tags**: `#windows-server`, `#system-compatibility`, `#security-hardening`, `#legacy-software`, `#enterprise-infrastructure`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [Skip the DRAM Tier: MoRI UMBP Runs Agentic KV Cache on NVMe](https://vllm.ai/blog/2026-11-23-skip-the-dram-tier) ⭐️ 9.0/10

rss · vLLM Blog · Nov 23, 00:00

**「Background」** Agentic LLM workloads—like multi-turn coding sessions—repeatedly resend long prefixes, making KV cache hit rate critical: a 1% increase in hit rate boosted throughput by ~10% in Kimi-K3 tests. But GPU memory fills quickly, and host DRAM \(e.g., 1.8 TB at $76,000\) holds only ~23–47 minutes of KV under real traffic, forcing premature evictions and recomputation.

**「Solution」** The authors replaced the DRAM KV cache tier entirely with local NVMe SSDs using AMD’s open-source MoRI UMBP pool, running vLLM on AMD MI355X GPUs. A 1.8 TB NVMe pool matched DRAM’s throughput within ±1% across 48–96 concurrent sessions on Kimi-K3 and DeepSeek-V4-Pro—despite using only ~80 GB of DRAM for write buffering \(64 GB\) and read staging \(16 GiB\). Key enablers were async prefill overlap \(hiding NVMe latency\), small 256 MiB segment files \(raising hit rate 1.2% and throughput 15.6%\), and ‘touch’-based usage tracking to prevent premature eviction of GPU-cached prefixes. NVMe’s cost advantage stems from pricing per TB written—not held—so drives rated for Kimi-K3’s 83 TB/day writes cost ~$59,000 for one-day retention versus $3.5M for equivalent DRAM. Limitations include SSD wear \(addressed via distributed writes in roadmap\) and sensitivity to segment size and checkpointing strategy.

**「Takeaway」** NVMe can serve as the primary KV cache tier for agentic LLMs without throughput penalty—challenging the assumption that DRAM is required for low-latency caching—and delivers dramatically better cost-per-retention economics when capacity and write patterns are properly engineered.

**Tags**: `#LLM inference`, `#KV caching`, `#NVMe optimization`, `#agentic systems`, `#memory hierarchy`

---

<a id="item-tech-blog-2"></a>
### [Flailing Well: A Feedback-Driven Approach to Ambiguity](https://seangoedecke.com/when-in-doubt-flail-about/) ⭐️ 8.0/10

rss · Sean Goedecke · Nov 23, 00:00

**「Background」** When engineers face ambiguous problems—unclear product direction, intractable systems, or cross-team organizational friction—traditional planning often fails because there’s insufficient information to reason forward reliably.

**「Solution」** The author advocates disciplined &\#x27;flailing&\#x27;: rapidly trying many low-cost, speculative interventions while rigorously observing feedback from users, metrics, and colleagues—and instantly abandoning anything that lacks strong positive signals \(e.g., &\#x27;wow\!&\#x27; reactions or measurable improvement\). This works because ambiguity prevents accurate upfront judgment; only direct contact with reality reveals what matters. In product flailing \(e.g., GitHub Models\), one unassuming idea—AI inference via GitHub Actions tokens—emerged as the seed for &\#x27;Continuous AI&\#x27; only after discarding many dead ends. Engineering flailing means making speculative code changes or refactorings \(aided by AI agents\) and measuring impact before deep analysis. Organizational flailing—like automating manual handoffs or proposing structural fixes—builds trust when paired with acute feedback sensitivity, especially since people rarely articulate root causes clearly in stalled situations.

**「Takeaway」** Flailing isn’t randomness—it’s a psychologically honest, feedback-constrained exploration strategy that treats uncertainty not as a barrier but as data-gathering terrain; its effectiveness hinges on speed, humility, and the willingness to feel foolish while staying tightly coupled to evidence.

**Tags**: `#engineering-practice`, `#technical-ambiguity`, `#experimentation`, `#organizational-dynamics`, `#feedback-loops`

---

<a id="item-tech-blog-3"></a>
### [OpenAI’s Perplexity Graph: Transparency, Limits, and Pretraining Revival](https://seangoedecke.com/notes-on-openais-perplexity-reveal/) ⭐️ 7.0/10

rss · Sean Goedecke · Nov 23, 00:00

**「Background」** OpenAI unexpectedly published a graph showing perplexity trends across its released models—a first for a frontier AI lab—framing it as a transparency and safety measure. Perplexity, measured on a fixed held-out dataset, reflects how well a model predicts text during pretraining but says nothing about post-training techniques like RLHF.

**「Solution」** The graph reveals several unexpected patterns: few models share the same base perplexity, contradicting rumors of widespread post-training from shared checkpoints like GPT-4o; GPT-4.5 plateaued despite decent perplexity, suggesting utility diverges from this metric; and perplexity loss accelerated sharply starting with GPT-5.2, challenging the narrative that OpenAI had abandoned pretraining in favor of RL. The author notes that while perplexity correlates broadly with perceived capability \(e.g., GPT-3.5 → GPT-4\), gaps remain—like the underwhelming feel of GPT-4.1 versus the strong performance of o3 despite identical base perplexity—implying post-training quality \(e.g., chain-of-thought elicitation, sycophancy avoidance\) dominates subjective improvement. He also cautions that without public details on the held-out dataset or unreleased model perplexities, the data’s utility for alignment monitoring or cross-lab standards remains limited.

**「Takeaway」** OpenAI’s perplexity release is a landmark in transparency—but it underscores that perplexity alone cannot capture capability gains from post-training, nor reliably signal alignment-relevant risks. Its real value lies not in enabling external oversight, but in revealing that pretraining progress has recently accelerated, reshaping assumptions about where frontier model improvements originate.

**Tags**: `#perplexity`, `#model evaluation`, `#pretraining`, `#AI transparency`, `#LLM alignment`

---

## Financial News

<a id="item-finance-news-1"></a>
### [JPMorgan and Hyundai Card test AI agents for autonomous FX transactions](https://www.cnbc.com/2026/11/18/jpmorgan-hyundai-card-ai-agents-payments.html) ⭐️ 7.0/10

JPMorgan and Hyundai Card completed a private blockchain-based proof-of-concept in which AI agents conducted a simulated foreign exchange transaction without human intervention; the test included hard-coded $5 million transaction limits and targets multi-agent negotiation by H1 2027.

rss · CNBC Finance · Nov 23, 06:06

**「Background」** This is the first known private blockchain test of autonomous bank-to-client AI agents for corporate treasury management, building on Hyundai Card’s prior stablecoin cross-border payment experiments and JPMorgan’s Kinexys blockchain payments platform.

**「Impact」** Corporate treasurers and financial infrastructure providers face new governance demands as AI agents shift accountability from monitoring humans to monitoring machine-to-machine dependencies, with risks of cascading errors if guardrails like spending limits fail.

**Tags**: `#AI finance`, `#payments infrastructure`, `#banking innovation`, `#corporate treasury`, `#financial regulation`

---

<a id="item-finance-news-2"></a>
### [Ant Group Leads $100M Funding for Simplexity Robotics](https://www.bloomberg.com/news/articles/2026-11-22/ant-group-bets-on-simplexity-to-thrive-in-china-s-humanoid-race) ⭐️ 7.0/10

Ant Group led a $100 million pre-A funding round for Chinese embodied intelligence startup Simplexity Robotics, valuing the company at $1.6 billion, according to Bloomberg.

telegram · zaihuapd · Nov 23, 02:02

**「Background」** Simplexity Robotics is a Chinese embodied intelligence startup founded in July 2025, with core team members from Li Auto and prior disclosures of five funding rounds totaling ~RMB 2 billion \(≈$275 million\) by March 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://robottoday.com/suppliers-discovery/simplexity-robotics">Simplexity Robotics - RobotToday</a></li>
<li><a href="https://www.ai-market-watch.com/company/simplexity-robotics">Simplexity Robotics - AI Startup Profile | AI Market Watch</a></li>

</ul>
</details>

**Tags**: `#artificial-intelligence`, `#robotics`, `#venture-capital`, `#china-tech`, `#startup-funding`

---

<a id="item-finance-news-3"></a>
### [Shanghai Metro Fares Rise After 21 Years](https://weibo.com/1699432410/5368461393397183) ⭐️ 7.0/10

Shanghai raised metro fares for the first time in 21 years, effective December 1, 2026, with a new distance-based structure starting at 3 yuan for the first 0–4 km and incremental charges of 1 yuan per additional 4, 4, 4, 7, 7, 10, 10 km, then 1 yuan per 15 km beyond 50 km.

telegram · zaihuapd · Nov 23, 10:45

**「Background」** The previous fare structure had been in place since 2005, using a simpler tiered system without such granular distance increments or tiered discounts.

**「Impact」** Millions of daily commuters in Shanghai will face higher out-of-pocket costs unless they use newly introduced counted tickets \(e.g., 35 rides for 190 yuan\) or qualify for the monthly 90-yuan threshold discount.

**Tags**: `#public\_transport`, `#local\_policy`, `#consumer\_costs`

---