# Course scope

The project must stay within the syllabus of *Aprendizagem Automática 2026/27*. A simpler model that is correctly evaluated and well explained is worth more than a stronger model the course did not cover.

## Syllabus

| Topic | Contents |
|---|---|
| Fundamentals | Concepts and terminology; supervised vs. unsupervised learning; model learning, evaluation and selection |
| Tree models | Decision trees |
| Distance-based models | k-NN classification and regression; distance-based clustering; hierarchical clustering |
| Probabilistic models | Naive Bayes |
| Linear models | Regression; regularised models; perceptron; support vector machines; kernels and nonlinear extensions |
| Neural networks | Multilayer networks; backpropagation |
| Ensembles | Voting; bagging; boosting; stacking |
| Hands-on ML | Feature transformation, construction and selection; model learning, evaluation and selection |

## The assignment's classifier families

Task 1 needs **5 classifiers from at least 3** of these families (plus optionally one ensemble):

| Family | Candidates (scikit-learn) |
|---|---|
| Tree | `DecisionTreeClassifier` |
| Probabilistic | `GaussianNB`, `CategoricalNB`, `BernoulliNB` |
| Distance-based | `KNeighborsClassifier` |
| Linear | `LogisticRegression`, `Perceptron`, `SGDClassifier`, `LinearSVC`, `SVC` (kernels) |
| Ensemble (optional) | `VotingClassifier`, `BaggingClassifier`, `AdaBoostClassifier`, `StackingClassifier` |
| Neural network | `MLPClassifier` (in the syllabus, but not one of the four required families) |

## Clustering (Task 2)

`KMeans`, `AgglomerativeClustering` (single / complete / average / Ward linkage), with internal metrics (silhouette, Davies–Bouldin, Calinski–Harabasz) and external metrics against `AdoptionSpeed` (adjusted Rand index, normalised mutual information, homogeneity / completeness, purity).

## Rule for anything else

Every technique proposed from outside research is classified as:

1. **Within syllabus** — use freely.
2. **Potentially within syllabus** — discuss as a team, record the decision in [`DECISIONS.md`](DECISIONS.md).
3. **Outside syllabus** — do not use in the final solution without explicit team approval (and a clear justification in the notebook).

See [`RESEARCH.md`](RESEARCH.md) §5 for the classification of Kaggle techniques. Examples of *outside syllabus*: XGBoost, LightGBM, CatBoost, CNN image features, transformer text models.

## Bibliography

1. P. Flach, *Machine Learning: The Art and Science of Algorithms that Make Sense of Data*. <http://people.cs.bris.ac.uk/~flach/mlbook/>
2. G. James et al., *An Introduction to Statistical Learning with Applications in Python*. <https://www.statlearning.com/>
