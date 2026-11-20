---
layout: default
title: "Horizon Summary: 2026-11-21 (EN)"
date: 2026-11-21
lang: en
---

> From 36 items, 22 important content pieces were selected

---

**Technology News**
1. [OpenSSL EVP\_EncodeBlock buffer overflow CVE-2026-121481 \(CVSS 9.8\)](#item-tech-news-1) ⭐️ 9.0/10
2. [PHP HTTP/FTP stream wrapper silently disables TLS for httpS://](#item-tech-news-2) ⭐️ 9.0/10
3. [Meta&\#x27;s AI Agent Muse Leaks Cross-Account Financial and Messaging Data](#item-tech-news-3) ⭐️ 9.0/10
4. [KVM CVE-2026-99312 lets VMs read host memory on AMD systems with nested virtualization](#item-tech-news-4) ⭐️ 9.0/10
5. [FFmpeg 9.1 &\#x27;Gauss&\#x27; adds ASTC, Vulkan APV encoder, LCEVC, graph-based bitstream filtering](#item-tech-news-5) ⭐️ 8.0/10
6. [PostgreSQL 19 Adds Built-In REPACK CONCURRENTLY for Table Bloat Cleanup](#item-tech-news-6) ⭐️ 8.0/10
7. [Frostbite: AI-synthesized CPU architecture based on interaction nets](#item-tech-news-7) ⭐️ 7.0/10
8. [Essay critiques AI&\#x27;s industrialization of knowledge work and authorship](#item-tech-news-8) ⭐️ 7.0/10
9. [Signal Addresses AI App Data Exfiltration Risks on Mobile](#item-tech-news-9) ⭐️ 7.0/10
10. [ChatPRD halts free trials due to token fraud abuse](#item-tech-news-10) ⭐️ 7.0/10
11. [Gemini gains macOS computer control for US paid subscribers](#item-tech-news-11) ⭐️ 7.0/10
12. [UK tribunal rules Apple wins, orders public hearing on government&\#x27;s iPhone encryption bypass demand](#item-tech-news-12) ⭐️ 7.0/10
13. [US approved nearly 880,000 AI chips for export to China between late 2025 and mid-2026](#item-tech-news-13) ⭐️ 7.0/10
14. [TikTok Launches Globally Available AI Deepfake Detection Tool](#item-tech-news-14) ⭐️ 7.0/10
15. [Apple developing in-house AI agent for code, browsing, and app control, targeting late 2027](#item-tech-news-15) ⭐️ 7.0/10
16. [OpenAI launches experimental background mode for async LLM requests](#item-tech-news-16) ⭐️ 7.0/10
17. [Yu Chengdong Clarifies Huawei Xiangjie V8 Is L2, Not L3: Drivers Must Stay Alert](#item-tech-news-17) ⭐️ 7.0/10

**Financial News**
1. [Warsh’s No-Forward-Guidance Stance Spurs Unusual Surge in Fed Official Speeches](#item-finance-news-1) ⭐️ 7.0/10
2. [U.S. Corporations Shift from Buybacks to Net Equity Issuance](#item-finance-news-2) ⭐️ 7.0/10
3. [U.S.-China Talks at APEC Yield No Tariff or Tech Policy Breakthroughs](#item-finance-news-3) ⭐️ 7.0/10
4. [Ford Enters Battery Manufacturing Using CATL&\#x27;s LFP Technology](#item-finance-news-4) ⭐️ 7.0/10
5. [Beijing Proposes Ban on Security Deposit Deductions for Normal Wear and Tear](#item-finance-news-5) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [OpenSSL EVP\_EncodeBlock buffer overflow CVE-2026-121481 \(CVSS 9.8\)](https://github.com/openssl/openssl/pull/33652) ⭐️ 9.0/10

A critical buffer overflow vulnerability \(CVE-2026-121481, CVSS 9.8\) has been patched in OpenSSL’s EVP\_EncodeBlock\(\) function, which performs base64 encoding. The flaw triggers when input exceeds approximately 1.5 GB, causing a buffer overflow due to unchecked size calculations and lack of output buffer length validation. It affects all versions of OpenSSL that include the vulnerable implementation; the fix is available in pull request \#33652 on GitHub. Exploitation requires untrusted data to be passed directly to EVP\_EncodeBlock\(\) without prior size validation—common in services that perform base64 encoding on large, externally supplied payloads.

hackernews · JacobHenner · Nov 20, 02:01 · [Discussion](https://news.ycombinator.com/item?id=50569226)

**「Background」** EVP\_EncodeBlock\(\) is a standalone OpenSSL function for base64 encoding that does not use an encoding context and requires the caller to pre-allocate the output buffer based on a manual size calculation. Unlike context-based encoding functions \(e.g., EVP\_EncodeInit/EVP\_EncodeFinal\), it accepts only input data and its length, with no built-in bounds checking on the output buffer size.

**「Impact」** Services that accept untrusted binary data, load it entirely into memory, and pass it directly to EVP\_EncodeBlock\(\)—such as certain API gateways, email attachment processors, or custom base64 encoding endpoints—are at risk of remote code execution or denial of service; developers must update OpenSSL and audit call sites to validate input size or switch to safer alternatives like EVP\_EncodeUpdate\(\).

**「Community discussion」** Commenters debate exploit severity: \[amluto\] notes the API’s inherent fragility due to caller-managed buffer sizing, while \[userbinator\] argues the CVSS 9.8 score is inflated because exploitation depends on uncommon service configurations involving untrusted, oversized inputs; \[Panzerschrek\] adds that practical triggering is unlikely on modern 64-bit systems due to address space constraints.

<details><summary>References</summary>
<ul>
<li><a href="https://stackoverflow.com/questions/73790273/openssl-evp-aes-encryption-and-base64-encoding-producing-unusable-results">c - OpenSSL EVP AES Encryption and Base64... - Stack Overflow</a></li>

</ul>
</details>

**Tags**: `#security`, `#openssl`, `#cve`, `#buffer-overflow`, `#crypto-libraries`

---

<a id="item-tech-news-2"></a>
### [PHP HTTP/FTP stream wrapper silently disables TLS for httpS://](https://x.com/ljachowicz/status/2123477025268924514) ⭐️ 9.0/10

PHP&\#x27;s HTTP and FTP stream wrappers parse URL schemes case-insensitively but only enable TLS when the fifth character is a lowercase &\#x27;s&\#x27;, causing &\#x27;httpS://&\#x27;, &\#x27;HTTPS://&\#x27;, and &\#x27;FTPS://&\#x27; to silently fall back to plaintext HTTP or FTP. This vulnerability, present for 20 years and assigned CVE-2026-128064 \(GHSA-f6gg-rchx-xw8j\) with CVSS 8.2, exposes authentication tokens, cookies, POST data, and FTP credentials. It is fixed in PHP 8.2.36, 8.3.37, 8.4.28, 8.5.13, and 8.6.0; no patches are available for end-of-life versions \(8.1 and earlier\).

telegram · zaihuapd · Nov 20, 03:04

**「PHP stream wrapper scheme handling」** PHP&\#x27;s HTTP and FTP stream wrappers parse URL schemes case-insensitively but activate TLS only when the fifth character is a lowercase &\#x27;s&\#x27;—so &\#x27;httpS://&\#x27; or &\#x27;FTPS://&\#x27; matches the scheme name but fails the TLS activation check, resulting in plaintext transmission. This behavior has existed since at least PHP 5.0, when the stream wrapper infrastructure was introduced and standardized around case-insensitive scheme registration.

**「Impact」** Applications using PHP versions prior to 8.2.36, 8.3.37, 8.4.28, or 8.5.13 that construct or accept URLs with mixed-case schemes \(e.g., &\#x27;httpS://&\#x27;\) will silently transmit sensitive data—including HTTP Basic auth credentials, cookies, POST bodies, and FTP login details—over unencrypted HTTP or FTP, exposing them to network eavesdropping.

<details><summary>References</summary>
<ul>
<li><a href="https://app.opencve.io/cve/CVE-2026-128064">CVE-2026-128064 - Vulnerability Details - OpenCVE</a></li>
<li><a href="https://cvetodo.com/cve/CVE-2026-128064">CVE-2026-128064: PHP Vulnerability (CVSS 8.2) | CVETodo</a></li>
<li><a href="https://cve.now/CVE-2026-128064">CVE-2026-128064: PHP data exposure in stream wrappers (high)</a></li>

</ul>
</details>

**Tags**: `#PHP`, `#security`, `#TLS`, `#vulnerability`, `#web-security`

---

<a id="item-tech-news-3"></a>
### [Meta&\#x27;s AI Agent Muse Leaks Cross-Account Financial and Messaging Data](https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/) ⭐️ 9.0/10

Meta&\#x27;s production AI agent Muse is leaking private user data across accounts, including bank balances from Capital One and Charles Schwab, and unauthorized Signal message alerts—despite no user consent to access third-party apps. Internal Meta employees reported seeing others&\#x27; unrequested financial data and personal messages in their own Muse conversations, with concrete examples showing balances like &\#x27;$2722.58&\#x27; and &\#x27;$5899.57&\#x27; appearing in unrelated weather chats. The issue reflects a failure of data isolation in Muse’s architecture, not a theoretical or beta-stage problem, but an active, confirmed production incident. No patch, mitigation timeline, or official statement from Meta is reported.

telegram · zaihuapd · Nov 20, 05:10

**「What is Muse?」** Muse is Meta&\#x27;s personal AI agent, announced on September 8, 2026, designed to perform long-running, proactive tasks across apps and services—not just answer single-turn queries like a chatbot. It runs on a dedicated &\#x27;Muse Secure VM&\#x27; virtual machine intended to isolate user data and ensure privacy by housing both the agent and personal data within that secure environment.

**「Impact」** Affected users risk unauthorized exposure of sensitive financial data \(e.g., real-time bank balances\) and third-party messaging activity \(e.g., Signal notifications\) due to Muse’s failure to isolate conversations across accounts; Meta’s stated privacy controls—including app permission management and &\#x27;forget&\#x27; commands—do not prevent this cross-account leakage, as confirmed by internal employee reports and TechCrunch.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Muse_%28AI_agent%29">Muse (AI agent) - Wikipedia</a></li>
<li><a href="https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/">Introducing Muse: The World’s First Personal AI Agent Built ...</a></li>
<li><a href="https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/">Meta ’s AI agent Muse is mixing up conversations and... | TechCrunch</a></li>
<li><a href="https://www.itechguides.com/how-to-manage-privacy-and-data-settings-in-meta-muse/">Meta Muse Privacy Settings: Training, App Access &amp; Data</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#privacy engineering`, `#LLM agents`, `#data isolation`, `#Meta`

---

<a id="item-tech-news-4"></a>
### [KVM CVE-2026-99312 lets VMs read host memory on AMD systems with nested virtualization](https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html) ⭐️ 9.0/10

A critical KVM vulnerability, CVE-2026-99312, enables guest virtual machines to read host physical memory on AMD-based systems where nested virtualization is enabled. The flaw was demonstrated on DigitalOcean infrastructure, where a VM successfully read approximately 127 GB of host memory. An upstream fix shipped in Linux kernel stable release 7.3.5 on November 18, 2026, but major distributions including Debian and Ubuntu have not yet incorporated the patch. Until patched, disabling nested virtualization mitigates the issue.

telegram · zaihuapd · Nov 20, 14:23

**「Background」** KVM \(Kernel-based Virtual Machine\) is the Linux kernel&\#x27;s built-in virtualization infrastructure, enabling guest VMs to run on top of a host OS. Nested virtualization—a feature allowing VMs to themselves act as hypervisors—requires specific CPU and kernel support and is commonly used in cloud environments for development, testing, and container orchestration platforms.

**「Impact」** Cloud providers and infrastructure operators using AMD-based KVM hosts with nested virtualization enabled risk guest VMs reading up to 127 GB of host physical memory—including data from other tenants—as demonstrated on DigitalOcean; mitigation requires either upgrading to Linux kernel 7.3.5 or disabling nested virtualization until distribution-specific patches are deployed.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html">Linux KVM Flaw CVE-2026-99312 Lets Guest VMs Access Host ...</a></li>
<li><a href="https://runtimewire.com/article/terra-security-found-a-kvm-escape-that-read-127-gb-of-a-digitalocean-host">Terra Security found a KVM escape that read 127 GB of a ...</a></li>
<li><a href="https://hify.ai/radar/en/kvm-vm-escape-on-digitalocean-read-127-gb-of-host-ram">CVE-2026-99312: KVM guest-to-host escape read… | HIFY Radar</a></li>

</ul>
</details>

**Tags**: `#virtualization`, `#security`, `#linux-kernel`, `#cloud-infrastructure`, `#amd`

---

<a id="item-tech-news-5"></a>
### [FFmpeg 9.1 &\#x27;Gauss&\#x27; adds ASTC, Vulkan APV encoder, LCEVC, graph-based bitstream filtering](https://ffmpeg.org/download.html#release_9.1) ⭐️ 8.0/10

FFmpeg 9.1 &\#x27;Gauss&\#x27; was released with concrete new capabilities: ASTC image encoding/decoding via libastcenc and support for .astc and KTX 1.0 containers; a new APV Vulkan encoder for GPU-accelerated video encoding; LCEVC payload merging bitstream filter and dual-track LCEVC handling in the ffmpeg CLI; a graph-based bitstream filtering API replacing the legacy linear filter chain; NVDEC CUARRAY hardware acceleration; and AMF Video Quality Enhancer \(vf\_vqe\_amf\) filter. These features are available immediately in the stable 9.1 release downloadable from ffmpeg.org.

hackernews · gyan · Nov 20, 04:02 · [Discussion](https://news.ycombinator.com/item?id=50569998)

**「Prerequisite context」** FFmpeg is a widely used open-source multimedia framework for processing video, audio, and other media formats. Version 9.0 &\#x27;Fresnel&\#x27;, released in May 2025, introduced initial Vulkan compute support and early LCEVC bitstream parsing capabilities, setting the foundation for the more comprehensive ASTC, Vulkan encoding, and graph-based filtering features in 9.1.

**「Impact」** Developers integrating FFmpeg into real-time streaming, game engine toolchains, or embedded graphics pipelines can now use ASTC natively and leverage Vulkan for encoding without CPU bottlenecks, while video enhancement workflows gain standardized LCEVC bitstream composition and more composable filtering via the new graph API.

**「Community discussion」** Commenters praised the release’s scope and sustainability, with one user noting FFmpeg&\#x27;s foundational role in open-source video infrastructure and others thanking maintainer gyan directly for builds and stewardship — reflecting broad community reliance on volunteer-maintained multimedia infrastructure.

**Tags**: `#multimedia`, `#video-encoding`, `#open-source`, `#gpu-compute`, `#ffmpeg`

---

<a id="item-tech-news-6"></a>
### [PostgreSQL 19 Adds Built-In REPACK CONCURRENTLY for Table Bloat Cleanup](https://www.snowflake.com/en/blog/engineering/postgres-19-repack-table-bloat/) ⭐️ 8.0/10

PostgreSQL 19 introduces the built-in \`REPACK CONCURRENTLY\` command to reclaim bloat from tables and indexes without requiring external extensions like \`pg\_repack\`. This feature replaces error-prone, third-party tools with a safer, integrated mechanism that avoids long-running locks, connection drops, and manual retry cycles. It is available starting with the official PostgreSQL 19 release, shipped in November 2026 \(two months later than usual due to AI-related security issue remediation\). The implementation avoids triggers and instead leverages PostgreSQL’s internal WAL and transaction infrastructure, improving reliability for production database administrators.

hackernews · craigkerstiens · Nov 20, 02:43 · [Discussion](https://news.ycombinator.com/item?id=50569516)

**「Background」** Table bloat—wasted disk space caused by PostgreSQL&\#x27;s MVCC implementation—has long required external tools like pg\_repack or pg\_squeeze to reclaim, as native VACUUM cannot fully remove dead tuples from heavily updated tables without exclusive locks. These extensions were widely adopted but introduced operational risk: they relied on triggers, temporary tables, and long-running connections, often failing mid-process and requiring manual recovery.

**「Impact」** Production PostgreSQL administrators can now reclaim bloat without relying on fragile external tools like pg\_repack or pg\_squeeze, eliminating multi-hour failures and connection-drop risks during maintenance windows; REPACK CONCURRENTLY is faster and generates less WAL under write load than those extensions.

**「Community reaction」** Users report severe operational pain with legacy repack tools—e.g., multi-hour failures during off-peak maintenance windows and unrecoverable interruptions requiring full restarts—making the built-in solution highly anticipated. Some developers highlight technical distinctions, such as \`pg\_squeeze\`’s WAL-tailing approach versus \`pg\_repack\`’s trigger-based method, and raise nuanced concerns about MVCC consistency trade-offs under concurrent repack operations.

<details><summary>References</summary>
<ul>
<li><a href="https://boringsql.com/">boringSQL | Supercharge your SQL &amp; PostgreSQL powers</a></li>

</ul>
</details>

**Tags**: `#PostgreSQL`, `#database-administration`, `#system-reliability`, `#open-source`

---

<a id="item-tech-news-7"></a>
### [Frostbite: AI-synthesized CPU architecture based on interaction nets](https://architectlabs.com/blog/frostbite) ⭐️ 7.0/10

A blog post introduces Frostbite, a CPU architecture synthesized by AI using interaction nets—a non-von Neumann, graph-rewriting computational model—as its foundational paradigm. The architecture is claimed to be fully designed and verified by AI, but no open-source artifacts, silicon implementation, benchmarks, or peer-reviewed validation are provided. The post does not specify the AI system used, training data, verification methodology, or target fabrication process; it remains a conceptual demonstration with no evidence of physical realization or performance measurement beyond unspecified claims.

hackernews · shioyama · Nov 20, 10:01 · [Discussion](https://news.ycombinator.com/item?id=50572503)

**「Background」** Interaction nets are a graph-rewriting formalism for modeling computation, originally introduced by Yves Lafont in 1990 as a foundation for parallel, non-von Neumann computation; they underpin dataflow and demand-driven execution models, differing fundamentally from traditional control-flow architectures like von Neumann or Harvard. Prior hardware explorations of related ideas include WaveScalar \(early 2000s\), a dataflow-inspired architecture that compiled high-level programs into static dataflow graphs but faced challenges in scalability and tooling support.

**「Impact」** Developers and researchers exploring non-von Neumann architectures must now assess whether Frostbite’s AI-synthesized interaction-net implementation offers practical advantages over prior dataflow approaches like WaveScalar—especially given its use of an in-order baseline and limited benchmarking, as noted by community skeptics.

**「Community discussion」** Commenters clarify that AI acted as a synthesizer of existing research—not an originator—integrating decades-old ideas like interaction nets and dataflow architectures \(e.g., WaveScalar\), while expressing skepticism about novelty and performance claims due to comparisons against in-order CPUs and lack of rigorous evaluation.

<details><summary>References</summary>
<ul>
<li><a href="https://architectlabs.com/blog/frostbite">Introducing Frostbite: A new CPU architecture discovered ...</a></li>
<li><a href="https://letsdatascience.com/news/architect-labs-unveils-frostbite-an-ai-designed-cpu-architec-88f8acbd">Architect Labs unveils Frostbite, an AI-designed CPU architecture</a></li>
<li><a href="https://cseweb.ucsd.edu/~swanson/papers/SwansonPhDThesis.pdf">The WaveScalar Architecture</a></li>
<li><a href="http://wavescalar.cs.washington.edu/">WaveScalar: A Dataflow Architecture for Imperative Languages</a></li>
<li><a href="https://ieeexplore.ieee.org/document/1253203">WaveScalar | IEEE Conference Publication | IEEE Xplore</a></li>

</ul>
</details>

**Tags**: `#CPU architecture`, `#AI-assisted design`, `#interaction nets`, `#computer science foundations`

---

<a id="item-tech-news-8"></a>
### [Essay critiques AI&\#x27;s industrialization of knowledge work and authorship](https://em-online.bearblog.dev/i-can-tell-you-wrote-this-yourself/) ⭐️ 7.0/10

Bruno Bernardino’s reflective essay examines how AI-assisted writing and knowledge work are transforming expectations around authorship, learning, and intellectual agency in education and professional software development. It documents a shift from optional to expected AI use—citing assignment instructions that strongly encourage \(and effectively require\) AI tools—and describes firsthand experiences such as spending eight-hour days prompting LLMs in windowless computer labs. The essay frames this trend as an &\#x27;industrialization of cognition&\#x27; that risks eroding deep learning, intuition, and personal intellectual labor, without announcing any new tool, policy, or technical capability.

hackernews · BrunoBernardino · Nov 20, 07:13 · [Discussion](https://news.ycombinator.com/item?id=50571189)

**「Background」** This essay builds on the broader, ongoing integration of large language models into educational curricula and software engineering workflows since 2023, following the public release of capable open and commercial LLMs. Unlike technical product announcements, it responds to documented institutional shifts—such as universities revising academic integrity policies and course syllabi to accommodate or mandate AI use—making the critique legible only against that recent pedagogical and professional context.

**「Impact」** For students and early-career developers, the normalization of AI-as-co-pilot creates tangible pressure to adopt these tools despite concerns about diminished skill acquisition, as evidenced by course structures that disadvantage non-users and lab environments designed around continuous prompting.

**「Community discussion」** Commenters broadly affirm the essay’s core concern: FinnLobsien compares AI to industrialization—beneficial yet process-agnostic—while borzi observes that self-directed thinking has long been a minority practice, now further displaced by AI delegation; both treat the phenomenon as sociotechnical rather than purely technical.

**Tags**: `#AI ethics`, `#education technology`, `#software engineering culture`

---

<a id="item-tech-news-9"></a>
### [Signal Addresses AI App Data Exfiltration Risks on Mobile](https://signal.org/blog/protecting-your-privacy/) ⭐️ 7.0/10

Signal published a blog post addressing how third-party AI apps on Android and iOS can access users&\#x27; Signal chat data via accessibility services, clipboard APIs, and other OS-level interfaces—even without Signal&\#x27;s explicit permission. The post confirms active engineering work to mitigate these exfiltration vectors, including technical countermeasures under development and plans for improved forensic transparency. Signal states it is &\#x27;cautiously optimistic&\#x27; about near-term progress but does not ship a complete fix in the post; no new client version or patch release date is announced. The issue affects all current Signal mobile clients \(Android and iOS\) and extends to cases where only a user&\#x27;s contact—not the user themselves—has installed a risky AI app.

hackernews · dotcoma · Nov 20, 09:42 · [Discussion](https://news.ycombinator.com/item?id=50572348)

**「Background」** Signal’s privacy model assumes trust in the underlying operating system, but recent AI integrations—such as on-screen scanning by OS-level AI agents on iOS 27 and some Android devices—bypass traditional app sandboxing by accessing screen content directly. This undermines Signal’s existing protections, including end-to-end encryption, because data becomes exposed at the OS level before encryption or after decryption. Signal’s response includes technical mitigations like screenshot restrictions, which rely on platform-specific APIs introduced in iOS 27 and certain Android versions.

**「Impact」** Signal&\#x27;s new technical measures—such as blocking screenshots and restricting clipboard access—require affected AI apps on Android and iOS to lose access to Signal chat content, but users remain exposed if their contacts run such apps, since forwarded messages or notifications may still leak data via OS-level APIs.

**「Community Discussion」** Commenters debate systemic responsibility: one suggests Signal publish its forensic investigation findings as a living document to help other developers, while another argues that app-level mitigations are insufficient and users must instead adopt privacy-hardened OSes like GrapheneOS. A separate comment notes the irony that macOS—often perceived as highly private—is highlighted as particularly vulnerable in this context.

<details><summary>References</summary>
<ul>
<li><a href="https://signal.org/blog/protecting-your-privacy/">Signal &gt;&gt; Blog &gt;&gt; Signal is Serious About Protecting...</a></li>
<li><a href="https://cybersecuritynews.com/signal-restricts-screenshots/">Signal Restricts Screenshots to protect User Privacy from AI ...</a></li>
<li><a href="https://www.fastcompany.com/91646370/signal-blocks-screenshots-ai-agents-hostile-privacy-meredith-whittaker">Signal blocks screenshots; AI agents &#x27;hostile to privacy ...</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#mobile-security`, `#ai-ethics`, `#secure-messaging`, `#operating-systems`

---

<a id="item-tech-news-10"></a>
### [ChatPRD halts free trials due to token fraud abuse](https://simonwillison.net/2026/Nov/20/token-fraud-is-here-and-its-bad/) ⭐️ 7.0/10

Claire Vo, founder of the AI product management platform ChatPRD, has discontinued free trials after widespread token fraud—including automated trial recycling, promo code abuse, and commercial tunneling—was used to power external businesses like Roblox and Fortnite map studios. The abuse involved prompt-based model fingerprinting \(e.g., pelican-on-bicycle SVGs\) to identify underlying LLMs, and occurred despite ChatPRD having been live since the GPT-4 era. No technical mitigation details or vendor-specific infrastructure changes are described; the response is operational \(trial removal\), not technical remediation.

rss · Simon Willison · Nov 20, 02:49

**「Background」** Token fraud in AI SaaS platforms refers to the malicious exploitation of API access tokens—often obtained via free trials, promo codes, or compromised accounts—to extract computational value at scale, either for resale or to power unauthorized commercial services. This abuse relies on the fact that many AI-native products expose powerful agent capabilities without robust identity verification, rate limiting, or usage telemetry, enabling attackers to tunnel traffic through legitimate endpoints. The phenomenon builds on earlier documented cases of LLM API scraping and model fingerprinting, where distinctive prompt patterns \(e.g., pelican SVGs\) are used to infer underlying model identities or bypass detection.

**「Financial and operational impact on AI SaaS founders」** Claire Vo’s decision to wind down free trials entirely—cited as the &quot;right decision&quot; in response to token fraud—demonstrates a concrete, immediate operational consequence: AI-native SaaS platforms must now treat trial abuse not as an edge case but as a direct financial exposure requiring architectural and policy-level intervention, as confirmed by her documented experience funding a commercial Roblox/Fortnite map studio via fraudulent token reuse.

<details><summary>References</summary>
<ul>
<li><a href="https://www.lennysnewsletter.com/p/how-i-fight-token-fraud-as-a-solo">How I fight token fraud as a solo founder - by Claire Vo</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#API abuse`, `#SaaS operations`, `#token economy`, `#product engineering`

---

<a id="item-tech-news-11"></a>
### [Gemini gains macOS computer control for US paid subscribers](https://www.bloomberg.com/news/articles/2026-11-19/google-s-gemini-can-now-control-mac-devices-on-users-behalf) ⭐️ 7.0/10

Google Gemini now offers &\#x27;computer control&\#x27; functionality on macOS, enabling it to click, type, navigate menus, and fill forms on behalf of users. The feature is available exclusively to US-based subscribers of Google AI Plus, Pro, or Ultra tiers using the Mac version of Gemini. It runs in a separate background window, supports per-app permission limits, real-time operation monitoring, on-demand pausing, and requires explicit user approval before critical actions. No independent verification of the capability’s implementation, security model, or actual release date is available, as the cited Bloomberg article URL is invalid \(2026 date, no matching publication\).

telegram · zaihuapd · Nov 20, 02:51

**「Background」** Gemini&\#x27;s &\#x27;computer use&\#x27; capability builds on its prior desktop integration, which previously supported only text-based interaction with local files and apps; this new feature introduces direct GUI automation—clicking, typing, and menu navigation—within an isolated background window. It follows Google&\#x27;s November 2026 announcement confirming the feature&\#x27;s launch for Mac users, explicitly distinguishing it from earlier web-only or file-reading capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/products/gemini-app/computer-use-mac/">Automate Mac tasks with Gemini computer use - The Keyword</a></li>
<li><a href="https://explainx.ai/blog/gemini-app-mac-computer-use-background-window-ai-plus-pro-ultra-november-2026">Gemini Computer Use on Mac: Who Gets It and How It Works ...</a></li>
<li><a href="https://pricingrank.org/google-gemini-computer-use-mac-november-2026/">Google’s Gemini Can Now Use Your Mac for You — But Only on ...</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#macOS`, `#Gemini`, `#human-AI interaction`, `#desktop automation`

---

<a id="item-tech-news-12"></a>
### [UK tribunal rules Apple wins, orders public hearing on government&\#x27;s iPhone encryption bypass demand](https://appleinsider.com/articles/26/11/19/uk-cant-hide-that-it-tried-ordering-apple-to-allow-access-to-user-data) ⭐️ 7.0/10

The UK Investigatory Powers Tribunal ruled that Apple prevailed in a case where the Home Office sought secret Technical Capability Notices \(TCNs\) requiring Apple to weaken iPhone encryption or provide access to user data. The tribunal ordered that most of the proceedings be made public and rejected the Home Office’s national security justification as &\#x27;unrealistic.&\#x27; The ruling applies specifically to TCNs issued under the Investigatory Powers Act 2016 and mandates transparency for this instance, though it does not invalidate TCNs broadly or establish a binding precedent across all future cases.

telegram · zaihuapd · Nov 20, 04:13

**「Background」** The UK Investigatory Powers Act \(2016\) authorizes the government to issue Technical Capability Notices \(TCNs\), compelling technology companies to assist with lawful access to communications data. Apple challenged two such TCNs in 2026: the first, issued in 2025, was dropped after diplomatic pressure from the US; the second, issued in July 2026 and targeting UK-only iCloud access, triggered Apple’s formal complaint before the Investigatory Powers Tribunal \(IPT\).

**「Impact」** Developers and vendors operating in the UK must now anticipate greater judicial scrutiny—and potential public exposure—when responding to TCNs demanding technical modifications that compromise end-to-end encryption, raising legal and reputational risks alongside technical compliance concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://fintechlaw.ai/blog/apple-uk-tcn-icloud-cross-border-encryption-challenge">Apple UK TCN Challenge: Cross-Border Encryption Fight 2026</a></li>
<li><a href="https://www.theguardian.com/technology/2026/aug/03/apple-legal-challenge-uk-government-data-access">Apple launches legal challenge against UK ... | The Guardian</a></li>
<li><a href="https://www.ft.com/content/46a5cf3c-a827-477f-b72f-e7415565e729?syn-25a6b1a6=1">UK loses bid to keep Apple ‘backdoor’ order secret</a></li>

</ul>
</details>

**Tags**: `#encryption`, `#privacy`, `#government-surveillance`, `#software-security`, `#legal-technology`

---

<a id="item-tech-news-13"></a>
### [US approved nearly 880,000 AI chips for export to China between late 2025 and mid-2026](https://foreignaffairs.house.gov/news/press-releases/chairman-brian-mast-exercises-legislative-authority-to-publicly-release-ai-chip-license-information-for-china) ⭐️ 7.0/10

U.S. export licenses approved 879,868 AI chips—including NVIDIA H200 and AMD MI325X—for Chinese companies including Tencent, ByteDance, Alibaba, Baidu, and others between December 2025 and May 2026, according to a document attributed to the U.S. House Foreign Affairs Committee; however, the cited timeframe is anachronistic \(as of the item’s November 2026 publication date\), no verifiable source document or official dataset was provided, and the linked URL does not contain the claimed data. All 21 reported licenses were approved but remained undelivered as of May 11, 2026.

telegram · zaihuapd · Nov 20, 04:25

**「U.S. AI chip export controls and licensing framework」** Since October 2022, the U.S. Department of Commerce’s Bureau of Industry and Security \(BIS\) has imposed strict export controls on advanced AI chips—including NVIDIA’s A100, H100, and later H200, and AMD’s MI250X and MI325X—restricting sales to Chinese entities without a license. These controls were tightened further in October 2023 and again in 2024 to close loopholes and expand coverage to lower-tier chips and cloud-based access. Licenses are granted case-by-case, with approvals not equivalent to shipments and subject to end-use verification.

**「Impact」** The reported approval of nearly 880,000 AI chips—including NVIDIA H200 and AMD MI325X—for Chinese firms listed on the U.S. military-end-user list \(e.g., Alibaba, Tencent, Baidu, BYD\) raises compliance concerns, as shipments to such entities require enhanced scrutiny under U.S. export control rules; however, all 21 approved licenses cited were marked &\#x27;not shipped&\#x27; as of May 11, 2026, meaning no actual transfer occurred, and the reported timeframe \(Dec 2025–May 2026\) is anachronistic and unsupported by verifiable official records.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zerohedge.com/geopolitical/revealed-trump-admin-cleared-879868-nvidia-amd-ai-chips-china-third-pentagon-listed">Revealed: Trump Admin Cleared 879,868 Nvidia , AMD AI... | ZeroHedge</a></li>
<li><a href="https://wccftech.com/trump-administration-approved-nearly-900000-nvidia-amd-ai-chips-for-china/">Over 30% Of Approved U.S. AI Chips, Including NVIDIA ’s H 200 , Went...</a></li>
<li><a href="https://www.nytimes.com/2026/11/19/business/economy/nvidia-chips-commerce-china-huang.html">Nvidia Asked to Sell Chips to Companies Tied to Chinese Military and...</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#export controls`, `#U.S.-China tech policy`

---

<a id="item-tech-news-14"></a>
### [TikTok Launches Globally Available AI Deepfake Detection Tool](https://www.straitstimes.com/world/tiktok-launches-tool-to-help-public-figures-detect-deepfakes-globally) ⭐️ 7.0/10

On November 20, 2026, TikTok launched its globally available Likeness Detection tool, which sends alerts to third-party-verified public figures and top creators when their likeness is used without authorization in AI-generated content. A companion transparency tool—accessible to anyone without a TikTok account—allows users to upload images or videos to check whether they were generated by TikTok’s own AI features. The tools are operational worldwide as of the launch date and align with the EU’s August 2026 requirement for AI content labeling, ahead of the 2027 European elections.

telegram · zaihuapd · Nov 20, 08:14

**「Background」** The EU’s AI Act mandates labeling of AI-generated content, with enforcement for political content beginning in August 2026 ahead of the 2027 elections; TikTok’s tools directly support compliance with this requirement. Prior to this, TikTok had not offered publicly accessible, third-party-validated detection capabilities for unauthorized likeness use or AI provenance verification.

**「Impact」** Verified public figures can now receive timely alerts about unauthorized AI-generated depictions of themselves and initiate takedowns, reducing exposure to reputational harm from deepfakes during election-sensitive periods.

**Tags**: `#AI safety`, `#deepfakes`, `#content provenance`, `#social media policy`, `#regulatory compliance`

---

<a id="item-tech-news-15"></a>
### [Apple developing in-house AI agent for code, browsing, and app control, targeting late 2027](https://www.bloomberg.com/news/articles/2026-11-19/apple-is-working-on-ai-agent-for-device-control-apps-browsing-and-coding) ⭐️ 7.0/10

Apple is developing an in-house AI agent capable of writing code, browsing the web, and controlling applications, with recruitment for senior engineering managers indicating active early-stage development. The project is targeted for release no earlier than late 2027. macOS 27.3 introduced a hardened 14-step permission flow for third-party AI agents seeking system control—up from 4 steps—suggesting Apple is proactively securing its platform ahead of its own agent’s launch. This is an announced internal initiative, not a shipped product or independently verified capability.

telegram · zaihuapd · Nov 20, 08:59

**「What is an AI agent?」** An AI agent is a software system that perceives its environment, makes decisions autonomously, and takes actions—such as running code, interacting with applications, or navigating websites—to achieve user-defined goals. Unlike static large language models, agents incorporate planning, tool use, memory, and execution loops; recent examples include OpenAI&\#x27;s Operator and Meta&\#x27;s Muse, both launched in 2024–2025.

**Tags**: `#AI agents`, `#Apple`, `#system security`, `#developer tools`, `#OS integration`

---

<a id="item-tech-news-16"></a>
### [OpenAI launches experimental background mode for async LLM requests](https://developers.openai.com/api/docs/guides/background) ⭐️ 7.0/10

OpenAI has introduced an experimental background mode for asynchronous LLM inference, available in beta on four GPT-6.x models: GPT-6.2 Astra, GPT-6.2 Sol, GPT-6.1 Terra, and GPT-6 Luna. Users enable it by setting background: true and choosing a completion window of either 2 hours \(30% token discount\) or 8 hours \(40% token discount\) via background\_options.completion\_window; omitting the flag defaults to synchronous &\#x27;soonest&\#x27; execution with no discount. The mode temporarily stores response data regardless of store: false or zero-data-retention settings. The official OpenAI documentation URL provided in the source returns a 404, and the announcement originates from an unverified Telegram channel, not an official OpenAI release.

telegram · zaihuapd · Nov 20, 11:15

**「Background」** GPT-6.2 Astra and Sol, along with GPT-6.1 Terra and GPT-6 Luna, are recently released OpenAI models—Astra and Sol launched two and three days ago respectively, with Astra positioned as the most capable frontier model and Sol as an efficient, versatile model for everyday use. These models form the exclusive initial set supporting the new background mode, which builds on their existing capabilities by adding asynchronous execution as an experimental feature.

**「Impact」** Developers relying on long-running LLM tasks may reduce token costs by up to 40%—but only if they can tolerate up to 8 hours of latency and accept that responses are temporarily stored despite explicit privacy configurations.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-2-astra-sol/">Introducing GPT-6.2 Astra and Sol | OpenAI</a></li>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT‑6 Sol and Luna - OpenAI</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-6.2-astra">GPT-6.2 Astra Model | OpenAI API</a></li>

</ul>
</details>

**Tags**: `#LLM APIs`, `#cost optimization`, `#asynchronous processing`

---

<a id="item-tech-news-17"></a>
### [Yu Chengdong Clarifies Huawei Xiangjie V8 Is L2, Not L3: Drivers Must Stay Alert](https://weibo.com/1664176597/Rsi4xEGAA) ⭐️ 7.0/10

Huawei Executive Yu Chengdong publicly corrected his earlier claim that drivers could sleep during L3 autonomous driving in the Xiangjie V8, stating the vehicle currently operates only at SAE Level 2 and requires continuous driver attention, including hands on the wheel. He confirmed that while the vehicle’s hardware supports L3 functionality, L3 software is not yet enabled or deployed. The clarification was issued on November 20, 2026, following controversy over remarks made during the same-day HarmonyOS Intelligent Driving Xiangjie V8 and Xingmang brand launch event. His original comments—suggesting drivers could sleep and would be awakened by alerts—were retracted as inaccurate.

telegram · zaihuapd · Nov 20, 12:55

**「Autonomous driving levels defined by SAE」** SAE International&\#x27;s J3016 standard defines six levels \(L0–L5\) of driving automation, where L2 requires continuous driver supervision and hands-on-the-wheel operation, while L3 permits conditional automation with driver fallback required only when the system requests it—though no production vehicle in China is currently certified for consumer-facing L3 operation on public roads.

**「Impact」** Automotive developers and safety compliance teams must treat the Xiangjie V8 as a Level 2 system requiring driver supervision, not a production-ready L3 system; this affects validation scope, human-machine interface design, and regulatory documentation for China’s MIIT and GB/T 40429–2021 ADAS certification.

**Tags**: `#autonomous-driving`, `#ai-safety`, `#automotive-software`, `#regulatory-compliance`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Warsh’s No-Forward-Guidance Stance Spurs Unusual Surge in Fed Official Speeches](https://www.cnbc.com/2026/11/20/warsh-fed-forward-guidance-rate-hikes.html) ⭐️ 7.0/10

Federal Reserve Chair Kevin Warsh has refused to provide forward guidance on interest rates in his first six months, prompting a record surge in public statements from other FOMC officials—more &\#x27;Fedspeak&\#x27; in two weeks than any similar period since early 2025, per Bank of America analysis.

rss · CNBC Finance · Nov 20, 15:20

**「Background」** Forward guidance is the Fed’s practice of signaling future policy moves to shape market expectations; Warsh rejects it as premature and inflexible, contrasting with past chairs who regularly weighed in to clarify whether hawks or doves held sway.

**「Impact」** The resulting flood of divergent public statements has increased short-term Treasury yield volatility and raised market odds of a December rate hike to 100%, according to CME FedWatch data.

**Tags**: `#Federal Reserve`, `#monetary policy`, `#forward guidance`, `#inflation`, `#FOMC`

---

<a id="item-finance-news-2"></a>
### [U.S. Corporations Shift from Buybacks to Net Equity Issuance](https://www.cnbc.com/2026/11/20/equity-issuance-bull-market-problem.html) ⭐️ 7.0/10

U.S. corporations have shifted from net share repurchases in 2024 to net equity issuance in 2026, with new share issuance totaling 3.1% of total U.S. stock market capitalization as of late November 2026, according to Acadian Asset Management.

rss · CNBC Finance · Nov 20, 14:15

**「Background」** For years, buybacks reduced the number of shares outstanding—supporting stock prices and earnings per share—so the reversal to net issuance increases supply and may pressure valuations.

**「Impact」** This shift directly affects investors by increasing market supply and potentially diluting earnings per share, raising concerns about bull market sustainability amid AI-driven fundraising.

**Tags**: `#equity\_issuance`, `#market\_supply`, `#corporate\_capital\_allocation`, `#AI\_investment`, `#bull\_market\_risk`

---

<a id="item-finance-news-3"></a>
### [U.S.-China Talks at APEC Yield No Tariff or Tech Policy Breakthroughs](https://www.cnbc.com/2026/11/20/apec-summit-trump-xi-china-trade-taiwan.html) ⭐️ 7.0/10

At the APEC summit in Shenzhen, Presidents Trump and Xi held bilateral and trilateral talks with Russia but announced no tariff reductions, no resolution on U.S. tech restrictions \(including those affecting Nvidia\), and no progress on Taiwan-related tensions.

rss · CNBC Finance · Nov 20, 13:29

**「Background」** Japan and China entered a diplomatic crisis in November 2025 after Prime Minister Sanae Takaichi stated that a Chinese attack on Taiwan could trigger Japan’s self-defense response, prompting Beijing’s strong condemnation and a notably chilly reception for her at the 2026 APEC summit in Shenzhen.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2025%E2%80%932026_China%E2%80%93Japan_diplomatic_crisis">2025 –2026 China – Japan diplomatic crisis - Wikipedia</a></li>
<li><a href="https://www.theguardian.com/world/2025/nov/11/japan-china-row-takaichi-taiwan-conflict-military-deployment">Japan and China in growing row after PM Takaichi says Taiwan ...</a></li>
<li><a href="https://www.cnbc.com/2026/11/19/japan-china-trump-takaichi-taiwan-.html">China gives Takaichi chilly welcome on first Japan PM visit since 2019</a></li>

</ul>
</details>

**Tags**: `#U.S.-China relations`, `#trade policy`, `#semiconductors`, `#geopolitics`, `#APEC`

---

<a id="item-finance-news-4"></a>
### [Ford Enters Battery Manufacturing Using CATL&\#x27;s LFP Technology](https://api3.cls.cn/share/article/2539395?sv=8.5.9) ⭐️ 7.0/10

Ford has begun shipping lithium iron phosphate \(LFP\) battery cells from its Marshall, Michigan plant—built using licensed technology from China’s CATL—to power its upcoming Fathom electric pickup, marking its formal entry into battery cell manufacturing; the plant has a planned annual capacity of 20 GWh.

telegram · zaihuapd · Nov 20, 06:04

**「Background」** Ford previously relied on external suppliers for EV batteries but is now vertically integrating cell production using CATL’s licensed LFP technology to support its new Fathom pickup and meet U.S. Inflation Reduction Act requirements for domestic battery content.

**Tags**: `#electric-vehicles`, `#battery-technology`, `#us-china-trade`, `#automotive-manufacturing`, `#supply-chain`

---

<a id="item-finance-news-5"></a>
### [Beijing Proposes Ban on Security Deposit Deductions for Normal Wear and Tear](https://mp.weixin.qq.com/s/PmGxh5knIyxiBRhpRoJnoQ) ⭐️ 7.0/10

Beijing’s housing and market regulation authorities have proposed a revised model rental contract that would prohibit landlords from deducting security deposits for normal wear and tear caused by tenants’ ordinary use of the property.

telegram · zaihuapd · Nov 20, 13:46

**「Background」** The draft, issued for public consultation on November 20, 2026, updates Beijing’s standard rental contract to strengthen tenant protections amid rising concerns over opaque deposit practices by landlords and rental platforms.

**Tags**: `#housing\_policy`, `#consumer\_protection`, `#rental\_market`, `#regulatory\_proposal`

---