"""Recompute paired signer-level QCA comparisons from canonical MU results."""

import csv
import json
from pathlib import Path

from scipy.stats import ttest_rel


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "runs" / "mu_loso_results.csv"
OUTPUT = ROOT / "paper" / "evidence" / "mu_paired_tests.json"


def main() -> None:
    rows = list(csv.DictReader(SOURCE.open(newline="", encoding="utf-8")))
    by_method = {
        method: {
            int(row["held_out_signer"]): row
            for row in rows
            if row["method"] == method
        }
        for method in ("none", "mlp", "qca", "se")
    }
    comparisons = {}
    for method in ("none", "mlp", "se"):
        qca = [float(by_method["qca"][signer]["test_accuracy"]) for signer in range(1, 6)]
        other = [float(by_method[method][signer]["test_accuracy"]) for signer in range(1, 6)]
        result = ttest_rel(qca, other)
        comparisons[f"qca_vs_{method}"] = {
            "t_statistic": float(result.statistic),
            "p_value": float(result.pvalue),
            "n_pairs": 5,
        }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(
            {
                "source": str(SOURCE.relative_to(ROOT)),
                "test": "two-sided paired t-test over held-out signer accuracies",
                "comparisons": comparisons,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
