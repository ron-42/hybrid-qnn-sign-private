# Literature Inventory

| Key | Work | Venue / Year | Identifier / Official Source | Role | Status |
|---|---|---|---|---|---|
| cerezo_2021_vqa | Variational quantum algorithms | Nature Reviews Physics, 2021 | doi:10.1038/s42254-021-00348-9 | VQA background and challenges | verified-citation |
| raubitzek_2023_applicability | On the Applicability of Quantum Machine Learning | Entropy, 2023 | doi:10.3390/e25070992 | Fair quantum--classical benchmarking | verified-citation |
| mari_2020_transfer | Transfer learning in hybrid classical-quantum neural networks | Quantum, 2020 | doi:10.22331/q-2020-10-09-340 | Closest hybrid image-classification paradigm | verified-citation |
| budiutama_2024_channel | Channel attention for quantum convolutional neural networks | Physical Review A, 2024 | doi:10.1103/PhysRevA.110.012447 | Closest quantum channel-attention work | verified-citation |
| perez_2020_reupload | Data re-uploading for a universal quantum classifier | Quantum, 2020 | doi:10.22331/q-2020-02-06-226 | QCA-v2 motivation | verified-citation |
| wadhawan_2020_static | Deep learning-based sign language recognition system for static signs | Neural Computing and Applications, 2020 | doi:10.1007/s00521-019-04691-y | Recent static-sign recognition context | verified-citation |
| erdogan_2024_signer | Signer-independent sign language recognition with feature disentanglement | Turkish Journal of Electrical Engineering and Computer Sciences, 2024 | doi:10.55730/1300-0632.4078 | Signer-independent evaluation motivation | verified-citation |
| hu_2018_se | Squeeze-and-Excitation Networks | CVPR, 2018 | doi:10.1109/CVPR.2018.00745 | Classical attention baseline | verified-citation |
| huang_2017_densenet | Densely Connected Convolutional Networks | CVPR, 2017 | doi:10.1109/CVPR.2017.243 | CNN backbone | verified-citation |
| deng_2009_imagenet | ImageNet: A Large-Scale Hierarchical Image Database | CVPR, 2009 | doi:10.1109/CVPR.2009.5206848 | Pretraining data | verified-citation |
| barczak_2011_mu | A New 2D Static Hand Gesture Colour Image Dataset for ASL Gestures | Research Letters in the Information and Mathematical Sciences, 2011 | hdl:10179/4514 | External dataset | official metadata read; no DOI |
| grassknoted_asl | ASL Alphabet | Kaggle dataset | https://www.kaggle.com/datasets/grassknoted/asl-alphabet | Source dataset | dataset page; no scholarly identifier |

## Close-Work Notes

### Budiutama et al. (2024)

This work introduces channel attention inside quantum convolutional neural
networks for quantum phase classification. Its task and data representation
differ from this paper's use of a quantum bottleneck to gate channels from a
classical image backbone. It supports motivation for quantum channel
attention, not a direct accuracy comparison.

### Mari et al. (2020)

This work studies hybrid transfer learning in which a pretrained classical
network extracts image features for a terminal variational quantum circuit.
It establishes the relevance of pretrained CNN--quantum pipelines. The
present paper differs by evaluating channel gating and by emphasizing matched
classical controls and signer-level analysis.

### Pérez-Salinas et al. (2020)

This work establishes data re-uploading as a way to construct expressive
quantum classifiers. It motivates the QCA-v2 ablation but does not imply that
re-uploading must improve this ASL attention task.

### Raubitzek and Mallinger (2023)

This work compares simulated quantum and classical learning methods under
randomized hyperparameter search. It supports transparent baseline and tuning
choices, not a claim about the present ASL architecture.

### Wadhawan and Kumar (2020); Erdoğan and Baytaş (2024)

The former establishes recent deep-learning practice for isolated static
signs. The latter shows why signer-specific representations can hinder
cross-signer generalization. Neither paper evaluates the present datasets and
architecture, so both are used only for scoped task motivation.
