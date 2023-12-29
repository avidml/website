---
author: "Freyam Mehta, Sudipta Ghosh, Carol Anderson, Jekaterina Novikova and Subho Majumdar"
title: "AVID Announces BiasAware - A Powerful Tool for Detecting Bias in Datasets"
date: "2023-11-20"
description: "A new tool to detect bias in datasets, developed by AVID and hosted on Hugging Face."
tags: ["vulnerabilities", "ethics", "social bias"]
categories: ["general"]
layout: single
ShowRelated: false
showToc: false
ShowBreadCrumbs: false
---

## Context
The upswing in the application of Artificial Intelligence (AI) comes with a ripple effect of concerns, one of the most significant being social biases. The brilliance and potential of AI is undeniable, but this belies the fact that AI models derive their characteristics, knowledge, and unfortunately, social biases from the dataset they are trained on. Social biases in AI systems are evident and highly pervasive. From speech recognition software struggling to comprehend diverse accents, sentiment analysis tools misinterpreting emotions outside Western contexts, to recommendation algorithms that recycle existing beliefs instead of broadening perspectives, the harmful impact of biases in AI is no secret. In scenarios where these biases result in unjust decisions, discrimination, and a lack of inclusivity, societal inequalities are only widened.

The focus today is often on model evaluations, with inadequate attention accorded to dataset evaluation. There is a lurking danger in neglecting the quality and fairness of the underlying data - we risk exposing the core of AI systems to inherited biases. These biases can create damaging effects such as fostering stereotypes, propagating underrepresentation, and advancing skewed perspectives, leading to the further marginalization of communities.

## BiasAware
Recognizing the urgency of addressing this issue, we developed BiasAware as a specialized tool dedicated to uncovering and quantifying social biases within training datasets. 

We are targeting gender bias with **BiasAware**, recognizing that gender bias is a pervasive issue in AI that deserves immediate attention. Gender bias in AI can manifest in various ways, from biased language models that produce sexist or derogatory content to algorithms that disproportionately target or exclude individuals based on their gender. This bias not only perpetuates harmful stereotypes but also reinforces existing inequalities and discrimination.

