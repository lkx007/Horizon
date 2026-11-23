# Evaluation goal

Evaluate whether a practicing engineer who already ships LLM features would learn a transferable AI-native practice. Score the writing, not the vendor. The reader is not a beginner: do not reward API walkthroughs, RAG tutorials, or language-specific starter guides. Do not require the example to be Java, and do not treat a Java stack as more relevant than any other production stack.

# Section tag

Include exactly one of these section ids as a tag, copied verbatim:

- `ai-native-product` — product redesign around model capability
- `ai-native-workflow` — team workflow, division of work, or quality control
- `ai-native-cases` — an implementation method with results and failure lessons

Add two to four more specific tags. Do not invent a fourth section id.

# Scoring rubric

- **9-10: Field record.** A first-hand postmortem or open implementation. It states the method, the conditions, a sourced outcome, and a real failure or limit.
- **7-8: High value.** Concrete and reusable. A practitioner can tell where it applies and what was measured versus what the author believes.
- **5-6: Partial.** One real case, but thin on conditions, failures, or the difference between a measurement and a claim.
- **3-4: Weak.** Concept essay, chat-wrapper announcement, marketing case study, or a beginner tutorial dressed as experience.
- **0-2: Noise.** Off-topic, promotional, or too vague to try.

# Evaluation guidance

Prefer first-hand postmortems, concrete methods, and open-source examples. Reject marketing and concept fluff. A claimed speedup, quality gain, or cost cut counts only when the source states how it was observed. Separate that observation from the author's advice. Use of a model inside an unchanged product is not AI-native product design.
