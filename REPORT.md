# Quantum Channel Attention for ASL Alphabet Classification
### Final report with unfrozen signer-held-out validation

---

## 1. Project Overview

This project evaluates variational quantum circuits as channel-attention
mechanisms inside pretrained convolutional image classifiers for American Sign
Language (ASL) recognition. The central question is not whether a hybrid model
can fit the dataset, but whether a quantum channel-attention (QCA) block offers
better parameter efficiency or low-data generalisation than fair classical
alternatives.

The study uses the Kaggle ASL Alphabet dataset: 87,000 RGB images across 29
classes (A–Z, `del`, `nothing`, and `space`). A fixed stratified split seed of
42 produces 69,600 training, 8,700 validation, and 8,700 test images. Low-data
experiments subsample only the training split and leave validation and test
unchanged.

Raw dataset images and the local sample grid are intentionally excluded from
the public repository. Obtain the source data from Kaggle before running the
dataset exploration command.

The principal result is negative: under matched frozen conditions, QCA does
not outperform Squeeze-and-Excitation (SE), and a parameter-matched classical
MLP outperforms QCA at 10% training data. In a separate unfrozen
signer-held-out study, QCA's small pooled lead is not significant and
disappears under equal-signer averaging. The work demonstrates a functioning
hybrid implementation, but it does not demonstrate a quantum advantage.

---

## 2. Architecture

### 2.1 Phase 0 — DenseNet121 Baseline

The baseline model is a standard pretrained DenseNet121 fine-tuned end-to-end on the ASL dataset. It serves as the accuracy ceiling reference.

```
Input Image (224×224×3)
    ↓
DenseNet121 Feature Extractor     [pretrained ImageNet weights, all params trainable]
    ↓
Global Average Pooling            → (B, 1024)
    ↓
Linear(1024 → 29)                 [classification head]
    ↓
Output Logits (29 classes)
```

**Trainable parameters:** 6,983,581

---

### 2.2 Phase 2 — DenseNet121 + Quantum Channel Attention

The hybrid model replaces the direct pooled-features-to-classifier path with a **Quantum Channel Attention (QCA) block** inserted between the pooled feature vector and the final classifier. This is inspired by the Squeeze-and-Excitation (SE) network architecture, but the gating function is implemented as a variational quantum circuit instead of classical fully-connected layers.

```
Input Image (224×224×3)
    ↓
DenseNet121 Feature Extractor     [pretrained ImageNet weights]
    ↓
Global Average Pooling            → (B, 1024)
    ↓
┌─────────────────────────────────────────────────────────────┐
│               Quantum Channel Attention Block                │
│                                                             │
│  Linear(1024 → 8)          [classical down-projection]      │
│  tanh(·) × π/2             [angle encoding rescaling]       │
│  AngleEmbedding (8 qubits) [classical → quantum state]      │
│  StronglyEntanglingLayers  [2 variational layers, 8 qubits] │
│  ⟨Z⟩ measurement × 8      [quantum → classical, ∈ [-1,1]]  │
│  Linear(8 → 1024)          [classical up-projection]        │
│  Sigmoid                   [attention weights ∈ (0,1)]      │
│  x × attention             [feature reweighting]            │
└─────────────────────────────────────────────────────────────┘
    ↓
Linear(1024 → 29)                 [classification head]
    ↓
Output Logits (29 classes)
```

**Quantum attention parameters:** 17,464  
**Total trainable parameters (frozen backbone):** 47,189  
**Total trainable parameters (unfrozen backbone):** 7,001,045

The quantum circuit uses PennyLane with the `default.qubit` simulator, `AngleEmbedding` for data encoding, and `StronglyEntanglingLayers` as the variational ansatz. Gradients are computed via backpropagation through the quantum circuit (`diff_method="backprop"`).

### 2.3 Matched classical controls

All controlled comparisons freeze the same pretrained DenseNet121 backbone.
The trainable alternatives after global pooling are:

- **No attention:** classifier only; 0 attention and 29,725 trainable parameters.
- **SE:** two-layer squeeze-and-excitation gate; 131,072 attention and 160,797
  trainable parameters.
