# Project brief

Our summary of the assignment in `notebooks/AA_202627_Project.ipynb`. **If anything here disagrees with the notebook, the notebook wins.**

## Context

| | |
|---|---|
| Course | Aprendizagem Automática (Machine Learning), 2026/27 |
| Institution | Faculdade de Ciências, Universidade de Lisboa |
| Team size | 3 students (smaller teams allowed only exceptionally) |
| Planned effort | 4 weeks |
| Deadline | **Sunday, 20 December 2026**, end of day, uploaded to Moodle |
| Group registration | Moodle group selection page (link in the notebook) |

## Deliverable

A single `.zip` named **`AA202627nn.zip`** (`nn` = group number), uploaded by one member, containing:

1. The completed Jupyter notebook (template: `AA_202627_Project.ipynb`; sections can be added or changed).
2. An **HTML export of the notebook with all outputs**.
3. Every other file needed to evaluate the project (e.g. Orange workflow files, if Orange is used).

## Grading rules stated in the notebook

- A Jupyter notebook is **mandatory**; other formats are not graded.
- **Decisions must be justified and results critically discussed.**
- Only relevant code and experiments should appear; failed attempts may be discussed in text.
- Notebooks with **only code and outputs, without discussion, get at most 10/20.**

## Tools

Python 3 + Jupyter, with **scikit-learn**, **Orange3** (programmatic or workflows), or both. If Orange workflows are used, include figures of each workflow and explain every widget option.

## Task 0 — Know your data

- 0.1 Load the data.
- 0.2 Understand the features, their distributions, potential errors, and especially the **class distribution**; plan the preprocessing.
- 0.3 Preprocessing shared by both tasks.

Notes from the professor: data may contain errors/typos, high-cardinality features that benefit from binning, missing values, irrelevant features, features that must be excluded for some analyses, and **class imbalance**.

## Task 1 — Supervised learning

Three classification problems:

1. **Adoption (binary)** using the new `ADOPTION` column.
2. **AdoptionSpeed (multiclass)** with 5 classes {0,1,2,3,4}; optionally regroup into 3 classes such as {0–1, 2–3, 4}.
3. **Specialised cat and dog models** for problems 1 and 2, compared against the joint models.

Requirements:

- **5 classifiers from at least 3 families**: tree, probabilistic, distance-based, linear. One ensemble may also be tried.
- **Cross-validation.**
- Describe each classifier's parameters and their impact.
- Choose and justify the **best classifier**.
- Report several metrics and **confusion matrices**; analyse per-class performance; pick metrics appropriate to the problem.

Sections: 1.1 preprocessing for classification · 1.2 learning and evaluating classifiers · 1.3 discussion and conclusions.

## Task 2 — Unsupervised learning

1. **Cluster adopted pets** and check whether clusters group pets with similar adoption speed; evaluate with **internal and external metrics**.
2. **Define and explore our own unsupervised task.**

Sections: 2.1 preprocessing for clustering · 2.2 learning and evaluating clusterings · 2.3 discussion and conclusions.

## Known ambiguities in the template

| # | Issue | Our working assumption |
|---|---|---|
| A1 | `ADOPTION = 1` is defined as `AdoptionSpeed` ∈ [0,4], which would make every pet "adopted" | **Resolved** in the updated template (26 Nov 2026): `ADOPTION = 1` for {0,1,2,3}, 0 for {4} |
| A2 | The dataset section lists codes 1–4 but not 0 | **Resolved** in the updated template: 0 = adopted on the same day it was listed |
| A3 | The CSV does not load with default settings | Custom loader `src/preprocessing/loader.py`, see [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md) §4 |
