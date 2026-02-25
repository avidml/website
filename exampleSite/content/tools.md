---
title: Tools for vulnerability discovery
description:
layout: page
url: /tools
---
AVID is pleased to host a small but growing collection of tools to evaluate failure modes in general-purpose AI (GPAI) systems, including LLMs, API-only AI systems, and end-to-end applications. Some tools are hosted on [HuggingFace](https://huggingface.co/avid-ml), and our SDK tooling is maintained in `avidtools`.

## AVIDtools SDK

[avidtools](https://github.com/avidml/avidtools) is AVID's developer SDK. It currently provides two core components:

- **Data models** for structured AVID vulnerability/report records
- **Connectors** for ingesting external sources and transforming them into AVID-compatible reports

Install from PyPI with `pip install avidtools`, and see the [API docs](https://avidml.org/avidtools/).


## [IndieLabel](https://huggingface.co/spaces/avid-ml/indie-label)
[IndieLabel](https://huggingface.co/spaces/avid-ml/indie-label), developed by [Michelle Lam and colleagues](https://hci.stanford.edu/publications/2022/Lam_EndUserAudits_CSCW22.pdf) at the [Stanford Human-Computer Interaction Group](https://hci.stanford.edu/), is a novel and powerful tool to enable individual users without computational expertise to perform algorithmic audits. IndieLabel allows users to investigate the Perspective API, a toxicity detection tool widely used for online content moderation. Previous work has shown that the Perspective API can sometimes over-flag, i.e. label benign comments as toxic, and this is especially true in discussions among or about marginalized communities. IndieLabel helps users to investigate topics of particular interest to them and to generate audit reports based on their findings. AVID’s deployment of IndieLabel, which is the only public-facing, live deployment of IndieLabel to date, also allows users to submit vulnerability reports directly to AVID.


## [BiasAware](https://huggingface.co/spaces/avid-ml/biasaware) 

[BiasAware](https://huggingface.co/spaces/avid-ml/biasaware) is a web app for evaluating gender bias in datasets.  Developed in-house at AVID by [a team of volunteers](https://avidml.org/blog/biasaware-1/), the app allows anyone to upload their own dataset and run automatic evaluations of gender bias by three different methods. Datasets hosted on the HuggingFace Hub can also be evaluated easily. Biasaware also generates reports that can be submitted to AVID.

## [Plug-and-Play Bias Detection](https://huggingface.co/spaces/avid-ml/bias-detection)

[Plug-and-Play Bias Detection](https://huggingface.co/spaces/avid-ml/bias-detection), developed at AVID by Subho Majumdar, allows users to evaluate language models for various types of bias in just a few clicks. Models are loaded automatically from the HuggingFace Hub, and various evaluation methods are available: 

For masked language models (e.g. BERT): 

* [**HONEST**](https://aclanthology.org/2021.naacl-main.191/) measures hurtful sentence completions across 10 different categories of harm.   
* [**WinoBias**](https://aclanthology.org/N18-2003/) measures gender bias in coreference resolution.   


For generative language models (e.g. EleutherAI/gpt-neo-125M): 

* [**BOLD**](https://dl.acm.org/doi/10.1145/3442188.3445924) measures fairness across five categories (profession, gender, race, religious ideologies, and political ideologies). 

 
The app also generates vulnerability reports that can be submitted to AVID.  

### Call for collaborations
Know a tool we should showcase here? Or want to help us develop new ones? Please [get in touch](https://avidml.org/contact/)!
