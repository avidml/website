---
title: Database
layout: page
url: /database
---

The database component of AVID houses full-fidelity information (model metadata, harm metrics, measurements, benchmarks, and mitigation techniques if any) on evaluation examples of harm (sub)categories defined by the taxonomy. The aim here is transparent and reproducible evaluations. It
<!-- Because of their ready availability and widespread use, we shall start by evaluating large-scale NLP models that are either open-source or accessible through APIs. -->
- Is expandable to account for novel and hitherto unknown vulnerabilities
- enables AI developers can freely share evaluation use cases for the benefit of the community
- Is composed of evaluations submitted in a schematized manner, then vetted and curated.

AVID stores instantiations of AI risks---categorized using the AVID [taxonomy](../taxonomy)---using two base data classes: **Vulnerability** and **Report**. A *vulnerability* (vuln) is a high-level evidence of an AI failure mode, in line with the NIST CVEs. A *report* is one example of a particular vulnerability occurring, supported by qualitative or quantitative evaluation.

Information about either is schematized and stored in AVID. To learn more about the motivations and technical details of vulns and reports, you can read [this](https://github.com/avidml/.github/tree/main/docs/understanding-avid.pdf) document, or refer to their respective [schema](https://github.com/avidml/avid-db/tree/main/schema) in AVID.

## Vulnerability
Vulnerabilities are linked to the taxonomy through multiple tags, denoting the AI risk domains (Security, Ethics, Performance) this vulnerability pertains to, (sub)categories under that domain, as well as AI lifecycle stages. A vulnerability in AVID can pertain to one or more of the three levels: *dataset*, *model*, or *system*.

### List of Vulnerabilities

##### 2022
| | | | |
|---|---|---|---|
| [AVID-2022-V001](/database/AVID-2022-V001) | [AVID-2022-V002](/database/AVID-2022-V002) | [AVID-2022-V003](/database/AVID-2022-V003) | [AVID-2022-V004](/database/AVID-2022-V004) |
| [AVID-2022-V005](/database/AVID-2022-V005) | [AVID-2022-V006](/database/AVID-2022-V006) | [AVID-2022-V007](/database/AVID-2022-V007) | [AVID-2022-V008](/database/AVID-2022-V008) |
| [AVID-2022-V009](/database/AVID-2022-V009) | [AVID-2022-V010](/database/AVID-2022-V010) | [AVID-2022-V011](/database/AVID-2022-V011) | [AVID-2022-V012](/database/AVID-2022-V012) |
| [AVID-2022-V013](/database/AVID-2022-V013) | | | |

##### 2023
| | | | |
|---|---|---|---|
| [AVID-2023-V001](/database/AVID-2023-V001) | [AVID-2023-V002](/database/AVID-2023-V002) | [AVID-2023-V003](/database/AVID-2023-V003) | [AVID-2023-V004](/database/AVID-2023-V004) |
| [AVID-2023-V005](/database/AVID-2023-V005) | [AVID-2023-V006](/database/AVID-2023-V006) | [AVID-2023-V007](/database/AVID-2023-V007) | [AVID-2023-V008](/database/AVID-2023-V008) |
| [AVID-2023-V009](/database/AVID-2023-V009) | [AVID-2023-V010](/database/AVID-2023-V010) | [AVID-2023-V011](/database/AVID-2023-V011) | [AVID-2023-V012](/database/AVID-2023-V012) |
| [AVID-2023-V013](/database/AVID-2023-V013) | [AVID-2023-V014](/database/AVID-2023-V014) | [AVID-2023-V015](/database/AVID-2023-V015) | [AVID-2023-V016](/database/AVID-2023-V016) |
| [AVID-2023-V017](/database/AVID-2023-V017) | [AVID-2023-V018](/database/AVID-2023-V018) | [AVID-2023-V019](/database/AVID-2023-V019) | [AVID-2023-V020](/database/AVID-2023-V020) |
| [AVID-2023-V021](/database/AVID-2023-V021) | [AVID-2023-V022](/database/AVID-2023-V022) | [AVID-2023-V023](/database/AVID-2023-V023) | [AVID-2023-V024](/database/AVID-2023-V024) |
| [AVID-2023-V025](/database/AVID-2023-V025) | [AVID-2023-V026](/database/AVID-2023-V026) | [AVID-2023-V027](/database/AVID-2023-V027) | |

## Reports
Reports are occurrences of a vulnerability. Based on the references provided in a specific report, reports can potentially more granular and reproducible than vulnerabilities. We classify reports in four types, in increasing degree of quantitative evidence:
1. *Issue*: qualitative evaluation based on a single sample or handful of samples,
2. *Advisory*: qualitative evaluation based on multiple Incidents,
3. *Measurement*: quantitative evaluation with associated data and metric,
4. *Detection*: A Measurement deemed critical by a threshold or statistical test.

These types are reminiscent of the [three levels of AI Auditing](https://informationashvins.wordpress.com/2022/11/29/three-levels-of-ai-auditing/), and accommodate diverse AI evaluation scenarios from the user perspective.

### List of Reports

#### 2022
| | | | |
|---|---|---|---|
| [AVID-2022-R0001](/database/AVID-2022-R0001) | [AVID-2022-R0002](/database/AVID-2022-R0002) | [AVID-2022-R0003](/database/AVID-2022-R0003) | [AVID-2022-R0004](/database/AVID-2022-R0004) |
| [AVID-2022-R0005](/database/AVID-2022-R0005) | | | |

#### 2023
| | | | |
|---|---|---|---|
| [AVID-2023-R0001](/database/AVID-2023-R0001) | [AVID-2023-R0002](/database/AVID-2023-R0002) | [AVID-2023-R0003](/database/AVID-2023-R0003) | |