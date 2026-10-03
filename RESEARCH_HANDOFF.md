# Quantum Neural Network Classification — Research Handoff

## Project context

This repository evaluates hybrid quantum-classical image classifiers on the
Kaggle ASL Alphabet dataset: 87,000 RGB images, 29 classes, with an 80/10/10
stratified split and seed 42. The current model applies a PennyLane quantum
channel-attention (QCA) block to pooled CNN features.

Read `AGENTS.md` before making changes. It contains model conventions,
completed runs, data rules, and quantum-circuit constraints.

## Research objective

Do **not** optimize or claim a contribution based only on raw accuracy. The
current random image-level split is near-saturated:

- DenseNet121 baseline: 100.00% held-out test accuracy.
- DenseNet121 + QCA: 100.00% validation accuracy with an unfrozen backbone.
- ResNet50 + QCA: 99.954% validation accuracy at epoch 3 of an incomplete run.

The core question is:

> Can quantum channel attention or a compact hybrid QNN classifier deliver
> competitive accuracy with better parameter efficiency, low-data performance,
> or robustness than fair classical alternatives?

All new experiments must compare matched training conditions and report
held-out test metrics.

## Existing architecture

- `src/models/quantum_attention.py`: `QuantumChannelAttention`.
  - Use `tanh(x) * (pi / 2)` before `AngleEmbedding`.
  - Keep the CPU bridge around PennyLane calls:
    `self.qlayer(z.cpu()).to(src_device)`.
  - Keep `n_qubits <= 10`.
- `src/models/densenet_quantum_attention.py`: DenseNet121 + QCA.
  - QCA is applied after global average pooling to a 1024-d feature vector.
- `src/models/resnet_quantum_attention.py`: ResNet50 + QCA.
  - QCA is applied after global average pooling to a 2048-d feature vector.
- `src/models/classical_attention.py`: existing SE and CBAM modules.
- `src/train_quantum.py`: shared QCA trainer with `--backbone densenet|resnet`.
- `src/evaluate.py`: reconstructs quantum checkpoints using saved
  `args.backbone`.

## Required experiment sequence

Complete phases in order. Do not start a later phase before the corresponding
baseline and evaluation outputs are reproducible.

### Phase A — Finish reference metrics

1. Evaluate the saved unfrozen DenseNet-QCA checkpoint:

   ```bash
   make evaluate \
     CKPT=runs/densenet_quantum/best_model.pt \
     DATA_ROOT=asl-dataset
   ```

2. Complete or cleanly rerun the ResNet50-QCA experiment for seven epochs:

   ```bash
   python -m src.train_quantum \
     --config configs/resnet_quantum.yaml \
     --data-root asl-dataset \
     --epochs 7
   ```

3. Evaluate the ResNet checkpoint after training:

   ```bash
   make evaluate \
     CKPT=runs/resnet_quantum/best_model.pt \
     DATA_ROOT=asl-dataset
   ```

4. Record in `AGENTS.md`:
   - completed epochs;
   - best validation accuracy and epoch;
   - test accuracy and macro-F1;
   - total and attention-module trainable parameter counts;
   - exact config path and output directory.

Acceptance criteria:
- Every reported result has `history.csv`, `best_model.pt`, `test_report.txt`,
  and independent `evaluate.py` output.
- No claim uses validation accuracy as test accuracy.

### Phase B — Train fair classical-attention baselines

Implement a training entry point for the existing SE attention model. Adapt
the structure of `train_quantum.py`; do not create a one-off training loop.

Requirements:
- Support DenseNet121 first, then ResNet50 if practical.
- Match the QCA data split, augmentation, optimiser, scheduler, batch size,
  learning rate, pretrained weights, frozen/unfrozen setting, and epochs.
- Save the same checkpoint fields and artifacts as quantum training.
- Log `attention_params`, total trainable parameters, total parameters, and
  best validation accuracy.
- Add YAML configuration, Makefile target, and a model smoke test.
- Ensure `evaluate.py` reconstructs and evaluates the new checkpoint type.

Run both:

1. Frozen-backbone comparison:
   - QCA + classifier
   - SE + classifier
   - no-attention classifier head

2. Unfrozen-backbone comparison:
   - QCA
   - SE
   - no attention

Important: report the QCA module parameter count separately from all trainable
backbone parameters. An unfrozen 23.6M-parameter ResNet result is not evidence
of QCA parameter efficiency.

Acceptance criteria:
- Each condition has a held-out test result.
- The comparison table contains accuracy, macro-F1, attention parameters,
  total trainable parameters, epochs, and seed.

### Phase C — Low-data sample-efficiency study

This is the preferred primary research contribution.

Add a `train_fraction` configuration/CLI argument to the data pipeline or
training entry point. It must subsample **only the training split**, stratified
by class, after the fixed 80/10/10 split. Validation and test splits must
remain unchanged.

Run fractions:

```text
1%, 5%, 10%, 25%, 50%, 100%
```

Run each fraction with seeds:

```text
42, 43, 44
```

Compare:

```text
No attention
SE attention
QCA
```