- **Matched MLP:** an 8-dimensional nonlinear bottleneck with 17,480 attention
  and 47,205 trainable parameters, only 16 more than QCA.
- **QCA-v1:** 17,464 attention and 47,189 trainable parameters.

The matched MLP is the most important control because it isolates the quantum
circuit from the effects of adding a similarly sized nonlinear attention block.

### 2.4 QCA-v2 data re-uploading

QCA-v2 re-embeds the projected inputs before each variational layer while
keeping the same 17,464 parameters. It was evaluated as a targeted 1%,
single-seed pilot. This was an architecture probe, not part of the confirmatory
three-seed comparison.

---

## 3. Experimental Setup

| Setting | Value |
|---|---|
| Software | Python 3.12.11, PyTorch 2.12.0, PennyLane 0.45.0 |
| Hardware | Apple M4 Air; MPS for CNN operations, CPU for quantum simulation |
| Split | Stratified 80/10/10, fixed split seed 42 |
| Low-data seeds | 42, 43, 44; training subset only |
| Optimiser / schedule | AdamW / cosine annealing |
| Controlled runs | 15 epochs, LR 1e-3, batch size 32, frozen backbone |
| External signer folds | 15 epochs, backbone LR 1e-5, head LR 1e-3, batch size 32, fully unfrozen |
| Image size | 224×224 |
| Data augmentation | Random rotation ±10°, colour jitter (no horizontal flip — ASL signs are handedness-sensitive) |
| Primary metrics | Held-out test accuracy and macro-F1 |

Every reported low-data checkpoint was evaluated independently with
`src.evaluate`; the three-seed summaries use sample standard deviation.
Parameter counts come from reconstructed model parameters, not file size.

---

## 4. Results

### 4.1 Baseline — DenseNet121 (Phase 0)

| Epoch | Train Loss | Train Acc | Val Loss | Val Acc |
|---|---|---|---|---|
| 1 | 0.0867 | 98.35% | 0.00303 | 99.92% |
| 2 | 0.0137 | 99.64% | 0.00054 | **99.99%** |

**Test set accuracy: 100.00%** (8,700 images, 300 per class, all 29 classes at 1.0000 F1)

The baseline converged in 2 epochs and achieved perfect test accuracy, confirming the known ceiling for DenseNet121 on this dataset.

---

### 4.2 Quantum Model — Frozen Backbone (7 Epochs)

Backbone frozen; only the quantum attention block (17,464 params) and classifier (29,725 params) trained.

| Epoch | Train Loss | Train Acc | Val Loss | Val Acc |
|---|---|---|---|---|
| 1 | 0.9684 | 77.36% | 0.3990 | 89.51% |
| 2 | 0.3846 | 89.07% | 0.2856 | 92.22% |
| 3 | 0.3024 | 91.06% | 0.2168 | 93.89% |
| 4 | 0.2657 | 91.91% | 0.1902 | 94.68% |
| 5 | 0.2396 | 92.79% | 0.1870 | 94.53% |
| 6 | 0.2250 | 93.18% | 0.1679 | 95.21% |
| 7 | 0.2146 | 93.53% | 0.1641 | **95.30%** |

**Test set accuracy: 95.30%** — model still converging at epoch 7.

---

### 4.3 Quantum Model — Frozen Backbone (15 Epochs)

Same configuration extended to 15 epochs.

| Epoch | Train Loss | Train Acc | Val Loss | Val Acc |
|---|---|---|---|---|
| 1 | 0.9684 | 77.36% | 0.3990 | 89.51% |
| 5 | 0.2433 | 92.39% | 0.1828 | 94.30% |
| 9 | 0.1993 | 93.73% | 0.1343 | 95.94% |
| 11 | 0.1856 | 94.04% | 0.1338 | 96.06% |
| 14 | 0.1801 | 94.28% | 0.1286 | **96.10%** (best) |
| 15 | 0.1740 | 94.41% | 0.1388 | 95.72% |

**Test set accuracy: 95.98%**

The model plateaued around 96% — the cosine LR schedule decayed to zero at epoch 15, and the frozen backbone became the limiting factor.

---

### 4.4 Quantum Model — Unfrozen Backbone (Full Fine-Tuning)

