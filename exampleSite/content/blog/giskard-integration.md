---
author: "Matteo Dora, Subho Majumdar"
title: "AVID Announces Integration with Giskard Scan"
date: "2024-01-31"
description: "Giskard Scan results can now be exported as AVID reports."
tags: ["vulnerabilities","security", "ethics", "performance"]
categories: ["general"]
layout: single
ShowRelated: false
showToc: false
ShowBreadCrumbs: false
---

The AI Vulnerability Database (AVID) is the first open-source knowledge base of failure modes of AI models, datasets, and systems. Today, we are pleased to announce the integration of Giskard with AVID! In this blog post we give an overview on how to structure results from Giskard LLM Scans into AVID’s reporting schema, that you can submit into AVID or use for your own purposes!

## What is Giskard Scan?

[Giskard](https://www.giskard.ai/) is an open-source testing framework dedicated to ML models, covering any Python model, from tabular to LLMs.

Testing machine learning applications can be tedious: Where to start testing? Which tests to implement? What issues to cover? How do we implement the tests? Some of the most critical vulnerabilities that affect LLMs are prompt injection, sensitive information disclosure, and hallucination. Giskard's scan feature ensures the identification of these hidden vulnerabilities—and many others. The library generates a comprehensive report which quantifies these into interpretable metrics, crafts domain-specific tests, and leverages the Quality Assurance best practices of the open-source community.
For more information, you can check Giskard's documentation following [this link](https://docs.giskard.ai/en/latest/getting_started/quickstart/quickstart_llm.html).

## Why Integrate?

The AVID project has two focus areas:
- A **Taxonomy** of failure modes of AI systems across the categories of security, ethics, and performance
- A **Database** of reports about such failures, containing detailed and structured information about each failure event

The Giskard scan is a powerful tool to detect vulnerabilities in your AI models, from traditional ML to LLMs. Its integration with AVID resources provides improved **standardized reporting of vulnerabilities**, and the ability to share your vulnerability reports with the community.
How does it work?
The Giskard python library provides an automatic scan functionality designed to automatically detect potential vulnerabilities affecting your LLMs. For examples of how to use its LLM scanning capabilities, check out [these tutorials](https://docs.giskard.ai/en/task-avid-docs-gsk-2195/tutorials/llm_tutorials/index.html).

Once you run a Giskard scan, you can export your Giskard scan report as an AVID report. First, make sure you have installed the avidtools package in your environment:

```bash
pip install avidtools
```

Then, you can export the report as an AVID report:

```python
import giskard as gsk

scan_report = gsk.scan(my_model, my_dataset)
avid_reports = scan_report.to_avid()
```

You can also export these reports directly in a JSONL file (one AVID report per line):

```python
scan_report.to_avid("avid_report.jsonl")
```

All Giskard scan detectors are assigned AVID taxonomy categories by default. When you display a report coming out of such scans, it shows the AVID taxonomy categories by default.

For more details, check out Giskard [docs](https://docs.giskard.ai/en/latest/integrations/avid/index.html), as well as this [Tutorial](https://docs.giskard.ai/en/latest/integrations/avid/avid-integration-llm.html).

## The Way Forward
As you use Giskard and find novel LLM vulnerabilities, we encourage you to report your findings to AVID using the above reporting schema. Also feel free to use AVID resources for your own purposes, or contribute to their open-source work!


---

## About the Authors

[Matteo Dora](https://www.linkedin.com/in/mattbit/) is a machine learning researcher at Giskard, where he leads the LLM safety team. His work focuses on the practical applications and implications of AI, emphasizing the intersection of ethics, safety, and security. With his current team, Matteo has developed a unique expertise in conducting red team assessments of generative AI applications. Prior to this, he worked as an academic researcher in the field of neuroscience and applied mathematics.

[Subho Majumdar](https://www.subhomajumdar.com/) is a technical leader in applied trustworthy AI who believes in a community-centric approach to data-driven decision-making. He has pioneered the use of trustworthy AI methods in industry settings, wrote a [book](https://www.amazon.com/Practicing-Trustworthy-Machine-Learning-Transparent/dp/1098120272), and founded multiple nonprofit efforts in this area---TrustML, Bias Buccaneers, and AVID. Currently, Subho is Co-founder and Head of AI at [Vijil](https://vijil.ai/), an AI software startup on a mission to help developers build and operate intelligent agents that people can trust.