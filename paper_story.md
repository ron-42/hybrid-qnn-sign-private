# Paper Story

## Working Title

Compact Quantum Channel Attention for Static ASL Recognition: A Controlled
Study with Parameter-Matched Baselines

## Thesis

The proposed method is an eight-qubit QCA module used as a compact channel
gate for static ASL recognition. It is evaluated under parameter-matched,
low-data, and signer-held-out protocols. The parameter reduction relative to
SE does not translate into a reliable predictive advantage over classical
controls. SE is a control, not the proposed method.

## Task Boundary

- **Inputs:** static RGB images of isolated ASL hand gestures.
- **Outputs:** A--Z or 29-class ASL labels, depending on the benchmark.
- **Supported settings:** simulated QCA in pretrained DenseNet121, frozen
  low-data controls, and unfrozen signer-held-out fine-tuning.
- **Out of scope:** dynamic sign recognition, sentence translation, quantum
  hardware speed or energy, and claims of practical quantum advantage.

## Gap

Hybrid quantum image classifiers are often compared with large classical
networks or without a parameter-matched nonlinear control. Such comparisons
cannot determine whether a result follows from the quantum circuit, the added
parameters, the pretrained backbone, or an easy data split.

## Technical Challenge

1. Image-level ASL splits saturate under end-to-end fine-tuning.
2. Quantum simulation cost constrains qubit and layer sweeps.
3. Attention modules differ greatly in parameter count.
4. External signers are imbalanced, so pooled metrics can reverse rankings.

## Method Insight

Use an eight-dimensional entangling circuit to mix compressed channel
descriptors before expanding its measurements into DenseNet channel gates.
Isolate this proposed transformation with a nearly identical classical MLP, a
stronger SE block, and a no-attention head under identical data and
optimization.

## System / Method Stages

1. Extract 1,024-dimensional pooled DenseNet121 features.
2. Project to eight bounded rotation angles.
3. Apply an eight-qubit, two-layer variational circuit and Pauli-Z measurement.
4. Project measurements to sigmoid channel gates.
5. Reweight features and classify.

## Contributions

- A proposed DenseNet-QCA channel gate with explicit simulator/device bridging
  and 17,464 attention parameters.
- A four-way protocol including no attention, SE, and a 17,480-parameter MLP
  that isolates parameter count from quantum computation.
- A three-seed low-data evaluation and a five-fold, fully unfrozen
  signer-held-out evaluation.
- A negative-result analysis showing that pooled weighting, saturated splits,
  and unmatched controls can create misleading conclusions.

## Evidence

- SE leads all 1%, 5%, and 10% frozen low-data conditions.
- At 10%, MLP exceeds QCA by 0.58 percentage points.
- In MU signer-held-out evaluation, no attention has the highest equal-signer
  mean (94.78%); QCA has the highest pooled result (94.99%).
- QCA's paired signer-level differences are not significant.

## Related Work Positioning

The paper connects variational quantum classifiers and quantum transfer
learning with classical channel attention. QCA is the proposed compact
architecture; the controlled evidence, rather than representational
superiority, is the principal validated contribution.

## Claims to Make

- QCA uses 7.5 times fewer attention parameters than the tested SE block.
- This parameter reduction is accompanied by lower frozen-study accuracy.
- QCA does not reliably beat no attention or a parameter-matched MLP.
- Equal-signer and pooled external summaries produce different leaders.
- QCA is the proposed approach because it is the only new task-specific
  architecture evaluated, not because it achieves the highest accuracy.

## Claims to Be Careful About

- The external study suggests parity, but has only five signers and one seed.
- Frozen backbones isolate heads but are not the primary deployment setting.
- A simulator validates optimization, not hardware efficiency.

## Claims to Avoid

- Quantum advantage, superiority, speedup, or state of the art.
- Generalisation to dynamic ASL, unseen acquisition domains, or hardware.
- Treating 100% in-distribution accuracy as evidence for QCA.
- Treating QCA's 0.11-point pooled lead as a robust improvement.

## Reviewer Risks

- Novelty may be judged primarily empirical or negative.
- The original Kaggle data lack signer metadata.
- The MU mirror has provenance and licence limitations.
- The external study lacks multiple initialization seeds.
- Five signer pairs provide low statistical power.
