---
title: Database
layout: page
url: /database
---

The database component of AVID houses full-fidelity information (model metadata, harm metrics, measurements, benchmarks, and mitigation techniques if any) on evaluation examples of harm (sub)categories defined by the taxonomy. The aim here is transparent and reproducible model evaluations.
<!-- Because of their ready availability and widespread use, we shall start by evaluating large-scale NLP models that are either open-source or accessible through APIs. -->

AVID is
- Expandable to account for novel and hitherto unknown vulnerabilities
- Enable ML developers can freely share evaluation use cases for the benefit of the community
- Be composed of evaluations submitted in a schematized manner, then vetted and curated.

AVID stores instantiations of AI risks---categorized using the AVID [taxonomy](../taxonomy)---using two base data classes: **Vulnerability** and **Report**. A *vulnerability* (vuln) is a high-level evidence of an AI failure mode, in line with the NIST CVEs. These are linked to the taxonomy through multiple tags, denoting the AI risk domains (Security, Ethics, Performance) this vulnerability pertains to, (sub)categories under that domain, as well as AI lifecycle stages. A *report* is one example of a particular vulnerability occurring, supported by qualitative or quantitative evaluation. Based on the references provided in a specific report, reports can potentially more granular and reproducible than vulnerabilities.

Information about either is schematized and stored in AVID. To learn more about the motivations and technical details of vulns and reports, you can read [this](https://github.com/avidml/.github/tree/main/docs/understanding-avid.pdf) document,or refer to their respective [schema](https://github.com/avidml/avid-db/tree/main/schema) in AVID.



## List of Vulnerabilities

### 2022
| | | | |
|---|---|---|---|
| [AVID-2022-V001](/database/AVID-2022-V001) | [AVID-2022-V002](/database/AVID-2022-V002) | [AVID-2022-V003](/database/AVID-2022-V003) | [AVID-2022-V004](/database/AVID-2022-V004) |
| [AVID-2022-V005](/database/AVID-2022-V005) | [AVID-2022-V006](/database/AVID-2022-V006) | [AVID-2022-V007](/database/AVID-2022-V007) | [AVID-2022-V008](/database/AVID-2022-V008) |
| [AVID-2022-V009](/database/AVID-2022-V009) | [AVID-2022-V010](/database/AVID-2022-V010) | [AVID-2022-V011](/database/AVID-2022-V011) | [AVID-2022-V012](/database/AVID-2022-V012) |
| [AVID-2022-V013](/database/AVID-2022-V013) | | | |


## List of Reports

### 2022
| | | | |
|---|---|---|---|
| [AVID-2022-R0001](/database/AVID-2022-R0001) | [AVID-2022-R0002](/database/AVID-2022-R0002) | [AVID-2022-R0003](/database/AVID-2022-R0003) | [AVID-2022-R0004](/database/AVID-2022-R0004) |
| [AVID-2022-R0005](/database/AVID-2022-R0005) | | | |
