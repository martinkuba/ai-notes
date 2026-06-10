---
id: "01ktq9vndq3bz23twym21sj2n7"
title: "How Generative and Agentic AI Shift Concern from Technical Debt to Cognitive Debt"
author: "Margaret-Anne Storey"
source_url: "https://margaretstorey.com/blog/2026/02/09/cognitive-debt/"
category: "article"
tags: [ai]
saved_at: "2026-06-09T23:00:39.991000+00:00"
summarized_at: "2026-06-10T00:00:04Z"
---

# How Generative and Agentic AI Shift Concern from Technical Debt to Cognitive Debt

**Original source:** [How Generative and Agentic AI Shift Concern from Technical Debt to Cognitive Debt](https://margaretstorey.com/blog/2026/02/09/cognitive-debt/)

**Author:** Margaret-Anne Storey

## Summary

This article introduces "cognitive debt" as a critical concern in AI-augmented software development, arguing it poses a greater threat than technical debt. While technical debt refers to poor code quality accumulating in source code, cognitive debt refers to the erosion of shared understanding among developers about what a system does, how it works, and how to modify it. As generative and agentic AI accelerate development velocity, this loss of shared mental models becomes the more dangerous obstacle. Storey illustrates this through a student team that hit a development wall not because of messy code, but because no team member could articulate the reasoning behind key design decisions or how components interconnected—a loss of what Peter Naur called the program's "theory."

The article argues cognitive debt demands deliberate mitigation strategies rather than unchecked speed. Teams should ensure at least one human fully understands each AI-generated change, document the reasoning behind decisions (not just what changed), and rebuild shared understanding through pair programming, code reviews, and retrospectives. Warning signs include developer hesitation to make changes, concentration of "tribal knowledge" in few individuals, and perception of the system as a black box. Storey advocates for practices like test-driven development and refactoring—Kent Beck's principle of "make the hard change easy"—to prevent cognitive load from overwhelming teams. She concludes that research is urgently needed on measuring cognitive debt, identifying effective prevention practices, and understanding how it scales across distributed and open-source teams.

## Main Ideas

- Cognitive debt (loss of shared understanding in developers' minds) is a greater threat than technical debt as AI adoption accelerates development velocity
- AI-generated code can be technically clean yet incomprehensible if developers don't understand the underlying design decisions and system architecture
- Programs exist as theories in developers' minds; when this shared understanding fragments, the system becomes unmaintainable regardless of code quality
- Deliberate mitigation strategies are essential: require humans to fully understand AI changes, document reasoning behind decisions, and regularly rebuild shared mental models
- Warning signs of cognitive debt include reluctance to make changes, concentration of critical knowledge in few people, and systems perceived as black boxes
- Practices like pair programming, test-driven development, and refactoring address both technical and cognitive debt by slowing down to build understanding
- Cognitive debt poses unique challenges for distributed teams and open-source projects where newcomers must reconstruct system theory from scratch

## Key Quotes

- "Even if AI agents produce code that could be easy to understand, the humans involved may have simply lost the plot and may not understand what the program is supposed to do, how their intentions were implemented, or how to possibly change it."
- "A program is a theory that lives in the minds of the developer(s) capturing what the program does, how developer intentions are implemented, and how the program can be changed over time." (Peter Naur)
- "Cognitive debt tends not to announce itself through failing builds or subtle bugs after deployment, but rather shows up through a silent loss of shared theory."
