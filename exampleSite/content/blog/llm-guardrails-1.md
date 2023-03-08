---
author: "Carol Anderson"
title: "Guardrails on Large Language Models, Part 1: Dataset Preparation"
date: "2023-03-02"
description: "A non-technical introduction to the major guardrails on systems like ChatGPT. Part 1 of a four-part series."
tags: ["generative AI","LLMs","vulnerabilities", "safety"]
categories: ["general"]
layout: single
ShowRelated: false
showToc: false
ShowBreadCrumbs: false
---

With the recent spate of news about Bing/Sydney going haywire, I’ve noticed some misconceptions about the guardrails on large language models (LLMs).

To help dispel some of them, this is the first in a series of posts where I’ll give a non-technical introduction to each of the four major points of control for LLMs:


1. Pretraining data preparation
2. Model fine tuning
3. Prompt design
4. Content moderation


## Some quick background
The first stage of training a language model, which is known as “pretraining”, involves exposing the model to a massive quantity of text. In this critically important stage, the model learns patterns of language. Since the pretraining data for general-purpose LLMs is typically mostly web-scraped text, it contains problematic content such as hate speech, personal data, and copyrighted material, all of which the model can later mimic or even regurgitate verbatim. 

## Points of control

### Data sourcing
Ideally, pretraining would use datasets specifically created for this purpose and free of any unwanted content. In reality, the amount of data required is so huge that developers rely on web scraping. [OpenAI](https://openai.com) hasn’t released details of the training datasets used for ChatGPT and its siblings, but the training data for their predecessor, GPT-3, was about [80% web-scraped data](https://proceedings.neurips.cc/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf) (the remainder being books and English Wikipedia). 

### Data cleaning 

Model developers, including OpenAI, usually try to clean up the pretraining data to remove low-quality or objectionable content. But doing this by hand would be a monumental task, so the cleanup process relies on algorithms. This raises a few issues:

* Problematic content can be difficult to detect algorithmically.

* The algorithms that detect hate speech, bias, and toxicity are themselves biased, having a [known tendency](https://aclanthology.org/2021.findings-emnlp.210/) to over-flag speech about marginalized groups (e.g., flagging it as toxic even when it isn’t). This worsens the underrepresentation of marginalized groups in the dataset. 

* Cleanup can’t fix the fact that the dataset is fundamentally not representative of humans overall, since content on the web itself isn’t representative. 

## The current state of things

To date, no developers of general-purpose language models have invested the time or money needed to thoroughly curate pretraining data. With current practices, there’s still plenty of objectionable content left in the dataset after cleaning, as well as representational problems. (_Who decides what’s objectionable_ is an ethical issue that I’ll leave aside for today.)  

**TL;DR:** 
Language models mimic their pretraining data, which is mostly pulled from the web. Model developers try to clean it up, but lots of problematic content remains, and many human perspectives are underrepresented. 

---
This post was originally published at [www.carol-anderson.com](https://www.carol-anderson.com/blog/guardrails-on-large-language-models-part-1-dataset-preparation). Stay tuned for additional installments in the series.


## About the Author
[Carol Anderson](https://www.linkedin.com/in/carolmanderson/) a data scientist and machine learning practitioner with expertise in natural language processing (NLP), biological data, and AI ethics. She previously worked as a data scientist at [NVIDIA](https://www.nvidia.com/en-us/), [ConcertAI](https://www.concertai.com), and [Ancestry](https://www.ancestry.com/), and prior to that as an academic molecular biologist at [UCSF](https://www.ancestry.com/) and [Indiana University](https://www.indiana.edu). Currently, her main interest is operationalizing AI ethics and safety, especially in the area of generative AI.
