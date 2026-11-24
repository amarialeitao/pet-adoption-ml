# Research — the original PetFinder.my Kaggle competition

> **Read this first.** Everything in this document is **external context** about the original Kaggle competition. Our course dataset is a *selected and modified* version of that data, and the **professor's notebook is the authoritative specification** for our project. Nothing here is a result of our own experiments. Where we have checked a fact against our own data, it is marked **[verified on course data]**; competition facts we could not re-read at the source are marked **[to re-verify]**.

## 1. Competition overview

| Item | Details |
|---|---|
| Name | [PetFinder.my Adoption Prediction](https://www.kaggle.com/c/petfinder-adoption-prediction/) — "How cute is that doggy in the shelter?" |
| Host | [PetFinder.my](https://www.petfinder.my/), Malaysia's leading animal-welfare platform |
| Period | Approx. December 2018 – April 2019 **[to re-verify]** |
| Format | Kernels-only competition (code had to run inside Kaggle notebooks) **[to re-verify]** |
| Goal | Predict how fast a listed pet is adopted, so that the insights could be turned into tools that help shelters and rescuers write more appealing profiles ([Vice, 2020](https://www.vice.com/en/article/kaggle-data-science-community-rocked-by-pet-adoption-contest-cheating-scandal); [PetFinder.my AI Task Force](https://www.petfinder.my/ai_taskforce.htm)) |
| Metric | **Quadratic Weighted Kappa (QWK)** between predicted and true `AdoptionSpeed` **[to re-verify]** |

> The Kaggle pages render only with JavaScript, so we could not re-read the rules, data page or metric definition automatically. A teammate should open them in a browser and tick off the **[to re-verify]** items (tracked as an issue).

## 2. Original problem definition

The target was the ordinal variable **`AdoptionSpeed`**:

| Value | Meaning |
|---|---|
| 0 | Adopted on the same day it was listed |
| 1 | Adopted between 1 and 7 days (1st week) |
| 2 | Adopted between 8 and 30 days (1st month) |
| 3 | Adopted between 31 and 90 days (2nd & 3rd month) |
| 4 | No adoption after 100 days of being listed |

Two points matter for us:

- **It is ordinal.** Predicting 3 when the truth is 4 is a smaller error than predicting 0. QWK rewards this ordering, while accuracy and macro-F1 do not. This is why many competitors trained **regression** models and then cut the continuous prediction into classes with tuned thresholds.
- **"Adopted?" and "how fast?" are different questions.** Our assignment asks for both: a binary target (`ADOPTION`, derived from `AdoptionSpeed` ≠ 4) and the multiclass `AdoptionSpeed`. The binary problem is much easier; the boundaries between classes 1/2/3 are noisy (a pet adopted on day 7 vs. day 8 is almost indistinguishable).

## 3. Original data

| Source | Contents | In our course dataset? |
|---|---|---|
| Tabular `train.csv` | The 24 columns we have (type, age, breeds, gender, colours, size, fur, health flags, quantity, fee, state, rescuer, video/photo counts, description, PetID, AdoptionSpeed) | **Yes** — 14,993 rows, same columns **[verified on course data]** |
| Lookup tables | `breed_labels.csv`, `color_labels.csv`, `state_labels.csv` | **Yes** **[verified on course data]** |
| Images | Listing photos per PetID | **No** |
| Image metadata | Google Vision API output (labels, dominant colours, crop hints) | **No** |
| Sentiment | Google Natural Language API output on descriptions | **No** |
| Test set | Separate unlabelled test set | **No** — we evaluate with cross-validation on our labelled data |

The professor states that the course data **can contain errors, typos and missing values** on purpose. Our first audit confirms this (see [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md)). So results from Kaggle are **not directly comparable** to ours.

## 4. Interesting findings from the community

These come from public discussions and kernels. They are **hypotheses to test on our data**, not facts about it.

1. **Rescuer activity is very informative.** Competitors widely reported that the *number of listings per `RescuerID`* was one of the strongest features (large, organised rescuers tend to have different adoption dynamics than individuals). In our data there are 5,596 distinct rescuers for 14,993 listings **[verified on course data]**.
   - ⚠️ **Leakage risk:** listings from the same rescuer are correlated. Random CV splits can place the same rescuer in train and test and make scores optimistic. Grouped CV by `RescuerID` is worth considering.
2. **Age, photos and breed matter.** Younger animals, listings with more photos, and specific (non-"mixed") breeds were commonly associated with faster adoption.
3. **Text helps.** Description length and simple text statistics carried signal; top teams used TF-IDF and pretrained embeddings.
4. **Class 0 is rare** and hard to predict. In our data it is ~2.7% of listings (410 / 14,993) **[verified on course data]**.
5. **Ordinal post-processing** ("optimised rounder": choosing class thresholds on a regression output to maximise QWK) was a standard trick.

### A cautionary tale: the first-place disqualification

The original winning team ("BestPetting", 1st place, $10,000 prize) was **disqualified in January 2020**, about nine months after the competition. A competitor helping PetFinder.my deploy the solutions found that the team had scraped the test labels and hidden them inside obfuscated code, using them for roughly one in ten pets to keep the score realistic. Without the trick the submission would have scored around 0.43 QWK (~100th place) instead of 0.912. ([Vice, 14 Jan 2020](https://www.vice.com/en/article/kaggle-data-science-community-rocked-by-pet-adoption-contest-cheating-scandal))

Lesson for us: **suspiciously good scores are a red flag.** Always check for leakage before celebrating.

## 5. Potential modelling approaches

### 5.1 Within syllabus ✅

| Area | Techniques |
|---|---|
| Supervised | Decision trees; k-NN classification; Naive Bayes (Gaussian / categorical); logistic regression; regularised linear models (L1/L2); perceptron; SVMs with linear and kernel (RBF, polynomial) variants; multilayer perceptron; ensembles: voting, bagging, boosting (e.g. AdaBoost), stacking |
| Ordinal angle | Linear / k-NN regression on `AdoptionSpeed`, then rounding to classes (regression is in the syllabus) |
| Unsupervised | k-means and other distance-based clustering; hierarchical (agglomerative) clustering with different linkages; nearest-neighbour analysis |
| Hands-on | Encoding (one-hot, ordinal), scaling, binning (e.g. age), feature construction (rescuer listing count, description length, photo count bins, "is mixed breed", "has name"), feature selection, cross-validation, grid search |
| Imbalance | Class weights; stratified CV; resampling (the template links to `imbalanced-learn`) |

### 5.2 Potentially within syllabus ⚠️ (needs team approval)

| Technique | Why it might be acceptable |
|---|---|
| Random Forest | A bagging ensemble of decision trees; bagging is in the syllabus, but CLAUDE.md asks us not to use RF variants automatically |
| Gradient Boosting from scikit-learn | Boosting is in the syllabus; `GradientBoostingClassifier` / `HistGradientBoostingClassifier` are its scikit-learn forms |
| Bag-of-words / TF-IDF on `Description` | Pure feature construction feeding syllabus models; adds complexity and must be justified |
| PCA for visualising clusters | Dimensionality reduction is a standard feature transformation; check whether it was covered in class |
| DBSCAN / Gaussian mixtures | Clustering, but not explicitly listed |
| Quadratic Weighted Kappa as an extra metric | A metric, not a model; useful for the ordinal target |
| Grouped CV by `RescuerID` | Evaluation design choice to prevent leakage |

### 5.3 Outside syllabus ❌ (insight only)

XGBoost, LightGBM, CatBoost; pretrained CNN image features (DenseNet, EfficientNet, …); word embeddings / transformers on text; Google Vision / NL API features; heavy model blending with optimised rounders across dozens of models.

## 6. Methodological limitations to keep in mind

- Our data is modified, contains injected errors and has no images or sentiment, so Kaggle feature importances may not transfer.
- `AdoptionSpeed` buckets are defined by listing time; some listings may simply have been removed, so "not adopted" can mix different situations.
- Target noise near class boundaries caps achievable multiclass performance.
- Rescuer-level correlation can inflate cross-validated scores (see §4.1).

## 7. Sources

- Kaggle, *PetFinder.my Adoption Prediction*: <https://www.kaggle.com/c/petfinder-adoption-prediction/> (overview, data, rules)
- A. Gordon, "Data Science Community Rocked by Pet Adoption Contest Cheating Scandal", *Vice*, 14 Jan 2020: <https://www.vice.com/en/article/kaggle-data-science-community-rocked-by-pet-adoption-contest-cheating-scandal>
- PetFinder.my AI Task Force: <https://www.petfinder.my/ai_taskforce.htm>
- A. Lukyanenko, *Exploration of data step by step* (EDA kernel linked by the professor): <https://www.kaggle.com/artgor/exploration-of-data-step-by-step/notebook>
- P. Flach (2012); G. James et al. (2023) — see README references.
