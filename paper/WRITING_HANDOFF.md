# Writing Handoff

## Purpose

This file transfers ownership of the manuscript-writing task to another
agent. Treat repository evidence, canonical result files, and verified
citation records as authoritative. Do not strengthen claims beyond that
evidence.

## Read First

1. `AGENTS.md` for the complete research context and experiment history.
2. `paper_state.json` for the writing contract, blockers, and latest build.
3. `paper_story.md` and `claim_evidence_map.md` for the narrative and claim
   boundaries.
4. `experiment_inventory.md` and `numeric_evidence.json` for result
   provenance.
5. `citation_verification.md`, `citation_requests.json`, and
   `citation_lock.json` before changing citations.
6. `reviewer_analysis.md` for the main publication risks.

## Current Manuscript

- Main source: `paper/main.tex`
- Bibliography: `paper/references.bib`
- Compiled paper: `paper/main.pdf`
- Current title: **Compact Quantum Channel Attention for Static ASL
  Recognition: A Controlled Study with Parameter-Matched Baselines**
- Format: venue-neutral, 10-point, two-column article
- Length: 10 pages
- Author and date fields are intentionally blank.
- Stage: polished draft complete; a specific venue has not been selected.
- The paper-writing artifacts are local and excluded by `.gitignore` from the
  public code-only repository.

The user wants a more unique and catchy title, but has not approved a
replacement. Several earlier suggestions were rejected. Do not change the
title without presenting a new option and receiving approval.

## Scientific Story

The proposed approach is **Quantum Channel Attention (QCA)**: an eight-qubit,
two-layer variational bottleneck that converts pooled DenseNet121 features
into channel gates.

QCA is proposed because it is the task-specific architecture developed and
evaluated here, not because it achieves the highest accuracy. Its defensible
benefit is compactness relative to the tested SE block:

- QCA attention parameters: 17,464
- Parameter-matched classical MLP: 17,480
- SE attention parameters: 131,072
- SE therefore has 7.51 times as many attention parameters as QCA.

The central result is negative/inconclusive: QCA does not reliably outperform
no attention or the matched MLP. Do not claim quantum advantage, superiority,
speedup, hardware efficiency, robustness, or state-of-the-art performance.

## Evidence That Must Remain Accurate

### Kaggle low-data attribution study

- Frozen ImageNet-pretrained backbone; this is an attribution ablation, not
  the primary deployment/generalization experiment.
- Training fractions: 1%, 5%, and 10%.
- Training seeds: 42, 43, and 44.
- Validation and test sets remain fixed at 8,700 images each.
- Mean test accuracy:
  - 1%: SE 66.17%, no attention 64.69%, QCA 62.16%, MLP 60.80%.
  - 5%: SE 87.22%, no attention 86.43%, MLP 86.39%, QCA 86.13%.
  - 10%: SE 91.12%, MLP 90.93%, QCA 90.36%, no attention 90.19%.
- SE leads every tested fraction.
- Separate full-training-data frozen comparison: SE 97.10%, QCA 95.98%,
  no attention 95.89%.
- End-to-end full-data Kaggle runs saturate at approximately 100%; these runs
  cannot attribute performance to QCA.

### MU signer-held-out study

- This is the primary external/generalization protocol.
- All DenseNet layers are trainable. Do not describe this study as frozen.
- 1,815 A--Z images from five signers; one signer is held out per fold.
- Primary metric: equal-signer mean, because signer sample counts are
  imbalanced.
- Equal-signer accuracy:
  - No attention: 94.78% +/- 5.17%.
  - Matched MLP: 94.55% +/- 4.02%.
  - QCA: 94.50% +/- 4.95%.
  - SE: 93.72% +/- 5.17%.
- Pooled accuracy: QCA 94.99%, MLP 94.88%, no attention 94.82%, SE 94.71%.
- QCA's pooled lead is sample-weighted and disappears under equal-signer
  averaging.
- Exploratory paired signer-level accuracy tests are unadjusted:
  - QCA vs no attention: p = 0.543.
  - QCA vs MLP: p = 0.943.
  - QCA vs SE: p = 0.116.
- Failure to reject the null is not evidence of equivalence.
- The external experiment uses one training seed and only five signer pairs.

### QCA-v2 pilot

- A fixed-budget data-re-uploading pilot at 1% data and seed 42.
- QCA-v2: 61.38% test accuracy.
- Matched QCA-v1: 61.83%.
- Both use 17,464 attention parameters.
- The pilot does not justify a larger post-hoc sweep.

## Required Editorial Decisions Already Applied

