---
title: Taxonomy
image: "/uploads/avid.png"
layout: page
---

<!-- The AVID taxonomy consists of categories and subcategories of potential harms encompassing coordinates of responsible AI,such as fairness, robustness, privacy, explainablity, reliability, and alignment. Similar to the [MITRE ATT&CK](http://attack.mitre.org/) framework for cybersecurity risks and [MITRE ATLAS](https://atlas.mitre.org/) for adversarial ML threats, the AVID taxonomy will set a common, open standard to evaluate ML systems for downstream responsible behavior. Compared to MITRE ATLAS which pertains to intentional attacks on ML systems, the AVID taxonomy will cover the area of *ML failures* that are often unintentional in nature. -->

The AVID taxonomy is intended to serve as a common foundation for data science/AI engineering, product, and policy teams to manage potential risks at different stages of a developing an AI system. In spirit, this taxonomy is analogous to [MITRE ATT&CK](http://attack.mitre.org/) for cybersecurity vulnerabilities, and [MITRE ATLAS](https://atlas.mitre.org/) for adversarial attacks on ML systems.

At a high level, the AVID taxonomy consists of two views, intended to facilitate the work of two different user personas.

- **Effect view:** for the *auditor* persona that aims to assess risks for a ML system of components of it. 
- **Lifecycle view:** for the *developer* persona that aims to build an end-to-end ML system while being cognizant of potential risks.

Based on case-specific needs, people involved with building a ML system may need to operate as either of the above personas.

## Effect (SEP) view

The domains, categories, and subcategories in this view provide a 'risk surface' for the AI artifact being evaluated, may it be a dataset, model, or the whole system. This view contains three top-level domains:


<!-- | [Security](./security) || [Ethics](./ethics) || [Performance](./performance) ||
|---|---|---|---|---|---|
Software Vulnerability || Bias/Discrimination | Group fairness | Data issues | Data drift |
Supply Chain Compromise	| Model Compromise || Individual fairness ||		Concept drift |
|| Software compromise	| Explainability | Global explanations || Data entanglement |
Over-permissive API	| Information Leak || Local explanations ||	Data quality issues |
|| Excessive Queries | User actions	| Toxicity || Feedback loops |
| Model Bypass	| Bad Features || Polarization/ Exclusion | Robustness | Resilience/stability |
|| Insufficient Training Data | Misinformation | Deliberative Misinformation ||	OOD generalization |
|| Adversarial Example || Generative Misinformation || Scaling |
| Exfiltration	| Model inversion ||| Privacy | Anonymization |
|| Model theft |||| Randomization |
Data poisoning	| Ingest Poisoning ||||	Encryption |
||||| Safety	| Psychological Safety |
|||||| Physical safety |
|||||| Socioeconomic safety |
|||||| Environmental safety | -->

Each domain is divided into a number of categories and subcategories, each of which is assigned a unique identifier. Figure 1 presents a holistic view of this AVID taxonomy matrix. See the individual pages for [Security](./security), [Ethics](./ethics), [Performance](./performance) for more details.

| ![matrix.png](/uploads/matrix.png) |
|:--:|
| *Figure 1.* The AVID Taxonomy Matrix. |

## Lifecycle view

The stages in this view represent high-level sequential steps of a typical ML workflow. Following the widely-used Cross-industry standard process for data mining ([CRISP-DM](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining)) framework, we designate six stages in this view.

| ID | Stage |
| --- | --- |
| L01 | Business Understanding |
| L02 | Data Understanding |
| L03 | Data Preparation |
| L04 | Model Development |
| L05 | Evaluation |
| L06 | Deployment |

Figure 2 reconciles the two different views of the AVID taxonomy. We conceptually represent the potential space of risks in three dimensions, consisting of the risk domain—S, E, or P—a specific vuln pertains to; the (sub)category within a chosen domain; and the development lifecycle stage of a vuln. The SEP and lifecycle views are simply two different sections of this three-dimensional space.

| ![views.png](/uploads/views-small.png) |
|:--:|
| *Figure 2.* SEP and Lifecycle views of the AVID taxonomy represent different sections of the space of potential risks in an AI development workflow. |
