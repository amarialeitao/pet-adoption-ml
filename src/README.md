# src/

Small, reusable helpers imported by the notebook. Keep them simple; the notebook remains the place where results are produced and discussed.

| Package | Purpose |
|---|---|
| `preprocessing/` | Robust CSV loader, cleaning of invalid codes, imputation |
| `features/` | Feature construction (e.g. listings per rescuer, description length) |
| `supervised/` | Shared evaluation helpers for Task 1 (CV, metrics, confusion matrices) |
| `unsupervised/` | Clustering and cluster-validation helpers for Task 2 |
