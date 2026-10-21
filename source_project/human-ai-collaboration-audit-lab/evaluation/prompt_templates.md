# Prompt templates

Record exact prompts and outputs in the interaction log. Use the same task prompt for both conditions.

## Task prompt template

> You are assisting with a fictional healthcare governance exercise. Use only the source evidence supplied below. Do not invent facts, dates, policies, causes, or outcomes. Distinguish evidence from inference and recommendation. If evidence is insufficient, say so explicitly.
>
> **Task:** {task_instructions}
>
> **Source evidence:** {source_evidence}
>
> **Required output elements:** {required_output_elements}
>
> For each material factual claim, identify the source fact that supports it. Do not provide clinical diagnosis or treatment advice.

## One-shot condition
Submit the task prompt once and save the complete answer as `initial_output`. Do not provide corrective feedback in this condition.

## Structured-revision condition
First submit the same task prompt and save the initial answer. Then submit this standardised feedback prompt:

> Review your previous answer only against the source evidence and required output elements provided in the original task. Identify each factual claim that is unsupported, contradictory, incomplete, or not traceable to the evidence. Then provide a revised answer. Do not add new facts or external knowledge. Mark unresolved uncertainty explicitly. Include a short correction log listing each change and the source evidence supporting it.

Save the exact feedback prompt and complete revised answer. Do not silently edit the model output before scoring.

## Important
This is a research prototype, not a clinical decision-support system. Do not enter real patient information or confidential workplace material. Model responses are observations to be evaluated, not authoritative answers.
