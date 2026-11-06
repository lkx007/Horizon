---
layout: default
title: "Horizon Summary: 2026-11-06 (EN)"
date: 2026-11-06
lang: en
---

> From 47 items, 23 important content pieces were selected

---

**Technology News**
1. [OpenSSH 10.6p2 fixes CVE-2026-1105 password auth bypass via crypt\(\) &\#x27;\*&\#x27; ambiguity](#item-tech-news-1) ⭐️ 9.0/10
2. [OpenSSH 10.6p2 fixes Alpine Linux authentication bypass via 257–1024-byte passwords](#item-tech-news-2) ⭐️ 9.0/10
3. [Claude Code sends user email to external APIs like SEC without consent](#item-tech-news-3) ⭐️ 8.0/10
4. [Inkling 2 Small: US-developed open-weight LLM trained end-to-end in NVFP4](#item-tech-news-4) ⭐️ 8.0/10
5. [Ultimate MoE Training Handbook for Megatron-LM Released by Hugging Face](#item-tech-news-5) ⭐️ 8.0/10
6. [trainlint: static analyzer for non-crashing ML bugs in PyTorch/scikit-learn code](#item-tech-news-6) ⭐️ 8.0/10
7. [DialFork: First benchmark for procedural hallucination in conversational agents](#item-tech-news-7) ⭐️ 8.0/10
8. [600,000 NVIDIA H200 chips stranded in Hong Kong awaiting Chinese import approval](#item-tech-news-8) ⭐️ 8.0/10
9. [Moonshot AI negotiates to rent 8,000+ Nvidia Blackwell GPUs from European neoclouds](#item-tech-news-9) ⭐️ 8.0/10
10. [Baidu open-sources Ernie 5.5 Flash Base, 280B-parameter MoE model with 1M-token inference context](#item-tech-news-10) ⭐️ 8.0/10
11. [MS Paint Remote Code Execution Vulnerability CVE-2026-83844](#item-tech-news-11) ⭐️ 7.0/10
12. [Kagi removes account requirement for search](#item-tech-news-12) ⭐️ 7.0/10
13. [Motorola Signature 27 launches with official GrapheneOS support](#item-tech-news-13) ⭐️ 7.0/10
14. [ULC audio codec ported to Nintendo 64&\#x27;s RSP processor](#item-tech-news-14) ⭐️ 7.0/10
15. [Google TPUv7 Ironwood Delivers Competitive Inference Performance per Dollar on AgentX Benchmarks](#item-tech-news-15) ⭐️ 7.0/10
16. [SPH Fails to Match Lc0 Chess Performance in Empirical Test](#item-tech-news-16) ⭐️ 7.0/10
17. [Huawei Cloud Launches openPangu-2.1-Pro on November 15 for Enhanced ArkTS Code Generation](#item-tech-news-17) ⭐️ 7.0/10
18. [DeepSeek Harness reaches 1.54M DAU and ~35K plugins](#item-tech-news-18) ⭐️ 7.0/10
19. [Google Releases Gemini Omni 1.2 Flash Video Generation Model](#item-tech-news-19) ⭐️ 7.0/10
20. [China&\#x27;s NRTA Requires Human Review for All Aired Micro-Dramas, Bans AI &\#x27;Washing&\#x27; of Scripts](#item-tech-news-20) ⭐️ 7.0/10

**Technology Blog**
1. [A Database Is a Store for Global Variables](#item-tech-blog-1) ⭐️ 9.0/10

**Financial News**
1. [Top Democrats Call for National Data Center Moratorium After 2026 Midterm Wins](#item-finance-news-1) ⭐️ 7.0/10
2. [Barkin Signals Gradual Fed Rate Hikes Amid Persistent Inflation](#item-finance-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [OpenSSH 10.6p2 fixes CVE-2026-1105 password auth bypass via crypt\(\) &\#x27;\*&\#x27; ambiguity](https://sshhole.com/) ⭐️ 9.0/10

OpenSSH 10.6p2, released on 2026-11-05, fixes CVE-2026-1105: a critical password authentication bypass vulnerability affecting all OpenSSH versions prior to 10.6p2 when using password-based login. The flaw arises because OpenSSH’s authentication logic incorrectly treats the crypt\(\) function’s return value of &quot;\*&quot;—used both as a legitimate &\#x27;no-password&\#x27; sentinel \(e.g., in /etc/shadow entries for locked accounts\) and as an error indicator—as equivalent to the stored password hash, allowing attackers to bypass authentication. The fix modifies sshd to distinguish crypt\(\) failure from valid no-password states by checking errno and avoiding string equality comparison with &quot;\*&quot;. Alpine Linux confirmed the vulnerability affects its musl-based OpenSSH packages, and upstream musl libc had an incomplete workaround for DES crypt but missed the SHA-256 crypt path.

hackernews · josemrb · Nov 5, 12:19 · [Discussion](https://news.ycombinator.com/item?id=50378228)

**「Unix password field semantics and crypt\(\) return conventions」** Unix systems historically use the password field in /etc/passwd or /etc/shadow to store either a hashed password \(e.g., &\#x27;$6$...&\#x27;\) or special sentinel values like &\#x27;\*&\#x27; or &\#x27;\!&\#x27; to indicate that login with a password is disallowed. The crypt\(3\) function, used by OpenSSH to verify passwords, returns the input salt string on error — and some libc implementations \(including musl\) reuse &\#x27;\*&\#x27; as both a valid sentinel for &\#x27;no password&\#x27; and an error indicator from crypt\(\), creating ambiguous in-band signaling.

**「Consequence for users」** System administrators must upgrade to OpenSSH 10.6p2 immediately on all systems permitting password authentication, as unpatched servers allow unauthorized access even when user accounts have no password or are explicitly locked with &quot;\*&quot; or &quot;\!&quot; in /etc/shadow.

**「Key technical insight from comments」** Commenters highlight that the root cause is in-band signaling—reusing the string &quot;\*&quot; to mean both &\#x27;account disabled&\#x27; and &\#x27;crypt\(\) failed&\#x27;—and note that musl libc implemented a partial workaround for DES crypt but omitted it for SHA-256 crypt, leaving the vulnerability exploitable on musl-based distributions like Alpine Linux.

<details><summary>References</summary>
<ul>
<li><a href="https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/">Security advisory: openssh -server password authentication bypass</a></li>
<li><a href="https://github.com/akarkode/alpine-openssh-sshole-auth-bypass">GitHub - akarkode/alpine- openssh -sshole-auth- bypass : Vulnerability ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#openssh`, `#cryptography`, `#system-security`, `#libc`

---

<a id="item-tech-news-2"></a>
### [OpenSSH 10.6p2 fixes Alpine Linux authentication bypass via 257–1024-byte passwords](https://thehackernews.com/2026/11/openssh-issues-emergency-fix-for-flaw.html) ⭐️ 9.0/10

OpenSSH released version 10.6p2 on November 5, 2026, to urgently fix a critical authentication bypass vulnerability affecting Alpine Linux systems. The flaw allows attackers with network access and a valid username to authenticate using passwords of 257–1024 bytes—even when the target account is configured for key-only authentication and has no password set. Alpine Linux has issued patched packages for versions 3.16 and later; administrators unable to upgrade immediately are advised to disable password-based authentication by setting PasswordAuthentication no in sshd\_config. No active exploitation has been reported.

telegram · zaihuapd · Nov 5, 16:44

**「Background」** OpenSSH is the most widely used implementation of the SSH protocol for secure remote login and other network services. Alpine Linux, a lightweight distribution commonly used in containers and embedded systems, uses musl libc instead of glibc—this difference in C library behavior contributed to the unique manifestation of the authentication bypass flaw in Alpine environments.

**「Impact」** System administrators and DevOps teams managing SSH access on Alpine Linux must immediately upgrade to OpenSSH 10.6p2 or apply the recommended configuration mitigation, as the vulnerability permits full unauthorized access to key-only accounts without requiring password knowledge.

**Tags**: `#security`, `#openssh`, `#alpine-linux`, `#authentication-bypass`, `#critical-vulnerability`

---

<a id="item-tech-news-3"></a>
### [Claude Code sends user email to external APIs like SEC without consent](https://github.com/anthropics/claude-code/issues/107757) ⭐️ 8.0/10

Claude Code automatically transmits the user&\#x27;s email address to external APIs—including the U.S. Securities and Exchange Commission \(SEC\) API—without explicit user consent, disclosure, or opt-out. This behavior occurs during API calls made by Claude Code’s built-in tools, such as when fetching XBRL financial data from data.sec.gov, which requires an email in the User-Agent header per its documented policy. The transmission is not limited to the SEC API; users report similar exposure across other integrations, and prior GitHub issues \(\#55743, \#72518\) confirm recurring patterns of automatic email injection into contexts and requests. No version number, patch date, or mitigation status is specified in the source.

hackernews · motoroco · Nov 5, 22:17 · [Discussion](https://news.ycombinator.com/item?id=50385272)

**「SEC API email requirement」** The U.S. Securities and Exchange Commission \(SEC\) API requires a valid email address in the User-Agent header for all requests, and rejects requests that omit or misformat it. This policy is documented in the official SEC EDGAR API documentation and has been independently verified via curl tests showing HTTP 403 responses when the email is missing.

**「Impact」** Developers using Claude Code to query the SEC API are automatically exposing their personal email addresses in HTTP User-Agent headers—potentially leading to targeted spam, as corroborated by user reports linking increased personalized spam to switching from GitHub Copilot to Claude Code.

**「Community perspective」** Commenters argue that Claude Code should not access or transmit user identity data—especially email—unless explicitly provided by the user in chat, and that internet-connected functionality must be transparently logged and sandboxed; one user directly links a surge in personalized spam emails to switching from GitHub Copilot to Claude Code, suggesting real-world impact from this behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://sec-edgar.github.io/sec-edgar/usage.html">Common Usage Examples — secedgar 0.6.0 documentation</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#security`, `#ai-tools`, `#developer-tools`, `#api-integration`

---

<a id="item-tech-news-4"></a>
### [Inkling 2 Small: US-developed open-weight LLM trained end-to-end in NVFP4](https://thinkingmachines.ai/news/inkling-2-small/) ⭐️ 8.0/10

Inkling 2 Small is a newly released open-weight large language model developed in the United States and trained end-to-end in NVFP4 precision. It claims top-tier performance on standard LLM benchmarks—outperforming DeepSeek-V2, GLM-5.3 Flash, and Mistral-4—and supports accessible fine-tuning. The model is publicly available with weights, and its NVFP4 training methodology is presented as a novel technical achievement enabling faster, more efficient training. No real-world deployment validation or independent replication of benchmark results is reported.

hackernews · Philpax · Nov 6, 00:00 · [Discussion](https://news.ycombinator.com/item?id=50386338)

**「NVFP4 training and Inkling lineage」** Inkling 2 Small is the second-generation small-language-model release from Thinking Machines, succeeding an earlier Inkling model whose performance or training details were not specified in the available sources. NVFP4 \(NVIDIA’s 4-bit floating-point format\) is a low-precision numeric format designed for accelerated AI training on NVIDIA GPUs; prior to this release, no publicly documented LLM had been trained end-to-end—including pre-training, mid-training, and post-training stages—in NVFP4 precision.

**「Impact」** Developers and organizations seeking performant, US-sourced, open-weight models now have a new candidate that lowers the barrier to local fine-tuning and deployment—provided its NVFP4-trained weights remain compatible with existing inference tooling supporting FP4 quantization.

**「Community discussion」** Commenters highlight Inkling 2 Small’s domestic origin and NVFP4 training as distinguishing strengths, with one noting it may be the first US-based open-weight model &\#x27;good enough&\#x27; for most knowledge work; others express cautious optimism about its benchmark claims relative to GLM-5.3 Flash and Mistral-4, stressing the need for external validation outside controlled evaluations.

<details><summary>References</summary>
<ul>
<li><a href="https://blockchain.news/ainews/thinking-machines-unveils-inkling-2-small-with-nvfp4-training">Thinking Machines unveils Inkling 2 Small with NVFP4 training</a></li>
<li><a href="https://thinkingmachines.ai/news/inkling-2-small/">Introducing Inkling 2 Small - Thinking Machines Lab</a></li>
<li><a href="https://x.com/soumithchintala/status/2118490925634556026">Soumith Chintala on X: &quot;Our v2 small model is here. I&#x27;ve been ...</a></li>

</ul>
</details>

**Tags**: `#large-language-models`, `#open-source-ai`, `#model-training`, `#fp4-quantization`, `#hacker-news`

---

<a id="item-tech-news-5"></a>
### [Ultimate MoE Training Handbook for Megatron-LM Released by Hugging Face](https://www.reddit.com/r/MachineLearning/comments/1xorgq0/the_ultimate_moe_training_handbook_training/) ⭐️ 8.0/10

Hugging Face released a comprehensive, empirically grounded handbook for training Mixture-of-Experts \(MoE\) models using Megatron-LM, targeting practitioners familiar with dense model training. The handbook includes a step-by-step runbook \(Chapter 2\) covering hardware validation, Docker image building, dense baseline training, and single-node MoE training with direct baseline comparison; a deep technical dissection of MoE layers \(Chapter 3\) covering router design, load balancing, expert layout, and systems considerations—with all claims attributed to either the authors’ 800k GH200 GPU-hours on CSCS’s Alps cluster, cited frontier-model configurations, or labeled toy simulations; and guidance on serving and RL integration \(Chapter 4\). All code, 55 explanatory figures, and recommended Megatron-LM flags are publicly released.

reddit · r/MachineLearning · /u/Norlax\_42 · Nov 5, 19:13

**「Background」** Mixture-of-Experts \(MoE\) is a sparse architecture where only a subset of model parameters \(e.g., one or two experts per token\) is activated during inference or training, enabling higher capacity at lower computational cost—commonly used in models like Mixtral and DeepSpeed-MoE. Megatron-LM is an open-source, high-performance PyTorch framework developed by NVIDIA for training large language models, recently extended to support MoE topologies with features like expert parallelism and token-based routing.

**「Impact」** Practitioners transitioning from dense to MoE training now have a reproducible, systems-aware reference that directly maps architectural decisions \(e.g., router temperature, expert count, load balancing loss\) to empirical outcomes on real hardware—reducing trial-and-error in configuring Megatron-LM for MoE, especially on multi-GPU and multi-node setups.

**Tags**: `#Mixture-of-Experts`, `#Megatron-LM`, `#model-training`, `#systems-ml`, `#sparse-models`

---

<a id="item-tech-news-6"></a>
### [trainlint: static analyzer for non-crashing ML bugs in PyTorch/scikit-learn code](https://www.reddit.com/r/MachineLearning/comments/1xonrvy/trainlint_static_checks_for_ml_bugs_that_dont/) ⭐️ 8.0/10

trainlint is a Python static analysis tool that detects 14 empirically common, non-crashing machine learning bugs—including data leakage via fit-before-split, incorrect use of eval\(\) mode during training, and mismatched logits/losses \(e.g., softmax before CrossEntropyLoss\)—by parsing source code with the ast module. It requires no data, model, or GPU, supports only PyTorch and scikit-learn, and analyzes one file at a time using name-based pattern matching. The tool identified 20 real issues and 2 harmless findings in a manual audit of pytorch/examples at a pinned commit; earlier versions had 4 false positives, now fixed. It is open-source, early-stage, and available on GitHub.

reddit · r/MachineLearning · /u/Possible-Active-1903 · Nov 5, 16:54

**「Static analysis for silent ML bugs」** Static analysis tools for machine learning code are uncommon, especially those targeting non-crashing correctness errors like data leakage or incorrect loss function usage; most linters focus on style, syntax, or runtime crashes. trainlint fills this gap by applying AST-based pattern matching—without requiring execution, data, or model instantiation—to detect empirically common pitfalls in PyTorch and scikit-learn training pipelines.

**「Impact」** Practitioners can integrate trainlint into CI or pre-commit workflows to catch silent correctness bugs—such as feature leakage inflating accuracy from 50% to 85%—before model evaluation or deployment, though its reliance on naming conventions limits robustness on nonstandard codebases.

**Tags**: `#machine-learning`, `#static-analysis`, `#software-engineering`, `#ml-ops`, `#debugging`

---

<a id="item-tech-news-7"></a>
### [DialFork: First benchmark for procedural hallucination in conversational agents](https://www.reddit.com/r/MachineLearning/comments/1xofjrn/dialfork_a_benchmark_for_procedural_hallucination/) ⭐️ 8.0/10

DialFork is the first publicly released benchmark designed to measure procedural hallucination—defined as deviations from prescribed dialogue steps despite correct tool use and factual fluency—in conversational LLM agents. It comprises over 36,000 human-annotated dialogues across 24 tasks and 12 domains, with three evaluation tasks \(turn-level drift detection, dialogue-level procedural distance, and set-level distributional comparison\), all supported by open data, code, and a public Hugging Face leaderboard. The benchmark was developed by Idiap Research Institute and Logitech and released alongside a paper \(arXiv:2610.21561\), with all components—including human annotations, LLM judge calibration data, and baseline results—openly available.

reddit · r/MachineLearning · /u/sergbur · Nov 5, 10:44

**「Context」** Prior LLM agent evaluation has focused primarily on factual accuracy and correct tool invocation, but not on adherence to required procedural steps—such as mandatory confirmations or result disclosures—that define how a dialogue should unfold. DialFork explicitly introduces &\#x27;procedural hallucination&\#x27; as a distinct, measurable failure mode orthogonal to those two axes, filling a documented gap in agent reliability assessment.

**「Consequence」** Developers evaluating conversational agents must now account for procedural fidelity—not just correctness of outputs or tools—when assessing reliability, and can use DialFork’s turn-level task as a live guardrail to detect drift during inference.

**「Community response」** No community comments were available for analysis.

**Tags**: `#LLM evaluation`, `#conversational AI`, `#hallucination`, `#benchmark`, `#agent reliability`

---

<a id="item-tech-news-8"></a>
### [600,000 NVIDIA H200 chips stranded in Hong Kong awaiting Chinese import approval](https://www.reuters.com/world/china/nvidia-chips-pile-up-hong-kong-china-withholds-import-approval-2026-11-05/) ⭐️ 8.0/10

Approximately 600,000 NVIDIA H200 AI accelerator chips are held in Hong Kong, unable to enter mainland China due to lack of import approval from Beijing. A small number of Chinese internet companies have each received about 10,000 chips, and limited quantities have entered via intermediaries and indirect channels. Though not NVIDIA’s newest model, the H200 remains significantly more capable than current domestic Chinese AI chips; as of late October, an 8-GPU H200 server in mainland China was priced above ¥6 million—roughly triple its price a year earlier.

telegram · zaihuapd · Nov 5, 14:42

**「US export licensing and Chinese import controls」** In December 2025, the U.S. government conditionally approved exports of NVIDIA H200 chips to China, requiring per-shipment export licenses and a 25% revenue share for U.S. authorities; in response, Beijing imposed its own import approval process, which—unlike prior approvals for A100 or H100 chips—has not been granted at scale for the H200 as of November 2026.

**「Impact」** The backlog of ~600,000 H200 chips has driven the price of 8-GPU H200 servers in mainland China to over ¥6 million \(≈$900,000\) by late October 2026—roughly triple the price from a year earlier—forcing AI infrastructure buyers to face severe cost inflation and extended deployment delays.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/2026_Chinese_restrictions_on_Nvidia_H200_chips">2026 Chinese restrictions on Nvidia H200 chips — Grokipedia</a></li>
<li><a href="https://gokhshtein.com/news/2026-11-05-nvidia-h200-bottleneck-in-china-pushes-server-costs-to-900k">Nvidia H200 Server Costs Rise to $900K Amid China Backlog ...</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#semiconductor policy`, `#supply chain`, `#US-China tech tension`, `#NVIDIA`

---

<a id="item-tech-news-9"></a>
### [Moonshot AI negotiates to rent 8,000+ Nvidia Blackwell GPUs from European neoclouds](https://www.cnbc.com/2026/11/05/moonshot-ai-nvidia-chips-europe-china.html) ⭐️ 8.0/10

Moonshot AI is negotiating to rent over 8,000 Nvidia Blackwell GPUs from European neocloud providers for inference and some training workloads, circumventing U.S. export bans that prohibit direct import of Blackwell chips into China. The arrangement would require Moonshot to pay 30–50% higher prepayment than non-Chinese customers. This is not yet a confirmed deployment but an active negotiation, and the U.S. government has previously identified Moonshot’s use of Thai facilities to access Blackwell chips — a prior workaround now being extended to Europe.

telegram · zaihuapd · Nov 6, 05:02

**「US export controls on Nvidia Blackwell GPUs」** The US Department of Commerce’s Bureau of Industry and Security \(BIS\) added Nvidia’s Blackwell architecture GPUs—including the B200, GB200, and B100—to its Entity List and Export Administration Regulations in October 2023, effectively banning their direct export to China for AI training and inference. Subsequent enforcement actions and licensing policies have tightened restrictions, requiring foreign cloud providers to obtain case-by-case licenses before offering Blackwell-based services accessible from China.

**「Impact」** Moonshot AI’s plan to rent 8,000+ Blackwell GPUs from European neocloud providers enables continued high-performance inference for its Kimi LLMs despite U.S. export bans—though it incurs a 30–50% premium prepayment and introduces latency, data residency, and contractual compliance risks for Chinese users and developers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/11/05/moonshot-ai-nvidia-chips-europe-china.html">China&#x27;s Moonshot AI sought Nvidia chip access in Europe amid ...</a></li>
<li><a href="https://todayforai.com/en/items/art-39268eac-d80">Moonshot AI Seeks to Rent 8,000 Nvidia Blackwell GPUs in Europe</a></li>
<li><a href="https://eastasiabrief.com/trade-policy/moonshot-ai-taps-european-cloud-8-000-blackwell-chips-1163">Moonshot AI taps European cloud for 8,000 Blackwell chips</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#export controls`, `#cloud computing`, `#semiconductors`, `#geopolitics`

---

<a id="item-tech-news-10"></a>
### [Baidu open-sources Ernie 5.5 Flash Base, 280B-parameter MoE model with 1M-token inference context](https://www.news.cn/info/20261105/f3bbdb6854f5441ca9fb34062f213875/c.html) ⭐️ 8.0/10

Baidu has open-sourced Ernie 5.5 Flash Base, a 280-billion-parameter Mixture-of-Experts \(MoE\) language model where 14 billion parameters are activated per token. It was pre-trained on 33.5 trillion tokens with a 128K-token pretraining context window and supports up to 1 million tokens in inference and fine-tuning contexts. The model includes system-level optimizations to attention mechanisms, expert routing, and training objectives to improve computational efficiency. No benchmark results, training infrastructure details, or third-party validation are provided in the announcement.

telegram · zaihuapd · Nov 6, 05:41

**「Background」** Mixture-of-Experts \(MoE\) models distribute computation across specialized subnetworks \(&\#x27;experts&\#x27;\), activating only a subset per token to improve scaling efficiency. Ernie 5.5 Flash Base follows Baidu’s prior open-source base models—including Ernie 4, noted in community comments for its directness and distinctiveness—but represents a major architectural leap in scale and context length over earlier versions.

**「Impact」** Developers and researchers can now access and modify a large-scale MoE base model with extended context support, but the restrictive license—explicitly prohibiting use in the European Union, United Kingdom, and South Korea—limits deployment and derivative development in those jurisdictions.

**「Community discussion」** Commenters on Hacker News raised concerns about the model’s restrictive license banning use in several major regions, while others sought practical guidance on multi-node fine-tuning frameworks; one user noted Ernie 4’s prior distinctiveness but questioned whether 5.5 Flash Base recaptures that advantage amid rising competition.

**Tags**: `#large-language-models`, `#mixture-of-experts`, `#open-source-ai`, `#model-optimization`

---

<a id="item-tech-news-11"></a>
### [MS Paint Remote Code Execution Vulnerability CVE-2026-83844](https://www.cve.org/CVERecord?id=CVE-2026-83844) ⭐️ 7.0/10

A remote code execution vulnerability \(CVE-2026-83844\) has been reported in MS Paint version 11.0.0.0 through 11.2605.90.99, where an unauthenticated attacker can execute arbitrary code by sending a specially crafted packet to an affected service over the network. This is notable because traditional MS Paint has no network-facing components; the vulnerability implies architectural changes—such as integration with a Windows service, cloud sync backend, or modernized UI stack—that introduce unexpected network exposure. The patched version is 11.2605.91.0, available via the Microsoft Store but not yet distributed through Windows Update. Users running older versions \(e.g., pre-11.x\) may be unaffected, though confirmation of legacy version behavior is not provided.

hackernews · kuberwastaken · Nov 5, 20:43 · [Discussion](https://news.ycombinator.com/item?id=50384233)

**「Background」** MS Paint is a legacy Windows raster graphics editor historically designed as a local, non-networked application with no built-in network services or remote interfaces. The CVE-2026-83844 vulnerability contradicts this design by enabling remote code execution via a &\#x27;specially crafted packet to an affected service&\#x27;, implying architectural changes—such as integration with Windows AppContainer services, cloud sync infrastructure, or modernized UI frameworks—that introduced unexpected network-facing components.

**「Impact」** Windows system maintainers and security engineers must urgently verify whether their deployed MS Paint instances fall within the vulnerable version range and manually install the patched version from the Microsoft Store, as Windows Update does not currently deliver the fix.

**「Community Discussion」** Commenters express disbelief at Paint’s network exposure—\[pasteleft\] questions how remote, no-interaction RCE is possible, while \[xlayn\] challenges the architectural rationale for network-facing functionality in Paint—highlighting a widespread assumption that Paint remains a purely local, offline application.

**Tags**: `#windows-security`, `#remote-code-execution`, `#vulnerability-analysis`, `#software-supply-chain`, `#legacy-software-modernization`

---

<a id="item-tech-news-12"></a>
### [Kagi removes account requirement for search](https://kagi.com/changelog#11820) ⭐️ 7.0/10

Kagi has removed the account requirement for performing searches, making its search engine publicly accessible without registration. The change enables immediate use of core features including enforced SafeSearch, customizable site rankings, and on-demand AI summarization \(triggered by appending a question mark to queries\). This update applies to all users accessing kagi.com directly, with no stated limitations on functionality for unauthenticated sessions. The change is live as of the November 5, 2026 changelog entry.

hackernews · elashri · Nov 5, 20:03 · [Discussion](https://news.ycombinator.com/item?id=50383740)

**「Background」** Kagi previously required a paid account to use its search service, positioning itself as a privacy-focused, ad-free alternative to mainstream engines with its own index and customizable result ranking. The DNS-based enforced SafeSearch feature—long requested by enterprise and educational IT administrators—has been under discussion in Kagi’s public feedback forum since at least May 2022, with proposals noting that major engines like Google and Bing support it via CNAME records to comply with network-level content policies.

**「Impact」** Institutional network administrators relying on DNS-level SafeSearch enforcement \(e.g., schools or enterprises\) cannot currently block unsafe content via Kagi’s infrastructure, risking network-wide blocking due to the absence of an enforceable SafeSearch mode—unlike Google, Bing, or DuckDuckGo.

**「Community discussion」** Multiple users highlight the urgent need for DNS-enforced SafeSearch to prevent bypassing content controls, citing longstanding feedback dating to May 2022; others praise customizable site ranking and opt-in AI summarization as key differentiators from mainstream search engines.

<details><summary>References</summary>
<ul>
<li><a href="https://help.kagi.com/kagi/faq/faq.html">Frequently Asked Questions (FAQ) | Kagi &#x27;s Docs</a></li>
<li><a href="https://kagifeedback.org/d/3285-safe-search-dns-locking-for-it-administrators">Safe Search DNS locking for IT administrators - Kagi Feedback</a></li>
<li><a href="https://kagifeedback.org/roadmap">Roadmap - Kagi Feedback</a></li>

</ul>
</details>

**Tags**: `#search-engine`, `#privacy`, `#ai-ux`, `#open-web`

---

<a id="item-tech-news-13"></a>
### [Motorola Signature 27 launches with official GrapheneOS support](https://motorolanews.com/motorola-signature-27-2/) ⭐️ 7.0/10

Motorola has launched the Signature 27 smartphone with official, vendor-supported GrapheneOS installation—marking the first non-Google device to receive such endorsement. The device ships with a locked bootloader by default but includes Motorola-signed boot images compatible with GrapheneOS’s verified boot chain, and GrapheneOS confirms full support for its 2026.11 release. It is available now starting at $1,599 USD, exclusively through Motorola’s direct channel, and requires manual installation via GrapheneOS’s official tooling; no over-the-air GrapheneOS updates are provided by Motorola. Support is limited to the Signature 27 model \(codenamed &\#x27;sapphire&\#x27;\) and does not extend to prior or sibling Motorola devices.

hackernews · monneyboi · Nov 5, 16:01 · [Discussion](https://news.ycombinator.com/item?id=50380810)

**「GrapheneOS support beyond Pixel devices」** GrapheneOS has historically been available only on Google Pixel smartphones, relying on Pixel-specific hardware features like verified boot, attestation, and vendor image signing. The Motorola Signature 27 is the first non-Pixel device to receive official GrapheneOS support, following a partnership between Motorola and GrapheneOS developers that began in March 2026.

**「Impact」** Developers and security practitioners seeking long-term, vendor-backed GrapheneOS deployment now have a non-Pixel option—but must accept higher cost, reduced hardware transparency \(due to Motorola’s proprietary BSP components\), and reliance on Motorola’s continued cooperation for future bootloader unlock or firmware signing key management.

**「Community discussion」** Commenters express skepticism about trustworthiness due to Motorola’s opaque bootloader modifications \(&\#x27;mot\_sec&\#x27;\), Qualcomm licensing constraints limiting modem firmware auditability, and corporate ownership concerns—while others welcome the expansion of officially supported hardware beyond Google’s Pixel line.

<details><summary>References</summary>
<ul>
<li><a href="https://www.91mobiles.com/hub/motorola-signature-27-official-support-grapheneos-announced/">Motorola Signature 27 to officially support GrapheneOS ...</a></li>
<li><a href="https://xab.info/en/posts/motorola-signature-27-grapheneos-support-en">Motorola Signature 27 Flagship to Receive Official GrapheneOS ...</a></li>
<li><a href="https://www.comparos.in/news/motorola-signature-27-to-become-first-non-pixel-phone-supported-by-grapheneos">Motorola Signature 27 to Become First Non-Pixel Phone Supported ...</a></li>

</ul>
</details>

**Tags**: `#GrapheneOS`, `#mobile-security`, `#Android-privacy`, `#hardware-integration`

---

<a id="item-tech-news-14"></a>
### [ULC audio codec ported to Nintendo 64&\#x27;s RSP processor](https://phoboslab.org/log/2026/11/n64-ulc-codec) ⭐️ 7.0/10

The ULC \(Ultra Low Complexity\) audio codec has been successfully ported to the Nintendo 64’s Reality Signal Processor \(RSP\), fitting within its 4 KB instruction memory \(IMEM\) limit. The port targets the RSP’s MIPS-based architecture and operates under strict real-time constraints typical of N64 audio processing. It is a research and homebrew implementation—not an official Nintendo feature—and requires custom tooling to assemble and load into RSP IMEM. The codec’s small footprint and low computational overhead make it viable for use alongside game logic, though IMEM contention with graphics tasks remains a practical constraint.

hackernews · frostbyte7 · Nov 5, 12:51 · [Discussion](https://news.ycombinator.com/item?id=50378508)

**「ULC codec and N64 RSP constraints」** ULC \(Ultra-Low Complexity\) is an open, patent-free audio codec designed for embedded systems with extreme resource constraints; it uses a fixed-point, subband-based architecture with minimal memory and computational requirements. The Nintendo 64’s Reality Signal Processor \(RSP\) provides only 4 KiB of instruction memory \(IMEM\) and 4 KiB of data memory \(DMEM\), making it exceptionally challenging to run modern audio decoders without aggressive optimization or trade-offs in real-time graphics processing.

**「Compatibility constraint for N64 game integration」** Because the ULC decoder occupies nearly all 4 KB of the N64’s RSP instruction memory \(IMEM\), it cannot coexist with RSP-based graphics or audio processing routines used by commercial games—limiting its practical use to standalone audio playback demos or games that offload graphics processing entirely to the CPU.

**「Community discussion」** Commenters debated historical patent barriers—midnightclubbed noted that ULC likely would not have been licensable for the N64 in 1999 due to the dense MP3-related patent landscape—while hxorr raised a concrete concern about IMEM competition between audio decoding and graphics routines. Sesse\_\_ speculated about porting ULC to the MAS3507D DSP but highlighted the lack of public documentation on its program format as a major obstacle.

**Tags**: `#retrocomputing`, `#audio-codecs`, `#embedded-systems`, `#low-level-optimization`

---

<a id="item-tech-news-15"></a>
### [Google TPUv7 Ironwood Delivers Competitive Inference Performance per Dollar on AgentX Benchmarks](https://newsletter.semianalysis.com/p/tpu-strikes-the-king) ⭐️ 7.0/10

Google has released the first official long-context, multi-turn agentic inference benchmark results for TPUv7 Ironwood on the industry-standard InferenceX/AgentX suite, showing competitive or superior performance-per-dollar against NVIDIA B200, B300, GB200, GB300, and AMD MI355X across four models: Muse Spark \(SGLang\), GLM-5.2 \(vLLM\), Qwen3.5 \(vLLM with llm-d\), and Kimi K3 \(vLLM\). The benchmarks were conducted in FP8, NVFP4, and MXFP4 precisions and validated by external open-source ecosystem contributors including RadixArk and Inferact. TPUv7 is now used in production by OpenAI, Anthropic, Meta, and Oracle for inference workloads.

rss · Semianalysis · Nov 5, 19:03

**「Context」** This follows SemiAnalysis’s November 2025 report confirming Google began selling TPUs externally—and its September 2026 article outlining Google’s TPU externalization strategy and publishing initial TPUv7 Ironwood single-turn inference results showing up to 50% better performance-per-dollar than NVIDIA B200/B300 on Qwen 3.5 397B in FP8.

**「Consequence」** Organizations evaluating AI inference infrastructure now have independently benchmarked, production-validated evidence that TPUv7 delivers cost-competitive or superior throughput-per-dollar for realistic agentic workloads—enabling concrete procurement decisions beyond single-turn benchmarks and reducing reliance on NVIDIA’s software-hardware stack.

**Tags**: `#AI-hardware`, `#TPU`, `#inference-optimization`, `#open-source-ai`, `#cloud-ai-infrastructure`

---

<a id="item-tech-news-16"></a>
### [SPH Fails to Match Lc0 Chess Performance in Empirical Test](https://www.reddit.com/r/MachineLearning/comments/1xov58r/empirical_evaluation_of_sparse_predictive/) ⭐️ 7.0/10

An empirical study found that Sparse Predictive Hierarchies \(SPH\) — a biologically inspired, non-backpropagation architecture with ~99% sparsity and ~44.9M parameters — failed to learn chess policy and value prediction tasks, underperforming a much smaller \(3.8M parameter\) standard CNN trained via end-to-end backpropagation on the same Lc0 test80 dataset splits. The SPH model used fuzzy ART encoders and dendritic neural layers with byte-weight quantization but showed no convergence on policy accuracy or value loss. The failure was attributed to inability to propagate global credit \(e.g., Win/Draw/Loss outcomes\) to early layers and poor handling of dense, long-range spatial dependencies inherent in chess representations.

reddit · r/MachineLearning · /u/Severe-Heat-518 · Nov 5, 21:40

**「Background」** Sparse Predictive Hierarchies \(SPH\) are neuromorphic architectures inspired by cortical predictive coding and hierarchical temporal memory \(HTM\), designed to enable local, biologically plausible learning without global backpropagation. They build on prior work like Ogma’s AOgmaNeo framework and aim to support efficient, sparse computation for real-time or edge AI applications.

**「Impact」** The result provides concrete evidence that extreme sparsity \(~99%\) and local learning rules, as implemented in this SPH variant, are insufficient for mastering symbolic, globally constrained tasks like chess—highlighting a critical compatibility gap between current non-backprop architectures and domains requiring strict long-range credit assignment.

**Tags**: `#neuromorphic-ai`, `#backpropagation-alternatives`, `#reinforcement-learning`, `#sparse-models`, `#empirical-ml`

---

<a id="item-tech-news-17"></a>
### [Huawei Cloud Launches openPangu-2.1-Pro on November 15 for Enhanced ArkTS Code Generation](https://m.gelonghui.com/live/2748413) ⭐️ 7.0/10

Huawei Cloud will release openPangu-2.1-Pro on November 15, 2026, as an updated flagship model on its MaaS platform, with a focus on improved ArkTS code generation quality for HarmonyOS native app development. The model will be integrated across Huawei’s MaaS tools—including AgentArts, CodeArts, and OfficeAce—and existing users have been notified via SMS. The announcement clarifies that Huawei Cloud has not discontinued the Pangu series, correcting prior market misinterpretation.

telegram · zaihuapd · Nov 5, 13:27

**「Preceding model and platform context」** openPangu-2.0, released prior to June 2026, was already accessible via Huawei Cloud’s ModelArts API and formed the foundation of Huawei’s MaaS offerings. The upcoming openPangu-2.1-Pro is a direct versioned successor, announced as an upgrade focused specifically on ArkTS code generation—unlike the broader general-purpose capabilities of 2.0—and will be integrated across Huawei’s existing developer tools including CodeArts \(a cloud-based DevOps platform for multi-scenario application development\) and AgentArts \(an intelligent agent platform\).

<details><summary>References</summary>
<ul>
<li><a href="https://www.aimadetools.com/blog/openpangu-2-api-guide/">openPangu 2.0 API Guide: Access Huawei&#x27;s Model via ModelArts ...</a></li>
<li><a href="https://www.huaweicloud.com/intl/en-us/product/devcloud.html">CodeArts-HUAWEI CLOUD</a></li>
<li><a href="https://todayforai.com/en/items/art-cbf5a31a-246">Huawei Cloud to Launch openPangu-2.1-Pro Flagship Model on ...</a></li>

</ul>
</details>

**Tags**: `#artificial-intelligence`, `#machine-learning`, `#software-engineering`, `#open-source`, `#mobile-development`

---

<a id="item-tech-news-18"></a>
### [DeepSeek Harness reaches 1.54M DAU and ~35K plugins](https://mp.weixin.qq.com/s/xqyrRaiBpIcf0jeJzP7W0g) ⭐️ 7.0/10

DeepSeek Harness reported 1.54 million daily active users \(DAU\) and 92.1 trillion tokens processed per day as of November 4, 2026, with approximately 35,000 third-party plugins available—about 60% of active users having used or developed at least one plugin. The platform announced concrete next steps: improving plugin API stability, launching an official plugin marketplace, and introducing an &\#x27;Author Support Program&\#x27; offering token incentives, visibility, and enterprise partnership opportunities. These are vendor-reported metrics and plans; no independent verification, technical benchmarks, or architectural details were provided.

telegram · zaihuapd · Nov 5, 15:20

**「What is DeepSeek Harness?」** DeepSeek Harness is an open-source AI agent harness developed by DeepSeek, built on the Cordis plugin architecture where &\#x27;everything is a plugin&\#x27;. It provides a runtime environment for building and running AI agents, integrating models, tools, skills, sandboxes, storage, and scheduling. The platform supports both desktop and web-based deployment and targets everyday productivity and coding tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://www.deepseek.com/en/harness/">DeepSeek Harness | Explore the limits of intelligence</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#developer ecosystems`, `#LLM tooling`

---

<a id="item-tech-news-19"></a>
### [Google Releases Gemini Omni 1.2 Flash Video Generation Model](https://x.com/Google/status/2118390406316728555) ⭐️ 7.0/10

Google DeepMind released Gemini Omni 1.2 Flash, a production-optimized video generation model supporting up to 15-second videos at resolutions scalable from 360p or 720p drafts \(priced at $0.07/second\) to final 1080p or 4K output, with claimed 30% lower cost and faster inference. It enables iterative, dialogue-based editing of background, subject, and lighting, and improves temporal controllability—reducing jump cuts—and multimodal alignment, including natural lip sync for multi-speaker audio. The model is available now as a shipped capability, not just an announced plan or research preview.

telegram · zaihuapd · Nov 6, 00:21

**「Background」** Gemini Omni is Google DeepMind&\#x27;s multimodal video generation model family, first introduced in May 2024 as a successor to earlier video diffusion models like Lumiere and Phenaki. The original Gemini Omni \(1.0\) supported up to 15-second video generation with basic temporal coherence and multimodal alignment, but lacked fine-grained controllability and cost-optimized inference for short-form deployment.

**Tags**: `#AI-video-generation`, `#multimodal-AI`, `#Google-DeepMind`, `#generative-AI`, `#LLM-integration`

---

<a id="item-tech-news-20"></a>
### [China&\#x27;s NRTA Requires Human Review for All Aired Micro-Dramas, Bans AI &\#x27;Washing&\#x27; of Scripts](https://www.ithome.com/1/023/215.htm) ⭐️ 7.0/10

China&\#x27;s National Radio and Television Administration \(NRTA\) on November 5, 2026, reaffirmed support for human-performed micro-dramas while imposing strict regulatory requirements on AI-generated micro-dramas, mandating that all aired content undergo full human review \(&\#x27;all aired, all reviewed&\#x27;\) and banning AI &\#x27;washing&\#x27;—the use of AI to obscure or repackage unoriginal, infringing, or unauthorized material such as scripts, likenesses, or voices. The directive applies to all platforms distributing micro-dramas in China and explicitly requires human oversight of copyright and ethics compliance, with the NRTA reporting that AI-generated micro-dramas accounted for over 90% of the 430,000 titles launched in the first eight months of 2026. This is a binding enforcement policy, not a proposal or draft guideline.

telegram · zaihuapd · Nov 6, 06:40

**「Regulatory context for micro-dramas in China」** China&\#x27;s National Radio and Television Administration \(NRTA\) has regulated short-form dramas since at least 2023, when it introduced licensing requirements for platforms and content providers; in 2024, it began requiring registration of all micro-drama titles before broadcast. The current directive builds on those frameworks by explicitly differentiating treatment of human-made versus AI-generated content for the first time.

**「Impact」** Platforms distributing micro-dramas in China must now implement full human review workflows for every title before broadcast, directly increasing operational costs and delaying time-to-air for AI-assisted productions; developers of AI video/audio generation tools must redesign outputs and metadata handling to prevent circumvention of &\#x27;AI washing&\#x27; prohibitions, including explicit provenance tracking and restrictions on synthetic voice/face reuse without authorization.

**Tags**: `#AI regulation`, `#copyright`, `#media technology`, `#AI ethics`, `#content moderation`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [A Database Is a Store for Global Variables](https://seangoedecke.com/a-database-is-a-store-for-global-variables/) ⭐️ 9.0/10

rss · Sean Goedecke · Nov 6, 00:00

**「Background」** The essay challenges the dogma that global variables are inherently bad by observing that databases—widely accepted in production systems—are functionally identical: any part of a program can read or write them, creating implicit coupling and hidden data flow, just like global variables in code.

**「Solution」** The author rejects common justifications—like ACID guarantees or type safety—as insufficient, arguing instead that databases work \*despite\* being global because they are more explicit \(queries require visible connection objects and function calls\) and constrained by shared engineering norms \(e.g., avoiding database use for loop counters or config paths, validating column types on read\). Unlike ad-hoc global variables, database usage is bounded, deliberate, and socially enforced—not magically safe. The author notes that Rails’ invisible ActiveRecord queries undermine the explicitness benefit, and emphasizes that these advantages are contingent, not intrinsic: disciplined conventions around ordinary globals could, in principle, yield similar robustness.

**「Takeaway」** Databases aren’t exempt from the problems of global state—they’re merely managed more carefully through convention and interface design; this reveals that much of software architecture consists of context-sensitive heuristics, not universal laws.

**Tags**: `#software-architecture`, `#database-design`, `#programming-dogma`, `#state-management`, `#engineering-heuristics`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Top Democrats Call for National Data Center Moratorium After 2026 Midterm Wins](https://www.cnbc.com/2026/11/05/democrats-data-center-restrictions-midterms.html) ⭐️ 7.0/10

Following Democratic gains in the 2026 U.S. midterm elections, Senators Bernie Sanders and others called for a &\#x27;national data center moratorium,&\#x27; citing environmental and democratic concerns; the proposal remains aspirational and unlegislated as of November 5, 2026.

rss · CNBC Finance · Nov 5, 20:17

**「Background」** Democrats gained control of both the U.S. House and Senate in the 2026 midterm elections, enabling progressive lawmakers to advance policy proposals—including calls for a national moratorium on data center construction—that had previously lacked majority support.

**「Impact」** Semiconductor and AI-related stocks fell sharply—SOXX dropped nearly 9%, AMD more than 14%—as investors reacted to the prospect of regulatory constraints on data center construction.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bbc.com/news/election/2026/us/results">US midterm elections results 2026 - BBC News</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#data centers`, `#election impact`, `#tech regulation`, `#energy infrastructure`

---

<a id="item-finance-news-2"></a>
### [Barkin Signals Gradual Fed Rate Hikes Amid Persistent Inflation](https://www.cnbc.com/2026/11/05/barkin-sees-interest-rate-hikes-ahead-but-at-a-gradual-pace.html) ⭐️ 7.0/10

Richmond Fed President Thomas Barkin said further gradual interest rate hikes are likely to address inflation that remains &\#x27;too high,&\#x27; even as unemployment stays near record lows; markets price in an over 80% chance of a December 2026 hike and another in 2027.

rss · CNBC Finance · Nov 5, 16:34

**「Background」** Barkin is not a voting member of the Federal Open Market Committee \(FOMC\) in 2026 but will be in 2027, and his remarks follow the FOMC’s September 2026 quarter-point hike and its decision to hold rates steady at 3.75%–4.00% in early November.

**「Impact」** Investors and financial markets are directly affected, as Barkin’s forward guidance reinforces expectations for higher borrowing costs—already reflected in over 80% odds of a December 2026 rate hike per CME Group’s FedWatch tool.

**Tags**: `#monetary-policy`, `#inflation`, `#fed-officials`, `#credit-risk`, `#artificial-intelligence`

---