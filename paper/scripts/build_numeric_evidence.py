"""Build the manuscript numeric-evidence registry from canonical sources."""

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "numeric_evidence.json"


def entry(value, source, selector, representations=("raw",), tolerance=1e-6, note=""):
    result = {
        "value": value,
        "source": source,
        "selector": selector,
        "aggregate": "identity",
        "representations": list(representations),
        "tolerance": tolerance,
    }
    if note:
        result["note"] = note
    return result


def csv_rows(path):
    with (ROOT / path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def add_csv_value(entries, path, row, column, where, representations=("raw",), tolerance=1e-6):
    entries.append(
        entry(
            float(row[column]),
            path,
            {"kind": "csv", "column": column, "where": where},
            representations,
            tolerance,
        )
    )


def walk_numbers(value, pointer=""):
    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk_numbers(child, f"{pointer}/{key}")
    elif isinstance(value, (int, float)) and not isinstance(value, bool):
        yield pointer, value


def main():
    entries = []

    low_path = "runs/low_data_summary.csv"
    low_rows = csv_rows(low_path)
    for row in low_rows:
        where = {"model": row["model"], "train_fraction": row["train_fraction"]}
        for column in (
            "test_acc_mean",
            "test_acc_sample_std",
            "macro_f1_mean",
            "macro_f1_sample_std",
        ):
            add_csv_value(entries, low_path, row, column, where, ("percent",), 0.0051)

    for fraction in ("0.01", "0.05", "0.1"):
        row = next(
            item for item in low_rows
            if item["model"] == "none" and item["train_fraction"] == fraction
        )
        add_csv_value(
            entries,
            low_path,
            row,
            "train_fraction",
            {"model": "none", "train_fraction": fraction},
            ("percent",),
        )

    for method in ("none", "mlp", "qca", "se"):
        row = next(
            item for item in low_rows
            if item["model"] == method and item["train_fraction"] == "0.1"
        )
        where = {"model": method, "train_fraction": "0.1"}
        for column in ("attention_params", "trainable_params"):
            add_csv_value(entries, low_path, row, column, where)

    mu_summary_path = "runs/mu_loso_summary.csv"
    mu_summary = csv_rows(mu_summary_path)
    for row in mu_summary:
        where = {"method": row["method"]}
        for column in (
            "signer_mean_accuracy",
            "signer_sd_accuracy",
            "signer_mean_macro_f1",
            "signer_sd_macro_f1",
            "pooled_accuracy",
            "pooled_macro_f1",
        ):
            add_csv_value(entries, mu_summary_path, row, column, where, ("percent",), 0.0051)
        for column in ("attention_params", "trainable_params", "n_test"):
            add_csv_value(entries, mu_summary_path, row, column, where)

    mu_results_path = "runs/mu_loso_results.csv"
    mu_results = csv_rows(mu_results_path)
    for row in mu_results:
        where = {
            "method": row["method"],
            "held_out_signer": row["held_out_signer"],
        }
        add_csv_value(
            entries,
            mu_results_path,
            row,
            "test_accuracy",
            where,
            ("percent",),
            0.0051,
        )

    constants_path = "paper/evidence/study_constants.json"
    constants = json.loads((ROOT / constants_path).read_text(encoding="utf-8"))
    for pointer, value in walk_numbers(constants):
        representations = ["raw"]
        if pointer.endswith("_accuracy"):
            representations.append("percent")
        tolerance = 0.0051 if pointer.endswith("_ratio") else 1e-6
        entries.append(
            entry(
                value,
                constants_path,
                {"kind": "json-pointer", "pointer": pointer},
                representations,
                tolerance,
            )
        )

    tests_path = "paper/evidence/mu_paired_tests.json"
    tests = json.loads((ROOT / tests_path).read_text(encoding="utf-8"))
    for comparison, result in tests["comparisons"].items():
        entries.append(
            entry(
                result["p_value"],
                tests_path,
                {
                    "kind": "json-pointer",
                    "pointer": f"/comparisons/{comparison}/p_value",
                },
                ("raw",),
                0.00051,
            )
        )

    OUTPUT.write_text(
        json.dumps(
            {
                "schema_version": "ai-research-writing/numeric-evidence-v2",
                "entries": entries,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
