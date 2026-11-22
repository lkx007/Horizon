---
layout: default
title: "Horizon Summary: 2026-11-23 (EN)"
date: 2026-11-23
lang: en
---

> From 27 items, 13 important content pieces were selected

---

**Technology News**
1. [Silicon Valley’s Shift from Information Navigation to AI-Driven Growth](#item-tech-news-1) ⭐️ 7.0/10
2. [Perplexity as a Metric for AI Intelligence](#item-tech-news-2) ⭐️ 7.0/10
3. [Game lets players act as an LLM&\#x27;s subagent in browser](#item-tech-news-3) ⭐️ 7.0/10
4. [Anthropic&\#x27;s 2028 data center power mix projected at 87% gas, 11% coal](#item-tech-news-4) ⭐️ 7.0/10
5. [Muru: AI-assisted Rust server for Python ASGI/WSGI apps by mod\_wsgi creator](#item-tech-news-5) ⭐️ 7.0/10
6. [Tesla begins global rollout of Full Self-Driving v15](#item-tech-news-6) ⭐️ 7.0/10
7. [Google Gemini adds separate toggle to disable training data use while keeping chat history](#item-tech-news-7) ⭐️ 7.0/10
8. [Phison launches Pascari Space SSD series with 488 TB for StarVault-001 orbital data center](#item-tech-news-8) ⭐️ 7.0/10

**Technology Blog**
1. [To Code Well, Avoid Blunders](#item-tech-blog-1) ⭐️ 8.0/10

**Financial News**
1. [Robot Startup Foundation Future Industries Cuts Health Benefits Amid Cash Crunch](#item-finance-news-1) ⭐️ 7.0/10
2. [FT Alleges Cambodian Group Smuggled $4.6B in NVIDIA Chips to China](#item-finance-news-2) ⭐️ 7.0/10
3. [US Tech Stocks Plunge, Asia Enacts Market Stabilization Measures](#item-finance-news-3) ⭐️ 7.0/10
4. [Record Super El Niño Strains Global Food Aid](#item-finance-news-4) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Silicon Valley’s Shift from Information Navigation to AI-Driven Growth](https://www.oreilly.com/radar/what-happened-to-silicon-valley/) ⭐️ 7.0/10

The essay traces Silicon Valley’s strategic evolution—from post-dotcom-bust focus on information navigation and network effects, through Web 2.0 and ZIRP-fueled expansion, to today’s AI-centric growth-at-all-costs paradigm. It argues that underlying economic assumptions \(e.g., shareholder-value maximization\) and design choices \(e.g., attention-harvesting architectures\) have increasingly subordinated human flourishing and technical sustainability to short-term scale and valuation metrics. The piece does not announce a product, policy, or technical change but offers a historically grounded critique of industry-wide priorities and incentives. It explicitly references Tim O’Reilly’s 2005 &\#x27;What Is Web 2.0?&\#x27; essay and Herbert Simon’s 1971 observation about attention scarcity as foundational reference points.

hackernews · greenyouse · Nov 22, 19:20 · [Discussion](https://news.ycombinator.com/item?id=50602947)

**「Historical shift from Web 2.0 to AI-driven growth」** The essay builds on the author’s 2005 foundational definition of Web 2.0—as a response to post-dotcom-bust information abundance and attention scarcity—and traces how that framework evolved under zero-interest-rate policy \(ZIRP\) conditions, enabling scale-at-all-costs strategies. It positions today’s AI-centric tech strategy not as a technical discontinuity but as an intensification of earlier economic and design logics, particularly the optimization of shareholder value over user or societal outcomes.

**「Impact」** Developers and product leaders face heightened tension between building robust, user-centered systems and complying with AI-driven KPIs \(e.g., engagement velocity, model training scale\) that incentivize feature bloat, data harvesting, and opaque automation—raising concrete risks to maintainability, auditability, and long-term trust.

**「Community Discussion」** Commenters diverge on root causes: \[Animats\] attributes the crisis to unaccountable &\#x27;mechanism designers&\#x27; optimizing capitalism itself, while \[CoolestBeans\] emphasizes the ZIRP era as the proximate enabler of unsustainable scale and AI-driven cannibalization of core competencies; neither view is presented as empirically settled in the comments.

**Tags**: `#technology-industry`, `#capitalism-and-tech`, `#AI-strategy`, `#Web-2.0`, `#attention-economy`

---

<a id="item-tech-news-2"></a>
### [Perplexity as a Metric for AI Intelligence](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 7.0/10

An unverifiable article titled &\#x27;Perplexity and Intelligence&\#x27;—cited on Hacker News but inaccessible at the claimed OpenAI URL \(404\)—proposes perplexity as an underutilized, meaningful metric for assessing AI intelligence. The piece prompted expert-level discussion about perplexity’s definition, limitations, and relevance amid evolving evaluation paradigms like RLHF versus cross-entropy loss. Community comments clarify that perplexity quantifies model surprise in next-token prediction \(range: 1 to vocabulary size\), but note the article fails to specify the data or task domain for its reported perplexity values. No shipped tool, versioned implementation, benchmark release, or empirical result is described or verifiable in the available evidence.

hackernews · acossta · Nov 22, 17:06 · [Discussion](https://news.ycombinator.com/item?id=50601525)

**「What perplexity measures in language modeling」** Perplexity is a standard information-theoretic metric derived from cross-entropy loss, quantifying how well a language model predicts a sequence of tokens: it equals 2 raised to the power of the model’s average cross-entropy per token \(in bits\) over a test corpus. Lower perplexity indicates better predictive performance, with a value of 1 representing perfect prediction and values approaching the vocabulary size indicating near-random guessing. It has long been used to evaluate language models during pretraining, though its relevance has been questioned as post-training alignment methods like RLHF shift behavior away from pure next-token prediction.

**「Community Discussion」** Commenters debate whether perplexity meaningfully reflects intelligence: one notes it&\#x27;s only interpretable relative to a specific dataset or task \(&\#x27;perplexity on what?&\#x27;\), while another expresses skepticism about claims of ability &\#x27;emergence&\#x27; at threshold perplexity values, citing task-specialized smaller models with high general perplexity. These disagreements highlight unresolved tensions in evaluation rigor and interpretability, not consensus.

<details><summary>References</summary>
<ul>
<li><a href="https://en.m.wikipedia.org/wiki/Perplexity">Perplexity - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI evaluation`, `#language modeling`, `#perplexity`, `#benchmarking`, `#Hacker News`

---

<a id="item-tech-news-3"></a>
### [Game lets players act as an LLM&\#x27;s subagent in browser](https://github.com/gulivan/worker755) ⭐️ 7.0/10

Worker755 is an open-source, browser-based game where players assume the role of a subagent under an LLM &\#x27;manager&\#x27;, executing terminal-style commands \(e.g., ls, cat, rm -rf\) to complete tasks while observing how the LLM delegates, interprets, and reacts to their actions. The game runs entirely client-side with no backend or external API calls; the LLM manager logic is implemented via deterministic JavaScript rules—not a live language model. It is available at https://github.com/gulivan/worker755 and requires no installation beyond opening the HTML file in a modern browser.

hackernews · ivantgam · Nov 22, 13:56 · [Discussion](https://news.ycombinator.com/item?id=50599762)

**「Background」** The concept of &\#x27;subagents&\#x27; arises in hierarchical AI agent designs—where a top-level LLM delegates work to specialized subagents \(e.g., for file I/O, web search, or code execution\)—a pattern explored in frameworks like LangChain and AutoGen. Worker755 simplifies and dramatizes this architecture for pedagogical purposes, turning delegation dynamics into an interactive, rule-based simulation rather than relying on actual LLM inference.

**「Impact」** Developers and educators gain a tangible, low-barrier tool to explore prompt engineering trade-offs, delegation failures, and the brittleness of instruction-following—e.g., issuing &\#x27;rm -rf /&\#x27; triggers a scripted safety response, illustrating how real-world agent systems might enforce constraints.

**「Community discussion」** Commenters highlight both playful engagement \(e.g., testing destructive commands\) and conceptual friction—Seb0927 notes the manager overly prescribes steps rather than allowing autonomous problem-solving, while boricj expresses disappointment that the simulation does not support local LLM integration.

**Tags**: `#AI agents`, `#LLM architecture`, `#interactive learning`, `#AI safety`, `#prompt engineering`

---

<a id="item-tech-news-4"></a>
### [Anthropic&\#x27;s 2028 data center power mix projected at 87% gas, 11% coal](https://betterdatacenterproject.com/2026/11/16/how-ai-is-powered-a-breakdown-of-byop-and-grid-power/) ⭐️ 7.0/10

Anthropic’s projected 2028 data center electricity supply is estimated to consist of 87% natural gas and 11% coal, with only 2% from renewable sources. This projection reflects the company’s current infrastructure commitments and grid procurement strategy in the United States, not a voluntary or contractual clean energy target. The figures are cited as forward-looking estimates from an analysis published on November 16, 2026, and do not represent a formal corporate disclosure or binding pledge. No evidence is provided that Anthropic has announced plans to shift this mix before 2028.

hackernews · happosai · Nov 22, 08:57 · [Discussion](https://news.ycombinator.com/item?id=50597612)

**「Background」** Anthropic’s Colossus 1 data center, located in South Memphis, Tennessee, began operations in 2024 after construction started at a repurposed Electrolux plant; it relies on temporary gas turbines and draws power from the regional grid, which is heavily fossil-fueled. The broader Colossus infrastructure—sometimes conflated with xAI’s similarly named facilities—is central to Anthropic’s compute scaling, and its local environmental impact \(e.g., air pollution in Memphis\) has drawn community criticism and regulatory scrutiny.

**「Impact」** Developers and organizations relying on Anthropic’s AI services may face growing reputational and compliance risks as regulatory scrutiny intensifies around AI-related emissions—especially given the absence of public US-based renewable energy commitments from Anthropic, unlike peers such as Alphabet.

**「Community discussion」** Commenters criticize Anthropic for leasing the Colossus 1 data center in Memphis amid documented local air pollution and for lacking US renewable energy commitments, contrasting it with Alphabet’s more robust sustainability efforts; others argue the issue underscores the need for binding regulation to internalize environmental externalities.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Colossus_%28data_center%29">Colossus ( data center ) - Wikipedia</a></li>
<li><a href="https://www.scientificamerican.com/article/spacexais-colossus-data-center-is-fueling-a-massive-backlash/">SpaceXAI’s Colossus data center is fueling... | Scientific American</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#sustainable computing`, `#energy policy`, `#corporate accountability`

---

<a id="item-tech-news-5"></a>
### [Muru: AI-assisted Rust server for Python ASGI/WSGI apps by mod\_wsgi creator](https://simonwillison.net/2026/Nov/21/muru/) ⭐️ 7.0/10

Graham Dumpleton, creator of mod\_wsgi, has released Muru — an early-stage, open-source Rust-based server for Python ASGI and WSGI applications, designed for both development and production use. Announced in November 2026, Muru incorporates AI-assisted operational features \(e.g., automated canary deployments, scaling decisions, and in-browser debugging toolbars\) and emphasizes deep integration with modern infrastructure like Kubernetes and containers. The project is actively documented in a public blog series spanning 19 posts from November 4–22, 2026, but no stable release, version number, or public package distribution \(e.g., PyPI or crates.io\) is mentioned in the source. It remains unreleased as production software and lacks independently verified performance or compatibility claims.

rss · Simon Willison · Nov 21, 23:56

**「Background」** mod\_wsgi, created by Graham Dumpleton two decades ago, remains a foundational WSGI server for deploying Python web applications in production, especially with Apache. Its design prioritized stability and integration over modern concurrency models, leaving a gap for a next-generation server that natively supports both WSGI and ASGI while incorporating observability, dynamic scaling, and container-native operation—capabilities Muru explicitly aims to deliver.

**Tags**: `#Python`, `#Rust`, `#Web Servers`, `#ASGI`, `#Systems Engineering`

---

<a id="item-tech-news-6"></a>
### [Tesla begins global rollout of Full Self-Driving v15](https://x.com/Tesla/status/2124222447855743019) ⭐️ 7.0/10

Tesla has begun a global over-the-air rollout of Full Self-Driving \(FSD\) software version 15, available to eligible customers with FSD subscriptions or purchases. The update includes a claimed 25× improvement in handling safety-critical scenarios, introduces the &\#x27;Tesla Reality View&\#x27; augmented-reality interface that overlays planning visualizations onto live camera feeds in full-screen, map, or split-screen modes, and adds refined driving behaviors—including adaptive speed control in school zones and adverse weather, improved handling of potholes and road debris, and quieter, fading turn-signal audio cues. The update is shipped and actively being deployed, not merely announced or in limited beta.

telegram · zaihuapd · Nov 22, 00:03

**「Background」** Tesla&\#x27;s Full Self-Driving \(FSD\) software is a supervised autonomous driving system requiring driver attention and continuous input; it is not SAE Level 4 or 5 autonomy. FSD v12, released in late 2023, marked Tesla&\#x27;s shift to an end-to-end neural network architecture, replacing modular components with a single vision-language-action transformer model.

**「Impact」** Owners of Tesla vehicles with active FSD subscriptions or purchases will experience immediate changes to vehicle behavior and UI during driving, including new visual feedback on the center display and altered speed modulation in weather- or location-sensitive conditions—requiring drivers to reacquaint themselves with system responses and maintain appropriate supervision per regulatory requirements and Tesla’s own operational design domain limitations.

**Tags**: `#autonomous-driving`, `#AI-systems`, `#human-computer-interface`, `#real-time-systems`

---

<a id="item-tech-news-7"></a>
### [Google Gemini adds separate toggle to disable training data use while keeping chat history](https://blog.google/innovation-and-ai/products/gemini-app/updated-controls/) ⭐️ 7.0/10

Starting in the coming weeks, Google Gemini will replace its single &\#x27;Keep activity&\#x27; setting with two independent controls: one governing how long chat history is retained \(defaulting to approximately two months\), and another specifically determining whether text conversations and attachments are used to train Google&\#x27;s generative AI models. Users can now retain their chat history while opting out of model training entirely. Audio inputs and Gemini Live sessions remain excluded from training by default, and the new settings will initially mirror the prior state of the original toggle.

telegram · zaihuapd · Nov 22, 01:24

**「Background」** Previously, Gemini’s privacy controls used a single &\#x27;Keep activity&\#x27; switch that simultaneously governed both chat history retention and the use of those interactions for model improvement—offering no way to separate the two functions. This all-or-nothing design conflicted with privacy regulations like GDPR and user expectations for granular consent over AI training data.

**「Impact」** Developers integrating Gemini APIs or building on Google’s AI infrastructure must now account for users’ explicit opt-out from training data collection—even when chat history remains enabled—which affects how they design consent flows, audit logs, and data handling compliance documentation.

**Tags**: `#AI ethics`, `#privacy engineering`, `#LLM deployment`, `#user consent`

---

<a id="item-tech-news-8"></a>
### [Phison launches Pascari Space SSD series with 488 TB for StarVault-001 orbital data center](https://videocardz.com/newz/phison-announces-488tb-of-ssd-storage-for-space-data-centers-pricing-expected-to-be-astronomical) ⭐️ 7.0/10

Phison has launched the Pascari Space SSD series, specifically engineered for space environments, including radiation hardening and pSLC endurance enhancements of up to 60×. A 488 TB configuration—comprising multiple drives—is confirmed for Lonestar Data Holdings’ StarVault-001 orbital data center, scheduled for launch in early 2027; usable capacity in low Earth orbit is estimated at ~370 TB. The series includes three variants \(Flight Critical, Main Storage, Orbital Data Center\), with individual drive capacities up to 128 TB, and the product line is commercially available now.

telegram · zaihuapd · Nov 22, 10:31

**「Background」** Phison&\#x27;s Pascari line was previously introduced as an enterprise SSD series optimized for high-write-intensity workloads, with no initial space-specific design. The newly announced Pascari Space SSD series represents a radiation-hardened, pSLC-enhanced adaptation of that platform—distinct from the earlier lunar mission \(tool-1-2\), which used non-space-rated Pascari SSDs on a one-off Falcon 9 payload without orbital data center integration.

**「Impact」** Organizations developing orbital infrastructure—particularly Lonestar for StarVault-001—now have a commercially available, space-qualified SSD option enabling on-orbit data storage and processing, reducing reliance on downlink-limited architectures for AI/ML and edge computing workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://www.phisonenterprise.com/">PASCARI by Phison : Redefining Enterprise Data Storage</a></li>
<li><a href="https://www.tweaktown.com/news/103564/phisons-new-pascari-enterprise-grade-ssd-launches-on-rocket-lands-the-moon-march-4/index.html">Phison &#x27;s new Pascari enterprise-grade SSD launches on a rocket...</a></li>

</ul>
</details>

**Tags**: `#space computing`, `#SSD`, `#edge AI`, `#hardware reliability`, `#orbital infrastructure`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [To Code Well, Avoid Blunders](https://seangoedecke.com/to-code-well-avoid-blunders/) ⭐️ 8.0/10

rss · Sean Goedecke · Nov 22, 00:00

**「Background」** In large commercial codebases, sustainable code quality depends less on brilliance and more on rigorously avoiding catastrophic blunders—especially those that break consistency or bloat requirements. Engineers often misprioritize clever abstractions over disciplined restraint, but the author argues this is a fundamental misconception rooted in how software failures compound uniquely.

**「Solution」** The core insight is that avoiding blunders—not optimizing for elegance or novelty—is the dominant lever for durable code quality. Key blunders include introducing parallel systems, dual sources of truth, unsafe async conversions, new failure points, or overcomplicated interfaces; all stem from inconsistency or unnecessary requirements. Unnecessary requirements are especially dangerous because they persist \(due to context loss\) and interact combinatorially, rapidly increasing cognitive load and risk. The author prescribes two concrete habits: first, fitting new work into the most normal, established pattern in the codebase; second, ruthlessly trimming each task to its minimal viable requirement set. Cleverness is treated as a warning sign—not an asset—because it diverts attention from consistency and simplicity. This approach applies equally to human-written and AI-assisted code.

**「Takeaway」** Great programming in large-scale systems is defined not by intellectual flair but by disciplined avoidance of consistency-breaking and requirement-bloated blunders—because in software, one such mistake can irreversibly degrade maintainability, while flawless execution compounds advantage reliably.

**Tags**: `#software-engineering`, `#code-quality`, `#system-design`, `#engineering-culture`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Robot Startup Foundation Future Industries Cuts Health Benefits Amid Cash Crunch](https://www.cnbc.com/2026/11/22/foundation-future-industries-health-benefits-payroll-base-group.html) ⭐️ 7.0/10

Foundation Future Industries terminated employee health benefits retroactive to October 2026 after missing payroll since October, and is offering COBRA coverage while promising reimbursement; the company is seeking a bridge loan ahead of an uncertain $150 million investment from South Korea’s Base Group.

rss · CNBC Finance · Nov 22, 18:55

**「Background」** Foundation Future Industries is a humanoid robot startup co-founded by Sankaet Pathak—whose prior startup collapsed in 2024—and backed by Eric Trump, who holds the title of chief strategy advisor; the company has missed payroll since October and taken a $4.6 million loan from itself in 2025.

**Tags**: `#startup-failure`, `#employee-compensation`, `#corporate-governance`, `#venture-capital`, `#health-benefits`

---

<a id="item-finance-news-2"></a>
### [FT Alleges Cambodian Group Smuggled $4.6B in NVIDIA Chips to China](https://www.ft.com/content/f3ad8a81-3890-4a8a-8853-ff0a94b08ba9?syn-25a6b1a6=1) ⭐️ 7.0/10

The Financial Times reported that individuals linked to Cambodia’s Prince Group allegedly smuggled NVIDIA AI chips into China using shell companies and private aircraft, citing $4.6 billion in related imports by its Malaysian subsidiary Megaspeed between December 2024 and December 2025; the Prince Group denies the allegations.

telegram · zaihuapd · Nov 22, 04:34

**「Background」** The US Treasury has sanctioned the Prince Group for ties to illicit finance, and US export controls prohibit the sale of advanced AI chips like NVIDIA’s A100 and H100 to China without a license.

**Tags**: `#semiconductors`, `#export-controls`, `#US-China-technology-rivalry`

---

<a id="item-finance-news-3"></a>
### [US Tech Stocks Plunge, Asia Enacts Market Stabilization Measures](https://news.bjd.com.cn/2026/11/22/12039852.shtml) ⭐️ 7.0/10

US tech stocks plunged on Friday, with the Nasdaq falling 5.28% and the Philadelphia Semiconductor Index dropping nearly 11%; in response, mainland China, South Korea, and Taiwan introduced coordinated regulatory measures including margin adjustments, short-selling restrictions, and buyback rule changes effective November 23–24, 2026.

telegram · zaihuapd · Nov 22, 13:24

**「Background」** The sell-off followed a sharp reversal in AI-related tech valuations, prompting Asian regulators to act swiftly to prevent contagion and maintain market stability.

**「Impact」** These interventions directly affect retail and institutional investors across Asia by tightening credit for stock trading, limiting speculative short positions, and increasing liquidity support mechanisms.

**Tags**: `#US stock market`, `#Asian financial regulation`, `#tech sector volatility`, `#short-selling policy`, `#market intervention`

---

<a id="item-finance-news-4"></a>
### [Record Super El Niño Strains Global Food Aid](https://www.wired.com/story/how-this-years-super-el-nino-will-worsen-global-hunger/) ⭐️ 7.0/10

A super El Niño has raised sea surface temperatures in the central tropical Pacific to 3.5°C above normal as of October—breaking the prior record of ~2.75°C—and is forecast to peak near 4°C in early winter; the World Food Programme warns it could push an additional 49 million people into acute food insecurity by the end of 2027.

telegram · zaihuapd · Nov 22, 14:09

**「Background」** El Niño is a natural climate pattern that warms the central and eastern tropical Pacific, disrupting global weather and often reducing crop yields in vulnerable regions.

**「Impact」** With global food aid funding down 30% since 2022, the WFP’s capacity to respond has sharply declined—e.g., its coverage in Somalia dropped from 10 million to under 1 million people during similar drought conditions.

**Tags**: `#climate-risk`, `#food-security`, `#humanitarian-aid`, `#macroeconomic-impact`, `#El-Nino`

---