---
author: "Brian Pendleton, Abhishek Gupta, Subho Majumdar"
title: "Red Teaming is a Critical Thinking Exercise: Part 1"
date: "2025-04-16"
description: ""
tags: ["red teaming","ai vulnerabilities"]
categories: ["general"]
layout: single
ShowRelated: false
showToc: false
ShowBreadCrumbs: false
---

> **Note from Brian**

> The genesis of this series of blog posts and paper about Red Teaming came about because Abhishek Gupta asked me (Brian) to write a paper with him about the topic. During our time working on the paper, Abhi never told me that he was severely ill, only that he had returned home to India to have some medical procedures done. I also faced some personal medical issues as well and we stopped working on the paper. Once I was able to do so again, I reached out to Abhi: only to hear the sad news of his passing.
> 
> Abhi was always a champion for me in the AI field. When he was thinking about a topic, he frequently reached out to ask my opinion. When I made posts on various social media, he would often let me know what he thought, sometimes agreeing, sometimes helping me see other points of view. When I felt like I didn’t belong in the AI community, Abhi was one of the people who helped me see that I was a valuable part of the community.
> 
> To honor our friendship, and the work that he put into our project, I asked another friend, Subho, who also knew Abhishek, to help me finish the paper and expand the sections into blog posts that cover each section in more detail than the paper. If you enjoy them or if AI ethics is of interest to you, please check out other pieces that Abhi wrote or had a part in at the Montreal AI Ethics Institute [website](https://montrealethics.ai). A curated selection of Abhi's published works and talks can also be found [here](https://brief.montrealethics.ai/p/special-edition-honouring-the-legacy).
> 
> During the 2022 holiday season, a small group of us coded up the first version of the AVID website, compiled the first set of reports and vulnerabilities, and put together our taxonomy based on discussions in the past months. This body of work went live in January 2023. In the months that followed, AI became a household name: alongwith which came the need for rigorous approaches to managing the risks of this emergent technology became obvious to the general public, companies, and governments around the world. AVID provided an outlet to this groundswell of interest. During the rest of 2023, we launched a slew of public events to channel this interest to productive outlets, partnered with like-minded organizations in community efforts, and had a number of releases seeding technical resources that would be indispensable to AI risk practitioners for decades to come.

In the recent past, the term AI red teaming has gained significant attention in diverse circles as a potential solution to find and address security, safety, and reliability concerns in generative AI systems. When ChatGPT came out in November 2022, not many people in the AI field except those that had previously been in the military or cybersecurity knew about red teaming. Less than a year in, the largest ever AI red teaming exercise was organized at DEF CON, a leading hacker conference[^1]<sup>,</sup>[^2]. Fast forward to today where we are in the middle of a (supposed) GenAI revolution, AI red teaming dominates conversations in academia[^3]<sup>,</sup>[^4], think tank advice[^5]<sup>,</sup>[^6], and popular media articles[^7]<sup>,</sup>[^8]<sup>,</sup>[^9]. The notion of red teaming is being touted as a panacea to many of the problems AI might have, and its application to LLMs has been and continues to be encouraged as a matter of practice. While that’s not necessarily a bad thing because red teaming is definitely a part of solving the AI security/safety problem, it’s only a small part of a more complete set of tools that should be used.

Red-teaming is a critical thinking exercise that helps ascertain the appropriateness of an approach and its robustness to solve complex challenges. Having evolved from military war games to cybersecurity practices, and now to surfacing AI security vulnerabilities and safety harms, red teaming goes beyond manual or automated testing by technical people. Rather than simply testing technological components---hardware, software, networks, and models---it extends to scrutinizing governance structures and challenging the foundational assumptions of designs from their earliest conception. As such, red teaming is not just a technical exercise but a thought process that can be employed by non-technical staff, such as the management, legal and risk management teams, to craft governance guidelines and engage in meaningful dialogue with technical teams about unforeseen post-deployment challenges. Sensitivity to the differences in the requirements posed by safety, security, privacy, alignment, and ethics alongside the application of this methodology to the total AI ecosystem of hardware, software, networks, data---and, most importantly, people---will be critical for success.

There is a critical disconnect between the rich technical foundation and industry best practices in cybersecurity and the current approach to AI red-teaming. Despite decades of research and education in security, today's AI red teaming efforts remain narrowly focused on technical vulnerabilities in LLMs. This missing link negates the tremendous benefits that are unrealized in bridging communities of practice in AI and cybersecurity, which could ultimately lead to us finding better ways to achieve robust and effective AI governance and AI solutions that adhere more closely to the espoused principles of responsible AI.

To effectively implement red teaming in sociotechnical systems, we must expand our perspective beyond the narrow technical focus currently dominating the discourse. Red teaming originated as a strategic thinking exercise where a designated team not just simulates adversarial actions, but challenges assumptions and identifies blind spots as part of a well-defined project greenlighting process. The current approach of testing something that's already been built—as many LLM companies are doing [^10]<sup>,</sup>[^11]---misses the point of preemptive critical analysis that red teaming was designed to provide.

Red teaming is fundamentally a team exercise. It should bring together multifunctional and cross-functional teams around the common goal of ultimately improving a product or user experience. The means of this exercise are to explore hypotheticals centered around two primary questions: (1) Does the system work for their interests? (2) Could it work against their interests? This multidisciplinary approach acknowledges that systems built for a specific purpose exist within complex sociotechnical environments where technical, social, and organizational factors interact. Technical teams can probe for model vulnerabilities while policy experts identify regulatory conflicts. Ethicists can surface value alignment issues, and domain specialists can evaluate real-world impact scenarios.
Red teaming is NOT an adversarial exercise where the goal is to capture as many clever "gotcha" flags as possible or find ways to break the system. It is a collaborative process that attempts to answer the critical question: “What did we do, or not do, that could lead to failure in real-world conditions?” This collaborative mindset fosters blameless transparency about blind spots, bad assumptions, and vulnerabilities. Organizations need not address every risk that red teamers identify, but they benefit immensely from comprehensive awareness of potential failure modes before deployment. Effective red teaming examines not just the product itself but the entire ecosystem—the development processes, organizational structures, incentive systems, and operational contexts in which the technology will function. In many ways red teaming is similar to writing a research paper: the team starts with a skeleton and rough draft of the paper, then goes through cycles of redlines, experiments, and writing iterations to come up with the final version of the artifact.

Organizations implementing AI red teaming should establish clear processes for translating findings into actionable improvements. This includes tracking identified issues, prioritizing them based on risk assessment, implementing mitigations, and verifying that fixes don't introduce new problems. Without this feedback loop, red teaming becomes merely a performative exercise rather than a meaningful critical practice. In many ways, red teaming is similar to acceptance testing in software development. And we all know that no amount of pre-deployment testing can anticipate all potential issues. Red-teamed systems operate in dynamic environments with evolving threats and user behaviors. This reality necessitates ongoing monitoring, continuous evaluation, and adaptive response capabilities that extend well beyond initial red teaming exercises.

As we move forward in defining AI governance and risk management practices, let's remember that red teaming is broader than just security or AI and deeper than just pentesting or fuzzing. It's a critical thinking methodology that, when properly applied across the entire development lifecycle, can substantially maximize the utility and minimize the risks of complex sociotechnical systems. Stay tuned for our next blog post, where we'll dig into the fascinating history of red teaming—from military war rooms to corporate boardrooms—and unpack the literature that shows how these diverse origins can help us build better practices today.

## About the Authors
[Subho Majumdar](https://www.subhomajumdar.com/) is a technical leader in applied trustworthy AI who believes in a community-centric approach to data-driven decision-making. He has pioneered the use of responsible AI methods in industry settings, wrote a [book](https://www.amazon.com/Practicing-Trustworthy-Machine-Learning-Transparent/dp/1098120272), and founded multiple nonprofit efforts in this area---TrustML, Bias Buccaneers, and AVID. Currently, Subho is Co-founder and Head of AI at [Vijil](http://vijil.ai/), an AI software startup on a mission to help developers build and operate intelligent agents that people can trust.

[Brian Pendleton](https://www.linkedin.com/in/bwpen/) is an AI security researcher and Founding Director of ARVA. He is passionate about pariticipatory approaches in mitigating AI security harms, and was one of the founding members of the [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/). Besides leading ARVA activities, Brian also leads community efforts in AI Village.

## References

[^1]: [AI Village at DEF CON announces largest-ever public Generative AI Red Team](https://aivillage.org/generative%20red%20team/generative-red-team/). Cattell, Chowdhury, and Carson, 2023.

[^2]: [Don't expect quick fixes in 'red-teaming' of AI models. Security was an afterthought](https://apnews.com/article/ai-cybersecurity-malware-microsoft-google-openai-redteaming-1f4c8d874195c9ffcc2cdffa71e4f44b). Bajak, 2023.

[^3]: [Summon a demon and bind it: A grounded theory of LLM red teaming](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0314658). Inie *et al*, PLOS One, 2025.

[^4]: [Revisiting AI Red-Teaming](https://cset.georgetown.edu/article/revisiting-ai-red-teaming). Ji and Shea-Blymyer, 2024.

[^5]: [Scaling Up Mischief: Red-Teaming AI and Distributing Governance](https://hdsr.mitpress.mit.edu/pub/ded4vcwl/release/2). Metcalf and Singh, 2024.

[^6]: [Red-Teaming in the Public Interest](https://datasociety.net/library/red-teaming-in-the-public-interest). Singh *et al*, 2025.

[^7]: [How to Red Team a Gen AI Model](https://hbr.org/2024/01/how-to-red-team-a-gen-ai-model). Burt, 2024.

[^8]: [Secure AI? Dream on, says AI red team](https://www.infoworld.com/article/3805151/secure-ai-dream-on-says-ai-red-team.html). Barker, 2025.

[^9]: [The Expanding Role of Red Teaming in Defending AI Systems](https://www.technewsworld.com/story/the-expanding-role-of-red-teaming-in-defending-ai-systems-179669.html). Patwa, 2025.

[^10]: [Challenges in red teaming AI systems](https://www.anthropic.com/news/challenges-in-red-teaming-ai-systems). Anthropic, 2024.

[^11]: [OpenAI enhances AI safety with new red teaming methods](https://www.artificialintelligence-news.com/news/openai-enhances-ai-safety-new-red-teaming-methods/). Daws, 2024.