Backbone unfrozen; all 7,001,045 parameters trained jointly. LR reduced to 3e-4 (safe for fine-tuning pretrained weights).

| Epoch | Train Loss | Train Acc | Val Loss | Val Acc |
|---|---|---|---|---|
| 1 | 0.1148 | 97.98% | 0.00698 | 99.89% |
| 2 | 0.0140 | 99.64% | 0.00019 | **100.00%** |
| 3 | 0.0083 | 99.78% | 0.00131 | 99.94% |
| 4 | 0.0085 | 99.77% | 0.00031 | 99.99% |

**Best validation accuracy: 100.00% at epoch 2. Independently evaluated test
accuracy: 100.00%, macro-F1: 1.0000.** Training stopped after epoch 4 because
the random image-level split was saturated.

---

### 4.5 Full-data and frozen-control comparison

| Model | Attention Params | Trainable Params | Best Val Acc | Test Acc | Macro-F1 |
|---|---:|---:|---:|---:|---:|
| DenseNet121, full fine-tune | 0 | 6,983,581 | 99.99% | 100.00% | 1.0000 |
| No attention, frozen | 0 | 29,725 | 96.17% | 95.89% | 0.9588 |
| QCA-v1, frozen | 17,464 | 47,189 | 96.10% | 95.98% | 0.9599 |
| SE, frozen | 131,072 | 160,797 | 97.72% | 97.10% | 0.9710 |
| QCA-v1, full fine-tune | 17,464 | 7,001,045 | 100.00% | 100.00% | 1.0000 |
| ResNet50 + QCA, full fine-tune | 34,872 | 23,602,325 | 99.954% | 100.00% | 1.0000 |

The matched frozen comparison is the informative one. SE exceeds QCA by
1.12 percentage points. QCA exceeds no attention by only 0.09 points in this
single-seed full-data run. The unfrozen results only demonstrate saturation;
they cannot identify an attention-module contribution.

### 4.6 Low-data sample efficiency

| Training Fraction | Method | Test Accuracy (mean ± SD) | Macro-F1 (mean ± SD) |
|---:|---|---:|---:|
| 1% | No attention | 64.69% ± 0.63% | 0.6342 ± 0.0092 |
| 1% | SE | **66.17% ± 0.42%** | **0.6525 ± 0.0011** |
| 1% | QCA-v1 | 62.16% ± 1.16% | 0.6049 ± 0.0146 |
| 1% | Matched MLP | 60.80% ± 1.31% | 0.5906 ± 0.0179 |
| 5% | No attention | 86.43% ± 0.55% | 0.8638 ± 0.0056 |
| 5% | SE | **87.22% ± 0.88%** | **0.8718 ± 0.0090** |
| 5% | QCA-v1 | 86.13% ± 0.93% | 0.8606 ± 0.0094 |
| 5% | Matched MLP | 86.39% ± 0.47% | 0.8634 ± 0.0050 |
| 10% | No attention | 90.19% ± 0.60% | 0.9017 ± 0.0062 |
| 10% | SE | **91.12% ± 0.45%** | **0.9113 ± 0.0046** |
| 10% | QCA-v1 | 90.36% ± 0.35% | 0.9035 ± 0.0038 |
| 10% | Matched MLP | 90.93% ± 0.24% | 0.9094 ± 0.0023 |

![Low-data learning curve](runs/low_data_learning_curve.png)

SE ranks first at all three fractions. QCA trails no attention by 2.53 points
at 1% and 0.30 points at 5%; at 10% it leads no attention by only 0.17 points,
which is smaller than the across-seed variation. The parameter-matched MLP
beats QCA by 0.58 points at 10%.

### 4.7 QCA-v2 data re-uploading pilot

At 1% training data and seed 42, QCA-v2 achieved **61.38% test accuracy** and
**0.6007 macro-F1**, compared with **61.83%** and **0.6030** for matched
QCA-v1. Re-uploading reduced accuracy by 0.45 points while retaining the same
17,464 parameters. One seed is not sufficient for a general claim, but this
pilot provides no rationale for a larger QCA-v2 sweep.

### 4.8 Unfrozen signer-held-out evaluation

