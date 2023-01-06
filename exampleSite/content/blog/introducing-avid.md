---
author: "Subho Majumdar"
title: "Introducing AVID v0.1"
date: "2023-01-06"
description: "The First AVID Taxonomy and Database is now Live!"
tags: ["community","vulnerabilities","taxonomy"]
layout: single
categories: ["general"]
ShowRelated: false
showToc: false
ShowBreadCrumbs: false
disableAnchoredHeadings: true
---

We at AI Vulnerability Database (AVID) are proud to unveil the very first ever release (v0.1) of our taxonomy and database of AI failures to the public.
This was the result of many hours of collaborations, debates, and meetings, inside and outside the AVID community. I am grateful to the contributors to this exercise.

As a short introduction to AVID, we have two main focus areas: the Taxonomy and The Database.

### Taxonomy
This is intended to serve as a common foundation for data science/AI engineering, product, and policy teams to manage potential risks at different stages of a developing an AI system. In spirit, this taxonomy is analogous to [MITRE ATT&CK](http://attack.mitre.org/) for cybersecurity vulnerabilities, and [MITRE ATLAS](https://atlas.mitre.org/) for adversarial attacks on ML systems.

The AVID Taxonomy has two views: an effect view, aimed at the *auditor* user persona, and an lifecycle view, aimed at the *developer* persona of users.
The effect view has three domains of harms Security, Ethics, and Performance. Each domain is divided into multiple categories and subcategories.
The lifecycle view represents sequential steps of a typical AI development workflow, adapted from the [CRISP-DM](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining) framework.

For more details about the taxonomy, go to: https://avidml.org/taxonomy.

### Database
This houses full-fidelity information (model metadata, harm metrics, measurements, benchmarks, and mitigation techniques if any) on evaluation examples of harm (sub)categories defined by the taxonomy. The aim here is transparent and reproducible evaluations that give practitioners a path to implementation.

The database is organized into two layers:
1. *Vunerability*: high-level evidence of an AI failure mode, in line with the [NIST CVE](https://nvd.nist.gov/vuln)s
2. *Report*: one example of a particular vulnerability occurring, supported by qualitative or quantitative evaluation. Based on the references provided in a specific report, reports can potentially more granular and reproducible than vulnerabilities.

We are starting small with 13 vulnerabilities and 5 reports, but will expand quickly.

To check out the database, and vulnerabilities and reports therein, go to: https://avidml.org/database. 

## How can you help
If there's AI failure you'd like to be included in AVID (e.g. examples of a large language model malfunctioning), you can do so *today* using our [Vulnerability Reporting Form](https://airtable.com/shrOCPagOzxNpgV96) or opening a pull request in the [github repository](https://github.com/avidml/avid-db) housing all vulnerabilities and reports.

You can collaborate with us by joining our [discord server](https://discord.gg/FcXYZzmv3T), and through other avenues [here](https://www.avidml.org/get-involved).

## About the Author
[Subho Majumdar](https://www.subhomajumdar.com) is a technical leader in applied trustworthy machine learning who believes in a community-centric approach to data-driven decision making. He has pioneered the use of responsible ML methods in industry settings, wrote a [book](https://learning.oreilly.com/library/view/practicing-trustworthy-machine/9781098120269), and founded multiple nonprofit efforts in this area---[TrustML](https://www.trustworthyml.org), [Bias Buccaneers](https://biasbounty.ai), and AVID. Currently, Subho is a ML scientist in Twitch, where he leads applied science efforts in Responsible AI.