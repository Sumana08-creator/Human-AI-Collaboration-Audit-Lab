# Research protocol

## 1. Working title
**Human–AI Interaction in Healthcare Governance: Error Detection, Evidence Fidelity, and Accountability in Fictional Audit Tasks**

## 2. Status and purpose
This is a pre-analysis protocol for a small controlled pilot using fictional healthcare governance scenarios. The initial study assesses AI-generated outputs, not the behaviour or competence of actual healthcare professionals. It is a feasibility and methods exercise, not a clinical validation study.

## 3. Rationale
Generative AI can produce fluent professional documents, but fluency alone does not establish that a response is correct, supported, complete, or traceable to source evidence. This project examines how interaction design—especially structured feedback and revision—changes output quality and what limitations remain after revision.

## 4. Research questions
- **RQ1:** What types of evidence errors, unsupported claims, and omissions occur in AI-generated responses to fictional healthcare governance tasks?
- **RQ2:** How do outputs differ between a one-shot workflow and a structured, evidence-based revision workflow?
- **RQ3:** Which verification and traceability practices appear useful for maintaining accountable AI-assisted work?

## 5. Design
A small, paired, scenario-based output evaluation. For each selected scenario, create two outputs:
- **Condition A — one-shot:** the model receives the task and source evidence and produces one answer.
- **Condition B — structured revision:** the model receives the same task and source evidence, then receives a standardised feedback prompt requesting an evidence check and revision.

Use the same model/version, task wording, source evidence, and settings where possible. Record the model/version, date, settings if visible, and deviations. If settings cannot be controlled, record that limitation. This design does not isolate every possible mechanism of human–AI collaboration and does not involve real professional users unless separately approved.

## 6. Scenario selection
The initial dataset contains fictional cases with short evidence packs and reference facts. Select 3–5 scenarios for a feasibility pilot. Freeze the scenarios before collecting outputs. Do not change source evidence after seeing outputs without recording the change. Avoid tasks requiring clinical diagnosis, treatment advice, or real-world safety decisions.

## 7. Procedure
1. Select and freeze the scenarios.
2. Submit the one-shot prompt and save the complete response.
3. Submit the structured-revision condition using the same initial task and save the revision prompt and revised response.
4. Record prompts, outputs, model/version and date in the interaction log.
5. Score each response using the predefined rubric.
6. Where feasible, ask a second reviewer to independently score a subset without seeing the condition label.
7. Record ambiguity, rubric issues, missing values, and protocol deviations.
8. Run the analysis script and manually verify calculations.
9. Report all completed scenarios, missingness, deviations, and limitations.

## 8. Outcomes and scoring
The rubric uses ordinal scores from 0 to 2 for evidence-supported accuracy, evidence fidelity, completeness, traceability, and correction success (revised outputs only). Unsupported claims are also counted separately. These are exploratory researcher-developed coding measures, not validated clinical or organisational safety scales.

## 9. Analysis plan
For paired outputs, report the number of scenarios, rubric score distributions by condition, within-scenario score differences, unsupported-claim counts, error categories, and carefully selected examples from recorded outputs. Use descriptive summaries and paired tables/plots. Avoid strong inferential or causal claims from a very small pilot. If the pilot is expanded, revise the analysis plan before analysing the expanded dataset.

## 10. Quality assurance
Maintain an audit trail for prompts, outputs, scoring and revisions. Use a stable rubric version. Record reviewers using non-identifying labels. Double-score a subset if feasible and report agreement descriptively. Do not silently replace missing or ambiguous data. Manually verify generated summary tables against the source log.

## 11. Ethics, privacy, and safety
All initial cases are fictional. Do not include patient data, employer documents, identifiable people, or confidential material. This initial pilot does not involve human participants. If real professionals are later recruited, obtain relevant ethics approval, informed consent, data-management plans, and organisational permissions before recruitment. Do not use this prototype to make or validate clinical decisions.

## 12. Limitations
The pilot may use few scenarios, a single model, and one researcher for scoring. Outputs may vary across model versions and runs. The rubric is unvalidated. Fictional scenarios do not reproduce the full complexity of professional work. Results cannot establish how healthcare workers actually behave, clinical safety, or generalisability to other professions.

## 13. Reporting commitments
Report results regardless of whether revision improves, worsens, or does not materially change output quality. Separate protocol decisions from post-hoc observations. Do not fabricate data or claim findings before completing the procedure.
