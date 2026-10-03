# Reviewer Analysis

## Executive Summary

- **Likely stance:** technically honest and reproducible negative-result study,
  but stronger as a thesis chapter, workshop paper, or empirical note than as
  a top-tier method paper.
- **Strongest part:** four-way attribution controls plus the distinction
  between signer-balanced and pooled external metrics.
- **Highest rejection risk:** limited novelty and statistical power--the
  external result has five signers and one training seed.
- **Recommended decision:** discuss venue and contribution type with the
  supervisor before starting more experiments. If publication is the goal,
  add external seeds only under a preregistered analysis.

## Spec-Compliance Review

- Complete paper sections, tables, figures, future-scope boundaries, and
  bibliography are present.
- Headline values trace to canonical CSVs through `numeric_evidence.json`.
- Scholarly citations have verified DOI/arXiv metadata and sentence-level
  support records.
- Frozen results are labeled as attribution ablations; fully unfrozen MU LOSO
  is the primary external protocol.
- Unsupported quantum advantage, speed, hardware, and state-of-the-art claims
  are excluded.

## Five-Dimension Assessment

| Dimension | Assessment | Reason |
|---|---|---|
| Contribution | Pass with caveat | QCA is clearly identified as the proposed compact architecture, but evidence does not support accuracy superiority. |
| Writing clarity | Pass | Thesis, controls, protocols, and negative conclusion are explicit. |
| Experimental strength | Needs evidence | Low-data has three seeds, but MU has one seed and only five signer pairs. |
| Evaluation completeness | Pass with caveats | Controls are fair and metrics expose weighting; hardware/noise is out of scope. |
| Method soundness | Pass | Architecture, tensor/device bridge, optimization, and checkpoint selection are documented. |
| Responsibility | Needs revision | MU mirror license/provenance and human-image consent terms require confirmation before release. |

## Major Risks

| Risk | Why Reviewers May Care | Severity | Recommended Action |
|---|---|---|---|
| Limited novelty | QCA ingredients are known and the contribution is empirical | High | Target an evaluation/negative-results venue or sharpen the protocol contribution |
| Five signer pairs | Paired tests are low-power and sensitive to one signer | High | Add preregistered seeds if the supervisor approves; otherwise keep claims narrow |
| One shared training schedule | Equal settings are controlled but may not be optimal for each method | Medium | State this limitation and avoid claims about each model's attainable optimum |
| Frozen Kaggle study | Frozen heads may not reflect deployment | Medium | Keep it secondary; foreground unfrozen MU results |
| Kaggle image-level saturation | Near-duplicate capture conditions may inflate scores | Medium | Treat full-data scores only as saturation checks |
| Simulated circuits | No hardware cost or robustness conclusion is possible | Medium | Keep speed/energy/quantum-advantage claims excluded |
| Dataset rights | Public mirror may not establish redistribution permission | High for release | Confirm original terms before packaging data or derived examples |

## Simulated Review

**Summary:** The paper evaluates a simulated eight-qubit channel-attention
module in DenseNet121 for static ASL classification. It compares QCA with no
attention, SE, and a parameter-matched MLP in a three-seed frozen low-data
study and a fully unfrozen five-signer LOSO study. Results do not support a
quantum advantage.

**Strengths:** Fair controls; transparent negative result; useful
signer-balanced versus pooled analysis; strong artifact traceability.

**Weaknesses:** The architecture itself is incremental; external statistical
power is weak; no hardware/noise evidence; the broad relevance beyond this
task is uncertain.

**Key reason for accept/reject:** Acceptance depends on whether the venue
values rigorous negative results and evaluation methodology. A method-focused
venue may reject for limited novelty despite sound execution.

**Questions for authors:** How sensitive are MU results to training seed?
Would equal tuning budgets change the ranking? What are the dataset
redistribution and consent terms?

**Actionable suggestions:** Add external seeds only if preregistered, report
compute cost descriptively without implying speedup, confirm data rights, and
select a venue before compressing to a page limit.

**Confidence:** High on claim/evidence assessment; moderate on venue outcome
because no target venue is specified.

## Claims Intentionally Weakened or Removed

- Removed: quantum advantage, superiority, robustness, speedup, and
  state-of-the-art language.
- Weakened: external ``lead'' to a pooled descriptive result that reverses
  under equal-signer weighting.
- Scoped: conclusions apply only to this architecture, simulator, data, and
  optimization protocol.

## Submission-Blocking Issues

1. The specific target conference and official template are unspecified,
   although the venue-neutral draft is eight pages.
2. External replication uses one seed.
3. MU mirror licensing and redistribution terms are unresolved.

The paper is currently strongest on fair attribution and transparent negative
evidence. Its highest remaining reviewer risk is contribution significance,
not prose or mechanical completeness.
