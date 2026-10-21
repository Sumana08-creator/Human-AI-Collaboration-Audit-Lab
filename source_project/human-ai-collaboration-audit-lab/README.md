# Human–AI Collaboration Audit Lab

**Research prototype:** Human–AI interaction in fictional healthcare governance tasks  
**Status:** Initial protocol and pilot materials; no empirical findings yet  
**Author:** Sumana Beena Shivaprakash

## Project overview

This project develops a small, transparent evaluation framework for examining how iterative feedback may change AI-generated outputs in fictional healthcare governance tasks.

It compares:
1. **One-shot workflow:** a generative AI system receives the task and source evidence once and produces an answer.
2. **Evidence-based iterative workflow:** the system receives the same task and evidence, then receives structured feedback requesting an evidence check and revision.

Outputs are assessed for evidence-supported accuracy, evidence fidelity, completeness, traceability, correction success, and unsupported claims.

## Scope and integrity statement

This repository begins as a **research protocol and pilot framework**. It does not yet establish that iterative AI collaboration improves performance, that healthcare professionals behave in a particular way, or that findings generalise to real healthcare settings. Findings must only be reported after outputs have been collected, scored, checked, and analysed.

The initial materials use **fictional scenarios and invented evidence only**. Do not include patient records, real incident reports, employer documents, or confidential information. The initial pilot assesses AI outputs, not the behaviour of actual healthcare professionals.

## Research questions

- **RQ1:** What types of evidence errors, unsupported claims, and omissions occur in AI-generated responses to fictional healthcare governance tasks?
- **RQ2:** How do outputs differ between a one-shot workflow and a structured, evidence-based revision workflow?
- **RQ3:** Which verification and traceability practices appear useful for maintaining accountable AI-assisted work?

## Repository structure

- `research/` — protocol and design decisions
- `data/` — fictional scenarios and blank interaction log
- `code/` — scoring and summary script
- `evaluation/` — rubric and prompt templates
- `report/` — report template
- `results/` — generated tables and figures (empty until analysis)
- `docs/` — data dictionary and decision log

## Quick start

Python 3.10 or newer recommended.

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python code/analyse_interactions.py --input data/interaction_log_template.csv --output results
```

The blank template will produce no substantive findings. Add reviewed observations only after completing the pilot and following the protocol.

## Minimum pilot workflow

1. Read `research/research_protocol.md`.
2. Review `data/fictional_scenarios.csv` and `evaluation/evaluation_rubric.md`.
3. Select 3–5 scenarios for a feasibility pilot.
4. Run the same task in both conditions, using the same model/version where possible and recording date and settings.
5. Save the initial output, feedback, and revised output in a working copy of the interaction log.
6. Score outputs using the rubric. Ideally, have a second reviewer independently score a subset.
7. Run the analysis script and manually verify the results.
8. Write up results, including null or mixed findings, limitations, and protocol deviations.

## Research integrity

- Keep protocol, pilot data, and completed findings distinct.
- Never fabricate outputs, observations, participants, quotations, or results.
- Do not claim that rubric scores are validated clinical safety measures.
- Do not use real patient data or confidential workplace documents.
- If real professionals are later recruited, obtain appropriate ethics approval, informed consent, and permissions before recruitment.
- Do not describe this project as peer-reviewed or published unless that status is accurate.
