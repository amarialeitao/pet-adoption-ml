<div align="center">

# 🐾 Learning about Pet Adoption

**Predicting whether — and how fast — shelter pets get adopted, and discovering what adopted pets have in common.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![pandas](https://img.shields.io/badge/pandas-data-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/status-in%20progress-yellow)](#-roadmap)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-fe5196?logo=conventionalcommits&logoColor=white)](https://www.conventionalcommits.org/)

Machine Learning course project · *Aprendizagem Automática 2026/27* · Faculdade de Ciências, Universidade de Lisboa

</div>

---

## 📌 At a glance

| | |
|---|---|
| **Problem** | ~15,000 pet listings from [PetFinder.my](https://www.petfinder.my/), Malaysia's largest animal-welfare platform. Can a listing's attributes tell us whether a pet will be adopted, and how quickly? |
| **Task 1 · Supervised** | Binary classification (*adopted vs. not adopted*), multiclass classification (*adoption speed*), and specialised cat vs. dog models. |
| **Task 2 · Unsupervised** | Clustering adopted pets to find groups with similar adoption speed, plus one open-ended unsupervised question chosen by the team. |
| **Stack** | Python · pandas · NumPy · scikit-learn · Matplotlib · Seaborn · Jupyter |
| **Approach** | Interpretable, course-syllabus models evaluated with cross-validation, with every choice justified and discussed. |
| **Deadline** | 20 December 2026 |

> **Project status:** 🚧 Repository set up and data audit started. **No models have been trained yet**, so no results are reported. This README will be updated with findings as they are produced and verified.

## 🎯 Why this matters

Every day a pet stays in a shelter costs space, money and the chance to help another animal. If rescuers know which listing attributes (photos, age, fee, health information, description, …) relate to faster adoption, they can improve their listings and focus effort on the animals that need it most. This project studies that question with a rigorous, reproducible ML workflow.

## 🧪 Tasks

### Task 0 · Know your data
Exploratory data analysis, data-quality audit (the course dataset intentionally contains **errors, typos and missing values**), and preprocessing shared by both tasks.

### Task 1 · Supervised learning — predicting adoption and adoption speed
1. **Adoption (binary):** create `ADOPTION` = 1 if the pet was adopted (`AdoptionSpeed` ∈ {0,1,2,3}), 0 otherwise (`AdoptionSpeed` = 4).
2. **AdoptionSpeed (multiclass):** predict the original 5 classes {0,1,2,3,4}, and explore coarser groupings such as {0–1, 2–3, 4}.
3. **Cats vs. dogs:** train specialised models per species and compare them with the joint models.

Requirements from the assignment: **5 classifiers from at least 3 families** (tree, probabilistic, distance-based, linear; optionally one ensemble), **cross-validation**, per-class analysis with **confusion matrices**, and a justified choice of the best classifier.

### Task 2 · Unsupervised learning — characterising adopted pets
1. **Cluster adopted pets** and check whether groups share a similar adoption speed, using **internal and external** clustering metrics.
2. **Define and explore our own unsupervised question.**

## 📊 Dataset

A modified subset of the Kaggle competition [PetFinder.my Adoption Prediction](https://www.kaggle.com/c/petfinder-adoption-prediction/), supplied by the course instructor.

- **14,993 listings × 24 columns** (dogs and cats), plus lookup tables for breeds (307), colours (7) and Malaysian states (15).
- **Target `AdoptionSpeed`:** 0 = same day · 1 = 1–7 days · 2 = 8–30 days · 3 = 31–90 days · 4 = not adopted after 100 days.
- Features cover the animal (type, age, breed, gender, colours, size, fur), its care (vaccinated, dewormed, sterilised, health), the listing (fee, quantity, photos, videos, free-text description) and the rescuer.

See [`docs/DATA_DICTIONARY.md`](docs/DATA_DICTIONARY.md) for every column and the data-quality issues found so far.

> ⚠️ **The data files are not included in this repository.** They come from a Kaggle competition whose redistribution terms are unclear, so they are distributed to students through the course page only. See [`data/README.md`](data/README.md) to set them up locally.

## 🧭 Methodological constraints

This is an academic project, so the **toolbox is deliberately limited to the course syllabus**: decision trees, k-NN, Naive Bayes, linear and regularised models, perceptron, SVMs and kernels, multilayer perceptrons, and ensembles (voting, bagging, boosting, stacking), plus k-means-style and hierarchical clustering. Techniques that dominated the original Kaggle leaderboard (gradient-boosting libraries, image CNNs, external sentiment APIs) are studied for insight but **not used** unless the team explicitly approves them. Details in [`docs/COURSE_SCOPE.md`](docs/COURSE_SCOPE.md).

## 🗂️ Repository structure

```text
pet-adoption-ml/
├── README.md                ← you are here
├── CLAUDE.md                ← working rules for AI-assisted collaboration
├── requirements.txt
├── docs/
│   ├── PROJECT_BRIEF.md     ← the assignment, in our own words
│   ├── COURSE_SCOPE.md      ← syllabus, allowed / not allowed techniques
│   ├── METHODOLOGY.md       ← planned workflow and evaluation protocol
│   ├── DATA_DICTIONARY.md   ← columns, codes and known data issues
│   ├── RESEARCH.md          ← what we learned from the Kaggle competition
│   ├── DECISIONS.md         ← decision log
│   └── MEETING_NOTES.md
├── data/
│   ├── README.md            ← how to obtain the (non-public) data
│   ├── raw/                 ← original files, never modified (git-ignored)
│   └── processed/           ← generated datasets (git-ignored)
├── notebooks/
│   └── AA_202627_Project.ipynb   ← the main deliverable
├── src/                     ← helper code imported by the notebook
│   ├── preprocessing/  ├── features/  ├── supervised/  └── unsupervised/
├── reports/
│   ├── figures/
│   └── tables/
└── submission/
    └── README.md            ← how the final ZIP is built
```

## 🚀 Getting started

```bash
git clone https://github.com/amarialeitao/pet-adoption-ml.git
cd pet-adoption-ml

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# place the course data files in data/raw/ (see data/README.md), then:
jupyter notebook notebooks/AA_202627_Project.ipynb
```

## 🛣️ Roadmap

| Milestone | Scope | Status |
|---|---|---|
| **M1** · Project setup & data understanding | Repo, docs, Kaggle research, robust data loading, data audit | 🟡 In progress |
| **M2** · EDA & preprocessing | Distributions, target balance, cleaning, encoding, feature construction | ⚪ Planned |
| **M3** · Supervised learning | Baselines, 5 classifiers, binary / multiclass / cat-vs-dog experiments | ⚪ Planned |
| **M4** · Unsupervised learning | Clustering adopted pets, internal & external validation, own task | ⚪ Planned |
| **M5** · Evaluation & interpretation | Model comparison, error analysis, critical discussion | ⚪ Planned |
| **M6** · Final notebook & submission | Clean notebook, HTML export, `AA202627nn.zip` | ⚪ Planned |

Work is tracked in [GitHub Issues](https://github.com/amarialeitao/pet-adoption-ml/issues) and on the project board.

## 📈 Results

*No results yet.* This section will summarise the best classifiers, their cross-validated metrics, and the most interesting clustering findings once the experiments are run. Nothing will be reported here that is not reproduced in the notebook.

## 👥 Team

| Member | GitHub |
|---|---|
| Maria Leitão | [@amarialeitao](https://github.com/amarialeitao) |
| *To be added* | |
| *To be added* | |

## 📦 Academic submission

The deliverable is a ZIP named `AA202627nn.zip` (where `nn` is the group number on Moodle) containing the completed notebook, its **HTML export with all outputs**, and any files needed to reproduce the results. See [`submission/README.md`](submission/README.md).

## 🤝 Contributing (team)

- One issue per task; branch names like `feat/eda-target-distribution`; open a pull request and ask a teammate to review.
- Commits follow [Conventional Commits](https://www.conventionalcommits.org/), e.g. `feat(eda): plot adoption speed by pet type`.
- Record important methodological choices in [`docs/DECISIONS.md`](docs/DECISIONS.md).

## 📚 References

- P. Flach. *Machine Learning: The Art and Science of Algorithms that Make Sense of Data.* Cambridge University Press, 2012. <http://people.cs.bris.ac.uk/~flach/mlbook/>
- G. James, D. Witten, T. Hastie, R. Tibshirani, J. Taylor. *An Introduction to Statistical Learning with Applications in Python.* Springer, 2023. <https://www.statlearning.com/>
- Kaggle. *PetFinder.my Adoption Prediction* (2019). <https://www.kaggle.com/c/petfinder-adoption-prediction/>
- scikit-learn user guide. <https://scikit-learn.org/stable/user_guide.html>

---

<sub>Academic project for *Aprendizagem Automática* (FCUL, 2026/27). The dataset belongs to PetFinder.my / Kaggle and is not redistributed here. No license has been chosen yet; see <a href="docs/DECISIONS.md">DECISIONS.md</a>.</sub>
