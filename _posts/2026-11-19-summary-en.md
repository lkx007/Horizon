---
layout: default
title: "Horizon Summary: 2026-11-19 (EN)"
date: 2026-11-19
lang: en
---

> From 44 items, 24 important content pieces were selected

---

**Technology News**
1. [Java4Shell: RCE in OpenJDK Base64 decoding on AVX-512 CPUs](#item-tech-news-1) ⭐️ 9.0/10
2. [Xint discloses NGINX2Root exploit chain: 5 nginx vulnerabilities plus kernel flaw enable unauthenticated remote root access](#item-tech-news-2) ⭐️ 9.0/10
3. [Google AI answers cut organic search traffic by 40%](#item-tech-news-3) ⭐️ 8.0/10
4. [Energy-Based Reasoners claim 385x more efficient inference for Sudoku](#item-tech-news-4) ⭐️ 8.0/10
5. [Microsoft AI releases MAI Code 2 and Code 2 Flash coding models](#item-tech-news-5) ⭐️ 8.0/10
6. [Datasette Lite 2.0 launches with service workers for full client-side Datasette](#item-tech-news-6) ⭐️ 8.0/10
7. [Microsoft&\#x27;s ONNX Runtime GitHub repository taken offline amid security concerns](#item-tech-news-7) ⭐️ 7.0/10
8. [Gemini 4 Carbon shows high latency, token bloat, and excessive tool calls](#item-tech-news-8) ⭐️ 7.0/10
9. [Harvard study finds AI coding agents shift bottleneck from writing to code review](#item-tech-news-9) ⭐️ 7.0/10
10. [IRS mandates ID.me sign-in with smartphone-only enrollment barrier](#item-tech-news-10) ⭐️ 7.0/10
11. [Quad9 exits France over court-ordered DNS piracy blocking](#item-tech-news-11) ⭐️ 7.0/10
12. [Phrack 73 publishes new security research including Docker escape exploit](#item-tech-news-12) ⭐️ 7.0/10
13. [curl maintainer highlights 300+ commits and 200+ bugfixes during Rust rewrite period](#item-tech-news-13) ⭐️ 7.0/10
14. [External sandboxes for coding agents: three sandbox server implementations released](#item-tech-news-14) ⭐️ 7.0/10
15. [US AI chip rules pause $480M ByteDance GPU loan for Malaysia data center](#item-tech-news-15) ⭐️ 7.0/10
16. [Anthropic launches beta Linked Billing for Claude API](#item-tech-news-16) ⭐️ 7.0/10
17. [Nine Chinese ministries propose vehicle-battery integrated scrapping for EVs](#item-tech-news-17) ⭐️ 7.0/10
18. [DeepSeek makes server-side search and web crawling free](#item-tech-news-18) ⭐️ 7.0/10
19. [Voyager 1 reaches one light-day from Earth after 49 years](#item-tech-news-19) ⭐️ 7.0/10

**Technology Blog**
1. [FlyDSL MonoKernels for Low-Latency LLM Decode on AMD GPUs](#item-tech-blog-1) ⭐️ 9.0/10

**Financial News**
1. [Waller Calls for 50-Basis-Point Rate Hike in December](#item-finance-news-1) ⭐️ 8.0/10
2. [JPMorgan and Hyundai Card test AI agents for autonomous FX transactions](#item-finance-news-2) ⭐️ 7.0/10
3. [UK Immigration and Asylum Bill Passes House of Commons](#item-finance-news-3) ⭐️ 7.0/10
4. [China and South Korea Conclude FTA Expansion Talks on Services and Investment](#item-finance-news-4) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Java4Shell: RCE in OpenJDK Base64 decoding on AVX-512 CPUs](https://calif.io/java4shell/) ⭐️ 9.0/10

A remote code execution vulnerability dubbed Java4Shell \(CVE-2026-114938, CVSS 4.0 score 9.2\) was disclosed in OpenJDK’s Base64 decoding logic, exploitable via network-based heap grooming on HotSpot-based JVMs—including OpenJDK, Oracle JDK, and GraalVM—when running on x86-64 processors with AVX-512 VBMI support \(e.g., Intel Ice Lake+ Xeon, AMD Zen 4+ EPYC/Ryzen\). It affects Java 17.0.6+, 21, 25, and 27; standard Java 8 and 11 are generally unaffected, except Oracle Java 8 Performance Pack. The exploit has been demonstrated over the public internet—not just in lab conditions—and requires stable, low-jitter network round-trip times for reliability.

hackernews · werrett · Nov 17, 21:11 · [Discussion](https://news.ycombinator.com/item?id=50538240)

**「Background」** Base64 decoding in OpenJDK has long relied on CPU-specific intrinsics for performance, including AVX-512 vectorized implementations introduced in JDK 17 for x86-64. The Java4Shell vulnerability arises from memory corruption in the AVX-512 VBMI-based Base64 intrinsic decoder—a low-level, JIT-compiled HotSpot stub not present in non-HotSpot JVMs like OpenJ9 or GCJ.

**「Impact」** Organizations running Java 17.0.6+ \(or 21/25/27\) on AVX-512–capable x86-64 servers must urgently assess exposure, as the vulnerability enables unauthenticated remote code execution without requiring application-level deserialization or unsafe reflection—bypassing many existing Java security mitigations.

**「Community discussion」** Commenters highlighted the exploit’s dependence on precise network conditions \(e.g., low RTT and jitter\) for reliability over the internet, while others questioned the long-term viability of complex JIT- and heap-dependent runtimes like Java in light of such deep runtime-level vulnerabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sophos.com/en-us/security-advisories/sophos-sa-20261118-java4shell">Advisory: OpenJDK Base64 Vulnerability - Java4Shell (CVE-2026 ...</a></li>
<li><a href="https://computingforgeeks.com/java4shell-cve-2026-114938/">Java4Shell CVE-2026-114938: Patch Vulnerable OpenJDK ...</a></li>
<li><a href="https://securitylabs.datadoghq.com/articles/java4shell-remote-code-execution-in-openjdk-cve-2026-114938/">Java4Shell: Remote Code Execution in OpenJDK (CVE-2026-114938)</a></li>

</ul>
</details>

**Tags**: `#java`, `#security`, `#vulnerability`, `#jvm`, `#exploitation`

---

<a id="item-tech-news-2"></a>
### [Xint discloses NGINX2Root exploit chain: 5 nginx vulnerabilities plus kernel flaw enable unauthenticated remote root access](https://nginx2root.com/) ⭐️ 9.0/10

Xint disclosed NGINX2Root—a chained exploit combining five previously unknown nginx vulnerabilities \(including CVE-2026-123007, a critical unauthenticated HTTP/2 stream control memory corruption\) and one Linux kernel flaw—to achieve unauthenticated remote root access via HTTP/2. The vulnerabilities were patched in nginx 1.30.7 and 1.31.9, released on November 18, 2026. A public proof-of-concept exploit has been released by Rapid7; mitigation guidance recommends disabling HTTP/2 if upgrading is not immediately possible. No in-the-wild exploitation has been observed.

telegram · zaihuapd · Nov 18, 16:21

**「Background」** NGINX2Root relies on HTTP/2 stream control mechanisms in nginx, which were introduced in nginx 1.9.5 \(2015\) and became production-ready with HTTP/2 support enabled by default in later versions. The exploit chain builds upon long-standing assumptions about isolation between nginx worker processes and the host kernel—assumptions undermined by the combination of user-space memory corruption in nginx and a pre-existing Linux kernel vulnerability.

**「Impact」** Organizations running nginx versions prior to 1.30.7 or 1.31.9 with HTTP/2 enabled are at risk of unauthenticated remote root compromise, requiring immediate patching or HTTP/2 disablement as a workaround.

**Tags**: `#nginx`, `#security`, `#exploit-chain`, `#http2`, `#root-compromise`

---

<a id="item-tech-news-3"></a>
### [Google AI answers cut organic search traffic by 40%](https://revscope.co/blog/search-seo-geo-2026/) ⭐️ 8.0/10

Google&\#x27;s AI-powered direct answers—delivered in Search results without requiring users to click through to external sites—are reportedly reducing organic search traffic to publishers by 40%. This effect is observed across a range of informational queries and reflects a structural shift in user behavior, where users increasingly accept AI-synthesized answers instead of navigating the open web. The claim originates from industry analysis \(RevScope blog, November 2026\) and is echoed in technical discussion on Hacker News; it describes an already-occurring, measurable impact—not a forecast or pilot program.

hackernews · slashdev · Nov 18, 00:17 · [Discussion](https://news.ycombinator.com/item?id=50540178)

**「AI Overviews as a Google Search feature」** Google launched AI Overviews in May 2024 as a generative, answer-first feature integrated into search results, initially rolling out to U.S. users and expanding globally through 2024–2025. The feature synthesizes information from multiple web sources to provide direct answers above traditional organic results, altering the longstanding link-based SERP layout. It builds on earlier Google efforts like featured snippets and Knowledge Panels but represents a structural shift from retrieval to synthesis.

**「Impact」** Web publishers and SEO-dependent businesses face demonstrably lower referral traffic from Google Search, undermining traditional content monetization and discovery models; this necessitates adaptation toward AI-aligned content strategies or alternative distribution channels.

**「Community Discussion」** Commenters debate whether AI answers represent a natural evolution of user expectations \(e.g., preferring instant answers over clickbait-laden SERPs\) or an acceleration of the &\#x27;death of discovery&\#x27;, with some arguing that SEO practices had already eroded open-web exploration before AI intensified the trend.

**Tags**: `#search-engine-optimization`, `#ai-impact`, `#web-ecosystem`, `#information-retrieval`, `#google-ai`

---

<a id="item-tech-news-4"></a>
### [Energy-Based Reasoners claim 385x more efficient inference for Sudoku](https://energy-based-reasoners.github.io/) ⭐️ 8.0/10

Energy-Based Reasoners \(EBRs\) are introduced as a new inference paradigm achieving up to 385× more efficient inference than baseline methods on structured reasoning tasks like Sudoku; the claim is presented on a GitHub Pages site without specifying hardware, baselines, datasets, or measured metrics. The approach uses energy-based cell selection—assigning higher energy to conflicting cells to prioritize conflict resolution—and restricts sampling probabilities for clues and clue cells. No version number, release date, software artifact, or independently verified benchmark results are provided, and the work appears unpublished and not yet deployed in production systems.

hackernews · frenchmajesty · Nov 18, 09:29 · [Discussion](https://news.ycombinator.com/item?id=50543989)

**「Energy-based models and Logical Intelligence&\#x27;s Kona 1.0」** Energy-based models \(EBMs\) define a scalar &\#x27;energy&\#x27; function over candidate outputs, where lower energy corresponds to higher plausibility; inference involves searching for low-energy configurations, often via iterative optimization rather than autoregressive token generation. Logical Intelligence recently released Kona 1.0—the first commercially shipped energy-based reasoning model—demonstrating high accuracy on Sudoku \(96.2% on hard puzzles\) and positioning EBMs as an alternative to LLMs for formal reasoning tasks.

**「Impact」** Developers working on logic and constraint-satisfaction tasks may reduce inference energy consumption by up to 385× compared to baseline architectures referenced in the source, but only for narrow, structured domains like small-scale Sudoku—where EBRs avoid autoregressive token generation and instead use energy-guided cell updates; however, no evidence confirms scalability to larger instances or integration into production reasoning pipelines.

**「Community discussion」** Commenters highlight EBRs’ potential advantages over LLMs in formal logic, counting, and constraint satisfaction—citing Yann LeCun’s Logical Intelligence initiative as relevant context—while also noting practical challenges: training difficulty, narrow scalability \(e.g., limited Sudoku grid size\), and ambiguity in the definition of &\#x27;energy&\#x27; as a scalar function over reals.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/when-predicting-next-word-isnt-enough-what-reasoning-actually-bahri-zncff">When Predicting the Next Word Isn&#x27;t Enough: What Energy - Based ...</a></li>
<li><a href="https://finance.yahoo.com/news/logical-intelligence-introduces-first-energy-182100439.html">Logical Intelligence Introduces First Energy - Based Reasoning AI...</a></li>
<li><a href="https://paperlens.io/idea/kona-1/">Kona 1: Energy - Based Reasoning | PaperLens</a></li>
<li><a href="https://apexneuralnews.com/news/energy-based-reasoners-385x-more-efficient-inference">Energy-Based Reasoners: 385x more efficient inference</a></li>

</ul>
</details>

**Tags**: `#artificial-intelligence`, `#reasoning-systems`, `#energy-based-models`, `#constraint-satisfaction`, `#ai-architecture`

---

<a id="item-tech-news-5"></a>
### [Microsoft AI releases MAI Code 2 and Code 2 Flash coding models](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/) ⭐️ 8.0/10

Microsoft AI released MAI Code 2 and MAI Code 2 Flash—specialized, high-efficiency large language models for coding tasks. According to Microsoft&\#x27;s announcement, MAI Code 2 delivers 98% of &\#x27;GPT-6.1 Sol’s&\#x27; performance at 40% of the cost and 96% of &\#x27;Claude Opus 5.5’s&\#x27; performance at 5% of the cost; MAI Code 2 Flash is a further optimized variant. The models are available via GitHub Copilot \(e.g., offered at 50% discount as reported by a user\), and early real-world usage includes resolving Python build issues in Windows WSL/Ubuntu, generating passing test cases, and fixing Azure Bicep deployment code. The benchmarks and model names \(&\#x27;GPT-6.1 Sol&\#x27;, &\#x27;Claude Opus 5.5&\#x27;\) appear unofficial and are not independently verified.

hackernews · lemonish97 · Nov 17, 18:25 · [Discussion](https://news.ycombinator.com/item?id=50535885)

**「Predecessor: MAI Code 1」** MAI Code 2 and Code 2 Flash succeed the original MAI Code model, which Microsoft introduced in 2025 as a lightweight, coding-specialized LLM powering early versions of GitHub Copilot’s inline suggestions and basic code completion. The new models expand the family from narrow assistance to support for complex, agentic software engineering tasks—including full-file reasoning, test generation, and infrastructure-as-code \(e.g., Azure Bicep\) resolution—while emphasizing cost-efficient inference.

**「Impact」** Developers using GitHub Copilot can now access lower-cost, coding-specialized models that users report resolving complex, real-world engineering tasks—such as WSL-based Python builds and Azure Bicep deployments—with performance comparable to top-tier general-purpose models, potentially reducing inference cost and improving workflow integration without sacrificing utility.

**「Community discussion」** Users report concrete improvements in development workflows—e.g., resolving Python build issues in WSL and Azure Bicep deployments—while questioning the provenance and realism of benchmark claims like &\#x27;GPT-6.1 Sol&\#x27; and cost comparisons, with one commenter speculating about model distillation or privileged access to OpenAI models, though no evidence for such access is provided.

<details><summary>References</summary>
<ul>
<li><a href="https://github.blog/changelog/2026-11-17-mai-code-2-and-mai-code-2-flash-in-github-copilot/">MAI Code 2 and MAI Code 2 Flash in GitHub Copilot</a></li>

</ul>
</details>

**Tags**: `#AI`, `#software-engineering`, `#LLM`, `#developer-tools`, `#model-optimization`

---

<a id="item-tech-news-6"></a>
### [Datasette Lite 2.0 launches with service workers for full client-side Datasette](https://simonwillison.net/2026/Nov/17/datasette-lite/) ⭐️ 8.0/10

Datasette Lite 2.0, a complete rewrite released on November 17, 2026, enables the full Datasette Python application—including SQLite/CSV/JSON browsing, plugin installation, and version selection—to run entirely client-side in browsers using Pyodide and service workers. Users can load specific Datasette versions \(from PyPI or GitHub commits/tags\), choose among over 100 SQLite versions, and install plugins like datasette-maplibre via URL parameters; all functionality is delivered through https://lite.datasette.io/ with no backend server required. The service-worker architecture replaces the original 2022 web worker hack, enabling proper JavaScript execution, dynamic script loading, and reliable offline-first behavior—making it functionally indistinguishable from server-side Datasette for most use cases. CORS-enabled remote files \(e.g., from GitHub Gists\) are supported for databases, metadata, and SQL scripts.

rss · Simon Willison · Nov 17, 16:48

**「Background」** Datasette is a Python-based open-source tool for publishing data from SQLite, CSV, and JSON as interactive, searchable web interfaces. The original Datasette Lite launched in May 2022 as an experimental Pyodide port but relied on a fragile web worker + innerHTML approach that broke JavaScript-dependent features. This 2026 release replaces that implementation with a service-worker-driven architecture to properly handle dynamic module loading, script execution, and routing.

**「Impact」** Developers and data publishers can now create shareable, self-contained, offline-capable links to Datasette instances—including custom plugins and unreleased versions—for demos, bug reports, and documentation without provisioning or maintaining any server infrastructure.

**Tags**: `#webassembly`, `#python`, `#pyodide`, `#datasette`, `#offline-web`

---

<a id="item-tech-news-7"></a>
### [Microsoft&\#x27;s ONNX Runtime GitHub repository taken offline amid security concerns](https://github.com/microsoft/onnxruntime) ⭐️ 7.0/10

Microsoft&\#x27;s official ONNX Runtime GitHub repository \(github.com/microsoft/onnxruntime\) became inaccessible on or before November 17, 2026, with no public explanation from Microsoft. The outage coincides with confirmed compromise of the Microsoft Agent Framework PyPI package and its associated GitHub repository, which is also offline. Community speculation links the incident to potential security breaches, telemetry-related controversies, or proactive removal due to undisclosed vulnerabilities; however, no official statement, root cause, or restoration timeline has been provided, and the status remains unconfirmed as of the report date.

hackernews · nvader · Nov 17, 23:18 · [Discussion](https://news.ycombinator.com/item?id=50539610)

**「Background」** ONNX Runtime is an open-source inference engine for ONNX models, widely used to deploy AI/ML models across hardware and platforms. In March 2026, a critical parser flaw was identified in ONNX Runtime that allowed arbitrary file or memory access without validation when loading malicious ONNX models \(tool-1-2\). Separately, on November 17, 2026, Microsoft&\#x27;s agent-framework PyPI package was confirmed compromised—versions 1.26.1 and 1.26.2 contained credential-stealing malware delivered via .pth hooks \(tool-2-1\).

**「Impact」** Developers and organizations relying on ONNX Runtime for AI/ML model inference—especially those depending on GitHub-hosted source, CI/CD integrations, or direct git dependencies—face immediate build failures, inability to audit or patch code, and uncertainty about supply-chain integrity.

**「Community discussion」** Commenters explicitly connect the outage to the compromised Microsoft Agent Framework package and raise concerns about ONNX Runtime’s default telemetry behavior—specifically that it exfiltrates application data without an opt-out mechanism unless built from source with telemetry disabled.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50539610">Microsoft &#x27;s ONNX Runtime has disappeared from GitHub</a></li>
<li><a href="https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer">Microsoft ’s agent - framework PyPI package Compromised ... | Socket</a></li>

</ul>
</details>

**Tags**: `#AI-infrastructure`, `#security-incident`, `#telemetry`, `#open-source-vulnerability`

---

<a id="item-tech-news-8"></a>
### [Gemini 4 Carbon shows high latency, token bloat, and excessive tool calls](https://kernel.dev/blog/why-is-gemini-4-carbon-taking-so-long/) ⭐️ 7.0/10

Gemini 4 Carbon exhibits significantly higher inference latency \(6m 08s vs 2m 04s for peers\), generates nearly 2.4× more output tokens \(16.4k vs 6.8k\), and makes nearly twice as many tool calls \(21 vs 11\) — all statistically significant findings from benchmarking across 146 head-to-head comparisons. These inefficiencies stem from design choices prioritizing frontier capability and reasoning depth over inference efficiency, not from implementation bugs or temporary deployment issues. The model is shipped and publicly available, and its behavior is empirically observed, not merely claimed by Google. No official timeline or mitigation plan for these performance characteristics has been announced.

hackernews · deenadz · Nov 18, 04:14 · [Discussion](https://news.ycombinator.com/item?id=50541790)

**「Gemini 4 Carbon&\#x27;s release and positioning」** Gemini 4 Carbon was announced by Google on October 28, 2026, as its new flagship AI model, positioned ahead of Gemini 4 Argon and other variants like Hydrogen; however, general availability had not been confirmed as of the article’s publication on November 18, 2026. It is explicitly contrasted with efficiency-focused models such as Hydrogen and earlier models like Argon, which are used for different operational roles—including security-sensitive orchestration—highlighting Google’s strategy of segmenting models by capability versus inference efficiency.

**「Impact」** Developers integrating Gemini 4 Carbon into latency-sensitive or cost-constrained production systems face measurable overhead: benchmark data shows it takes ~3× longer to complete tasks \(6m 08s vs 2m 04s\), generates ~2.4× more output tokens \(16.4k vs 6.8k\), and makes nearly twice as many tool calls \(21 vs 11\) compared to peer models—directly increasing inference cost, API wait times, and orchestration complexity.

**「Community discussion」** Commenters widely attribute Gemini 4 Carbon’s inefficiency to Google’s deliberate trade-off: optimizing for maximum capability and reasoning quality rather than speed or token economy, with one user noting Google has &\#x27;huge amounts of cash and compute&\#x27; and maintains separate efficient models like Hydrogen. Another user observes that despite its slowness, Carbon delivers a distinct, architecture-aware problem-solving style—&\#x27;light touch while still driving toward sensible architecture&\#x27;—that contrasts with Claude’s &\#x27;bulldozer attitude&\#x27; and even earlier Gemini versions.

<details><summary>References</summary>
<ul>
<li><a href="https://projedefteri.com/en/blog/gemini-4-carbon-release-date/">Gemini 4 Carbon Release Date , Price and Access | Proje Defteri</a></li>
<li><a href="https://askhari.in/gemini-4-carbon/">Gemini 4 Carbon : Release Date , Benchmarks, Price, vs Argon</a></li>
<li><a href="https://deepmind.google/models/gemini/">Gemini — Google DeepMind | Our next era of frontier intelligence</a></li>

</ul>
</details>

**Tags**: `#LLMs`, `#model inference`, `#performance benchmarking`, `#AI engineering`

---

<a id="item-tech-news-9"></a>
### [Harvard study finds AI coding agents shift bottleneck from writing to code review](https://complexdiscovery.com/harvard-researchers-find-ai-coding-agents-shifted-the-bottleneck-to-code-review/) ⭐️ 7.0/10

Harvard researchers, using data from engineering analytics firm Jellyfish, found that AI coding agents have shifted the primary bottleneck in software development from code authoring to code review. This conclusion is based on empirical analysis of real-world development workflows, not theoretical modeling or lab experiments. The shift is corroborated by widespread practitioner reports on Hacker News, where developers describe spending most of their time reviewing AI-generated code—often more voluminous and over-engineered than human-written equivalents—and express concerns about cognitive load, understanding, and maintainability. The study does not claim AI-generated code is inherently defective, but identifies review as the new critical path for quality assurance and knowledge transfer.

hackernews · judahmeek · Nov 17, 21:16 · [Discussion](https://news.ycombinator.com/item?id=50538303)

**「Background」** The finding builds on prior economic models of software development as a two-stage process requiring complementary inputs—code authoring and code review—where gains in one stage can be offset by bottlenecks in the other. This Harvard study, using real-world engineering analytics from Jellyfish across hundreds of firms, empirically confirms that AI coding agents increase code output substantially but also lengthen review cycles, turning review into the limiting factor.

**「Impact」** Developers and engineering teams must now prioritize review process design—including tooling, checklists, role definitions, and training—over authoring efficiency, since review has become the dominant time sink and quality gate; this increases demand for reviewers with deep system knowledge and raises risks for onboarding and long-term codebase comprehension when no human authored key components.

**「Community discussion」** Commenters report divergent experiences: one senior developer \(\[alkonaut\]\) claims AI agents outperform humans at finding bugs and can even self-review effectively, while others \(\[AlwaysRock\], \[littlecranky67\]\) describe exhausting, low-satisfaction review work dominated by over-engineered solutions and diminished shared understanding; several note the research feels retrospective given how rapidly teams have already adapted to this bottleneck in practice.

<details><summary>References</summary>
<ul>
<li><a href="https://pondero.ai/news/2026-10-12-harvard-jellyfish-code-review-bottleneck/">Harvard study of 718 firms finds AI coding agents&#x27; output ...</a></li>
<li><a href="https://fion.ac/jellyfish.pdf">Artificial Intelligence in the Firm: Bottlenecks in Software ...</a></li>

</ul>
</details>

**Tags**: `#AI coding`, `#software engineering`, `#code review`, `#developer workflow`, `#LLM applications`

---

<a id="item-tech-news-10"></a>
### [IRS mandates ID.me sign-in with smartphone-only enrollment barrier](https://consumerrights.wiki/w/ID.me_terms_required_for_IRS_sign-in) ⭐️ 7.0/10

The IRS now requires taxpayers to use ID.me for online account access, and ID.me’s enrollment process mandates a smartphone—blocking users without one from signing in to IRS.gov or accessing TreasuryDirect. This requirement is in effect as of early 2026, with no official alternative offered by the IRS despite federal policy directing agencies to support login.gov by 2028. Users report being locked out of critical services including I-bond redemptions and tax return information retrieval.

hackernews · DeepLogin · Nov 18, 00:51 · [Discussion](https://news.ycombinator.com/item?id=50540437)

**「IRS and TreasuryDirect shift to ID.me authentication」** The IRS began requiring ID.me for online account access in early 2022, following earlier use of its own login system; this move drew criticism over facial recognition and accessibility, prompting the IRS to announce a transition away from ID.me in February 2022 — though that reversal was not sustained. By October 28, 2026, TreasuryDirect fully replaced its legacy login with ID.me as the sole online authentication method, and the IRS now mandates either ID.me or Login.gov for most services, per its current sign-in guidance.

**「Impact」** Taxpayers without smartphones are blocked from accessing IRS services and TreasuryDirect accounts due to ID.me’s smartphone-only enrollment requirement, forcing urgent workarounds like redeeming I-bonds early or switching to login.gov where available.

**「Community concern centers on smartphone-only enrollment blocking access for non-smartphone users, with reports of TreasuryDirect lockouts and skepticism about ID.me’s suitability for government identity verification; some users confirm login.gov now works for IRS sign-in, though it is not officially promoted or documented by the IRS.」** Community concern centers on smartphone-only enrollment blocking access for non-smartphone users, with reports of TreasuryDirect lockouts and skepticism about ID.me’s suitability for government identity verification; some users confirm login.gov now works for IRS sign-in, though it is not officially promoted or documented by the IRS.

<details><summary>References</summary>
<ul>
<li><a href="https://www.irs.gov/help/creating-an-account-for-irsgov">Creating an account for IRS.gov - Internal Revenue Service</a></li>
<li><a href="https://www.sapling.com/13770541/what-is-irs-idme">IRS ID.me Is a No-Go - Sapling</a></li>
<li><a href="https://www.thinkitsascam.com/treasurydirect-idme/">TreasuryDirect ID . me Email: Legit or a Scam?</a></li>
<li><a href="https://factually.co/fact-checks/finance/irs-switch-idme-to-login-gov-timeline-implications-f6b6f2">Will the IRS Switch From ID.me to Login . gov — Timeline ...</a></li>

</ul>
</details>

**Tags**: `#identity-verification`, `#government-tech`, `#accessibility`, `#authentication`, `#public-infrastructure`

---

<a id="item-tech-news-11"></a>
### [Quad9 exits France over court-ordered DNS piracy blocking](https://techstackups.com/articles/quad9-leaves-france-dns-blocking/) ⭐️ 7.0/10

Quad9 discontinued its DNS resolver service for users in France after refusing to comply with a French court order requiring DNS-based blocking of piracy-related domains. The organization stated that such blocking is technically infeasible at the DNS resolver level, undermines user privacy and security, and violates open internet principles. Quad9’s withdrawal took effect on or before November 18, 2026, and applies to all users resolving via its public DNS infrastructure \(e.g., 9.9.9.9\) who appear to be located in France. The decision follows similar public positions by Cloudflare and other infrastructure providers rejecting jurisdictional mandates for DNS-level content filtering.

hackernews · ritzaco · Nov 18, 13:18 · [Discussion](https://news.ycombinator.com/item?id=50545958)

**「Background」** DNS resolvers like Quad9 translate human-readable domain names into IP addresses and operate without persistent user identity or session context, making them technically unsuited for geographically targeted or content-based filtering. Courts in France have previously ordered DNS providers to block domains associated with copyright infringement—a practice criticized by Quad9 and Cloudflare as ineffective, privacy-invasive, and incompatible with DNS protocol design.

**「Impact」** Quad9 will stop serving French users on November 24, 2026, after a Paris court imposed a €1,000 daily penalty for noncompliance with DNS-based piracy blocking orders; this makes Quad9 the second DNS resolver to exit France over such mandates, directly reducing privacy-preserving, encrypted DNS options for French internet users.

**「Community discussion」** Commenters debated the legitimacy and efficacy of DNS-based enforcement, with one arguing that all anti-piracy measures short of prosecuting individuals serve as speech-suppression backdoors, and another questioning how Quad9 reliably identifies and excludes French users given DNS’s lack of built-in geolocation or identity mechanisms.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50538994">Quad 9 &#x27;s withdrawal from France : A canary in the coal... | Hacker News</a></li>
<li><a href="https://dzen.ru/a/avzqq-wLzhLQqjku">Quad 9 свернёт публичный DNS во Франции после иска beIN | Дзен</a></li>
<li><a href="https://torrentfreak.com/dns-resolver-quad9-will-leave-france-after-court-orders-piracy-blocking-penalty/">DNS Resolver Quad 9 Will Leave France After Court... * TorrentFreak</a></li>

</ul>
</details>

**Tags**: `#DNS`, `#internet-censorship`, `#network-infrastructure`, `#privacy`, `#cyber-policy`

---

<a id="item-tech-news-12"></a>
### [Phrack 73 publishes new security research including Docker escape exploit](https://phrack.org/issues/73/introduction_md) ⭐️ 7.0/10

Phrack 73, the latest issue of the long-running hacker magazine, was released on November 17, 2026, and includes original security research such as a Docker escape exploit. The issue features contributions from established figures including Halvar Flake and maintains Phrack’s tradition of practitioner-driven, technically detailed content. It is available online at phrack.org/issues/73/ and through the Phrack archives. No information in the source confirms whether the Docker exploit was responsibly disclosed, assigned a CVE, or coordinated with vendors prior to publication.

hackernews · notmine1337 · Nov 17, 18:31 · [Discussion](https://news.ycombinator.com/item?id=50535992)

**「Background」** Phrack is a long-running, underground security magazine founded in 1985, historically distributed via BBSes and known for publishing foundational technical content on telecommunications hacking, reverse engineering, and exploit development. It ceased regular publication after issue \#72 in 2014 but re-emerged with issue \#73 in November 2026, marking its first new release in over a decade.

**「Community discussion」** Commenters debated disclosure practices—specifically whether the Docker escape exploit had undergone responsible disclosure or CVE assignment—while others highlighted Halvar Flake’s influence and praised Phrack’s unpolished, open format as fostering authentic technical expression distinct from professionalized platforms like Hacker News.

**Tags**: `#security-research`, `#exploit-development`, `#hacker-culture`, `#docker`, `#responsible-disclosure`

---

<a id="item-tech-news-13"></a>
### [curl maintainer highlights 300+ commits and 200+ bugfixes during Rust rewrite period](https://simonwillison.net/2026/Nov/18/daniel-stenberg/) ⭐️ 7.0/10

During a ~3.5-week period in which external agents reportedly converted 185,000 lines of curl’s C code into 340,000 lines of Rust, the official curl project merged over 300 commits—including more than 200 bugfixes and several vulnerability patches. These improvements were delivered to the production C codebase and are not present in the Rust rewrites. Stenberg notes that an additional ~200 bugfixes and further vulnerability patches followed in the subsequent month.

rss · Simon Willison · Nov 18, 15:58

**「curl&\#x27;s maintenance velocity during Rust rewrite efforts」** curl is a widely deployed, C-based command-line tool and library for transferring data with URLs, first released in 1998 and maintained continuously by Daniel Stenberg. The background to this statement is the recent emergence of AI-powered &\#x27;coding agents&\#x27; attempting full Rust rewrites of curl — a project whose security-critical nature and decades-long maintenance history make it a high-stakes test case for language migration claims.

**「Impact」** Users and integrators relying on the canonical curl distribution benefit from continuous security and reliability updates during the Rust migration window—whereas Rust rewrites lack those fixes unless manually backported or independently maintained.

**Tags**: `#curl`, `#rust`, `#security`, `#software-engineering`, `#language-migration`

---

<a id="item-tech-news-14"></a>
### [External sandboxes for coding agents: three sandbox server implementations released](https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/) ⭐️ 7.0/10

Prime Radiant and Simon Willison introduced the &\#x27;external sandbox&\#x27; architectural pattern to isolate code execution by AI coding agents—running agent logic outside a dedicated, restricted environment where untrusted code executes. Three sandbox server implementations are now publicly available: external-sandbox-v86 \(Node.js + v86 WebAssembly-based Alpine Linux\), external-sandbox-container \(Python + Apple Containers\), and external-sandbox-quicksand \(Python + Microsoft Quicksand, bundling QEMU and Alpine Linux\). All expose a uniform localhost API and include optional network policy controls \(HTTP/HTTPS allow-listing\) and credential replacement for authenticated API calls, enabling integration with agents like Pi, Claude Code, or Codex.

rss · Simon Willison · Nov 17, 22:52

**「Background」** Sandboxing untrusted code—especially that generated or executed by AI coding agents—has long relied on containerization \(e.g., Docker\), virtual machines, or WebAssembly runtimes to enforce isolation. Prior approaches often embed the sandbox within the same process or host environment as the agent, increasing risk from escape vulnerabilities or misconfigurations.

**「Impact」** Developers integrating local LLM-based coding agents can now adopt prebuilt, API-compatible sandbox servers to mitigate risks from prompt injection or erroneous code execution—without implementing isolation from scratch—but must verify compatibility with their agent’s tool-calling infrastructure and runtime constraints \(e.g., WebAssembly support for v86, Apple Containers availability, or Quicksand’s Python-native QEMU dependency\).

**Tags**: `#AI safety`, `#code execution security`, `#coding agents`, `#sandboxing`, `#LLM tooling`

---

<a id="item-tech-news-15"></a>
### [US AI chip rules pause $480M ByteDance GPU loan for Malaysia data center](https://www.bloomberg.com/news/articles/2026-11-17/banks-pause-480-million-chip-loan-tied-to-china-s-bytedance) ⭐️ 7.0/10

Five banks have paused a $480 million loan arranged for Singapore-based cloud provider Aolani Cloud to finance ByteDance’s purchase of NVIDIA GPUs for a data center in Malaysia, citing compliance concerns with newly enacted U.S. AI chip export restrictions. The loan was led by DBS Group as the mandated lead arranger, and Aolani Cloud confirmed it is assessing the new rules with regulators and lenders to ensure compliance. No disbursement has occurred, and banks state the financing cannot advance until the regulatory implications are fully evaluated.

telegram · zaihuapd · Nov 18, 05:11

**「U.S. AI chip export controls tightened in November 2026」** The U.S. government recently updated its export control regulations governing advanced AI chips, specifically expanding restrictions on the sale and financing of high-end NVIDIA GPUs to entities operating in or connected with China, including through third-country data centers. These rules, announced on November 16, 2026, introduced new licensing requirements and compliance obligations for financial institutions involved in transactions supporting such hardware deployments.

**「Impact」** ByteDance’s planned deployment of advanced AI infrastructure in Malaysia is delayed, and Aolani Cloud faces uncertainty in fulfilling its financing commitment—potentially requiring restructuring of the deal or alternative sourcing if U.S.-origin GPUs remain restricted for this use case.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gate.com/news/detail/NVDA/bytedance-480m-loan-stalled-after-us-tightens-ai-chip-export-rules-25700410">ByteDance $480M Loan Stalled After US Tightens AI Chip Export ...</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#export controls`, `#cloud infrastructure`, `#semiconductor policy`, `#global supply chain`

---

<a id="item-tech-news-16"></a>
### [Anthropic launches beta Linked Billing for Claude API](https://thenextweb.com/news/anthropic-linked-billing-claude-api-customers-pay) ⭐️ 7.0/10

Anthropic has launched a beta version of Linked Billing for the Claude API, allowing direct-paying organizational customers to attribute API usage to their own Claude organization accounts, set monthly spending limits, and immediately unbind billing at any time. When billing fails—such as due to payment method issues—the API automatically rejects requests instead of falling back to the developer’s payment method. The feature is unavailable to customers billed via AWS Marketplace, Google Cloud, Azure, or those on subscription-only plans, and does not extend HIPAA or zero-data-retention guarantees to linked-billing traffic.

telegram · zaihuapd · Nov 18, 07:24

**「Background」** Prior to this release, Claude API customers had no native mechanism to delegate or attribute API usage costs to internal organizational accounts with enforceable spending controls; billing was tied directly to the individual or entity that provisioned the API key. Linked Billing introduces an explicit account-level delegation layer, distinct from cloud marketplace reselling or flat-rate subscriptions.

**「Impact」** Enterprise teams integrating the Claude API must now configure billing delegation before deploying production workloads if they require centralized cost tracking, budget enforcement, or fail-safe rejection on payment failure—otherwise, they risk unexpected charges falling to individual developers’ accounts.

**Tags**: `#AI APIs`, `#cloud billing`, `#enterprise AI`, `#Anthropic`, `#API operations`

---

<a id="item-tech-news-17"></a>
### [Nine Chinese ministries propose vehicle-battery integrated scrapping for EVs](https://wallstreetcn.com/articles/3786200) ⭐️ 7.0/10

China&\#x27;s Ministry of Commerce and eight other departments proposed on November 17, 2026, revisions to the &\#x27;Detailed Rules for the Implementation of the Measures for the Administration of Scrapping Motor Vehicle Recovery&\#x27; to mandate &\#x27;vehicle-battery integrated scrapping&\#x27; for new energy vehicles. The proposal includes establishing a digital ID system for traction batteries to track battery flow throughout the recycling chain, building on an April 2024 interim rule that already requires报废新能源汽车 \(scrapped NEVs\) missing their动力电池 to be classified as incomplete vehicles. The specific administrative regulations and implementation details remain under development.

telegram · zaihuapd · Nov 18, 12:22

**「Background」** The April 2024 interim rule under the &\#x27;Measures for the Implementation of the Administrative Measures on Recycling Scrapped Motor Vehicles&\#x27; first established that a new energy vehicle missing its traction battery at scrapping must be deemed incomplete. This earlier regulation laid the groundwork for battery accountability but did not mandate integrated scrapping or require digital traceability.

**Tags**: `#electric-vehicles`, `#battery-recycling`, `#regulatory-policy`, `#circular-economy`, `#supply-chain-transparency`

---

<a id="item-tech-news-18"></a>
### [DeepSeek makes server-side search and web crawling free](https://www.ithome.com/1/029/058.htm) ⭐️ 7.0/10

Starting November 18, 2026 at 12:00 Beijing time, DeepSeek eliminated separate per-request fees for its server-side search and web crawling functionality, charging users only for model token usage when these features are triggered via the联网 tool, Anthropic API&\#x27;s web\_search tool, or Responses API&\#x27;s web\_search tool. Previously, the standalone Search and Fetch APIs charged 5 RMB per 1,000 successful requests. The change applies to all users invoking those integrated search capabilities, but the announcement does not specify rate limits, latency guarantees, coverage scope, or data freshness constraints.

telegram · zaihuapd · Nov 18, 13:44

**「Pricing model evolution for DeepSeek&\#x27;s search and web fetch capabilities」** DeepSeek previously offered Search and Fetch APIs as separately billed services, charging 5 RMB per 1,000 successful requests. This usage-based pricing applied to server-side search and webpage fetching triggered by integrations such as the联网工具, Anthropic API’s web\_search tool, and Responses API’s web\_search tool.

**「Impact」** Developers building RAG, agentic systems, or real-time knowledge-augmented applications now face lower and more predictable costs—removing a fixed per-request charge simplifies budgeting and improves scalability for high-volume search-augmented inference.

**Tags**: `#AI-infrastructure`, `#RAG`, `#developer-tools`, `#LLM-ecosystem`, `#search-integration`

---

<a id="item-tech-news-19"></a>
### [Voyager 1 reaches one light-day from Earth after 49 years](https://www.cnn.com/2026/11/18/science/voyager-1-light-day) ⭐️ 7.0/10

Voyager 1 reached a distance of approximately 26 billion kilometers \(one light-day\) from Earth on November 18, 2026, at 5:16 a.m. ET—49 years after its 1977 launch. At this distance, one-way radio signal travel time is exactly 24 hours, and round-trip communication takes about two days. NASA confirmed continued two-way communication and recently reconfigured onboard power distribution to reduce consumption by ~10 watts, extending the mission’s operational lifetime by approximately 2.5 years. Only two scientific instruments remain active.

telegram · zaihuapd · Nov 18, 14:41

**「Background」** Launched by NASA on September 5, 1977, Voyager 1 is the farthest and fastest human-made object, having entered interstellar space in August 2012 after crossing the heliopause—the boundary where solar wind gives way to interstellar medium. Its longevity relies on radioisotope thermoelectric generators \(RTGs\), whose power output decays predictably, necessitating progressive instrument shutdowns since the early 2000s.

**「Impact」** NASA’s power reallocation extends Voyager 1’s science operations into the mid-2030s, preserving unique low-energy cosmic ray and plasma measurements from interstellar space—data unobtainable by any other current or planned mission.

**「Community Discussion」** No community comments were provided; therefore, no substantive discussion is available to summarize.

**Tags**: `#space-exploration`, `#embedded-systems`, `#communications`, `#power-management`, `#NASA`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [FlyDSL MonoKernels for Low-Latency LLM Decode on AMD GPUs](https://vllm.ai/blog/2026-11-18-flydsl-monokernels) ⭐️ 9.0/10

rss · vLLM Blog · Nov 18, 00:00

**「Background」** Interactive LLM agents demand ultra-low decode latency—each token generation sits on the critical path for tool calls and user responsiveness—and small-batch serving prioritizes per-user speed over aggregate throughput. Traditional GPU execution fragments decode into many small, dependent kernels \(e.g., projections, attention, MoE\), each incurring dispatch overhead, synchronization waits, and underutilized GPU capacity; HIP graphs reduce CPU launch cost but not GPU-side kernel boundaries or memory-traffic exposure.

**「Solution」** vLLM introduces FlyDSL MonoKernels: model-specific, manually scheduled GPU kernels that collapse multiple decode stages into persistent launches—reusing thread blocks across stages, prefetching weights during computation, and passing intermediate results via tagged mailboxes instead of full kernel handoffs. Boundaries are chosen per model \(e.g., DeepSeek-V4 splits into K1/K2; MiniMax-M3 fuses only FFN\) to respect data dependencies, TP communication patterns, and hardware limits like LDS size. FlyDSL enables fine-grained control over layouts, low-precision ops \(MXFP4, FP8\), and synchronization, with kernels compiled just-in-time for specific TP size, step width, and GPU architecture \(MI355X/MI325X\). Integrated opt-in via --monokernel, MonoKernels coexist with vLLM’s stock stack—preserving scheduling, KV cache, speculative decoding, and HIP graphs—while delivering 1.20×–2.26× concurrency-1 interactivity gains \(e.g., DeepSeek-V4.1-Flash jumps from 318.1 to 429.1 tok/s/user at TP2\) and verified accuracy within noise across benchmarks like GSM8K and GPQA-Diamond.

**「Takeaway」** Reducing decode latency for interactive agents is less about optimizing individual kernels and more about rethinking GPU execution boundaries—MonoKernels prove that author-controlled, model-specific fusion—enabled by FlyDSL’s low-level scheduling and memory primitives—delivers substantial, hardware-contextualized latency wins without sacrificing accuracy or integration fidelity.

**Tags**: `#LLM inference`, `#GPU kernel optimization`, `#vLLM`, `#FlyDSL`, `#interactive agents`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Waller Calls for 50-Basis-Point Rate Hike in December](https://www.cnbc.com/2026/11/18/federal-reserve-governor-christopher-waller.html) ⭐️ 8.0/10

Federal Reserve Governor Christopher Waller said a 50-basis-point interest rate hike is &\#x27;probably necessary&\#x27; at the December 8–9 FOMC meeting to counter persistently high and broadening inflation, contrasting with market expectations fully pricing in only a 25-basis-point increase.

rss · CNBC Finance · Nov 18, 15:13

**「Background」** The Fed had cut rates three times in 2025 as inflation appeared to moderate, but inflation reignited after U.S.- and Israel-led strikes on Iran in late February 2026 spiked energy prices and prolonged tariff effects, keeping inflation above 3%—well above the Fed’s 2% target.

**「Impact」** Waller’s public call increases the likelihood of a larger-than-expected December rate hike, which would raise borrowing costs for households and businesses more quickly and challenge market pricing that assumes gradual tightening.

**Tags**: `#monetary-policy`, `#inflation`, `#federal-reserve`

---

<a id="item-finance-news-2"></a>
### [JPMorgan and Hyundai Card test AI agents for autonomous FX transactions](https://www.cnbc.com/2026/11/18/jpmorgan-hyundai-card-ai-agents-payments.html) ⭐️ 7.0/10

JPMorgan and Hyundai Card completed a private blockchain-based proof-of-concept in which autonomous AI agents executed a simulated foreign exchange transaction for corporate treasury management; they aim to expand to multi-agent negotiation by the first half of 2027.

rss · CNBC Finance · Nov 18, 06:18

**「Background」** This trial used Kinexys—a JPMorgan blockchain platform—to enable a Hyundai Card AI agent to request an FX transaction into its blockchain deposit account, marking the first such autonomous bank-agent-to-client-agent test in corporate treasury.

**「Impact」** Corporate treasurers and financial institutions face new governance challenges—including accountability, spending limits, and cascading failure risks—as AI agents begin executing payments without human intervention.

**Tags**: `#AI finance`, `#banking innovation`, `#payments infrastructure`, `#corporate treasury`, `#financial regulation`

---

<a id="item-finance-news-3"></a>
### [UK Immigration and Asylum Bill Passes House of Commons](https://www.bloomberg.com/news/articles/2026-11-17/uk-s-house-of-commons-passes-controversial-immigration-bill) ⭐️ 7.0/10

The UK House of Commons passed the Immigration and Asylum Bill by 290 votes to 94, raising the standard residency requirement for settlement from 5 to 10 years—though healthcare and social care workers earning at least £25,000 annually retain the 5-year path.

telegram · zaihuapd · Nov 18, 05:51

**「Background」** The bill follows years of political pressure to reduce net migration and reform a system widely seen as slow and inconsistent, especially in processing asylum claims and appeals.

**Tags**: `#immigration-policy`, `#UK-economy`, `#labor-markets`, `#public-policy`, `#healthcare-workforce`

---

<a id="item-finance-news-4"></a>
### [China and South Korea Conclude FTA Expansion Talks on Services and Investment](https://x.com/Jaemyung_Lee/status/2122988472994791476) ⭐️ 7.0/10

China and South Korea announced on 18 November 2026 the substantive conclusion of eight years and eight months of follow-up negotiations to expand their free trade agreement into services and investment, with China committing to grant South Korea most-favored-nation \(MFN\) treatment in film and video games, and to broaden audiovisual co-production to include TV dramas, animation, variety shows, and documentaries.

telegram · zaihuapd · Nov 18, 10:02

**「Background」** The original China–South Korea Free Trade Agreement entered into force in 2015, and follow-up talks on services and investment began in March 2018 to deepen market access beyond goods trade.

**「Impact」** Korean entertainment, finance, legal, construction, and tourism firms will gain improved market access in China, including equal treatment with third-country firms in film and game distribution and broader co-production rights.

**Tags**: `#trade-policy`, `#Korea`, `#China`, `#media-industry`, `#FTA`

---