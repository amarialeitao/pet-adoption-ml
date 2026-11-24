# Methodology

The **planned** workflow. It will be refined as the team takes decisions (recorded in [`DECISIONS.md`](DECISIONS.md)). Nothing here is a result.

## Workflow

```mermaid
flowchart LR
    A[Load & audit data] --> B[EDA]
    B --> C[Shared preprocessing]
    C --> D1[Task 1: supervised]
    C --> D2[Task 2: unsupervised]
    D1 --> E[Evaluation & interpretation]
    D2 --> E
    E --> F[Final notebook + HTML + ZIP]
```

1. **Problem understanding** — [`PROJECT_BRIEF.md`](PROJECT_BRIEF.md).
2. **Data loading** — robust parser for the malformed CSV ([`DATA_DICTIONARY.md`](DATA_DICTIONARY.md) §4). The raw file is never modified.
3. **Data-quality audit** — missing values, out-of-domain codes, shifted columns, duplicates, outliers. Every fix is documented with its reason and the number of rows affected.
4. **EDA** — target distribution (both `AdoptionSpeed` and `ADOPTION`), univariate distributions, feature-vs-target relationships, cats vs. dogs, correlations. Every plot comes with a written interpretation.
5. **Preprocessing** — imputation or removal, encoding (one-hot for nominal codes, ordinal for ordered ones), scaling for distance-based and linear models, binning for high-cardinality or skewed features (`Age`, `Fee`, `Breed1`, `State`).
6. **Feature construction** (candidates, to be justified) — listings per rescuer, description length / word count, `has_name`, `is_mixed_breed`, number of colours, `is_free`, photo-count bins.
7. **Evaluation protocol** (below).
8. **Baselines** — majority-class (`DummyClassifier`) and stratified-random baselines for every problem.
9. **Models** — at least 5 classifiers from at least 3 families (see [`COURSE_SCOPE.md`](COURSE_SCOPE.md)).
10. **Hyper-parameter selection** — grid or randomised search *inside* the cross-validation (nested or with a held-out test split) to avoid optimistic estimates.
11. **Comparison and interpretation** — per-class metrics, confusion matrices, feature importance / coefficients, error analysis.
12. **Limitations and conclusions.**

## Evaluation protocol (Task 1)

| Item | Plan |
|---|---|
| Splitting | Stratified k-fold CV (k = 5 or 10) with a fixed `random_state`. Consider **grouped CV by `RescuerID`** to avoid rescuer leakage, and compare. |
| Leakage control | All preprocessing (imputation, scaling, encoding, resampling) inside a scikit-learn `Pipeline`, fitted on training folds only. |
| Binary metrics | Balanced accuracy, precision / recall / F1 per class, macro-F1, ROC-AUC, confusion matrix. |
| Multiclass metrics | Macro-F1, per-class recall, confusion matrix; **Quadratic Weighted Kappa** as an extra metric because the target is ordinal (to be approved, see `RESEARCH.md` §5.2). |
| Imbalance | Class weights and/or resampling, applied only to training folds. |
| Cats vs. dogs | Same protocol on each subset; compare against the joint model **evaluated on the same subset**. |
| Reporting | Mean ± standard deviation across folds. |

## Evaluation protocol (Task 2)

| Item | Plan |
|---|---|
| Data | Adopted pets only (`ADOPTION` = 1). `AdoptionSpeed` is **not** used to build clusters. |
| Features | Chosen and scaled deliberately; distance metric justified (e.g. Euclidean on scaled numeric, Gower-like or one-hot for categorical). |
| Algorithms | k-means (several k), agglomerative clustering (several linkages), with dendrograms. |
| Internal metrics | Silhouette, Davies–Bouldin, Calinski–Harabasz, elbow / inertia. |
| External metrics | Adjusted Rand index, NMI, homogeneity / completeness, purity against `AdoptionSpeed`. |
| Interpretation | Cluster profiles (centroids, distributions) and adoption-speed composition of each cluster. |
| Own task | Defined by the team in M4 and recorded in `DECISIONS.md`. |

## Reproducibility

- Fixed random seeds, pinned minimum library versions in `requirements.txt`.
- The notebook runs top to bottom from `data/raw/` with no manual steps.
- Helper functions live in `src/` and are imported by the notebook; the notebook stays the single source of results.
