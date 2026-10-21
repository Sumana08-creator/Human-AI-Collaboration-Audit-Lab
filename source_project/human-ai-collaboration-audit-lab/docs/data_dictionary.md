# Data dictionary

## `fictional_scenarios.csv`
- `scenario_id`: stable fictional scenario identifier
- `task_type`: type of governance task
- `scenario_title`: short label
- `context`: fictional task context
- `source_evidence`: facts the model may rely on
- `required_output_elements`: items the response must include
- `reference_facts`: facts reviewers use to assess evidence fidelity
- `safety_note`: interpretation boundaries

## `interaction_log_template.csv`
One row represents one output under one condition. Use two rows per scenario when comparing both conditions.
- `scenario_id`: must match the scenario dataset
- `condition`: `one_shot` or `structured_revision`
- `run_id`: unique run identifier
- `model_name_version`: model name/version if known
- `run_date_utc`: recorded date/time if possible
- `prompt_text`: exact task prompt
- `initial_output`: full initial output
- `feedback_prompt`: exact feedback prompt, if used
- `revised_output`: full revised output if applicable
- `reviewer_id`: non-identifying reviewer label
- `accuracy_score`, `evidence_fidelity_score`, `completeness_score`, `traceability_score`: 0–2 or blank
- `correction_success_score`: 0–2 or blank; revision only
- `unsupported_claim_count`: non-negative integer after review
- `error_types`: semicolon-separated codes from the rubric
- `review_notes`: brief rationale and evidence references
- `protocol_deviation`: describe deviation, otherwise blank

Never put personal, patient, employer, or confidential information in this file. For large outputs, use an appropriate private working copy and publish only material you are permitted to share.
