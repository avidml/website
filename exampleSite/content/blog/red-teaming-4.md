---
author: "Brian Pendleton Abhishek Gupta, Subho Majumdar"
title: "Red Teaming is a Critical Thinking Exercise: Part 4"
date: "2025-07-29"
description: ""
tags: ["red teaming","ai vulnerabilities"]
categories: ["general"]
layout: single
ShowRelated: false
showToc: false
ShowBreadCrumbs: false
---

# Red Teaming is a Critical Thinking Exercise: Part 4

As we finalize this series of blog posts, let's recap what we've previously discussed. In [part 1](https://avidml.org/blog/red-teaming-1) of the series, we described what red teaming is and what it isn't. The most important idea being that red teaming is not just a security exercise but a broader and deeper critical thinking exercise that helps organizations question assumptions, identify potential gaps in planning, and highlight risks that might be created by their plans.

In [part 2](https://avidml.org/blog/red-teaming-2), we discussed the history of red teaming, its adoption in the cybersecurity space back in the 1980s and now in AI. One key idea is that AI red teaming and AI security has failed to look at the decades of research and practical experience from cybersecurity. The best example of this being the adoption of red teaming as a security measure without understanding where it fits in the overall security lifecycle for any system being developed and put into operation.

In [part 3](https://avidml.org/blog/red-teaming-3) of the series, we illustrated how system-level red teaming can be implemented at various stages in the development; operations, including maintenance; and retirement of an AI system. Then we touched on a new taxonomy of red teaming developed by Inie et al for tactical-level red teaming of models.

In this final post, we will discuss how strategic-level, critical thinking tools can identify the areas of interest for the tactical-level red team employing both critical thinking and technical tools to obtain the information needed to make appropriate decisions regarding the AI systems being developed or used within the organization.

## Strategic-level Red Teaming

As we discussed in part 2 of the series, red teaming was partially birthed from the efforts of several militaries from various times and countries. In 2004, the United States Army created the University of Foreign Military and Cultural Studies (UFMCS) which was often called Red Team University. UFMCS trained military personnel, and some civilians, in the art of critical thinking. As part of that training, staff members wrote The Red Team Handbook, an essential guide to understanding what red teaming is truly about. UFMCS continued to operate till 2020.

The Red Team Handbook[^1] went through nine versions before UFMCS was shut down. Versions 7.0 and 8.0 saw the name change to The Applied Critical Thinking Handbook[^2] but the name returned to The Red Team Handbook for version 9.0. We point this out to highlight that critical thinking will always be an important part of the red team process. Within The Red Team Handbook, there are many different tools presented to help people think critically and we'd like to highlight two of them – Premortems and the Five Whys.

## Premortems

Most people have heard of a postmortem – either in relation to a death or as a review of an incident that has occurred during a project or in a security setting. For our discussion, we want to focus on post-mortems on projects, plans, or security incidents.

A majority of the time, post-mortems are conducted after the project or plan has been completed or after the security incident has been resolved. Often, they are a tool for assigning blame rather than critically thinking about the project, plan or incident. However, with the twist of doing the review before the completion of the project, implementation of the plan or discovery of the security incident, the pre-mortem can help us think critically about the project, plan or incident and allow us to strengthen our plans or prevent failures by identifying issues ahead of time.

When conducting a pre-mortem, a team is gathered to discuss the end-to-end plan to develop a proposed new AI system for use internal or external (customer-facing) to the organization. From the start of the pre-mortem, the group must assume that the system has failed and each member of the group, individually, should use their expertise and knowledge to suggest ways that the systems failed, what caused the failure, and what the impact to the organization could be.

Once each member of the group has individually developed their answers, they are shared with the group and discussed one by one. When several people have the same, or nearly the same idea, that idea is highlighted for more discussion later. When an idea is only brought up by one person, the group members should do a gut check of the idea from their own perspectives, come together to express their opinions, then consider the proposer's perspective, expertise, and experience to decide saliency of that idea. By the end of the discussion, the group should have a prioritized list of possible issues or improvements for the project or plan that can be implemented before the project or plan even begins. By conducting the pre-mortem, the organization can make better plans by anticipating potential points of failure or weakness or highlighting blind spots that need to be investigated further before the project or plan is finalized.

## Five Whys

The 5 Whys was developed as a technique to uncover the root cause of a problem by personnel at Toyota Motors. While often seen and used as a tool for troubleshooting, the 5 Whys can be used to better understand the purpose of an action or plan.

In its simplest form, the name of the tool is exactly how you use the tool. As part of a larger group, a person makes a statement or asks a question, then others in the group take turns asking why questions that will guide the group to get to the root of the problem or the purpose of the action or plan.

While this sounds extremely simple, the tool can provide very valuable information when the group includes representatives from different parts of the organization and experience levels. Additionally, each member of the group should ask why five times, ensuring they are asking a why question from their perspective.

### Example

A department wants to develop an AI agent that can handle routine questions on the organization's website.

The first why question from a finance representative might be – Why should we spend the money on this instead of another product or service?

The first why question from a legal representative might be – Why should we expose ourselves to the risk of a catastrophic failure of the agent to provide correct information?

The first why question from a security representative might be – Why do we want to add a product like this to our system?

When trying to find the reason for an action or plan, there will be times when "why" isn't the appropriate question to ask; instead "who" or "what" questions might be appropriate. At the end of the exercise, the group should have an informed idea of weaknesses or critical areas of an action or plan.

## Tactical-level Red Teaming

One of the most important ideas of tactical-level red teaming is that the organization has identified a risk or concern, sometimes with strategic-level red teaming, that it wants investigated to better understand how that risk or concern can be eliminated or at least mitigated to an acceptable level.

An example of this is when during the strategic planning phase of a product, the potential reputational damage from an AI agent on the organization's public facing website replying to queries with private information about the organization or its customers.

At that point, it's up to the tactical red team to identify the tools it needs to interrogate the underlying model, and the system built around it, to find out if that concern is a possibility. If it is, the red team should then work with the model security team to alleviate the possibility as much as possible.

Remember, the red team isn't there just for those "gotcha moments." The tactical red team is there to help make a product or service better. This might mean making it safer, more secure, more user friendly, or all of those and more.

From a tactical-level AI perspective, there are many different tools that are available to help test models for many different possible risks. Here's a short list of tools to start with:

1. Garak[^3]
2. PyRIT[^4]
3. Counterfit[^5]
4. LM Evaluation Harness[^6]
5. Spyglass[^7]

The list is far from comprehensive but those five are a great starting place for a technical AI red team. Note that these tools are still mostly designed for testing LLMs. To test purpose-built AI Agents, development teams still need to work with internal stakeholders and security/safety experts to design test payloads that are relevant to the potential utilities and harms of the agent under test.

## Conclusion

In this set of blog posts, we have tried to highlight some ideas about red teaming, whether it is for AI or something else.

1. Red teaming is a critical thinking exercise first and foremost.
2. Red teaming is for more than the security team. When possible and appropriate, it should include members of every part of the organization because each area/department/function has its own experiences, needs and perspectives.
3. Red teaming the entire system is just as important as red teaming individual components.
4. Lower-level red teaming, such as technical red teaming, should be driven by concerns, gaps, and risks uncovered in higher-level red teaming exercises.

Though the idea of red teaming as an offensive mindset is probably too ingrained into us at this point to change, we hope that this series of posts has given the reader something to consider about the field of red teaming and how it can be much more than just a technical exercise.

**P.S.** We recently wrote a paper compiling and expanding on the ideas in this series. You can find it [here](https://arxiv.org/abs/2507.05538)!

## References

[^1]: [The Red Team Handbook](https://home.army.mil/wood/application/files/6115/8222/0759/RedTeamHB.pdf). University of Foreign Military and Cultural Studies, version 9.0.

[^2]: University of Foreign Military and Cultural Studies, The Applied Critical Thinking Handbook, version 7.0, January 2015.

[^3]: [Garak](https://garak.ai/)

[^4]: [PyRIT](https://github.com/Azure/PyRIT)

[^5]: [Counterfit](https://github.com/Azure/counterfit)

[^6]: [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness)

[^7]: [Spyglass](https://dreadnode.io/spyglass)