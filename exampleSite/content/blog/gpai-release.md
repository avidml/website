---
author: "Subho Majumdar"
title: "What's New in AVID: AI Vulnerability Database Rebuilt for the Age of AI Agents"
date: "2026-03-04"
description: "AVID releases a major update, with focus on general-purpose AI failures."
tags: ["vulnerabilities"]
categories: ["release"]
layout: single
ShowRelated: false
showToc: false
ShowBreadCrumbs: false
---

When we launched AVID more than three years ago, the AI landscape looked very different, arguably much simpler. From specific ML/AI systems driving narrow decision making, the world has moved to general-purpose AI (GPAI) systems: LLM and genAI-powered applications, agentic workflows, developer tooling, retrieval-augmented generation (RAG) pipelines, and multiagent systems that millions of people interact with daily.

With the expansion of scope, came the expansion of attack surface. Every new capability is a potential new attack vector, exploit, or hazard. Thanks to the Cursors of the world, vibe-coders are shipping so many capabilities every day that security practitioners and safety researchers can hardly keep up with the detection and tracking of the limits of those capabilities.

## A new AVID

Today, we are releasing a broad update of AVID, covering a host of architectural changes, and more importantly new reports of AI vulnerabilities and failures.

The need for a centralized knowledge base for what could go wrong with AI has never been more urgent. In light of how AI has taken off and the focus on AI security and safety has sharpened, we decided to take a second look at AVID. The most fundamental shift is in what AVID covers. Instead of *all* ML/AI models and systems, from now on we will cover the stack for building **general-purpose AI (GPAI) systems**: a category that includes
1. Open-weight generative models
2. Closed-API systems, including assistants (ChatGPT, Claude.ai) and general-purpose APIs (GPT series, Claude series)
3. GPAI developer tools and libraries
4. End-to-end AI applications, agents, and multiagent systems.

This change reflects the reality that many consequential AI failures today happen at the system level: such as a path traversal vulnerability in DB-GPT ([AVID-2026-R0010](https://avidml.org/database/AVID-2026-R0010)), an authorization bypass in Lunary ([AVID-2026-R0004](https://avidml.org/database/AVID-2026-R0004)), a prompt injection leading to remote code execution in GPT Academic ([AVID-2026-R0018](https://avidml.org/database/AVID-2026-R0018)). These are the kinds of failures that AVID now catalogs, in addition to traditional LLM red teaming results using tools such as garak.

In total, we have added 277 new vulnerability reports in this new release, which cover
- GPAI Supply Chain Vulnerability CVEs, obtained from AI Security Digests by [Mileva](https://milev.ai/)
- LLM red teaming results from [garak](https://github.com/NVIDIA/garak), [Inspect AI](https://inspect.aisi.org.uk/), and [0DIN](https://0din.ai/) jailbreak scans
- Published CVEs related to OpenClaw, thanks to [OpenClawCVEs](https://github.com/jgamblin/OpenClawCVEs/)
- A number of crowdsourced failures reported by Wiz, The Browser Company, and Mindgard.ai.

We will *not* be adding new vulnerabilities for the time being, keeping all new submissions as reports. This is because the community is yet to zero in on a broadly agreed-upon definition of AI vulnerability. We want to respect that, and would like to work together with practitioner and research organizations on an accepted standard definition.

> We have preserved our older records as legacy entries, with a note that pre-2025 entries were curated under a broader AI/ML scope.

## Updated Developer tools and Documentation

The biggest addition for practitioners is the expanded Python SDK (`avidtools`). Beyond the Pydantic data models that define AVID's report and vulnerability schemas, the SDK now contains connectors and integrations that pull data from external sources and structure them as AVID records. You can import MITRE ATLAS case studies, NIST NVD entries by CVE ID, as well as ingest LLM red teaming scan results by garak, and safety evaluations from Inspect AI.

There is one feature we particularly love. It is the **URL connector**. We now have an agentic workflow, in `avidtools.connectors.url`, that automatically scrapes information and structures it into a submission-ready vulnerability report from just a single URL. Filling out multiple fields in a long form is a pain point almost all of our early vulnerability submitters faced. With this connector we are solving that.

The SDK, connectors, and integrations are designed to position AVID as something broader than just a database. We want AVID to power the public-interest infrastructure for AI safety that can pull from open-source AI vulnerability scanners and audit tools to populate itself, and pass on that information to development teams across the world that are building GPAI systems. This way, we help the community make structured vulnerability record-keeping a part of the GPAI development workflow rather than an afterthought.

All changes are now live in `avidtools`, with usage information in our documentation site: [docs.avidml.org](https://docs.avidml.org/).

## The Taxonomy Library

The last major architectural change concerns the handling of failure classification. In the original AVID, our taxonomy—the SEP (Security, Ethics, Performance) framework with its Effect and Lifecycle views—was *the* taxonomy. Every record was mapped to it.

We have now introduced the **Taxonomy Library**: a growing collection of classification frameworks where the AVID taxonomy is one of several reference schemes. Taxonomies are shared using the standardized [MISP](https://www.misp-project.org/datamodels/) format, which means any organization can bring their own risk framework and map AVID records to it. As a user of AVID, you can use AVID's SEP categories, CVSS risk scores, MITRE ATLAS techniques, or your own internal classification: all against the same underlying database of evidence.

This matters because no single taxonomy captures the full spectrum of what could go wrong: even more so for a nascent area like AI. A security team thinks in CVSS scores, a policy team thinks in regulatory categories, an ML engineer thinks in lifecycle stages. The Taxonomy Library lets all of them work from the same evidence base without forcing a single classification lens.

## What's Next

Going forward, we will continue to grow the database with one release every 1-2 weeks, focusing on expanding coverage in breadth and depth. We are also working on a number of new features and connectors for richer sourcing of GPAI failures. Stay tuned for all of these.

---

Explore the updated AVID at [avidml.org](https://avidml.org). Browse the database, read the docs, or [submit a vulnerability](https://docs.google.com/forms/d/e/1FAIpQLSe-jxZrx257Xce7JTa_QeaQmmQEQJfLlrBKjSzgHtNs5T-oKg/viewform?usp=dialog). AVID is a project of the [AI Risk and Vulnerability Alliance (ARVA)](https://avidml.org/arva), a U.S. 501(c)(3) nonprofit.