Following supervisory guidance, a second study fine-tuned every DenseNet layer
rather than freezing the backbone. It used the A–Z subset of MU HandImages:
1,815 images from five signers. For each fold, one signer was reserved for
testing and 15% of the remaining-signers' images formed a stratified validation
set. All models trained for 15 epochs with backbone LR `1e-5`, head LR `1e-3`,
batch size 32, and seed 42.

The public mirror is strongly signer-imbalanced: signers 1–5 contribute 650,
645, 130, 130, and 260 A–Z images. Equal-signer means are therefore the primary
summary; pooled metrics are included but overweight signers 1 and 2.

| Method | Attention Params | Trainable Params | Signer Accuracy (mean ± SD) | Signer Macro-F1 (mean ± SD) | Pooled Accuracy | Pooled Macro-F1 |
|---|---:|---:|---:|---:|---:|---:|
| No attention | 0 | 6,980,506 | **94.78% ± 5.17%** | **0.9461 ± 0.0528** | 94.82% | 0.9477 |
| SE | 131,072 | 7,111,578 | 93.72% ± 5.17% | 0.9304 ± 0.0543 | 94.71% | 0.9463 |
| Matched MLP | 17,480 | 6,997,986 | 94.55% ± 4.02% | 0.9395 ± 0.0445 | 94.88% | 0.9482 |
| QCA-v1 | 17,464 | 6,997,970 | 94.50% ± 4.95% | 0.9426 ± 0.0494 | **94.99%** | **0.9497** |

\newpage

![Accuracy for each held-out signer](runs/mu_loso_signer_accuracy.png)

QCA has the highest pooled accuracy by 0.11 points over the matched MLP, but
not the highest equal-signer mean. Its paired signer-level accuracy differences
are not significant versus no attention (`p=0.543`), SE (`p=0.116`), or the
matched MLP (`p=0.943`; paired two-sided t-tests, five folds). Exact Wilcoxon
signed-rank tests reach the same conclusion (`p=0.75`, `0.25`, and `1.00`).
This study therefore provides no statistically supported quantum advantage.

\newpage

![Pooled confusion matrices for all unfrozen methods](runs/mu_loso_confusion_matrices.png)

---

## 5. Key Findings

1. **No quantum advantage was observed.** QCA never ranks first under the
   matched frozen-backbone conditions, and no paired external comparison is
   statistically significant.
2. **SE is strongest only in the frozen study.** It leads at 1%, 5%, 10%, and
   full training data there, but not in the unfrozen signer-held-out study.
3. **QCA is smaller than SE, but less accurate.** It uses 7.5× fewer attention
   parameters, with a 1.12-point full-data accuracy deficit. This is a
   size–accuracy trade-off, not evidence of quantum superiority.
4. **QCA does not reliably improve over omitting attention.** Its differences
   from no attention range from −2.53 to +0.17 points in the low-data study.
5. **The matched MLP removes parameter count as an explanation.** It exceeds
   QCA at 10%, and the two methods are close at 5%; QCA only leads at 1%,
   while both trail no attention and SE.
6. **Data re-uploading did not improve the pilot.** QCA-v2 was 0.45 points
   worse than QCA-v1 for the matched 1%-seed-42 condition.
7. **Perfect unfrozen scores are not evidence for the attention head.** The
   plain DenseNet121 baseline also achieves 100%, showing that the split is
   saturated under full fine-tuning.
8. **External signer-held-out results are effectively tied.** QCA has the
   highest pooled accuracy (94.99%), while no attention has the highest
   equal-signer mean (94.78%); QCA's advantages and deficits are all
   statistically inconclusive across five signers.

---

## 6. Limitations and Threats to Validity

- **Image-level random split:** the Kaggle dataset does not expose signer IDs
  for a signer-disjoint split. Correlated background, capture conditions, or
  near-duplicate samples may occur across train, validation, and test sets.
- **Repeated use of one held-out split:** all model families are ultimately
  compared on the same 8,700-image test partition. This supports controlled
  comparison but does not establish external generalisation.
- **Simulation only:** the quantum layer runs on an ideal state-vector
  simulator. The study makes no claim about execution time, energy, or
  performance on quantum hardware.
