* Human-AI Collaboration Audit Lab: preliminary descriptive analysis only.
* Fictional scenarios; provisional scores; no independent ratings.
* Exclude duplicate HG002 record and unresolved records from any comparison.

GET DATA
 /TYPE=TXT
 /FILE='AI_Audit_Lab_Cleaned_Analysis_Dataset.csv'
 /ENCODING='UTF8'
 /DELCASE=LINE
 /DELIMITERS=","
 /QUALIFIER='"'
 /ARRANGEMENT=DELIMITED
 /FIRSTCASE=2
 /IMPORTCASE=ALL
 /VARIABLES=
 output_id A45 scenario_id A8 scenario_name A30 condition A8 stage A24
 accuracy_score F2.0 evidence_fidelity_score F2.0 completeness_score F2.0 traceability_score F2.0
 correction_success_score F2.0 unsupported_claim_count F3.0 error_types A80 provenance_status A120
 prompt_alignment_status A100 protocol_deviation A140 eligible_primary_A_vs_B A70 assessment_status A90 notes A250.
EXECUTE.

FREQUENCIES VARIABLES=condition stage accuracy_score evidence_fidelity_score completeness_score traceability_score correction_success_score unsupported_claim_count /ORDER=ANALYSIS.
DESCRIPTIVES VARIABLES=accuracy_score evidence_fidelity_score completeness_score traceability_score unsupported_claim_count /STATISTICS=MEAN STDDEV MIN MAX.
* Filter eligibility manually before making comparisons. Do not infer a causal effect or generalise beyond the pilot.
