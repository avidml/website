---
title: Security
layout: page
---

This domain is intended to codify the landscape of threats to a ML system.

| ID | | Name | Description |
|---|---|---|---|
| S0100 | | Software Vulnerability | Vulnerability in system around model---a traditional vulnerability |
| S0200 | | [Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010/) | Compromising development components of a ML model, e.g. data, model, hardware, and software stack. |
| | S0201 | Model Compromise | Infected model file |
| | S0202 | Software compromise | Upstream Dependency Compromise |
| S0300 | | Over-permissive API | Unintended information leakage through API |
| | S0301 | Information Leak | Cloud Model API leaks more information than it needs to |
| | S0302 | Excessive Queries | Cloud Model API isn’t sufficiently rate limited |
| S0400 | | [Model Bypass](https://atlas.mitre.org/techniques/AML.T0015/) | Intentionally try to make a model perform poorly |
| | S0401 | Bad Features | The model uses features that are easily gamed by the attacker |
| | S0402 | Insufficient Training Data | The bypass is not represented in the training data |
| | S0403 | Adversarial Example | Potential Cause: Over permissive API |
| S0500 | | [Exfiltration](https://atlas.mitre.org/techniques/AML.T0024/) | Directly or indirectly exfiltrate ML artifacts |
| | S0501 | Model inversion | Reconstruct training data through strategic queries |
| | S0502 | Model theft | Extract model functionality  through strategic queries |
| S0600 | | [Data poisoning](https://atlas.mitre.org/techniques/AML.T0020/) | Usage of poisoned data in the ML pipeline |
| | S0601 | Ingest Poisoning | Attackers inject poisoned data into the ingest pipeline |

> **NOTE**  
A number of categories map directly to techniques codified in MITRE ATLAS. In future, we intend to cover the full landscape of adversarial ML attacks under the Security domain.