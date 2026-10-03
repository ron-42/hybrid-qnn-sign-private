# Literature Positioning

## Closest Works

| Work | Similarity | Difference | Reviewer Risk |
|---|---|---|---|
| Mari et al. (2020) | Pretrained CNN plus variational quantum component for images | Terminal quantum classifier rather than channel gate; no identical control set | Overstating architectural novelty |
| Budiutama et al. (2024) | Explicit quantum channel-attention mechanism | Quantum-state/QCNN phase classification rather than classical RGB transfer learning | Treating distinct tasks as directly comparable |
| Pérez-Salinas et al. (2020) | Data re-uploading circuit design | General classifier expressivity rather than fixed-budget attention | Implying theoretical expressivity guarantees empirical improvement |
| Raubitzek and Mallinger (2023) | Controlled quantum--classical comparison | General tabular benchmarks rather than channel attention or ASL | Claiming their findings directly predict ours |
| Erdoğan and Baytaş (2024) | Signer-independent recognition motivation | Other sign languages and a temporal model | Treating signer generalization as dataset-independent |
| Hu et al. (2018) | Channel-wise sigmoid recalibration | Fully classical and substantially larger in the tested configuration | Ignoring the accuracy cost of QCA's smaller parameter count |

## Our Position

- **Task boundary:** evaluation of channel attention for static ASL image
  classification with a pretrained DenseNet121.
- **Proposed approach:** a compact eight-qubit channel gate for pooled
  DenseNet features, presented as a task-specific architecture rather than an
  accuracy-winning method.
- **Main distinction:** a controlled attribution study with SE,
  parameter-matched MLP, and no-attention controls across frozen low-data and
  unfrozen signer-held-out settings.
- **Evidence:** three low-data seeds and five held-out signers show no reliable
  QCA advantage.
- **Claim:** QCA is a compact workable module, but compactness alone does not
  establish superiority.
- **Careful claim:** external methods are effectively tied within five-signer
  uncertainty.
- **Avoid:** novelty or state-of-the-art claims for quantum attention broadly.

## Contribution Boundary

The paper proposes the task-specific QCA integration and contributes a
reproducible controlled evaluation with a negative comparative result. The
block combines known channel gating, variational circuits, and transfer
learning ideas; the manuscript must not present those ingredients as invented
in isolation.
