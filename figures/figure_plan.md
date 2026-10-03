# Figure Plan

## Figure 1: Fair-Evaluation Logic

- **Class:** concept/method.
- **Role:** motivation overview.
- **Message:** each common attribution risk requires a corresponding control
  before a strong claim is defensible.
- **Entities:** saturated split, unmatched controls, pooled subjects,
  low-data test, matched baselines, equal-signer metrics, bounded claim.
- **Layout:** three converging risk-to-fix pathways.
- **Backend:** deterministic TikZ for exact terminology.
- **Asset:** `paper/figures/fair_evaluation.tex`.

## Figure 2: QCA Pipeline

- **Class:** concept/method.
- **Role:** architecture overview.
- **Message:** QCA is an eight-dimensional bottleneck gate between pooled
  DenseNet features and the classifier.
- **Entities:** image, DenseNet121, global pooling, down projection, angle
  encoding, two-layer eight-qubit circuit, Pauli-Z measurements, up projection,
  sigmoid gates, classifier.
- **Layout:** left-to-right pipeline with classical components in blue and the
  quantum circuit in purple.
- **Backend:** deterministic TikZ for exact dimensions and operator labels.
- **Asset:** `paper/figures/qca_overview.tex`.
- **Fallback:** concise textual pipeline in the Method section.

## Figure 3: Control Comparison

- **Class:** concept/method.
- **Role:** experimental control overview.
- **Message:** every method shares features and classifier; only the
  intervening channel transformation changes.
- **Layout:** one shared input branching through four methods and reconverging.
- **Backend:** deterministic TikZ.
- **Asset:** `paper/figures/control_comparison.tex`.

## Figure 4: Low-Data Accuracy

- **Class:** evidence/result.
- **Role:** main frozen-study result.
- **Message:** SE leads at every tested fraction; methods converge as data grow.
- **Source:** `runs/low_data_summary.csv`.
- **Backend:** deterministic matplotlib output from `src/summarize_low_data.py`.
- **Asset:** `runs/low_data_learning_curve.png`.

## Figure 5: Held-Out Signer Accuracy

- **Class:** evidence/result.
- **Role:** external generalisation and variability.
- **Message:** rankings vary by signer and signer 5 is substantially harder.
- **Source:** `runs/mu_loso_results.csv`.
- **Backend:** deterministic matplotlib output from `src/summarize_mu_loso.py`.
- **Asset:** `runs/mu_loso_signer_accuracy.png`.

## Removed: Evidence Ladder

The previous evidence-hierarchy figure was removed. It restated the protocol
and did not report a result of the study.

## Figure 6: Proposed QCA Confusion Matrix

- **Class:** evidence/result.
- **Role:** error structure of the proposed module only.
- **Message:** pooled MU mistakes of QCA concentrate on a few letter pairs
  (M/N, V/W, A/T). Counts are printed in occupied cells.
- **Source:** `runs/mu_loso_signer*_qca_seed42/test_predictions.csv`.
- **Backend:** matplotlib heatmap, zeros left blank.
- **Asset:** `paper/figures/qca_confusion_matrix.png`.

## Table Plan

- **Table 1:** parameter counts, QCA row marked proposed.
- **Table 2:** signer-held-out results for proposed QCA versus controls.
- **Table 3:** per-signer accuracies, QCA row marked proposed.
- **Table 4:** frozen low-data accuracy, QCA row marked proposed.
- **Table 5:** frozen low-data macro-F1, QCA row marked proposed.