- QCA is presented as the proposed compact architecture, not the
  accuracy-best approach.
- Figure and table captions are concise single source lines.
- The confusing two-track protocol diagram was removed.
- The former Limitations section is now `Future Scope`.
- `Conclusion` is the final authored section; only the bibliography follows.
- `\FloatBarrier` prevents figures or tables from entering or following the
  Conclusion.
- Supporting analysis and reproducibility details appear before Future Scope.
- Figure 6, the evidence hierarchy, was redrawn with equal-width centered
  boxes, consistent spacing, and straight vertical arrows.

Current figure order:

1. Evaluation risks and controls.
2. Proposed QCA architecture.
3. Four channel transformations, with QCA marked proposed.
4. MU held-out-signer accuracy.
5. Pooled confusion matrix of proposed QCA only.
6. Kaggle low-data accuracy.

The evidence-hierarchy figure and the four-panel confusion
figure were removed. The old reproducibility section was
removed. Every comparison table labels the QCA row as
proposed. The manuscript avoids first-person pronouns.

## Citation Policy

- Every cited scholarly work currently has a fresh verified lock record.
- Seven scholarly references are dated 2020--2024.
- Three older references are retained only as essential primary sources:
  DenseNet, ImageNet, and SE.
- Dataset identities are cited through official footnotes because they do not
  have suitable DOI/arXiv records for the scholarly citation lock.
- Never invent metadata or add a citation from memory.
- If a citation changes, update `citation_requests.json`, regenerate
  `citation_lock.json`, update `citation_verification.md`, and rebuild.

## Language and Originality

The user wants low similarity and writing that does not read as generic
machine-generated prose.

- Write an original, project-specific synthesis grounded in these experiments.
- Do not copy source wording; paraphrase ideas accurately and cite them.
- Avoid repetitive templates, inflated adjectives, generic transitions, and
  unsupported novelty language.
- Preserve the user's scientific voice and direct wording where possible.
- Do not attempt to manipulate or evade AI-writing detectors; such scores are
  unreliable and cannot be guaranteed.
- Recommend Turnitin or iThenticate for an external similarity check before
  submission.
- Follow the selected venue's policy for disclosure of AI-assisted editing.

## Remaining Decisions and Risks

1. Select a conference and adapt the official template while staying within
   the requested maximum of 10 pages.
2. Propose a genuinely distinctive title and obtain user approval before
   changing the current title.
3. Decide with the supervisor whether to repeat MU folds with more training
   seeds.
4. Confirm the MU mirror's provenance and redistribution terms before
   releasing data-derived artifacts.
5. Perform a final visual proofread after applying a venue template; short
   captions may wrap differently under another layout.

Do not start another training sweep, noise experiment, qubit/layer grid, or
new external study without supervisor approval.

## Build and Verification

Run commands from the repository root unless a command explicitly changes
directory.

```bash
# Rebuild numeric provenance after changing manuscript numbers or evidence.
python3 paper/scripts/build_numeric_evidence.py

# Verify citation metadata after any citation change.
SSL_CERT_FILE="$(python3 -c 'import certifi; print(certifi.where())')" \
  python3 .agents/skills/ai-research-writing-skill/scripts/verify_citations.py .

python3 .agents/skills/ai-research-writing-skill/scripts/check_citations.py \
  paper/main.tex paper/references.bib
python3 .agents/skills/ai-research-writing-skill/scripts/check_citation_lock.py .
python3 .agents/skills/ai-research-writing-skill/scripts/check_numeric_evidence.py .

# Compile and attest the real PDF.
python3 .agents/skills/ai-research-writing-skill/scripts/record_build.py . --run
python3 .agents/skills/ai-research-writing-skill/scripts/parse_build_log.py \
  paper/build-attestation.log
python3 .agents/skills/ai-research-writing-skill/scripts/research_quality_gate.py .
```

Latest attested build:

- Status: passed
- Tectonic: 0.16.9
- Pages: 8
- Input SHA-256:
  `229b8caa113fe3070ecbfa42b1175a01467a43be7c62dbe68108860bbbe0a8f7`
- PDF SHA-256:
  `da426c9e447655cd32478356a73489cb395666f194b6c4b64a17f59862d8ac74`
- Errors, undefined citations/references, missing files, and overfull boxes: 0
- Ten underfull-box warnings remain and are non-blocking.

The generic camera-ready checker expects a section literally named
`Limitations`, acknowledgments, and a venue checklist. It will report those
items until a venue is selected. This is expected because the user explicitly
requested `Future Scope`, blank author metadata, and a venue-neutral draft.
