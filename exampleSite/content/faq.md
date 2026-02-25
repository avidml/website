---
title: Frequently Asked Questions (FAQ)
layout: legal # is necessary
url: /faq
---

### What is an AI Vulnerability?
AI vulnerabilities include classic [security-related vulnerabilities](https://nvd.nist.gov/vuln) that can be exploited by malicious actors, as well as unintentional failures (for example, harmful bias, unsafe model behavior, brittleness, or poor performance under realistic conditions). AVID focuses on vulnerabilities in general-purpose AI (GPAI) systems, including LLMs, API-only AI systems, developer tools, and end-to-end applications and agents.

### Why do we need AVID?
As GPAI systems become widely deployed, practitioners need structured and reproducible information about concrete failures. AVID provides a community database of reported GPAI failures so builders can learn from prior evidence, evaluate similar systems, and share findings in a common format.

### How is this different from [MITRE ATLAS](https://atlas.mitre.org)?
MITRE ATLAS focuses on adversarial tactics and techniques against AI systems: predictive and generative. AVID has a narrower system focus on GPAI systems, and a broader focus on observed and evaluated GPAI failures that include but is not limited to security vulnerabilities in the GPAI lifecycle. It also supports mapping records to multiple taxonomies, including AVID taxonomy and external frameworks such as ATLAS.

### How is this different from [AI Incident Database (AIID)](https://incidentdatabase.ai)?
AIID tracks incidents and narratives around deployed AI failures. AVID emphasizes technical, reproducible records for GPAI systems, components, and applications, with structured metadata and evaluation evidence.

### Why would companies open up their proprietary models and datasets to you?
They don't need to if they don't want to. AVID supports public reporting based on open-source assets, closed-box testing of closed APIs, and evaluations of end-to-end applications and agents. Teams can benefit from known failure evidence even without sharing proprietary internals.

**Have another question? [Ask us](mailto:avid.mldb@gmail.com) and we'll get back to you!**
