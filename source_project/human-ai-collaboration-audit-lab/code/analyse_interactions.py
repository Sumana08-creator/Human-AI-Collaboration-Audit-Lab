#!/usr/bin/env python3
"""Summarise scored human–AI interaction pilot logs using descriptive analysis."""
from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

SCORE_COLUMNS = ["accuracy_score", "evidence_fidelity_score", "completeness_score", "traceability_score"]


def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, keep_default_na=True)
    required = {"scenario_id", "condition", *SCORE_COLUMNS, "unsupported_claim_count"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Input is missing required columns: {sorted(missing)}")
    if not df.empty:
        valid_conditions = {"one_shot", "structured_revision"}
        observed = set(df["condition"].dropna().astype(str))
        invalid = observed - valid_conditions
        if invalid:
            raise ValueError(f"Unknown condition values: {sorted(invalid)}")
        for col in SCORE_COLUMNS:
            values = pd.to_numeric(df[col], errors="coerce").dropna()
            if not values.isin([0, 1, 2]).all():
                raise ValueError(f"{col} must contain only 0, 1, 2, or blank values.")
        counts = pd.to_numeric(df["unsupported_claim_count"], errors="coerce").dropna()
        if (counts < 0).any():
            raise ValueError("unsupported_claim_count cannot be negative.")
    return df


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/interaction_log_template.csv")
    parser.add_argument("--output", default="results")
    args = parser.parse_args()
    input_path, output_dir = Path(args.input), Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    df = load_data(input_path)
    if df.empty or df[["scenario_id", "condition"]].dropna().empty:
        print("No scored interaction records found. No findings generated.")
        print("Complete the interaction log and score outputs before running analysis.")
        return
    df["condition"] = df["condition"].astype(str)
    for col in SCORE_COLUMNS + ["unsupported_claim_count"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df["rubric_score_sum"] = df[SCORE_COLUMNS].sum(axis=1, min_count=1)
    summary = df.groupby("condition", dropna=False).agg(
        output_count=("scenario_id", "count"),
        unique_scenarios=("scenario_id", "nunique"),
        mean_accuracy=("accuracy_score", "mean"),
        mean_evidence_fidelity=("evidence_fidelity_score", "mean"),
        mean_completeness=("completeness_score", "mean"),
        mean_traceability=("traceability_score", "mean"),
        mean_rubric_score=("rubric_score_sum", "mean"),
        mean_unsupported_claims=("unsupported_claim_count", "mean"),
        total_unsupported_claims=("unsupported_claim_count", "sum"),
    ).reset_index()
    summary.to_csv(output_dir / "condition_summary.csv", index=False)
    paired = df.pivot_table(index="scenario_id", columns="condition", values="rubric_score_sum", aggfunc="mean")
    if {"one_shot", "structured_revision"}.issubset(paired.columns):
        paired["difference_revision_minus_one_shot"] = paired["structured_revision"] - paired["one_shot"]
        paired.reset_index().to_csv(output_dir / "paired_score_differences.csv", index=False)
    plot_df = summary.melt(id_vars="condition", value_vars=["mean_accuracy", "mean_evidence_fidelity", "mean_completeness", "mean_traceability"], var_name="dimension", value_name="mean_score").dropna(subset=["mean_score"])
    if not plot_df.empty:
        ax = plot_df.pivot(index="dimension", columns="condition", values="mean_score").plot(kind="bar", ylim=(0, 2), rot=20)
        ax.set_ylabel("Mean rubric score (0–2)")
        ax.set_xlabel("Rubric dimension")
        ax.set_title("Exploratory rubric scores by condition")
        ax.legend(title="Condition")
        plt.tight_layout()
        plt.savefig(output_dir / "rubric_scores_by_condition.png", dpi=160)
        plt.close()
    print(f"Saved descriptive summaries to: {output_dir.resolve()}")
    print("Interpret results cautiously; inspect missingness and verify calculations.")

if __name__ == "__main__":
    main()