Hosted on Hugging Face [(https://huggingface.co/spaces/avid-ml/biasaware)](https://huggingface.co/spaces/avid-ml/biasaware), BiasAware provides an interactive platform where anyone can assess local/hosted datasets. BiasAware's intuitive interface coupled with a set of  analysis capabilities makes it a valuable tool for individuals, researchers, and organizations aspiring for alignment of their datasets with principles of fairness and inclusivity.

![BiasAware Flow](/uploads/biasaware-1/BiasAware.png)

Now, let's dive into the methodologies that BiasAware employs to tackle gender bias in datasets.

### Gender Distribution (Term Identity Diversity)
This method measures the frequency of gender-related terms within text-based datasets or populations, tabulating how often each identity appears. The procedure uses a lexicon of predefined male and female gender terms. The text to be evaluated is parsed and compared to these lexicons to count occurrences of male and female terms. Each text is then tagged with a gender category based on the proportion of male and female terms. For example, a tag of 'Male Strongly Positive Gender' would be applied if male terms make up 75% or more of the total gender terms found in the text.

This methodology can reveal possible biases in text datasets, such as certain gender identities associated with specific topics on social media. Please note that this analysis is based on the frequency of gendered terms and does not provide any insights into the actual gender identities of individuals described within the text. There are essentially six categories to label gender representation in the text: 'No Gender,' 'Equal Gender,' 'Male Positive Gender,' 'Male Strongly Positive Gender,' 'Female Positive Gender,' 'Female Strongly Positive Gender.' This structured approach to gender analysis uses a content-based evaluation of the text to provide objective insights.

### Gender Profession Bias (Lexical Evaluation)
This method identifies and quantifies gender and profession-related information in text datasets. It focuses attention on instances where male and female pronouns are paired with various professions. To do this, it uses bespoke lexicons and complex regular expressions to systematically detect and analyze these links, giving detailed insights into the dynamics between gender and professions.

The procedure makes use of  predefined lexicons for male and female pronouns, and professions. It analyzes the text by parsing it and comparing it to these lexicons, thereby identifying occurrences of male and female pronouns linked to professions. Each section of the text then gets a gender tag based on the proportion of instances where male or female pronouns are associated with professions.


The data generated from this method can show the presence and match frequencies of male and female pronouns and profession terms. This approach can serve as part of the broader initiative to ensure fairness and equity in AI applications, as it can unveil inherent biases in the way language models associate professions with male or female pronouns. For instance, if a language model constantly matches male pronouns with tech-related roles while associating female pronouns with caregiving professions, it may generate biased recommendations in job searches or educational advising. Therefore, this analysis method can make sure AI applications provide unbiased and fair results.

### GenBiT (Microsoft Gender Bias Tool)
[GenBiT](https://github.com/microsoft/responsible-ai-toolbox-genbit) (part of [Microsoft’s Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox)) is a versatile tool that measures gender bias in language datasets by using word co-occurrence statistical methods and techniques like data augmentation, random sampling, and sentence classification. What makes GenBiT stand out is its adaptability to various forms of bias, not limited to gender. It can effectively address biases related to different dimensions, making it a valuable tool for bias mitigation in language datasets.

_Note: Given the current limitations with AVID's support for Dataset Evaluations, it's important to note that although we are generating and displaying reports on the app, formal submission to AVID is pending until full support is available._

## The Way Forward
As we continue our journey towards a more equitable and just technological landscape, the next crucial steps involve expanding our focus to incorporate various social biases beyond gender and actively engaging companies and organizations. This means developing tools and methodologies that can address biases related to race, age, disability, and other dimensions, ensuring that AI respects the diversity of the human experience. Going beyond tools and techniques, we also want to inculcate the culture of responsible disclosure and reporting of dataset and model evaluations to AVID, to shorten the iteration time on future similar analyses. Finally, it is essential to raise awareness and promote responsible AI practices among companies, encouraging them to prioritize fairness and inclusivity in their AI applications.

By collectively working towards these goals, we can shape a future where AI truly benefits all, regardless of their background or identity. _It's time to make the world "BiasAware" in more ways than one!_


## About the Authors
[Freyam Mehta](https://www.linkedin.com/in/freyam-mehta) is a computer science undergraduate at IIIT Hyderabad, with a focus on AI Security and Governance research. He is passionate about ensuring the secure and responsible use of AI in enterprise settings. He has experience working as a Cloud Security Engineer at Oracle, a Data Science (NLP) Researcher at Precog, and as a Technical Product Manager at Pradical. In his present role as an AI Security Engineer, he is dedicated to helping businesses in staying one step ahead in the ever-evolving landscape of AI and security.

[Sudipta Ghosh](https://www.linkedin.com/in/sudipta002/) is a data scientist with a background in product development within the healthcare domain, particularly in the realm of medical text. Currently serving as a Generative AI - Solution Architect, he is at the forefront of crafting innovative solutions and products, leveraging his expertise in prompt engineering, conversational AI, vector databases and Large Language Models (LLM). His passion for continuous learning is evident as he sets his sights on the cutting edge of Quantum NLP, driven by a curiosity that propels him towards groundbreaking research. 

[Carol Anderson](https://www.linkedin.com/in/carolmanderson/) is a data scientist and machine learning practitioner with expertise in natural language processing (NLP), biological data, and AI ethics. She previously worked as a data scientist at NVIDIA, ConcertAI, and Ancestry, and prior to that as an academic molecular biologist at UCSF and Indiana University. Currently, her main interest is operationalizing AI ethics and safety, especially in the area of generative AI.

[Jekaterina Novikova](https://jeknov.github.io/) is a computer scientist working in the field of natural language processing. At AVID she leads research efforts towards creating an open-source knowledge base of failure modes for AI models and datasets. She is also a Director of Machine Learning Research at Cambridge Cognition (prev. Winterlight Labs), where her main focus is on the intersection of language technology and machine learning in healthcare. Her aim is to make ML approaches more trustworthy and more interpretable in real world scenarios in order for them to be successfully applied to interdisciplinary areas, such as healthcare, spoken dialogue systems and human-robot interaction.

[Subho Majumdar](https://www.subhomajumdar.com/) is a technical leader in applied trustworthy machine learning who believes in a community-centric approach to data-driven decision-making. He has pioneered the use of responsible ML methods in industry settings, wrote a book, and founded multiple nonprofit efforts in this area—TrustML, Bias Buccaneers, and AVID. Currently, Subho is an ML scientist in Geico, where he is the technical lead of the Responsible AI team.
