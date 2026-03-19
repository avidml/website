---
author: "Subho Majumdar, Harsh Raj"
title: "AVID Announces the Inspect AI connector, contributes Bias Benchmarks"
date: "2026-03-18"
description: "AVID now integrates with the Inspect AI to convert evaluation logs into structured vulnerability reports, with contributions of BBQ and BOLD benchmarks to the `inspect-evals` library."
tags: ["bias", "benchmarks", "evaluation", "performance"]
categories: ["general"]
layout: single
ShowRelated: false
showToc: false
ShowBreadCrumbs: false
---

AVID collects and persists structured evidence of weaknesses and failures in AI systems. A key part of our mission is building integrations with existing AI evaluation tools—making it easy to translate evaluation results directly into shareable, evidence-based reports. Today we are excited to announce our integration with [Inspect AI](https://inspect.ai-safety-institute.org.uk/), the open-source evaluation framework developed by the UK AI Safety Institute.

## What is Inspect AI?

Inspect AI is an open-source framework for evaluating large language models (LLMs). It provides a structured way to define evaluation tasks, score model outputs, and log detailed results. The [inspect-evals](https://github.com/UKGovernmentBEIS/inspect_evals) library extends Inspect with a collection of community-contributed benchmark tasks spanning a wide range of capabilities and harm categories—including bias, toxicity, and fairness.

## Our Contributions: BBQ and BOLD

As part of this integration, AVID contributed two bias-focused benchmarks to the `inspect-evals` library:

- **BBQ** (Bias Benchmark for Question Answering): a dataset of hand-crafted questions targeting social biases across nine demographic dimensions, including age, disability status, gender identity, nationality, physical appearance, race/ethnicity, religion, socioeconomic status, and sexual orientation. BBQ measures whether models rely on stereotypes when context is ambiguous or absent.

- **BOLD** (Bias in Open-Ended Language Generation Dataset): a large-scale dataset for evaluating potential harms in open-ended text generation. BOLD assesses the toxicity and sentiment of model-generated continuations across demographic groups defined by race, gender, religion, political ideology, and profession.

Both benchmarks are available in Inspect Evals under the [Bias category](https://ukgovernmentbeis.github.io/inspect_evals/#category=Bias), alongside other community-contributed evaluations.

## Connecting Inspect AI to AVID

We have built a connector in [avidtools](https://avidml.org/avidtools/) that reads Inspect AI evaluation log files (`.eval`) and converts them into structured AVID reports. The connector extracts model metadata, scorer results, and dataset provenance from each log, and maps them to the AVID report schema. It supports normalization of model developer and deployment platform information to preserve uniqueness of model and model developer names across AVID reports.

The generated reports are published in the [AVID database](https://github.com/avidml/avid-db), capturing evaluation evidence from runs of BBQ and BOLD against several recent language models. These reports join over 700 existing vulnerability reports in the 2026 AVID release.

## Why This Matters

By connecting Inspect AI with AVID, evaluation results produced by anyone using the `inspect-evals` library can be surfaced as structured, citable, and searchable records of model behavior. This is especially important for bias and fairness evaluations, where aggregated evidence across models and deployment contexts helps practitioners make more informed decisions.

This integration exemplifies AVID's broader goal: to build a shared, community-driven evidence base for AI failures and limitations—grounded in reproducible evaluation data rather than anecdote.

---
The Inspect AI connector is part of `avidtools`. Full documentation, including usage examples and the connector API, is available in [our documentation](https://docs.avidml.org/developer-tools/python-sdk/connectors#inspect-ai). Vulnerability reports from BBQ and BOLD evaluations are available in the [latest release](https://github.com/avidml/avid-db/releases/tag/v0.3.2) of AVID.

## Get Involved
If you have an evaluation tool or benchmark you'd like to connect to AVID, [reach out](https://avidml.org/contact/) to us!
