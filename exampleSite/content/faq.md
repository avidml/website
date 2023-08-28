---
title: Frequently Asked Questions (FAQ)
layout: legal # is necessary
url: /faq
---

### What is an AI Vulnerability?
AI vulnerabilities not only include the classic [security-related vulnerabilities](https://nvd.nist.gov/vuln) that can be exploited by malicious actors, but also modes of unintentional failures---such as demographic biases in a dataset or model, incomplete/insufficient/poor quality datasets, high sensitivity of a model to small changes in the input data---that may have lasting impact on the world around us.

### Why do we need AVID?
As the datasets and models that form the core of AI-based decision making systems become more complex, the practitioner community faces the daunting task of shipping models with very little structured, reproducible information on their downstream risks. AVID will enable practitioners to (a) think about AI risks in a structured manner, and (b) inform and informed by the knowledge of the community by freely sharing risk evaluations of widely used AI models and datasets.

### How is this different from [MITRE ATLAS](https://atlas.mitre.org)?
The goal of MITRE ATLAS is to house a comprehensive taxonomy and supporting case studies to organize the different modes by which an AI model can be intentionally attacked  or exploited.  In addition to attacks, AVID intends to categorize unintentional failures pertaining to models and datasets, and house instances of such failures.

### How is this different from [AI Incident Database (AIID)](https://incidentdatabase.ai)?
AIID contains case studies/reports of failures of deployed AI systems. In addition to storing information on system-level failures, AVID (a) contains reproducible details down to specific models and datasets, and (b) organizes failure modes by a granular, operational taxonomy.

### Why would companies open up their proprietary models and datasets to you?
They don't need to if they don't want to! AVID can be useful in multiple ways, only one of them involves working with proprietary models or datasets. Beyond that, data scientists and ML engineers can benefit from having the information of known issues related to open-source resources (e.g. values of bias metrics for bert-base-uncased) when they adopt these resources into their workflow. Even without relevant use cases, the AVID taxonomy will provide valuable guidance to ML project scoping and auditing.

**Have another question? [Ask us](mailto:avid.mldb@gmail.com) and we'll get back to you!**