- **Restricted architecture search:** QCA-v1 was fixed at eight qubits and two
  layers. QCA-v2 was a one-seed pilot. Broader tuning after observing test
  results would increase selection bias and is not justified by the current
  evidence.
- **Three low-data seeds:** these quantify training-subset variation, but
  confidence intervals remain broad and the image split itself is fixed.
- **Accuracy is near saturation:** the full-data split is too easy to
  distinguish strong unfrozen models.
- **External signer imbalance:** MU signer sample counts range from 130 to
  650. Pooled metrics are dominated by the two largest signers, while five
  signer-level observations provide low statistical power.
- **One external training seed:** all five external folds use seed 42.
  Signer variation is measured, but stochastic training variation is not.
- **Validation is not signer-held-out:** validation images are stratified from
  the four non-test signers. Test signers remain completely unseen during
  training and checkpoint selection.
- **Dataset provenance:** the original MU hosting page is unavailable. The
  experiment uses a public mirror of the published filename-encoded dataset;
  this mirror does not declare a separate licence.

---

## 7. Conclusion

This study establishes a reproducible hybrid DenseNet–QCA pipeline and a
controlled comparison against no attention, SE, and a parameter-matched MLP.
QCA is parameter-efficient relative to SE, but that efficiency comes with
lower accuracy in the frozen study. Across the tested low-data conditions, SE
is consistently best, and QCA does not show a reliable advantage over either
no attention or the matched classical MLP. QCA-v2 data re-uploading also fails
to improve its matched pilot. In the unfrozen signer-held-out study, all four
methods are close: QCA leads the pooled metric by 0.11 points, but trails the
no-attention and matched-MLP equal-signer means, with no significant paired
difference.

The scientifically supported conclusion is therefore negative: **the
experiments do not demonstrate that quantum channel attention is superior to
classical CNN or ANN alternatives.** Both the original controlled study and
the unfrozen external signer-held-out extension are complete. Additional
architecture or seed sweeps should be motivated prospectively rather than used
to search for a favorable post-hoc result.

---

## 8. Reproducibility Artifacts

- Canonical per-run results: `runs/low_data_results.csv`
- Three-seed summaries: `runs/low_data_summary.csv`
- Learning curve: `runs/low_data_learning_curve.png`
- Aggregation script: `src/summarize_low_data.py`
- Frozen QCA reference: `configs/quantum_frozen.yaml`
- Matched low-data configs: `configs/*_10pct.yaml`
- QCA-v2 pilot config: `configs/quantum_v2_1pct.yaml`
- MU signer-held-out config: `configs/mu_loso.yaml`
- MU per-signer results: `runs/mu_loso_results.csv`
- MU signer-balanced and pooled summary: `runs/mu_loso_summary.csv`
- MU signer accuracy: `runs/mu_loso_signer_accuracy.png`
- MU confusion matrices: `runs/mu_loso_confusion_matrices.png`
- MU training and aggregation: `src/train_mu_loso.py`,
  `src/summarize_mu_loso.py`
- Independently generated reports and confusion matrices are stored in each
  run directory.

---

## 9. Protocol Amendment and Data Provenance

The initial external protocol proposed zero-shot evaluation of the frozen
10%-data checkpoints. Before any MU model result was examined, supervisory
guidance rejected frozen backbones as the main study. The protocol was amended
to full end-to-end fine-tuning with identical differential learning rates for
all four methods. Signer 1 was used first to verify runtime; no model,
hyperparameter, or stopping-rule change was made before running signers 2–5.

The experiment uses the A–Z subset of **MU HandImages ASL** (Barczak et al.).
The original description and filename metadata are available from the
[Massey University repository](https://mro.massey.ac.nz/items/d822add8-ffe4-4eec-9b5c-3c0aaa1c72be).
Because the legacy download is unavailable, images were obtained from the
public mirror at
[`hajarek24/asl-sign-language-recognition`](https://github.com/hajarek24/asl-sign-language-recognition),
revision `1e23d649fab0fbb1d4cac523d0c93b1ab06e2213`. The mirror contains 2,515
images across 36 alphanumeric classes, of which 1,815 A–Z images were used.

