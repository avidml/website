---
author: "Brian Pendleton, Abhishek Gupta, Subho Majumdar"
title: "Red Teaming is a Critical Thinking Exercise: Part 2"
date: "2025-05-13"
description: ""
tags: ["red teaming","ai vulnerabilities"]
categories: ["general"]
layout: single
ShowRelated: false
showToc: false
ShowBreadCrumbs: false
---

Red teaming has evolved from its origins in military strategy to become a widely discussed methodology across multiple domains, including cybersecurity and AI. In [Part 1](https://avidml.org/blog/red-teaming-1/), we outlined how, despite its current popularity in AI governance discussions, there appears to be a significant gap between the original intent of red teaming and its practical applications. In this Part 2, we set the context for this discussion by tracing the evolution of red teaming across different fields, with a particular focus on how it has been adapted to AI systems and the limitations of red teaming in its most recent incarnation.

## Military origins

Red teaming emerged from the tactical war games of the Prussian military in the early 19th century, evolving through Cold War simulations into today's formalized methodology for challenging conventional wisdom and identifying strategic and exploitable hazards. The Prussian army adopted *Kriegsspiel* (literally "wargame" in German) in 1812, a tabletop simulation developed by Lieutenant Georg Leopold von Reisswitz and his son, where blue pieces represented the Prussian forces and red represented the enemy[^1][^2]. This color-coding established the "red team" concept that persists to this day.

In the US, the concept of red teaming took shape during the Cold War, when the RAND Corporation conducted military simulations for the U.S. government. In these exercises, "red team" and the color red were used to represent the Soviet Union, while "blue team" and blue represented the United States[^3]. Following the intelligence failures that led to the September 11 attacks in 2001, the U.S. Department of Defense established formal red team units to prevent similar catastrophic oversights. The 9/11 Commission identified a "failure to connect the dots" as a primary cause of the intelligence breakdown, prompting systematic changes to prevent groupthink and foster alternative analysis[^4]. As a result, the Pentagon created specialized training centers like the University of Foreign Military and Cultural Studies at Fort Leavenworth to institutionalize red teaming methodologies. The US Army's University of Foreign Military and Cultural Studies at Fort Leavenworth, created after intelligence failures in Iraq, developed the modern framework for red teaming that transformed an ad-hoc practice into a systematic methodology for critical analysis[^5]. This program teaches military officers and government officials techniques to challenge assumptions, consider alternative perspectives, and introduce contrarian thinking into planning processes.

The concept of the "10th man" from Israeli military doctrine, popularized in the film "World War Z", illustrates another approach to institutionalized contrarian thinking: when everyone agrees on a particular outcome, it is the designated 10th man's responsibility to disagree and explore alternative scenarios. This concept reportedly developed after intelligence failures during the 1973 Yom Kippur War, when analysts unanimously agreed that Arab troop movements weren't a threat[^1]. In reality, while Israeli intelligence did establish a unit called *Ipcha Mistabra* ("the opposite side") to challenge prevailing assumptions after the Yom Kippur War, the specific "10th man" concept as portrayed in the film is somewhat fictionalized but based on real adversarial thinking practices in military intelligence[^3].

## Adoption in Cybersecurity

The National Security Agency (NSA) first recognized the need for proactive cybersecurity measures in the 1980s, and pioneered the concept of "red teams" tasked with assessing the security of classified systems[^6]. These early efforts involved independent evaluators simulating potential attackers and identifying weaknesses that required remediation.

As digital threats evolved in the 1990s, so did the practice of cybersecurity red teaming. The term "tiger team" was initially used to describe specialized groups that performed many of the same functions as modern red teams[^7]. These elite and highly specialized groups were hired to take on particular challenges against the security posture of organizations.

Following the 9/11 attacks, cybersecurity red teaming gained significant momentum as organizations recognized the need for more comprehensive security testing. The Central Intelligence Agency created a new "Red Cell" unit, and red teaming became increasingly common in various government agencies to model responses to asymmetric threats, including cyber attacks[^3]. This period marked the transition from isolated penetration testing to more holistic security assessments that incorporated physical security, social engineering, and other non-technical aspects.

Modern cybersecurity red teaming encompasses several key methodologies working in concert: technical assessments that test digital defenses through vulnerability scanning, exploitation, and lateral movement[^8]; physical security testing that evaluates access controls for facilities[^9]; social engineering that targets the human element through phishing and impersonation[^10]; and extended red team operations designed to achieve specific objectives while testing detection and response capabilities[^11]. These approaches are codified in frameworks such as NIST Special Publication 800-53, which includes specific controls for red team exercises designed to "simulate attempts by adversaries to compromise organizational information systems" and "provide comprehensive assessments that reflect real-world conditions"[^12].

The field continues to evolve with several cutting-edge approaches. Continuous Automated Red Teaming (CART) uses automation to assess security posture in real-time rather than through periodic manual assessments[^8]. Adversary Emulation models tactics after specific threat actors that might target the organization, guided by frameworks like MITRE ATT&CK[^13]. Purple Teaming fosters collaboration between red and blue teams to identify vulnerabilities and improve response strategies[^14]. Integrated IT-OT Assessments expand scope to include industrial control systems and critical infrastructure[^15]. AI-Enhanced Red Teaming that incorporates AI to improve the effectiveness of assessments[^16]. And finally, specialized services from organizations like CISA provide comprehensive evaluations for critical infrastructure sectors and government agencies[^13].

This evolution of cybersecurity red teaming from isolated technical assessments to comprehensive, intelligence-driven simulations reflects the increasing sophistication of cyber threats and the growing recognition that effective security requires a holistic approach that addresses technical, physical, and human vulnerabilities.

## Red Teaming AI

A working definition of the very new concept of AI red teaming is that it is structured testing to identify flaws and vulnerabilities in AI systems, typically conducted in controlled environments with developer collaboration. For LLMs specifically, red teaming is defined as "a process where participants interact with the LLM under test to help uncover incorrect or harmful behaviors"[^17]. LLM developer companies have implemented various approaches to red teaming, ranging from comprehensive security assessments to narrower evaluations focused on specific genAI features[^18]. Over the last two years, such approaches have emerged as "a critical practice in assessing the risks of AI models and systems"[^19].

Despite its growing popularity, researchers have identified significant challenges with current AI red teaming practices. There remains "a lack of consensus around the scope, structure, and assessment criteria for AI red-teaming"[^20], raising concerns that red teaming may sometimes function more as "security theater" than substantive risk mitigation. Many current approaches focus too narrowly on the models themselves, neglecting how vulnerabilities might manifest in production systems where AI models are a part of broader systems[^18]. Additionally, "AI experts are mostly not thinking about insider risk"[^21], and most testing processes remain limited to English-language evaluations[^17].

The process itself presents challenges for participants, who may experience negative psychological impacts when "required to think like adversaries and interact with harmful content, which can lead to decreased productivity or psychological harm"[^19]. Many red-teamers also lack training in crucial disciplines outside their technical expertise, as "employee red-teamers typically have little training in any other relevant proficiencies whether linguistic, sociocultural, historical, legal, or ethical"[^22].

As the field matures, there's growing recognition that "red teaming on its own is not a panacea for risk assessment"[^19]. More effective approaches like violet teaming are emerging that integrate complementary methods, recognizing that "red teaming provides awareness of risks, while blue teaming responds with solutions"[^23]. The concept of "violet teaming". Future success will likely depend on embracing greater diversity, and focusing more on practical red-teaming efforts that address "attacks that occur in practice, which are often less sophisticated than attacks present in academic papers"[^24].

## What's missing?

As such, the state-of-the-art of AI red teaming over indexes on model-specific behaviors rather than how these models interact with broader systems and social contexts, as well as the downstream consequences of their output. Current AI red teaming efforts tend to focus narrowly on harms rather than technical vulnerabilities while overlooking broader socio-technical considerations. The public interest dimension of red teaming remains underdeveloped[^25].

To mitigate these flaws, AI red teams must embrace cybersecurity's decades of experience with security testing and reporting. A lot of the testing done in the name of red teaming AI systems can be structured and automated through frameworks like MITRE ATT&CK for understanding adversarial behaviors, prioritizing vulnerabilities, and coordinating defensive responses[^26], and established practices for continuous monitoring, automated testing, and incident response[^27]. In comparison, true red teaming requires "an alchemist mindset" that extends beyond purely technical approaches[^28]. Successful cyber red team engagements typically involve creating diverse, highly realistic scenarios producing "actionable insights for proactive remediation"[^29]—principles that are often missing from AI red teaming.

Any red team activity should be part of a larger, coordinated risk and security effort. This includes pre-mortems conducted before the development of a model and associated systems begins, risk assessments of the model and associated systems, incorporation of AI-specific security processes in the model development lifecycle, inclusion of relevant security teams that can harden the model and associated systems, and a dedicated blue team that works with the red team to ensure security is a priority during development, deployment, production and retirement of the model and associated systems. In the next blog post, we'll dive deep into the strategies and mechanisms that can make this possible.

## About the Authors
[Brian Pendleton](https://www.linkedin.com/in/bwpen/) is an AI security researcher and Founding Director of ARVA. He is passionate about pariticipatory approaches in mitigating AI security harms, and was one of the founding members of the [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/). Besides leading ARVA activities, Brian also leads community efforts in AI Village.

[Abhishek Gupta](https://montrealethics.ai/in-memoriam-abhishek-gupta-dec-20-1992-sep-30-2024) was Founder and Principal Researcher of the Montreal AI Ethics Institute ([MAIEI](https://montrealethics.ai/)), Director for Responsible AI at the Boston Consulting Group (BCG), and a pioneering voice in the field of AI ethics. Abhishek’s research has been published in leading AI journals and presented at top-tier machine learning conferences such as NeurIPS, ICML, and IJCAI. Abhishek was also a Global Shaper with the World Economic Forum, a member of The Banff Forum, a Senior Fellow in Responsible AI at the United Nations Institute for Disarmament Research (UNIDIR), a Technical Committee Member at Accessibility Standards Canada, and more. 

[Subho Majumdar](https://www.subhomajumdar.com/) is a technical leader in AI ethics, security, and safety who believes in a community-centric approach to data-driven decision making. He has pioneered the use of trustworthy AI methods in multiple companies, wrote a [book](https://www.amazon.com/Practicing-Trustworthy-Machine-Learning-Transparent/dp/1098120272), and founded a number of nonprofit efforts in this area---Trustworthy ML Initiative, Bias Buccaneers, and AVID. Currently, Subho is Co-founder and Head of AI at [Vijil](http://vijil.ai/), an AI software startup on a mission to help developers build and operate intelligent agents that people can trust.

## References

[^1]: [The Tenth Man Rule: How to Take Devil’s Advocacy to a New Level](https://themindcollection.com/the-tenth-man-rule-devils-advocacy/). Meyer, 2025.

[^2]: [Kriegsspiel -- How a 19th Century Table-Top War Game Changed History](https://militaryhistorynow.com/2019/04/19/kriegsspiel-how-a-19th-century-war-game-changed-history/). Kay, 2020.

[^3]: [Red team](https://en.wikipedia.org/wiki/Red_team). Wikipedia, 2025.

[^4]: [9/11 Was A Terrible Tragedy: It Was Also The Birth Of Red Teaming](https://www.redteamthinking.com/blog/911-was-a-terrible-tragedy-it-was-also-the-birth-of-red-teaming). Red Team Thinking, 2021.

[^5]: [The Psychology of Red Teaming with Bryce Hoffman](https://www.rogerdooley.com/red-teaming-hoffman/). Dooley, 2017.

[^6]: [The History of Red Team Exercises](https://techround.co.uk/guides/history-red-team-exercises/). TechRound, 2023.

[^7]: [Red Team VS Blue Team: What’s The Difference?](https://purplesec.us/learn/red-team-vs-blue-team-cyber-security/) Firch, 2024.

[^8]: [What is red teaming?](https://www.ibm.com/think/topics/red-teaming) Anderson, Holdsworth, and Kosinski, 2025.

[^9]: [What is Red Teaming Cyber Security? How Does it Work?](https://www.sapphire.net/blogs-press-releases/red-teaming-cyber-security/) Sapphire, 2024.

[^10]: [Penetration Testing vs. Red Teaming](https://www.schellman.com/blog/cybersecurity/penetration-testing-vs-red-teaming). Tomkiel, 2024.

[^11]: [Red Teaming Operations](https://www.redscan.com/services/red-team-operations/). Redscan, 2024.

[^12]: [CA-8(2): Red Team Exercises](https://csf.tools/reference/nist-sp-800-53/r4/ca/ca-8/ca-8-2/). CSF Tools, 2021.

[^13]: [Enhancing Cyber Resilience: Insights from CISA Red Team Assessment of a US Critical Infrastructure Sector Organization](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-326a). CISA, 2024.

[^14]: [Penetration Testing: Understanding Red, Blue, & Purple Teams](https://www.compassitc.com/blog/penetration-testing-understanding-red-blue-purple-teams). DePalma, 2023.

[^15]: [Integrated IT-OT Assessment and Governance Model for Improved Holistic Cybersecurity](https://www.researchgate.net/publication/353175509_Integrated_IT-OT_Assessment_and_Governance_Model_for_Improved_Holistic_Cybersecurity). Frumento, ResearchGate, 2021.

[^16]: [What is red teaming?](https://www.techtarget.com/whatis/definition/red-teaming) Kirvan, TechTarget, 2024.

[^17]: [Red Teaming Contemporary AI Models: Insights from Spanish and Basque Perspectives](https://arxiv.org/abs/2503.10192). Romero-Arjona et al, arXiV, 2025.

[^18]: [Lessons From Red Teaming 100 Generative AI Products](https://arxiv.org/abs/2501.07238). Bullwinkel *et al*, arXiV, 2025.

[^19]: [OpenAI's Approach to External Red Teaming for AI Models and Systems](https://arxiv.org/abs/2503.16431). Ahmad *et al*, arXiV, 2025.

[^20]: [Red-Teaming for Generative AI: Silver Bullet or Security Theater?](https://arxiv.org/abs/2401.15897) Feffer *et al*, arXiV, 2024.

[^21]: [I'm Sorry Dave: How the old world of personnel security can inform the new world of AI insider risk](https://arxiv.org/abs/2504.00012). Martin and Mercer, arXiV, 2025.

[^22]: [AI red-teaming is a sociotechnical challenge: on values, labor, and harms](https://arxiv.org/abs/2412.09751). Gillespie *et al*, arXiV, 2025.

[^23]: [The Promise and Peril of Artificial Intelligence -- Violet Teaming Offers a Balanced Path Forward](https://arxiv.org/abs/2308.14253). Titus and Russell, arXiV, 2023.

[^24]: [Attack Atlas: A Practitioner's Perspective on Challenges and Pitfalls in Red Teaming GenAI](https://arxiv.org/abs/2409.15398), Rawat *et al*, arXiV, 2024.

[^25]: [Red-Teaming in the Public Interest](https://datasociety.net/library/red-teaming-in-the-public-interest). Singh *et al*, 2025.

[^26]: [MITRE ATT&CK](https://attack.mitre.org/), MITRE, 2023.

[^27]: [Security and Privacy Controls for Information Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final). NIST, 2020.

[^28]: [Summon a demon and bind it: A grounded theory of LLM red teaming](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0314658). Inie *et al*, PLOS One, 2025.

[^29]: [Enhancing cybersecurity resilience through advanced red-teaming exercises and MITRE ATT&CK framework integration: A paradigm shift in cybersecurity assessment](https://www.sciencedirect.com/science/article/pii/S2772918424000432). Yulianto *et al*, Cyber Security and Applications, 2025.
