# Citation Verification

Scholarly identifiers were resolved on 2026-09-23. Machine-verifiable
metadata, request hashes, and claim-support hashes are stored in
`citation_lock.json`.

| Key | Identifier | Primary source | Claim relation | Status |
|---|---|---|---|---|
| cerezo_2021_vqa | doi:10.1038/s42254-021-00348-9 | Crossref | direct | verified |
| raubitzek_2023_applicability | doi:10.3390/e25070992 | Crossref | direct | verified |
| mari_2020_transfer | doi:10.22331/q-2020-10-09-340 | Crossref | direct | verified |
| budiutama_2024_channel | doi:10.1103/PhysRevA.110.012447 | Crossref | direct | verified |
| perez_2020_reupload | doi:10.22331/q-2020-02-06-226 | Crossref | direct | verified |
| wadhawan_2020_static | doi:10.1007/s00521-019-04691-y | Crossref | background | verified |
| erdogan_2024_signer | doi:10.55730/1300-0632.4078 | Crossref | direct | verified |
| hu_2018_se | doi:10.1109/CVPR.2018.00745 | Crossref | direct | verified |
| huang_2017_densenet | doi:10.1109/CVPR.2017.243 | Crossref | direct | verified |
| deng_2009_imagenet | doi:10.1109/CVPR.2009.5206848 | Crossref | background | verified |
| mcclean_2018_barren | doi:10.1038/s41467-018-07090-4 | Crossref | direct | verified |
| schuld_2019_feature | doi:10.1103/PhysRevLett.122.040504 | Crossref | direct | verified |
| benedetti_2019_pqc | doi:10.1088/2058-9565/ab4eb5 | Crossref | direct | verified |
| rastgoo_2021_survey | doi:10.1016/j.eswa.2020.113794 | Crossref | background | verified |
| preskill_2018_nisq | doi:10.22331/q-2018-08-06-79 | Crossref | direct | verified |
| mitarai_2018_qcl | doi:10.1103/PhysRevA.98.032309 | Crossref | direct | verified |
| cong_2019_qcnn | doi:10.1038/s41567-019-0648-8 | Crossref | contrast | verified |
| henderson_2020_quanvolutional | doi:10.1007/s42484-020-00012-y | Crossref | contrast | verified |
| havlicek_2019_feature | doi:10.1038/s41586-019-0980-2 | Crossref | background | verified |
| camgoz_2018_slt | doi:10.1109/CVPR.2018.00812 | Crossref | contrast | verified |
| bowles_2024_benchmark | arxiv:2403.07059 | arXiv | direct | verified |
| bergholm_2018_pennylane | doi:10.48550/arXiv.1811.04968 | DataCite | software | verified |
| loshchilov_2019_adamw | doi:10.48550/arXiv.1711.05101 | DataCite | direct | verified |
| loshchilov_2017_sgdr | doi:10.48550/arXiv.1608.03983 | DataCite | direct | verified |

## Boundaries

- The manuscript uses impersonal wording. QCA is named as the proposed
  method in every comparison table. SE is a higher-capacity control.
- Budiutama et al., Cong et al., and Henderson et al. support nearby quantum
  vision designs. Their tasks are not this classical-image channel gate.
- Mari et al. support a pretrained CNN plus a variational circuit. They do
  not support a claim that the circuit outperforms a matched MLP.
- Pérez-Salinas et al. motivate re-uploading. The 1% pilot was worse than
  matched QCA-v1, so the citation does not predict an ASL gain.
- Bowles et al. and Raubitzek and Mallinger support careful baselines. They
  do not predict the ASL numbers.
- McClean et al. caution against growing random circuits. The manuscript
  does not claim that the eight-qubit gate is in a barren plateau.
- Preskill supports a noise caveat for future hardware claims.
- Loshchilov and Hutter (SGDR) introduce the cosine-restart schedule. The
  runs use cosine decay over a fixed epoch budget, without extra restarts.
- AdamW is cited for decoupled weight decay. The preprint year on DataCite
  is 2017; the bibliographic year is the 2019 ICLR version.
- Wadhawan and Kumar, Rastgoo et al., and Camgoz et al. locate the static
  alphabet task. They do not evaluate this model.
- Erdoğan and Baytaş motivate signer-independent testing on other sign
  data. They do not establish these ASL accuracies.
- Dataset identity for Kaggle ASL Alphabet and MU HandImages stays in
  footnotes. Those records do not have DOI entries in the scholarly lock.
