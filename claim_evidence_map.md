# Claim--Evidence Map

| Claim | Strength | Evidence | Manuscript Use |
|---|---|---|---|
| QCA is the proposed compact channel-gating architecture for static ASL | Scoped design claim | `src/models/quantum_attention.py`; `src/models/densenet_quantum_attention.py` | Title, Abstract, Introduction, Method, Conclusion |
| QCA has 17,464 attention parameters versus SE's 131,072 | Strong | `runs/low_data_summary.csv`; model parameter counts | Abstract, Method, Results |
| SE leads QCA at 1%, 5%, and 10% training data | Strong | `runs/low_data_summary.csv` | Abstract, Results |
| The matched MLP exceeds QCA at 10% by 0.58 points | Strong | `runs/low_data_summary.csv` | Results, Discussion |
| QCA-v2 does not improve the matched seed-42 pilot | Careful | Run reports in `runs/low_data_1pct_qca_v2_seed42/` and QCA-v1 counterpart | Ablation |
| End-to-end Kaggle results are saturated and cannot isolate attention | Strong | Plain DenseNet and QCA both reach 100% test accuracy | Experiments, Limitations |
| No attention has the highest equal-signer MU mean | Strong | `runs/mu_loso_summary.csv` | Abstract, Results |
| QCA has the highest pooled MU accuracy by 0.11 points | Strong but easily misread | `runs/mu_loso_summary.csv` | Results with immediate qualification |
| QCA's paired signer differences are not significant | Strong for tested folds | `runs/mu_loso_results.csv`; paired tests recorded in `REPORT.md` | Abstract, Results |
| Pooled weighting changes the apparent external leader | Strong | Unequal signer counts and pooled/equal-signer summaries | Discussion |
| QCA is hardware-efficient or faster | Forbidden | No hardware execution or valid timing evidence | Exclude |
| QCA is superior to classical attention | Forbidden | Contradicted or unsupported across controlled comparisons | Exclude |
| QCA is the best-performing approach | Forbidden | SE leads frozen low-data accuracy and no attention leads equal-signer MU accuracy | Exclude |
| Findings generalize to dynamic ASL | Forbidden | Static isolated images only | Exclude |

## Evidence Boundary

The paper may claim a controlled negative result for the tested architectures,
datasets, and protocols. It may not convert absence of statistical evidence
into proof that all quantum attention mechanisms are ineffective.
