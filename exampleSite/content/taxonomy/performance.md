---
title: Performance
layout: page
---

This domain is intended to codify deficiencies such as privacy leakage or lack or robustness.

| ID | | Name | Description |
|---|---|---|---|
| P0100 | | Data issues | Problems arising due to faults in the data pipeline |
| | P0101 | Data drift | Input feature distribution has drifted |
| | P0102 | Concept drift | Output feature/label distribution has drifted |
| | P0103 | Data entanglement | Cases of spurious correlation and proxy features |
| | P0104 | Data quality issues | Missing or low-quality features in data |
| | P0105 | Feedback loops | Unaccounted for effects of an AI affecting future data collection |
| P0200 | | Robustness | Ability for the AI to perform as intended in diverse circumstances |
| | P0201 | Resilience/stability | Ability for outputs to not be affected by small change in inputs |
| | P0202 | OOD generalization | Test performance doesn’t deteriorate on unseen data in training |
| | P0203 | Scaling | Training and inference can scale to high data volumes |
| P0300 | | Privacy | Protect leakage of user information as required by rules and regulations |
| | P0301 | Anonymization | Protects through anonymizing user identity |
| | P0302 | Randomization | Protects by injecting noise in data, eg. differential privacy |
| | P0303 | Encryption | Protects through encrypting data accessed |
| P0400 | | Safety | Minimizing maximum downstream harms |
| | P0401 | Psychological Safety | Safety from unwanted digital content, e.g. NSFW |
| | P0402 | Physical safety | Safety from physical actions driven by a AI system |
| | P0403 | Socioeconomic safety | Safety from socioeconomic harms, e.g. harms to job prospects or social status |
| | P0404 | Environmental safety | Safety from environmental harms driven by AI systems |



