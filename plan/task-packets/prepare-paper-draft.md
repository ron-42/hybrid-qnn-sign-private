# Task Packet: Prepare Research Paper Draft

## Goal

Produce a complete, venue-neutral LaTeX paper draft from the repository and
completed experiments, with claims constrained by reproducible evidence.

## Inputs

- `AGENTS.md` and `REPORT.md`
- Model and training code under `src/`
- Configurations under `configs/`
- Canonical results in `runs/low_data_*.csv` and `runs/mu_loso_*.csv`
- Deterministic figures generated from those results

## Deliverables

- Paper contract, inventories, story, and claim-evidence map
- Verified core bibliography and citation records
- Complete `paper/main.tex` and compiled `paper/main.pdf`
- Numeric-evidence registry, figure plan, reviewer analysis, and build record

## Acceptance Criteria

- No claim of quantum advantage or superiority
- Every headline number traces to a canonical CSV or checkpoint-derived report
- Frozen and unfrozen studies are distinguished explicitly
- Signer-balanced MU results are primary; pooled results are qualified
- LaTeX builds without missing citations, references, or assets
- Remaining scientific and venue blockers are visible
