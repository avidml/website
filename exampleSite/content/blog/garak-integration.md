---
author: "Leon Derczynski, Carol Anderson, and Subho Majumdar"
title: "AVID Announces Integration with garak, a Vulnerability Scanner for LLMs"
date: "2023-07-24"
description: "Vulnerabilities found by garak can now be converted easily into AVID reports."
tags: ["vulnerabilities","security", "ethics", "performance"]
categories: ["general"]
layout: single
ShowRelated: false
showToc: false
ShowBreadCrumbs: false
---

AVID collects, presents, and persists information about weaknesses and flaws in AI systems — "vulnerabilities." There are many different systems and many different ways this information can be collected and presented, so automation helps populate AVID at scale. To facilitate the above, we have started building integrations with existing AI evaluation tools and platforms. As our first integration, we’ve linked [garak](https://github.com/leondz/garak/), the open-source LLM vulnerability scanner developed by Leon Derczynski, to AVID. We are buildling a workflow for quickly converting  the vulnerabilities garak finds into informative, evidence-based reports.

## What is garak? 
Garak is a vulnerability scanner for large language models (LLMs). It's named after a smooth-talking, manipulative, persuasive, well-written character from a nineties TV series, because those are the kinds of tools we need to probe LLM behavior. Garak works by checking models against hundreds of different known weaknesses using thousands of different prompts, and examines the model’s response to see if the model has failed in some way.

For example, maybe we don’t want our model to output racist material. Many models won’t. But an attacker can encode racist material and then ask the model to decode it, and this can bypass safety measures that rely on keywords or word embeddings. We can check this with garak, by asking it to encode toxic text and give that encoded text to an LLM. A vulnerable LLM will output the decoded version of the toxic text.

![Example prompts and toxic output](/uploads/garak-integration/carbon.png)

## Why connect garak with AVID?

Through AVID, failure modes in AI models, datasets, and systems are shared and reported for everyone to learn about and protect their AI against. Because garak automatically discovers vulnerabilities in AI models, it makes a lot of sense for those discoveries to be shared in AVID, where others can learn about them. This gives us all more information about how certain models are vulnerable, and the ways that different models fail—and with a connection between AVID and garak, that knowledge is shared automatically.

## How does it work?
How can you use this connection? All the tools are included within garak, through connection to AVID’s [avidtools](https://github.com/avidml/avidtools) Python package. Continuing the example above, where garak checked for encoded-based safety bypass, we would first run garak, and then process its run log into an AVID report. For example, let’s run garak on the Hugging Face version of gpt2:

`python3 -m garak –model_type huggingface –model_name gpt2 –probes encoding`

This will generate a report, and the name of the report is printed out near the end of the run.

`📜 report closed :) garak.ea8ba884-0192-4869-a0c0-de0c53d7fff7.report.jsonl`

The next step is to process that report by calling garak one more time in the CLI:

`python3 -m garak –r garak.ea8ba884-0192-4869-a0c0-de0c53d7fff7.report.jsonl`

`📜 Converting garak reports garak.ea8ba884-0192-4869-a0c0-de0c53d7fff7.report.jsonl`
`📜 AVID reports generated at garak.ea8ba884-0192-4869-a0c0-de0c53d7fff7.avid.jsonl`

The result is a report ready to be submitted to AVID! To do so, you can currently use our AI Vulnerability reporting form. The API functionality to do so from the comfort of your CLI is coming soon (meanwhile check out our API tutorial).

## The Way Forward
Integrating with garak lets AVID quickly collect evidence-based reports of AI vulnerabilities in the wild, leading to more information about where models are weak, and better-informed decision making by people using AVID.

This integration is the beginning of a new way of baking transparency and common standards into AI evaluations. AVID is better for everyone the more information that’s shared, and we are actively seeking other integration partners. If you have a tool for assessing AI models —not just for intentional security exploits but also for societal harms and silent performance failures—get in touch with us by joining [our community](https://discord.com/invite/FcXYZzmv3T), or by [reaching out](https://avidml.org/contact/) directly!


## About the Authors
[Leon Derczynski](https://www.derczynski.com/) is a professor in NLP at the University of Washington and ITU Copenhagen, whose research specializes in online harms, efficient processing, and LLM security.

[Carol Anderson](https://www.linkedin.com/in/carolmanderson/) is a data scientist and machine learning practitioner with expertise in natural language processing (NLP), biological data, and AI ethics. She serves as AVID's machine learning lead. 

[Subho Majumdar](https://www.subhomajumdar.com) is a technical leader in applied trustworthy machine learning who believes in a community-centric approach to data-driven decision making. He has pioneered the use of responsible ML methods in industry settings, wrote a [book](https://learning.oreilly.com/library/view/practicing-trustworthy-machine/9781098120269), and founded multiple nonprofit efforts in this area---[TrustML](https://www.trustworthyml.org), [Bias Buccaneers](https://biasbounty.ai), and AVID. 
