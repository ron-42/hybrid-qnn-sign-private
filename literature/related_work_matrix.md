# Related Work Matrix

| Line of work | Representative papers | What they establish | What they do not establish here | Relation |
|---|---|---|---|---|
| Variational quantum learning | Cerezo et al. | Hybrid optimization and recognized trainability/efficiency challenges | Practical quantum advantage for this image task | Background and claim boundary |
| Quantum--classical benchmarking | Raubitzek and Mallinger | Fair comparisons require explicit baselines, tuning, and reproducible settings | Superiority of QCA or conclusions for ASL | Evaluation motivation |
| Hybrid quantum transfer learning | Mari et al. | Pretrained classical image features can feed a variational quantum component | Benefit of quantum channel gating over matched classical heads | Closest pipeline paradigm |
| Quantum channel attention | Budiutama et al. | Channel attention can be formulated for QCNN quantum-state classification | Superiority for classical RGB features or ASL | Mechanism motivation; different task |
| Data re-uploading | Pérez-Salinas et al. | Repeated encoding can increase classifier expressivity | Guaranteed empirical gain for a fixed attention budget | QCA-v2 ablation motivation |
| Classical channel attention | Hu et al. | SE learns channel-wise feature recalibration | Performance under this paper's frozen and signer-held-out protocols | Strong classical baseline |
| Dense image backbones | Huang et al.; Deng et al. | DenseNet architecture and ImageNet-scale pretraining | Attribution of saturated accuracy to an added attention block | Backbone and ceiling control |
| Static and signer-independent sign recognition | Wadhawan and Kumar; Erdoğan and Baytaş | Deep static-sign recognition and the importance of signer-independent representations | Performance of the present ASL architecture | Task and protocol motivation |
| Static ASL datasets | Kaggle ASL Alphabet; Barczak et al. | Large image-level benchmark and multi-signer external data | Dynamic sign recognition or broad deployment generalisation | Evaluation domains |

## Related Work Paragraph Plan

1. Introduce VQAs and fair quantum--classical benchmarking.
2. Position the proposed architecture beside hybrid quantum transfer learning
   and quantum channel attention while stating task differences.
3. Motivate SE and the parameter-matched MLP as attribution controls.
4. Place static-sign recognition and signer-independent evaluation before
   describing the two ASL datasets.
