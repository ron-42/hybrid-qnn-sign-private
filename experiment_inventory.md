# Experiment Inventory

## Kaggle ASL Alphabet

- **Task:** 29-class static image classification.
- **Data:** 87,000 images; fixed stratified 80/10/10 split, split seed 42.
- **Controls:** no attention, SE, parameter-matched MLP, QCA-v1.
- **Low-data setting:** frozen ImageNet DenseNet121; 1%, 5%, and 10% of the
  training partition; seeds 42, 43, and 44; unchanged validation/test sets.
- **Metrics:** held-out test accuracy and macro-F1; mean and sample SD.
- **Main result:** SE leads every low-data fraction. At 10%, SE, MLP, QCA, and
  no attention reach 91.12%, 90.93%, 90.36%, and 90.19% mean accuracy.
- **Full frozen setting:** SE reaches 97.10%; QCA 95.98%; no attention 95.89%.
- **End-to-end setting:** plain DenseNet and DenseNet-QCA both reach 100% test
  accuracy, establishing split saturation rather than an attention benefit.
- **QCA-v2 pilot:** 61.38% at 1%/seed 42, versus 61.83% for matched QCA-v1.
- **Supported claim:** QCA is smaller than SE but does not outperform fair
  classical controls in this controlled study.
- **Caveat:** image-level splitting and likely capture correlation limit
  generalisation claims.

## MU HandImages ASL

- **Task:** 26-class A--Z static image classification.
- **Data:** 1,815 images from five signers; counts 650, 645, 130, 130, 260.
- **Protocol:** five signer-held-out folds; stratified 15% validation split
  within the four development signers; seed 42.
- **Training:** all DenseNet layers unfrozen; 15 epochs; batch size 32;
  backbone LR 1e-5; head LR 1e-3.
- **Controls:** no attention, SE, parameter-matched MLP, QCA-v1.
- **Primary metric:** equal-signer mean accuracy and sample SD.
- **Secondary metric:** pooled accuracy, which weights larger signers more.
- **Main result:** equal-signer means are 94.78% no attention, 94.55% MLP,
  94.50% QCA, and 93.72% SE.
- **Pooled result:** QCA is highest at 94.99%, only 0.11 points above MLP.
- **Paired tests:** QCA accuracy versus no attention, SE, and MLP gives
  two-sided paired t-test p-values 0.543, 0.116, and 0.943.
- **Supported claim:** the four methods are statistically inconclusive across
  signers; sample weighting reverses the apparent leader.
- **Caveats:** one training seed, five signers, severe signer imbalance,
  ideal simulation, and unofficial public mirror of a published dataset.
