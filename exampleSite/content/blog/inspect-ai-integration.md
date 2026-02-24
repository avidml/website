---
author: "Subho Majumdar"
title: "AVID + Inspect AI: Integration and Enrich Workflow"
date: "2026-02-23"
description: "How the AVID Inspect AI connector works, our contributed benchmarks, and the enrich workflow for generated reports."
tags: ["vulnerabilities", "security", "ethics", "performance", "evaluation"]
categories: ["general"]
layout: single
ShowRelated: false
showToc: false
ShowBreadCrumbs: false
---

The AVID Inspect AI connector makes it straightforward to turn evaluation results into structured AVID reports, so teams can track, share, and operationalize model weaknesses consistently.

If you are new to the connector, start with the official integration docs:

- [Inspect AI integration in the AVID Python SDK](https://docs.avidml.org/developer-tools/python-sdk/integrations/inspect-ai)

This post focuses on two things:

- what the Inspect AI integration gives you,
- and how to run the **enrich** workflow on generated reports.

## What the integration does

Inspect evaluations are rich and detailed, but those results are often hard to compare across teams and tooling. AVID gives you a common schema and taxonomy for documenting failure modes across security, ethics, and performance dimensions.

With the connector + AVID workflow, you can:

- normalize report structure for consistency,
- keep evidence and metadata in one place,
- and enrich reports before downstream publication.

## Our Inspect AI benchmark contributions

We have contributed two benchmarks in the Inspect AI **Bias** category.

- Browse the Bias category here: [Inspect AI evaluations — Bias](https://inspect.aisi.org.uk/evals/#category=Bias)

These benchmark contributions help teams evaluate bias-related risks with a shared open ecosystem and then report findings in AVID-compatible form.

## Enrich workflow

Once you have generated AVID-compatible files from Inspect runs, run enrich in place to normalize and validate report content.

### Enrich with `inspect.py`

Run enrich on your Inspect-converted report file:

```bash
python scripts/review/inspect.py reports/2025/AVID-2025-R0003.json
```

What this does:

- applies Inspect-specific cleanup and text normalization,
- enforces schema alignment used by AVID tooling,
- rewrites the input file in place.

## Recommended pattern for enrich

For repeatable team workflows:

- keep generated artifacts under `reports/review/`,
- run the tool-specific enricher (`inspect.py` here),
- use `default.py` for generic JSON/JSONL enrich where appropriate,
- use `garak.py` for Garak-specific enrich behavior.

## Minimal command sequence

```bash
# enrich (inspect-specific)
python scripts/review/inspect.py reports/2025/AVID-2025-R0003.json
```

## Final notes

The Inspect AI connector gives you a solid bridge from evaluation output to standardized AVID reporting. Once this is in your pipeline, enrich becomes a predictable, auditable quality gate instead of ad hoc file handling.

If you are integrating this in CI, treat enrich as a required validation step before any downstream release workflow.
