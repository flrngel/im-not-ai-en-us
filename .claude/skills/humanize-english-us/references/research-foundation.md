# Research Foundation — Humanize US v0.1

This file summarizes the scholarly work that shaped the English (US) version. It is not a claim that a rule can prove authorship. The research supports a practical editorial stance: AI-generated and human-written text often differ in surface features, but detectors are fragile across domains, models, paraphrasing, and human co-editing.

## Design takeaways

| Research signal | What the literature suggests | Design choice in this repo |
|---|---|---|
| Detection is broad and contested | Modern surveys group approaches into watermarking, statistical, neural, and human-assisted methods, and emphasize out-of-distribution, adversarial, real-world-data, and evaluation problems. | Treat “AI tells” as editing cues, not authorship verdicts. |
| Stylometry still matters | Short-sample stylometry can encode lexical, grammatical, syntactic, and punctuation patterns and distinguish several human/LLM classes in controlled settings. | The taxonomy is organized by lexical, syntax, rhythm, connector, punctuation, and formatting patterns. |
| Human prose has more variability | Recent detection work highlights fluctuations in lexical and structural unpredictability; human writing often varies rhythm and surprise more than LLM outputs. | Category E focuses on sentence-length variation, paragraph rhythm, and “too-even” cadence. |
| Vocabulary shifts are measurable | PubMed and arXiv studies show spikes or changes in LLM-favored words such as “delve” and “significant.” Spoken academic discourse also shows measurable increases in ChatGPT-preferred words. | Category B flags stock LLM vocabulary, but only as density/context signals, not automatic deletions. |
| Vocabulary lists alone are weak | Work on GPTZero’s AI Vocabulary finds transparent word lists useful for explanation but limited as standalone detectors, especially beyond one generator/domain. | Single words are S2/S3 unless repeated or paired with other signals. |
| Paraphrasing breaks many detectors | A NeurIPS paper showed paraphrasing can evade multiple detectors without much semantic change. | This repo avoids detector-evasion claims and uses fidelity audits rather than detector-score goals. |
| Human judgment is biased | ACL 2025 work found raters often favored text labeled “Human Generated” even when labels were swapped. | The output summary avoids “human/AI proof” language and reports only concrete edits. |

## Sources

- Wu, Junchao, Shu Yang, Runzhe Zhan, Yulin Yuan, Lidia Sam Chao, and Derek Fai Wong. 2025. “A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions.” *Computational Linguistics* 51(1):275–338. DOI: 10.1162/coli_a_00549. https://aclanthology.org/2025.cl-1.8/
- Przystalski, Karol, Jan K. Argasiński, Iwona Grabska-Gradzińska, and Jeremi K. Ochab. 2025. “Stylometry recognizes human and LLM-generated texts in short samples.” arXiv:2507.00838. https://arxiv.org/abs/2507.00838
- Basani, Advik Raj, and Pin-Yu Chen. 2026. “Diversity Boosts AI-Generated Text Detection.” *Transactions on Machine Learning Research*. arXiv:2509.18880. https://arxiv.org/pdf/2509.18880
- Kobak, Dmitry, Rita González-Márquez, Emőke-Ágnes Horvát, and Jan Lause. 2024. “Delving into LLM-assisted writing in biomedical publications through excess vocabulary.” arXiv:2406.07016. https://arxiv.org/abs/2406.07016
- Geng, Ming, et al. 2025. “Human-LLM Coevolution: Evidence from Academic Writing.” arXiv:2502.09606. https://arxiv.org/abs/2502.09606
- Yakura, Hiromichi, et al. 2024. “Empirical evidence of Large Language Model's influence on human spoken communication.” arXiv:2409.01754. https://arxiv.org/abs/2409.01754
- Schmalz, Verena J. 2025. “Can GPTZero's AI Vocabulary Distinguish Between LLM- and Student-Written Texts?” BEA 2025. https://aclanthology.org/2025.bea-1.71/
- Krishna, Kalpesh, Yixiao Song, Marzena Karpinska, John Wieting, and Mohit Iyyer. 2023. “Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense.” NeurIPS 2023. https://arxiv.org/abs/2303.13408
- Zhu, Tiffany, Iain Weissburg, Kexun Zhang, and William Yang Wang. 2025. “Human Bias in the Face of AI: Examining Human Judgment Against Text Labeled as AI Generated.” Findings of ACL 2025. https://aclanthology.org/2025.findings-acl.1329/
- Terčon, Luka. 2025. “Linguistic Characteristics of AI-Generated Text: A Survey.” arXiv:2510.05136. https://arxiv.org/pdf/2510.05136

## Practical interpretation

This project takes the conservative interpretation of the literature:

1. Surface cues can help editors find generic, flat, or formulaic prose.
2. Surface cues cannot reliably prove authorship.
3. A rewrite system should optimize clarity, specificity, rhythm, and fidelity, not detector evasion.
4. High-stakes contexts require human review and policy compliance.
