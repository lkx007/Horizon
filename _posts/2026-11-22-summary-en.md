---
layout: default
title: "Horizon Summary: 2026-11-22 (EN)"
date: 2026-11-22
lang: en
---

> From 26 items, 11 important content pieces were selected

---

**Technology News**
1. [Critical double-free vulnerability in GPGME fixed in v2.3.0](#item-tech-news-1) ⭐️ 9.0/10
2. [TSMC halts sub-16nm chip orders for Chinese companies under tightened U.S. export controls](#item-tech-news-2) ⭐️ 9.0/10
3. [Zhejiang University Achieves First Physical QRAM Implementation on Tianmu-2 Superconducting Chip](#item-tech-news-3) ⭐️ 9.0/10
4. [Daraxonrasib shows 8.2% complete response in frontline metastatic pancreatic cancer](#item-tech-news-4) ⭐️ 9.0/10
5. [Lean formal verification of Generalized Riemann Hypothesis completed](#item-tech-news-5) ⭐️ 8.0/10
6. [OpenAI Reduces Adversarial Distillation Success Rate from 54.0% to 0.2%](#item-tech-news-6) ⭐️ 8.0/10
7. [Microsoft introduces RDMA over USB4 in Windows for multi-PC local AI inference](#item-tech-news-7) ⭐️ 8.0/10
8. [OpenRouter warns MiniMax prompts may have been intercepted by third parties](#item-tech-news-8) ⭐️ 8.0/10
9. [USB monitor hub caused 75% download speed loss via TCP ACK delays](#item-tech-news-9) ⭐️ 7.0/10

**Technology Blog**
1. [Why Output Caching Fails for LLM Agents](#item-tech-blog-1) ⭐️ 8.0/10

**Financial News**
1. [Trump Proposes Massive Tax on US Firms Building AI Data Centers Abroad](#item-finance-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Critical double-free vulnerability in GPGME fixed in v2.3.0](https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html) ⭐️ 9.0/10

A critical double-free vulnerability in GPGME \(GNU Privacy Guard Made Easy\), a cryptographic library used by GnuPG, GitLab, email clients, Samba, Flatpak, and XMPP clients, was disclosed on 2026-11-20 and fixed in version 2.3.0. The flaw affects all software using GPGME versions prior to 2.3.0—whether dynamically linked, statically linked, or bundled—and enables remote code execution when processing maliciously crafted OpenPGP data. Real-world exploitation was demonstrated in GitLab’s signed commit verification infrastructure, prompting accelerated disclosure after GitLab patched it earlier than the originally scheduled 2026-11-25 date. The vulnerability had gone undetected upstream for years, though Red Hat reportedly patched it internally five years earlier.

hackernews · gdgghhhhh · Nov 21, 08:32 · [Discussion](https://news.ycombinator.com/item?id=50587208)

**「Background」** GPGME \(GnuPG Made Easy\) is a C library that provides a high-level API to access GnuPG&\#x27;s cryptographic functions, widely used by applications requiring OpenPGP or S/MIME support. It has been maintained as part of the GnuPG project since its inception in the late 1990s and is distributed separately from the core gpg binary; versions prior to 2.3.0 were vulnerable to a double-free condition in key listing and signature verification code paths.

**「Immediate update required for all software using GPGME &lt;2.3.0」** All applications linking against GPGME versions prior to 2.3.0—including GitLab \(affecting its signed commit verification\), email clients, Samba, Flatpak, and Gpg4win—are vulnerable to a double-free flaw that cannot be ruled out as exploitable for remote code execution, prompting GnuPG to issue an urgent update recommendation.

**「Community discussion」** Some commenters questioned whether the issue is strictly a double-free bug rather than a full RCE chain, noting that RCE requires additional conditions beyond the memory corruption itself; others emphasized its severity in high-trust contexts like GitLab’s signed commits. A commenter clarified that the vulnerability resides in the &\#x27;gpgme&\#x27; library and does not affect apt, as apt does not use GPGME for signature verification.

<details><summary>References</summary>
<ul>
<li><a href="https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html">[Announce] GnuPG Security Advisory for GPGME ...</a></li>
<li><a href="https://thehackernews.com/2026/11/gnupg-warns-critical-gpgme-flaw-could.html">GnuPG Warns Critical GPGME Flaw Could Expose App Data via...</a></li>

</ul>
</details>

**Tags**: `#security`, `#cryptography`, `#vulnerability`, `#open-source`, `#systems-programming`

---

<a id="item-tech-news-2"></a>
### [TSMC halts sub-16nm chip orders for Chinese companies under tightened U.S. export controls](https://appleinsider.com/articles/26/11/20/apple-supplier-tsmc-cuts-off-china-chip-orders-amid-tighter-export-controls) ⭐️ 9.0/10

TSMC has halted acceptance of new orders for chips manufactured at 16nm and more advanced process nodes from Chinese companies, following updated U.S. export control rules that require prior U.S. government approval for such shipments. The rule change eliminates TSMC’s prior ability to self-assess whether a customer’s design qualifies for license exceptions, shifting responsibility to mandatory pre-approval by U.S. authorities — and no Chinese company currently appears on the U.S.-approved list. As a result, Chinese firms are restricted to older nodes like 28nm and 40nm, which lack the performance and power efficiency needed for AI data centers and high-bandwidth memory \(HBM\) integration.

telegram · zaihuapd · Nov 21, 02:01

**「U.S. export controls tightened to require pre-approval for sub-16nm chip exports to China」** U.S. export regulations governing advanced semiconductor manufacturing equipment and foundry services were recently updated to require prior U.S. government approval—rather than self-assessment by foundries—for any supply of chips fabricated at 16nm or more advanced process nodes to Chinese entities. This change builds on earlier controls that already restricted the export of EUV lithography tools and certain AI accelerator chips, but now extends enforcement to the foundry output level itself, directly constraining access to leading-edge logic and memory technologies.

**「Consequence for users and developers」** Chinese AI infrastructure developers face immediate constraints in deploying next-generation AI accelerators and data center systems, as sub-16nm nodes are essential for integrating high-bandwidth memory and achieving required compute density and energy efficiency — with no viable domestic foundry alternative currently available at scale.

**Tags**: `#semiconductor`, `#AI-hardware`, `#export-controls`, `#chip-manufacturing`, `#geopolitics`

---

<a id="item-tech-news-3"></a>
### [Zhejiang University Achieves First Physical QRAM Implementation on Tianmu-2 Superconducting Chip](https://finance.sina.com.cn/stock/2026-11-21/doc-iniznhsk3530826.shtml) ⭐️ 9.0/10

Zhejiang University researchers demonstrated the world&\#x27;s first physical implementation of quantum random access memory \(QRAM\) on their custom superconducting quantum processor &\#x27;Tianmu-2&\#x27;, publishing results in Nature Physics. The prototype successfully retrieved 4-bit and 8-bit data with measured fidelities of 80.9% and 60.4%, respectively, used a circuit depth reduced by over 30% compared to unoptimized designs, and showed experimentally verified local noise resilience. This is a functional hardware realization—not just a theoretical proposal or simulation—and applies specifically to superconducting qubit platforms.

telegram · zaihuapd · Nov 21, 08:31

**「Background」** Quantum random access memory \(QRAM\) is a theoretical hardware component proposed to enable quantum algorithms—such as Grover&\#x27;s search and quantum machine learning—to efficiently load classical data into quantum superposition. For over two decades, QRAM has remained unrealized in physical hardware due to extreme sensitivity to decoherence, control complexity, and scalability challenges in existing quantum platforms.

**「Impact」** The demonstration of functional QRAM on a physical superconducting chip enables near-term experimental validation of quantum algorithms—such as Grover’s search and quantum machine learning—that previously required QRAM only in theoretical models; developers now have a working hardware platform to test QRAM-dependent circuits, though current fidelity \(60.4% for 8-bit\) remains below the fault-tolerant threshold needed for scalable algorithmic advantage.

**Tags**: `#quantum computing`, `#QRAM`, `#superconducting qubits`, `#hardware acceleration`, `#quantum algorithms`

---

<a id="item-tech-news-4"></a>
### [Daraxonrasib shows 8.2% complete response in frontline metastatic pancreatic cancer](https://event.eortc.org/ena2026/2026/11/20/metastatic-pancreatic-cancer-responds-well-to-initial-treatment/) ⭐️ 9.0/10

In a single-arm phase I/II trial presented at ENA 2026, daraxonrasib \(RASONQUE\), an oral pan-RAS\(ON\) inhibitor, combined with gemcitabine/nab-paclitaxel achieved an 8.2% confirmed complete response rate \(5 of 61 patients\) and 76.6% 12-month overall survival in treatment-naïve metastatic pancreatic ductal adenocarcinoma. The regimen used daraxonrasib 200 mg once daily; median progression-free survival was 12.8 months and disease control rate was 90.2%, with median follow-up of 18.3 months. These results are not yet compared to a concurrent control arm, and the investigators explicitly stated that definitive efficacy assessment awaits ongoing phase III validation. Daraxonrasib was FDA-approved on August 26, 2026, for pretreated patients based on the phase III RMC-302 trial showing median overall survival of 13.2 vs 6.7 months versus control.

telegram · zaihuapd · Nov 21, 11:24

**「Background」** Daraxonrasib \(brand name RASONQUE\) is a first-in-class oral pan-RAS\(ON\) inhibitor approved by the FDA on August 26, 2026, for previously treated metastatic pancreatic ductal adenocarcinoma, based on the phase III RMC-302 trial showing a median overall survival of 13.2 months versus 6.7 months with chemotherapy. Unlike earlier RAS inhibitors targeting only KRAS G12C, daraxonrasib binds active-state RAS across multiple KRAS and NRAS mutations.

**「Impact」** Patients with treatment-naïve metastatic pancreatic ductal adenocarcinoma now have a new frontline option with daraxonrasib \(RASONQUE\) plus gemcitabine/nab-paclitaxel, showing an 8.2% complete response rate and 76.6% 12-month overall survival—substantially exceeding historical chemotherapy benchmarks—but its use remains contingent on confirmation from the ongoing phase III trial due to the single-arm design of the current study.

<details><summary>References</summary>
<ul>
<li><a href="https://www.drugs.com/rasonque.html">Rasonque ( daraxonrasib ): Uses, Dosage, Side Effects</a></li>
<li><a href="https://www.nytimes.com/2026/08/26/science/pancreatic-cancer-daraxonrasib-approval.html">F.D.A. Approves the Drug Daraxonrasib That’s Poised to Transform...</a></li>
<li><a href="https://www.tradingstocksnow.com/2026/08/27/revolution-medicines-built-a-platform-rasonque-is-the-opening-move/">Revolution Medicines Built a Platform. Rasonque Is the Opening Move.</a></li>

</ul>
</details>

**Tags**: `#oncology`, `#RAS inhibition`, `#pancreatic cancer`, `#targeted therapy`, `#clinical trials`

---

<a id="item-tech-news-5"></a>
### [Lean formal verification of Generalized Riemann Hypothesis completed](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) ⭐️ 8.0/10

A human-supervised, machine-checked formal verification of the Generalized Riemann Hypothesis \(GRH\) has been completed using the Lean theorem prover. The proof relies on two independently developed, self-consistency-verified Lean kernels—con-leche and con-ron—and builds on existing analytic number theory, not a new mathematical argument. It is not a proof of the classical \(non-generalized\) Riemann Hypothesis, nor does it replace peer-reviewed publication; rather, it is a fully formalized, computer-verified validation of GRH under standard ZFC foundations. The verification was led by Levent Alpöge and involved substantial formalization of complex analysis, algebraic number theory, and L-functions.

hackernews · g-b-r · Nov 21, 14:36 · [Discussion](https://news.ycombinator.com/item?id=50589618)

**「Background」** The Riemann Hypothesis \(RH\) is a 167-year-old conjecture in analytic number theory concerning the nontrivial zeros of the Riemann zeta function; its generalized form \(GRH\) extends this to Dirichlet L-functions. Prior to this work, RH had been formalized in Lean’s Mathlib as the statement \`RiemannHypothesis\`, vetted by experts and compiled correctly, but no machine-checked proof existed. The verification relies on two independently developed, self-verifying proof checkers—\`con-leche\` and \`con-ron\`—each accompanied by a formal consistency proof relative to Zermelo–Fraenkel set theory.

**「Impact」** Mathematicians and formal methods practitioners now have a machine-verified foundation for GRH-dependent results—such as many conditional bounds in analytic number theory and cryptography—enabling stronger confidence in theorems that assume GRH, provided the underlying Lean kernels remain correct and their consistency proofs hold.

**「Community discussion」** Commenters debate the degree of independence among the verification tools: \[rcr-anti\] asserts that concurrent bugs affecting both con-leche and con-ron—and their self-consistency proofs—would be vanishingly unlikely, while \[thejokeisonme\] cautions that past failures \(e.g., a fake Collatz refutation accepted by one checker\) reveal limitations in claimed independence, especially without continuous human oversight.

<details><summary>References</summary>
<ul>
<li><a href="https://leanprover-community.github.io/blog/posts/riemann-hypothesis/">Lean verification of the Riemann Hypothesis | Lean community blog</a></li>
<li><a href="https://www.clarin.com/us-news/who-is-levent-alpoge-the-anthropic-mathematician-who-claims-solved-the-riemann-hypothesis-with-claude_0_2WdGvYKBVM.html">Who is Levent Alpöge ? The Anthropic mathematician who claims he...</a></li>
<li><a href="https://news.ycombinator.com/item?id=50589618">Lean verification of the Riemann Hypothesis | Hacker News</a></li>

</ul>
</details>

**Tags**: `#formal-methods`, `#number-theory`, `#theorem-proving`, `#lean-prover`, `#mathematical-foundations`

---

<a id="item-tech-news-6"></a>
### [OpenAI Reduces Adversarial Distillation Success Rate from 54.0% to 0.2%](https://openai.com/index/combatting-adversarial-distillation/) ⭐️ 8.0/10

OpenAI has deployed enhanced defenses against adversarial distillation in its production models GPT-6.2 Astra and Sol, reducing the success rate of extracting reasoning traces from historical requests—from 54.0% to 0.2%—as measured in internal red team testing. The update applies specifically to inference-time protection of reasoning chains and is now active in those models. OpenAI also reports enforcing its policies weekly against thousands to tens of thousands of accounts engaged in model distillation, and previously briefed U.S. Congress on DeepSeek’s suspected distillation activity.

telegram · zaihuapd · Nov 21, 01:30

**「What is adversarial distillation?」** Adversarial distillation is a technique where attackers use carefully crafted queries—often involving system prompts, chain-of-thought prompting, or repeated probing—to extract internal model behaviors, reasoning traces, or even weights from API-accessed LLMs, effectively copying proprietary capabilities. It poses a direct threat to model intellectual property and safety controls, especially for models deployed via inference APIs without robust output filtering or query monitoring.

**Tags**: `#AI security`, `#model protection`, `#adversarial distillation`, `#LLM safety`, `#AI policy`

---

<a id="item-tech-news-7"></a>
### [Microsoft introduces RDMA over USB4 in Windows for multi-PC local AI inference](https://videocardz.com/newz/microsoft-brings-rdma-over-usb4-to-windows-allowing-multiple-pcs-to-run-one-local-ai-model) ⭐️ 8.0/10

Microsoft has released a developer preview of RDMA over USB4 for Windows, enabling multiple consumer PCs connected via standard USB4 cables to share memory and GPU resources to run a single local AI model. The implementation supports distributed inference on quantized models—demonstrated with three AMD Ryzen AI Max+ 395 systems running Qwen3-235B-A22B at 4-bit quantization, achieving ~18.5 tokens/second. It requires compatible USB4 hardware and is currently available only through the Windows Insider Program; no specialized networking hardware \(e.g., RoCE NICs or switches\) is needed.

telegram · zaihuapd · Nov 21, 06:13

**「Background」** RDMA \(Remote Direct Memory Access\) enables high-speed, low-latency data transfer between computers without involving the CPU or operating system kernel, traditionally requiring specialized hardware like InfiniBand or RoCE-capable Ethernet adapters. USB4, based on the Thunderbolt 3 protocol and supporting up to 40 Gbps bandwidth and PCIe tunneling, provides a consumer-grade physical layer that Microsoft now leverages to implement RDMA—extending its use beyond data centers into mainstream PCs.

**「Impact」** Developers targeting local AI inference on consumer hardware can now distribute model execution across multiple off-the-shelf PCs using only USB4 cables—eliminating the need for RDMA-capable NICs, InfiniBand, or managed switches, but requiring Windows Insider builds and compatible USB4 hosts with DMA support.

**Tags**: `#AI systems`, `#distributed computing`, `#Windows`, `#USB4`, `#local AI`

---

<a id="item-tech-news-8"></a>
### [OpenRouter warns MiniMax prompts may have been intercepted by third parties](https://news.ycombinator.com/item?id=50585962) ⭐️ 8.0/10

OpenRouter warned developers that prompts sent to MiniMax models via its API may have been read by third parties—including AtlasCloud, Novita, and StreamLake—due to time-correlated external URL access observed during security testing between July and October 2026. Specifically, test URLs embedded in prompts were accessed by external parties 40–130 hours after submission, suggesting potential prompt exfiltration through downstream infrastructure. In response, OpenRouter removed the &\#x27;zero data retention&\#x27; label from affected endpoints and advised users handling sensitive credentials to rotate API keys and passwords. The warning was issued via email and surfaced on Hacker News, but no official statement has been published on OpenRouter’s website.

telegram · zaihuapd · Nov 21, 06:53

**「Background」** MiniMax is a Chinese AI company providing LLM APIs through infrastructure partners including AtlasCloud, Novita, and StreamLake—some of which are used by OpenRouter to route requests to MiniMax models. OpenRouter previously marketed certain MiniMax endpoints with a &\#x27;zero data retention&\#x27; guarantee, implying no persistent storage or third-party access to user prompts. The current incident reveals that this claim was invalidated by observable external HTTP requests to test URLs embedded in prompts, correlated in time with model invocations.

**「Impact」** Developers using OpenRouter to access MiniMax models \(e.g., M2.5 or M3\) must assume their prompts—including those containing credentials, PII, or proprietary logic—may have been exposed to third parties via downstream infrastructure \(AtlasCloud, Novita, StreamLake\), requiring immediate API key rotation and avoidance of sensitive inputs until independent verification or remediation is confirmed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.okapi.bot/models/openrouter/minimax/minimax-m2-her/">minimax / minimax -m2-her shutdown: Nov 5, 2026 ( OpenRouter )</a></li>
<li><a href="https://aifree.dev/news/minimax-m31-flash-free-openrouter-space-bunny">MiniMax M3.1 Flash Goes Free on OpenRouter | aifree.dev</a></li>
<li><a href="https://openrouter.ai/zh-CN/minimax/minimax-01">MiniMax -01 - API 定价与提供商 | OpenRouter</a></li>

</ul>
</details>

**Tags**: `#security`, `#ai-ops`, `#api-security`, `#llm-infrastructure`, `#data-privacy`

---

<a id="item-tech-news-9"></a>
### [USB monitor hub caused 75% download speed loss via TCP ACK delays](https://blog.tymscar.com/posts/studiodisplayethernet/) ⭐️ 7.0/10

A developer discovered that routing Ethernet through the USB-C hub built into his Apple Studio Display reduced his 2.5 Gbps symmetrical internet connection to ~600 Mbps—a 75% throughput loss—due to added latency causing TCP ACK timing violations, buffer overflows, and packet drops on the USB-Ethernet adapter. The issue was confirmed via packet capture and resolved by switching to a different USB-Ethernet adapter \(ASIX AX88179\) with more tolerant ACK timing behavior. The problem affected only TCP-based downloads; UDP and local network transfers were unaffected. This is a shipped, empirically measured performance regression in real-world use, not an announced plan or vendor claim.

hackernews · soheilpro · Nov 21, 10:36 · [Discussion](https://news.ycombinator.com/item?id=50587875)

**「TCP Delayed ACK and USB Ethernet Latency」** TCP Delayed ACK is a standard optimization where a receiver waits up to 200 ms \(or until a second packet arrives\) before sending an acknowledgment, reducing overhead in interactive traffic. However, when combined with added latency—such as that introduced by USB hubs in monitor-embedded Ethernet adapters—it can cause ACKs to miss critical timing windows, leading to TCP retransmissions, receive window stalls, and severe throughput degradation.

**「Impact」** Users relying on USB-C monitors with integrated Ethernet hubs for high-speed wired networking may experience severe, undiagnosed TCP throughput degradation—especially on connections above 1 Gbps—and should verify adapter behavior with tools like iperf3 and tcpdump when speeds fall short of expectations.

**「Community discussion」** Commenters clarified that the root cause was not the monitor per se but the USB hub’s latency-induced TCP ACK timing failure, with one noting that a different USB-Ethernet adapter \(ASIX AX88179\) resolved the issue because it required less frequent ACKs; others emphasized that the problem was subtle and went unnoticed until benchmarking revealed the discrepancy.

<details><summary>References</summary>
<ul>
<li><a href="https://apple.stackexchange.com/questions/437555/macos-networking-brutally-slow-using-vnc-or-apple-remote-desktop">macOS networking brutally slow using VNC or Apple Remote Desktop</a></li>
<li><a href="https://www.linkedin.com/pulse/20141113153643-13386347-what-is-delayed-ack-and-how-can-it-be-a-bottleneck-in-your-network">What is Delayed ACK and how can it be a bottleneck in your network.</a></li>

</ul>
</details>

**Tags**: `#networking`, `#usb`, `#tcp`, `#debugging`, `#systems-engineering`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [Why Output Caching Fails for LLM Agents](https://seangoedecke.com/why-output-caching-doesnt-work/) ⭐️ 8.0/10

rss · Sean Goedecke · Nov 21, 00:00

**「Background」** LLM inference economics relies heavily on input caching to avoid recomputing full conversation histories—but output caching is often proposed as a parallel optimization, especially in agent systems where models repeatedly quote code, evidence docs, or prior outputs. Yet this intuition overlooks a critical constraint: visible output constitutes only a small fraction of total output tokens.

**「Solution」** The author analyzes real agent logs and finds that visible user-facing output accounts for just ~6% of total output tokens; the remaining 94% consists of internal reasoning tokens \(50%\) and tool calls \(44%\). Even eliminating \*all\* repetition in visible output—far beyond what’s realistically achievable—yields only ~4% total token savings, per Amdahl’s law. Attempts to reduce repetition via fine-tuning or reference-based prompting \(e.g., &\#x27;src/script.py:12–15&\#x27;\) fail to address the dominant cost driver: inefficient reasoning. Instead, improving model intelligence—reducing reasoning depth and tool call volume—is the high-leverage path: frontier models often cost more per token but use so few tokens overall \(e.g., 6× fewer\) that total inference cost drops.

**「Takeaway」** Optimizing LLM agent cost requires shifting focus from superficial output deduplication to fundamental improvements in reasoning efficiency—because output caching targets a vanishingly small portion of the token budget, while intelligence gains compound across the entire 94% of invisible output.

**Tags**: `#LLM optimization`, `#inference economics`, `#caching`, `#Amdahl&\#x27;s law`, `#agent systems`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Trump Proposes Massive Tax on US Firms Building AI Data Centers Abroad](https://apnews.com/article/trump-artificial-intelligence-data-centers-f1ac03b73d13445400eeed8631d9d879) ⭐️ 7.0/10

Donald Trump proposed a &\#x27;massive tax&\#x27; on U.S. tech companies building AI data centers overseas, aiming to keep such infrastructure in the U.S. and maintain AI competitiveness with China; the proposal is undeveloped, unconfirmed by official channels, and has not been shared with government officials.

telegram · zaihuapd · Nov 21, 03:26

**「Background」** Trump announced the proposal at a White House press conference on November 20, 2026, stating he had not yet shared it with his own administration officials.

<details><summary>References</summary>
<ul>
<li><a href="https://www.politico.com/news/2026/11/20/trump-overseas-data-center-tax-01178999">Trump says he’ll tax companies building data centers outside ...</a></li>
<li><a href="https://www.latintimes.com/trump-ai-data-centers-overseas-tax-threat-601669">Trump&#x27;s surprise data-center threat sends major tech and ...</a></li>
<li><a href="https://www.cnbc.com/2026/11/20/trump-data-centers-ai-companies-tax.html">Trump vows to stop U.S. companies from building data centers ...</a></li>

</ul>
</details>

**Tags**: `#US-China tech competition`, `#AI policy`, `#corporate taxation`, `#infrastructure policy`, `#election-year proposals`

---