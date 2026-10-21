# Human–AI Collaboration Audit Lab

### Exploring Human–AI Communication, Evidence Evaluation, Error Correction, and Accountability

## 1. Project Overview

The Human–AI Collaboration Audit Lab is an exploratory research project investigating how generative AI responds to structured tasks, how its outputs can be evaluated against source evidence, and how a structured human review process can identify and address errors, omissions, and unsupported claims.

The project examines an important question in human–AI collaboration: **How can people evaluate, challenge, correct, and maintain control over AI-generated outputs when accuracy, evidence fidelity, and accountability matter?**

Rather than treating an AI response as a finished product, the project approaches AI-assisted work as a process involving initial generation, evidence-based evaluation, feedback, and potential revision. It investigates how these stages can be documented and assessed, and what the resulting observations reveal about the strengths and limitations of a structured human–AI review process.

The pilot uses fictional healthcare-governance scenarios as a controlled setting for examining these questions. These scenarios involve training compliance, equipment-check delays, handover documentation, audit exceptions, overdue actions, and changes in recorded complaints. They provide opportunities to assess whether AI-generated statements remain faithful to the supplied evidence, distinguish established facts from uncertainty, and avoid unsupported conclusions.

All scenarios are fictional. The project is methodological and exploratory rather than an evaluation of real patients, healthcare organisations, or clinical decisions.

## 2. Research Motivation

As generative AI becomes integrated into knowledge-intensive work, its outputs increasingly require human interpretation, verification, and judgement. Producing an answer is only one part of the process. People must also decide whether the answer is supported by evidence, whether important information has been omitted, when an output requires correction, and when human intervention is necessary.

This project explores these challenges through an evidence-centred approach to human–AI interaction.

Its central interests include:

* **Human–AI communication:** Examining the relationship between initial AI responses, structured review, feedback, and revised outputs.
* **Evidence evaluation:** Assessing whether claims can be traced to the information supplied for a task.
* **Error detection and correction:** Identifying contradictions, unsupported claims, omissions, overgeneralisation, and failures to follow task instructions.
* **Human judgement and control:** Emphasising the importance of questioning AI-generated content rather than accepting it automatically.
* **Transparency and accountability:** Maintaining records of assessment decisions, unresolved uncertainties, methodological limitations, and corrections.
* **Responsible AI-assisted work:** Exploring how structured evaluation can support more careful use of AI in evidence-sensitive professional contexts.

These interests connect the project to broader questions about human agency, communication practices, professional judgement, and accountability in AI-augmented work.

## 3. Research Questions

The exploratory pilot is organised around the following questions:

1. How can the quality of AI-generated responses to evidence-based professional tasks be assessed systematically?
2. What types of factual errors, unsupported claims, omissions, and evidence-traceability problems can be identified through structured review?
3. How can an initial response and a subsequently revised response be evaluated for changes in accuracy, evidence fidelity, completeness, and traceability?
4. What methodological challenges arise when comparing one-shot AI responses with responses produced through an additional review-and-revision stage?
5. What can this approach contribute to understanding human oversight, feedback, and accountability in AI-assisted professional work?

These questions guide the pilot's current analysis. They are exploratory and do not imply that the study has established the effectiveness of structured revision.

## 4. Research Design and Methodology

The project uses a structured, scenario-based design to examine AI-generated responses under two conditions:

* **Condition A — One-shot response:** An initial AI response to a fictional governance scenario.
* **Condition B — Review and revision:** An initial AI response followed by a structured evidence-checking and revision stage.

The intended comparison concerns how responses are assessed and whether a revision process identifies or corrects material problems. A valid comparison requires sufficiently documented prompts, source evidence, response histories, and assessment procedures.

The evaluation framework considers four dimensions:

1. **Accuracy:** Whether the response is consistent with the supplied evidence.
2. **Evidence fidelity:** Whether factual statements remain faithful to the source material.
3. **Completeness:** Whether the response addresses the relevant information and requirements of the task.
4. **Traceability:** Whether material claims can be connected to identifiable source evidence.

A structured error-classification scheme is also used to record issues such as contradictions, unsupported claims, omissions, overgeneralisation, traceability problems, and missed instructions.

The project uses descriptive analysis and documented evidence review. IBM SPSS Statistics was used for frequency distributions and descriptive statistics, while Python-based project materials support the organisation and analysis of study data.

The methodology prioritises explicit decision rules, transparent documentation, preservation of uncertainty, and clear separation between observed evidence, interpretation, and recommendations.

## 5. Preliminary Findings and Limitations

The current work represents an exploratory pilot rather than a completed comparative evaluation.

