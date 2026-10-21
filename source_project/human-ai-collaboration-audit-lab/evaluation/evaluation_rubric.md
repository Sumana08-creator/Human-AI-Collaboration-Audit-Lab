# Evaluation rubric and coding guide

Score each output against the supplied fictional source evidence, not general plausibility or writing style. Fluency and confidence are not evidence of correctness. When a claim cannot be judged from the supplied evidence, flag it for review rather than assuming it is true.

Use 0, 1, or 2 for each dimension. Add a short rationale and identify the relevant source fact where possible.

## A. Evidence-supported accuracy
- **0 — Major problem:** A material claim contradicts supplied evidence, or multiple important claims are unsupported.
- **1 — Mixed:** Mostly consistent, but one or more minor errors or unresolved claims remain.
- **2 — Supported:** Material claims are consistent with the supplied evidence; no material contradiction identified.

## B. Evidence fidelity
- **0 — Poor:** Misstates or materially distorts key facts.
- **1 — Partial:** Most key facts are represented, but important nuance or context is lost.
- **2 — Strong:** Key facts and qualifications are accurately represented.

## C. Completeness
- **0 — Incomplete:** Omits a required major issue or section.
- **1 — Partial:** Addresses the main task but omits a relevant detail or qualification.
- **2 — Complete for task:** Covers all required elements in the scenario instructions.

## D. Traceability
- **0 — Not traceable:** Conclusions are not linked to supplied evidence, or references to evidence are misleading.
- **1 — Partial:** Some conclusions are traceable, but others lack clear support.
- **2 — Traceable:** Important factual claims and recommendations are linked to evidence or clearly labelled as recommendations/inferences.

## E. Correction success (revised outputs only)
- **0 — Not corrected/worsened:** Key identified errors remain or new material errors are introduced.
- **1 — Partially corrected:** Some issues are fixed, but others remain or a minor new issue appears.
- **2 — Corrected without identified new material issue:** Identified issues are corrected and no new material issue is detected in review.

## Unsupported-claim count
Count distinct factual claims not supported by the supplied evidence and not explicitly labelled as assumptions or recommendations. Record the claim and reason. Do not count the same repeated claim multiple times unless repetition creates a separate issue.

## Error-type codes
- `CONTRADICTION` — conflicts with a supplied fact
- `UNSUPPORTED` — factual assertion lacks supplied evidence
- `OMISSION` — required fact or issue is absent
- `OVERGENERALISATION` — conclusion extends beyond the evidence
- `TRACEABILITY` — claim cannot be linked to stated source
- `INSTRUCTION_MISSED` — required task element omitted or format not followed
- `OTHER` — explain in notes

## Scoring cautions
Do not interpret total scores as validated measures of safety or trustworthiness. Do not equate fewer unsupported claims with overall correctness. Record uncertainty and disagreements rather than forcing consensus. If a dimension does not apply, leave it blank and explain why; do not automatically enter zero.