Initially use a frozen pretrained backbone to isolate the attention head. If
time permits, repeat the most informative fractions with an unfrozen backbone.

For each run save:

- YAML or JSON copy of resolved configuration;
- `history.csv`;
- checkpoint;
- test report;
- train fraction and seed in checkpoint metadata;
- attention and total parameter counts.

Produce an aggregate CSV with:

```text
model, backbone, train_fraction, seed, best_val_acc, test_acc, macro_f1,
attention_params, trainable_params, total_params, best_epoch
```

Report mean and standard deviation across seeds. Do not select the best seed.

Acceptance criteria:
- All fractions use identical validation/test images for all methods.
- Aggregate results include mean ± standard deviation.
- A learning-curve plot is generated from aggregate results.

### Phase D — QCA ablations

Keep the backbone, split, optimiser, seed, and epoch budget fixed. Use the
best protocol from Phase C, ideally at 10% and 25% training data.

Grid:

```text
n_qubits: 4, 6, 8, 10
n_layers: 1, 2, 3
```

Add control conditions:

1. Trainable QCA circuit — current method.
2. Fixed random circuit — initialize once and freeze circuit parameters.
3. Parameter-matched classical MLP attention — match QCA attention-module
   trainable parameters as closely as possible.

Record circuit parameters, attention parameters, wall-clock time per epoch,
and test metrics. Keep `n_qubits <= 10`.

Acceptance criteria:
- Circuit and classical controls use the same feature projection dimensions.
- Results distinguish “quantum circuit effect” from “extra nonlinear head
  effect.”

### Phase E — Input and circuit noise robustness

Evaluate the best classical and QCA models under deterministic corruption
levels:

- Gaussian noise;
- Gaussian blur;
- JPEG compression;
- brightness/contrast shifts;
- small rotations;
- random occlusion.

Use the unchanged held-out test split. Save metrics for each corruption type
and severity.

Then add a configurable QCA noise mode using PennyLane `default.mixed` and
depolarizing channels. Preserve a noiseless default configuration.

Report:

- clean test accuracy;
- accuracy at every severity;
- relative degradation from clean accuracy;
- parameter count and inference time.

Acceptance criteria:
- Noise is disabled by default.
- The same trained checkpoint is used for clean and corrupted image tests.
- Quantum-noise results identify the device and channel probability.

### Phase F — Compact hybrid QNN classifier

Do not attempt a quantum circuit directly on raw images. Build a compact hybrid
classifier:

```text
image
  -> frozen pretrained CNN feature extractor
  -> learned projection from 1024/2048 features to 4–10 values
  -> tanh scaling to (-pi/2, pi/2)
  -> variational quantum circuit
  -> expectation values
  -> small classical 29-class linear head
```

Compare it with a parameter-matched classical version:

```text
same CNN features
  -> learned projection
  -> small classical MLP
  -> 29-class head
```

Implementation requirements:

- New dedicated model module; do not repurpose the
  `QuantumTokenSelfAttention` stub.
- Preserve the existing `forward_features`, `forward`, factory-function, and
  checkpoint conventions.
- Add model smoke tests including shape and backward-gradient checks.
- Keep circuit inputs on CPU and return outputs to the source device.
- Start with 4 or 6 qubits and one or two layers.

Primary evaluation: low-data sample efficiency from Phase C, not saturated
full-data accuracy.

## Scientific validity requirements

- Do not call 99%+ validation accuracy an improvement without a held-out test
  result and a matched baseline.
- The current random image-level split may contain highly correlated images.
  If signer/session metadata can be obtained, add group-disjoint splits.
- If a compatible external ASL dataset is available, add external validation
  with explicit class mapping and preprocessing documentation.
- Use macro-F1 in addition to accuracy.
- For multi-seed experiments, report mean ± standard deviation or confidence
  intervals.
- Record hardware, device, package versions, wall-clock duration, seed, and
  exact config with each run.
- Do not add horizontal flips: ASL signs are handedness-sensitive.

## Coding conventions

- Use `merge_config_and_args(parser)` for every training entry point.
- YAML keys use argparse destination names with underscores.
- Path settings are `pathlib.Path`.
- Follow this structure:

  ```text
  run_epoch -> CSV history -> best checkpoint by validation accuracy
  -> held-out test report
  ```

- Checkpoints must store `model_state`, `class_to_idx`, `epoch`, `val_acc`,
  `args`, and all architecture metadata needed by `evaluate.py`.
- `class_to_idx.json` must be saved with the run; do not recompute class order.
- Add Makefile targets for every new training method and smoke test.
- Update `AGENTS.md` only after a run has completed and its artifacts have been
  checked.

## Suggested deliverables

1. Reproducible configs and run directories.
2. Aggregate experiment CSV files.
3. Learning-curve and robustness plots.
4. A results table with fair baselines and parameter counts.
5. A concise report section answering:
   - Does QCA help in low-data settings?
   - Does QCA improve robustness?
   - Is the effect better than parameter-matched classical attention?
   - What is the compute cost of the quantum circuit?