The available analysis contains 19 records, with 15 records having recorded scores for the four assessment dimensions and four records missing scores. All 15 recorded scores are 2 across the four dimensions. This lack of score variation creates a ceiling effect and limits the ability of the scoring results to distinguish performance between records.

The review has also identified unresolved issues involving source provenance and the eligibility of records for a primary comparison between Conditions A and B. No scenario is currently confirmed as eligible for that primary comparison. The assessment process has not included an independent second reviewer.

Consequently, the current results do not establish that structured revision improves AI performance, that AI-generated responses are consistently reliable, or that the scoring framework is independently validated.

These limitations are documented as part of the research process. They inform the interpretation of the results and identify areas requiring further methodological development.

## 6. Relevance to Human–AI Interaction Research

This project is motivated by the broader question of how people maintain judgement and accountability when working with generative AI.

Its emphasis on iterative interaction, evidence evaluation, error correction, and the documentation of human review provides an initial methodological perspective on the work required to make AI-assisted processes dependable.

The project is particularly relevant to research interests concerning:

* How people communicate with and refine generative AI outputs.
* How feedback and correction shape successive stages of human–AI interaction.
* How responsibility and decision-making are distributed between people and AI systems.
* How people evaluate AI outputs and decide when to intervene.
* How transparency and accountability can be incorporated into AI-supported professional workflows.

The current pilot examines these questions in fictional healthcare-governance tasks. It does not yet establish how the observed patterns generalise to other professions, real-world workplaces, or interactions unfolding over extended periods.

Further research could build on this foundation by studying human participants in authentic professional settings, documenting interaction histories over time, and combining quantitative assessment with qualitative investigation of users' reasoning, communication practices, and experiences.

## 7. Research Integrity and Reproducibility

Research integrity is a central principle of this project.

The repository preserves research materials, analysis files, methodological documentation, assessment records, and project outputs to support transparency and review.

The project aims to distinguish clearly between source-supported findings, analytical interpretations, recommendations, and unresolved uncertainties. Missing information is not automatically treated as evidence of poor performance, and the limitations of the current data are acknowledged rather than concealed.

The pilot uses fictional scenarios and is intended as a methodological exercise. Its current findings should be interpreted within the scope of the available records and documented assessment process.

## 8. Future Research Direction

The next stage of development would strengthen the study design before making broader comparative claims. Priorities include resolving prompt and source provenance, defining eligibility criteria for paired comparisons, preserving complete interaction histories, and introducing independent assessment.

A subsequent study could extend the approach beyond fictional scenarios to investigate how professionals actually prompt, evaluate, revise, and use AI-generated content in their everyday work.

Such an extension could combine interaction logs, interviews, observations, or other suitable empirical methods to examine how human–AI communication evolves, how users adapt their practices, and how human judgement and control are maintained.

The longer-term research interest is to contribute to a more evidence-based understanding of human–AI collaboration and to inform the responsible design and governance of AI-assisted work.

---

**Project status:** Exploratory pilot
**Domain:** Human–AI interaction, evidence evaluation, and healthcare governance
**Methods:** Scenario-based evaluation, structured error classification, descriptive statistics, and documented review
**Tools:** Python and IBM SPSS Statistics
**Data:** Fictional scenarios and research materials
**Current claim:** Methodological exploration; comparative effectiveness has not been established.


## Purpose
Exploratory pilot on evidence fidelity, error detection, structured AI response
revision, and accountability using fictional healthcare-governance scenarios.

## Scope
Fictional scenarios only. This is not clinical validation and does not use real
patient data. The current records do not establish a valid primary paired
Condition A versus Condition B comparison.

## SPSS
The `spss/` folder contains locally available SPSS datasets, output files and
syntax. The `.sav` files are saved analysis copies; `.spv` files preserve SPSS
output. Review the output and dataset together before reporting results.

## Data and documentation
- `data/`: Excel and CSV datasets
- `spss/`: SPSS data, output and syntax
- `research/`: manuscript and literature-review files
- `report/`: reports and supporting documents
- `audit_trail/`: provenance, verification records, ZIP archives and manifest
- `source_project/`: preserved copy of the existing local project
- `docs/`: README and supporting documentation

## Important limitations
- No scenario is currently confirmed eligible for the primary paired A-versus-B
  comparison.
- Some prompts, source alignment and run metadata remain unverified.
- Available rubric scores are provisional single-assistant assessments.
- Do not claim revision effectiveness or inferential significance from this pilot.

## Reproducibility
See `audit_trail/LOCAL_FILE_MANIFEST.csv` for copied file paths, sizes and
SHA-256 checksums. The manifest records the local files copied by the preparation
script; it does not authenticate the original historical AI runs.
