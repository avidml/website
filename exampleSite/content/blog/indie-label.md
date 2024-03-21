---
author: "Michelle S. Lam, Christina A. Pan, Carol Anderson, Nathan Butters, and Borhane Blili-Hamelin"
title: "Anyone Can Audit! Users Can Lead Their Own Algorithmic Audits with IndieLabel"
date: "2024-03-20"
description: "ARVA publicly launches IndieLabel, a prototype tool that guides everyday users to perform algorithmic audits."
tags: ["vulnerabilities", "audits"]
categories: ["general"]
layout: single
ShowRelated: false
showToc: false
ShowBreadCrumbs: false
---

We’re delighted to announce the release of the [IndieLabel Space](https://huggingface.co/spaces/avid-ml/indie-label) on HuggingFace, a collaboration between researchers at the [Stanford HCI Group](https://hci.stanford.edu) and [ARVA](https://avidml.org/arva/) (The AI Risk and Vulnerability Alliance). IndieLabel is a prototype tool designed to support end-user audits — user-led evaluations of AI systems. It was the centerpiece of the [End-User Audits](https://dl.acm.org/doi/10.1145/3555625) paper, published at [CSCW](https://dl.acm.org/conference/cscw) 2022. 


## Why user-led audits?
ARVA envisions a world where communities are empowered to identify and mitigate the harmful flaws in AI systems. Everyday users are uniquely situated to discover harmful patterns in the algorithmic systems they use. For example, in 2020, users found that Twitter’s automatic [image cropping algorithm showed gender and racial bias](https://incidentdatabase.ai/cite/103/), tending to focus on white faces and women. This occurred even though [Twitter had apparently tested its model](https://www.theguardian.com/technology/2020/sep/21/twitter-apologises-for-racist-image-cropping-algorithm) for gender and racial bias prior to deployment, and had found none. Subsequently, Twitter’s 2021 bias bounty ([discussed here](https://www.ajl.org/bugs)) on the same algorithm received successful submissions from participants from a [“wide range of backgrounds, including people who do not have an expertise in machine learning.”](https://blog.x.com/engineering/en_us/topics/insights/2021/learnings-from-the-first-algorithmic-bias-bounty-challenge)


In spite of notable success stories like this, user-driven discovery of harm remains far too rare. [Expertise is a major barrier to entry into AI audit, bounties and evaluation](http://arxiv.org/abs/2307.10223), as users often lack the computational skills, time, and resources to systematically investigate the algorithms affecting them. The last year has dramatically expanded interest in public testing of AI systems — as showcased by projects like [Adversarial Nibbler](https://www.dataperf.org/adversarial-nibbler), the [DEFCON GRT Challenge](https://www.hackthefuture.com/defcon), [The AI Democracy Projects](https://www.proofnews.org/seeking-election-information-dont-trust-ai/), and [Tulsa Hack the Future](https://www.hackthefuture.com/greenwood). We need many more novel methods that lower barriers to entry and expand participation in end-user algorithmic audits. 

## How IndieLabel empowers users
IndieLabel, a web app developed by Michelle Lam and colleagues at the Stanford HCI Group, enables _end-users_ to _discover_ potential harms, _gather_ robust evidence, and _share_ their findings. As its core case study, IndieLabel allows users to investigate the [Perspective API](https://perspectiveapi.com), a toxicity-detection system used widely in online content moderation. Previous research found evidence of bias in the Perspective API, for example giving higher toxicity scores to text containing [racial or gender identity terms](https://dl.acm.org/doi/10.1145/3278721.3278729) or [phrases associated with African American English.](https://aclanthology.org/P19-1163/) In the context of a content-moderation tool, these kinds of biases can cause real harm, as they may lead to suppression of speech within or about marginalized communities. 

![Screenshot of the IndieLabel app](/uploads/indielabel_arva.png)

IndieLabel uses a novel approach to guide users in auditing the Perspective API. Users are prompted to assign toxicity scores to a small number of text examples (i.e., 20 social media posts). A lightweight model is then trained to predict the user’s opinion on a much larger number of examples (on the order of thousands of posts), and these predictions are used to surface potential areas of disagreement between the user and the Perspective API. For example, the system might surface that, relative to the user, the Perspective API is over-flagging posts related to marginalized racial identities, or that it is under-flagging veiled forms of hate speech. Users are then able to explore areas of potential disagreement, iteratively test hunches about the system’s behavior, and create reports documenting their findings. 

## Try it out!
We’re happy to provide the first public-facing deployment of IndieLabel, allowing users to submit reports directly to our AI Vulnerability Database (AVID). We hope that by adding it to our small but growing [collection of apps](https://avidml.org/tools/) for vulnerability detection, we can help spur interest in expanding IndieLabel’s innovative approach to many more models and AI systems. 

Please [try it out](https://huggingface.co/spaces/avid-ml/indie-label) or [view the demo](https://youtu.be/Je0DCDnJ6KQ?feature=shared) and [let us know what you think](https://forms.gle/vDXchpbBFjDeKjJA6)! 


## About the authors
[Michelle Lam](http://michelle123lam.github.io/ ) is a PhD Candidate at Stanford University in the HCI Group. Her research focuses on building systems that empower everyday users to surface their expertise to design and evaluate AI systems.

[Christina A. Pan](https://www.christinaapan.com/) started her career building machine learning (ML) models at Google, which inspired her passion for design thinking and AI ethics.

[Carol Anderson](https://www.linkedin.com/in/carolmanderson/) is a data scientist and machine learning practitioner with expertise in natural language processing (NLP), biological data, and AI ethics. She serves as AVID’s machine learning lead.

Nathan Butters is a product manager in the Office of Ethical and Humane Use at Salesforce. He is a cofounder of the AI Risk and Vulnerability Alliance (ARVA).

[Borhane Blili-Hamelin](https://borhane.xyz/) is an ethicist, researcher and AI risk management consultant. He is an officer at the AI Risk and Vulnerability Alliance (ARVA), an affiliate at Data & Society, and a senior consultant at BABL AI. 


