# Project Inventory

## Repository Map

- `src/models/quantum_attention.py`: QCA-v1 and data-reuploading QCA-v2.
- `src/models/densenet_quantum_attention.py`: DenseNet121 with QCA.
- `src/models/classical_attention.py`: SE and parameter-matched MLP controls.
- `src/train_quantum.py`: Kaggle QCA training and checkpointing.
- `src/train_classical_attention.py`: matched classical-control training.
- `src/mu_dataset.py`, `src/train_mu_loso.py`: MU signer-held-out pipeline.
- `src/summarize_low_data.py`, `src/summarize_mu_loso.py`: deterministic
  aggregation and figures.
- `configs/`: resolved experiment families and reproduction defaults.
- `runs/`: checkpoints, histories, reports, canonical CSVs, and plots.

## Method Evidence

- QCA projects 1,024 pooled DenseNet features to eight angles, applies
  `tanh(z) * pi/2`, runs an eight-qubit two-layer PennyLane circuit, measures
  eight Pauli-Z expectations, and projects them to 1,024 sigmoid gates.
- PennyLane simulation runs on CPU; CNN operations use MPS when available.
- The matched MLP retains the same 1,024-to-8 and 8-to-1,024 projections and
  differs from QCA by 16 attention parameters.
- Every MU model leaves all DenseNet layers trainable and uses differential
  backbone/head learning rates.

## Experiment Evidence

- `runs/low_data_results.csv`: 36 independently evaluated low-data runs.
- `runs/low_data_summary.csv`: three-seed means and sample standard deviations.
- `runs/mu_loso_results.csv`: 20 method-by-signer external runs.
- `runs/mu_loso_summary.csv`: equal-signer and pooled summaries.
- Run directories contain `resolved_config.yaml`, `history.csv`,
  `best_model.pt`, and test reports or metrics.

## Writing Assets

- `REPORT.md`: completed technical report and protocol history.
- `runs/low_data_learning_curve.png`: low-data result plot.
- `runs/mu_loso_signer_accuracy.png`: per-signer external accuracy.
- `runs/mu_loso_confusion_matrices.png`: pooled external confusion matrices.

## Citation Assets

- No project bibliography existed before this draft.
- Source comments point to arXiv works but are not accepted as verified
  bibliography records without metadata and claim checks.

## Missing Inputs

- Target venue, template, page limit, and anonymity requirements.
- Additional external training seeds.
- Quantum-hardware or noisy-simulator measurements.
- A reliable licence statement for the third-party MU dataset mirror.
