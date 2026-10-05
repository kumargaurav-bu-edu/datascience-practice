# Data Science Educational Notebook — Prompt Template

> **Purpose**: Copy-paste the Quick-Start Prompt below (filling in `{{placeholders}}`)
> into a new Cursor chat to generate a graduate-level educational notebook.
>
> **Philosophy**: Act as a graduate-level data science instructor.
> Use the notebook as the teaching medium and the dataset as the laboratory.
>
> **Reference notebook**: `sas_hackthon/stats_ml/06_multiple_regression.ipynb`
>
> **Cursor rule**: `.cursor/rules/datascience-notebook-template.mdc`
> (auto-activates for any `sas_hackthon/**/*.ipynb` file)
>
> **Last updated**: Sep 2026

---

## Quick-Start Prompt (copy & customize)

```text
Create a comprehensive, educational Jupyter notebook for learning the data
science concept described below. Follow the datascience-notebook-template
Cursor rule as the authoritative formatting and structural standard. Preserve
its conventions consistently, but adapt the analytical sequence when the
statistical method requires it.

### TOPIC DETAILS
- **Subject Area**: {{subject_area}}
- **Topic**: {{topic}}
- **Notebook Number**: {{number}}
- **Notebook Filename**: {{number}}_{{slug}}.ipynb
- **Dataset**: {{dataset_name}} at {{dataset_path}}
- **Target Variable**: {{target_variable}}
- **Key Concepts to Cover**: {{concepts_list}}

### LEARNING OBJECTIVES
By the end of this notebook, I should be able to:
- Explain {{concept}} in plain English.
- Explain the mathematical/statistical intuition behind {{concept}}.
- Implement {{concept}} in Python.
- Interpret the resulting output on real data.
- Explain when to use and when NOT to use {{concept}}.
- Identify common mistakes and limitations.
- Relate {{concept}} to previously learned concepts.

### OPTIONAL CONTEXT
- **Prerequisites**: {{previous_notebooks}}
- **Comparison With SAS**: {{yes_or_no}}
- **Companion Doc**: yes / no
```

---

## Filled-In Examples

### Example 1 — Logistic Regression

```text
Create a comprehensive, educational Jupyter notebook for learning the data
science concept described below. Follow the datascience-notebook-template
Cursor rule as the authoritative formatting and structural standard.

### TOPIC DETAILS
- **Subject Area**: Statistics & Machine Learning
- **Topic**: Logistic Regression for Binary Classification
- **Notebook Number**: 08
- **Notebook Filename**: 08_logistic_regression.ipynb
- **Dataset**: pva_donors.csv at data/VST152/pva_donors.csv
- **Target Variable**: Response (Yes/No)
- **Key Concepts to Cover**: log-odds, odds ratios, maximum likelihood
  estimation, confusion matrix, ROC curve, AUC, classification threshold
  tuning, Hosmer-Lemeshow test

### LEARNING OBJECTIVES
By the end of this notebook, I should be able to:
- Explain logistic regression and odds ratios in plain English.
- Explain the mathematical intuition behind maximum likelihood estimation.
- Implement logistic regression in Python (statsmodels + sklearn).
- Interpret coefficients as odds ratios.
- Build and interpret a confusion matrix and ROC curve.
- Explain when logistic regression is appropriate vs other classifiers.
- Identify common mistakes (class imbalance, threshold choice, leakage).
- Relate logistic regression back to linear regression concepts.

### OPTIONAL CONTEXT
- **Prerequisites**: 06_multiple_regression, 07_model_diagnostics
- **Comparison With SAS**: yes
- **Companion Doc**: yes
```

### Example 2 — Decision Trees & Random Forest (Classification)

```text
Create a comprehensive, educational Jupyter notebook for learning the data
science concept described below. Follow the datascience-notebook-template
Cursor rule as the authoritative formatting and structural standard.

### TOPIC DETAILS
- **Subject Area**: Machine Learning
- **Topic**: Decision Trees and Random Forest for Classification
- **Notebook Number**: 09
- **Notebook Filename**: 09_decision_trees_random_forest.ipynb
- **Dataset**: pva_donors.csv at data/VST152/pva_donors.csv
- **Target Variable**: Response (Yes/No)
- **Key Concepts to Cover**: information gain, Gini impurity, entropy,
  pruning, bagging, feature importance, out-of-bag error, hyperparameter
  tuning, cross-validation, overfitting vs underfitting

### LEARNING OBJECTIVES
By the end of this notebook, I should be able to:
- Explain how a decision tree splits data and why.
- Calculate information gain and Gini impurity by hand.
- Explain why Random Forest improves over a single tree.
- Implement and tune both models in scikit-learn.
- Interpret feature importance and partial dependence.
- Identify overfitting and apply pruning / hyperparameter tuning.
- Compare tree-based methods to logistic regression for this dataset.

### OPTIONAL CONTEXT
- **Prerequisites**: 08_logistic_regression
- **Comparison With SAS**: no
- **Companion Doc**: yes
```

### Example 3 — Clustering

```text
Create a comprehensive, educational Jupyter notebook for learning the data
science concept described below. Follow the datascience-notebook-template
Cursor rule as the authoritative formatting and structural standard.

### TOPIC DETAILS
- **Subject Area**: Unsupervised Learning
- **Topic**: K-Means and Hierarchical Clustering
- **Notebook Number**: 10
- **Notebook Filename**: 10_clustering.ipynb
- **Dataset**: pva_donors.csv at data/VST152/pva_donors.csv
- **Target Variable**: (none — unsupervised)
- **Key Concepts to Cover**: feature scaling, elbow method, silhouette
  score, dendrogram, Ward's method, cluster profiling, PCA for
  visualization, choosing K

### LEARNING OBJECTIVES
By the end of this notebook, I should be able to:
- Explain why clustering is unsupervised and what that means.
- Explain K-Means algorithm step-by-step.
- Explain why feature scaling matters for distance-based methods.
- Use the elbow method and silhouette scores to choose K.
- Interpret a dendrogram and choose a cut point.
- Profile clusters and describe them in business terms.
- Explain when clustering is appropriate and its limitations.

### OPTIONAL CONTEXT
- **Prerequisites**: 01_descriptive_statistics, 04_correlation_analysis
- **Comparison With SAS**: no
- **Companion Doc**: yes
```

---

## What the Template Enforces (5-Layer Architecture)

### Layer 1 — Task Definition

The prompt header: subject, topic, dataset, target, concepts, prerequisites.
Includes **Method Compatibility Check** — the AI must verify that the target
variable, method, and listed concepts are all consistent before generating.

### Layer 2 — Learning Objectives

Explicit "By the end of this notebook, I should be able to…" section.
Shifts the notebook from "here's how to do it" to "here's how to understand it."

### Layer 3 — Teaching Rules

| Rule | What it does |
|------|-------------|
| **Explain Before Computing** | Concept → intuition → question → expected output → code → actual interpretation → connect back |
| **Concept Teaching Framework** | What → Why → Intuition → Math → Assumptions → Code → Result → Interpretation → Mistakes → Alternatives → When to use → When not to |
| **Active Learning** | "🤔 Think About It" prediction exercises before revealing results |
| **Actual Output Interpretation** | Interpret real values, not generic advice ("R² = 0.38 means…" not "R² closer to 1 is better") |
| **📊 READOUT cells** | After every table or chart, add a dedicated code cell that computes and prints the actual key values with plain-English interpretation (see below) |
| **SAS ↔ Python Mapping** | Side-by-side procedure mapping when SAS mode is on |
| **statsmodels vs sklearn** | Use statsmodels for inference, sklearn for prediction; explain the difference |
| **Prerequisite Check** | Brief refresh of required prior concepts, don't re-teach entire notebooks |
| **Common Misconceptions** | 3–7 misconceptions with ❌ incorrect → ✅ correct → 💡 example |

### 📊 READOUT Cell Pattern (CRITICAL)

After **every** table display or visualization, insert a separate code cell
that computes and prints the actual values with interpretation. This is the
most important pattern for a learner.

**Cell structure:**
```python
# 📊 READOUT: {{what was just shown}}
print("=" * 120)
print("📊 READOUT: {{TITLE IN UPPER CASE}}")
print("=" * 120)

# Extract and print the ACTUAL computed values
print(f"\n  {{metric name}}: {{actual_value}}")
print(f"  ➡️  {{what that value means for THIS dataset}}")

# Flag the most notable finding
print(f"\n  🔴 MOST NOTABLE FINDING:")
print(f"     {{describe the specific outlier, spike, or pattern with real numbers}}")
print(f"     ➡️  {{plain-English consequence}}")

# Contextual comparison
print(f"\n  💡 WHAT THIS TELLS YOU:")
print(f"     {{connect the numbers back to the business/statistical question}}")
```

**Rules for READOUT cells:**
- ❌ NEVER write generic advice ("R² closer to 1 is better")
- ✅ ALWAYS use the actual computed value ("R² = 0.5462, meaning 54.6% of donation variance is explained")
- ✅ Identify the most extreme / notable observation by number and actual values
- ✅ Explain what a spike, outlier, or pattern means for this specific donor dataset
- ✅ Use `$` formatting for dollar amounts
- ✅ Compare thresholds to actual values (e.g., "Cook's D = 0.082, which is 63x the threshold of 0.0013")
- ✅ For multi-panel grids, provide a readout for each panel with its actual numbers
- ✅ For residual-by-regressor plots, report correlation, spread ratio, and whether LOWESS deviates from zero

### Layer 4 — Analytical & Engineering Rules

| Rule | What it does |
|------|-------------|
| **Statistical Rigor** | Check assumptions, distinguish significance from practical importance, no fabricated results |
| **Data Leakage** | Mandatory check for ML notebooks |
| **Modeling Mindset** | Question → target → features → train/test → assumptions → metric → generalization |
| **Reproducibility** | Random seeds, no hard-coded results, sequential execution |
| **Diagnostics** | Assumptions list → formal tests (✅/❌) → diagnostic plots → plain-English remedies |

### Layer 5 — Output Structure & QA

| Component | Details |
|-----------|---------|
| **Cell Sequence** | Cell 0: utils → Cell 1: libraries → Cell 2: data load → Cell 3: overview + objectives → For each step: Markdown → Code → 📊 READOUT → Misconceptions → Summary → Knowledge Check → Answer Key |
| **Styled Tables** | Green = data, Blue = stats, Orange = comparisons, Red = warnings, Purple = coefficients |
| **Print Banners** | `"=" * 80` major, `"-" * 80` sub, `TABLE N:` prefix |
| **Visualizations** | `fig, ax`, bold labels, grid, `tight_layout`, GridSpec for multi-plot |
| **Knowledge Check** | 5–10 questions (conceptual + interpretation of actual results), answers hidden below |
| **Companion Doc** | `docs/{{number}}_{{slug}}.md` with summary, key results, interpretation |
| **Validation** | 10-point checklist: imports, paths, variables, sequential execution, no fabricated results |

---

## Step Naming Reference

| Topic | Suggested Steps |
|-------|----------------|
| **Regression** | Data Prep → Observations Summary → Class Levels → Model Dimensions → Variable Selection → Stop Details → Fit Criteria Viz → Final Model → ANOVA → Parameter Estimates → Diagnostics → Summary |
| **Logistic Reg** | Data Prep → Class Balance → Feature Selection → Model Fitting → Odds Ratios → Confusion Matrix → ROC/AUC → Threshold Tuning → Goodness-of-Fit → Summary |
| **Hypothesis Testing** | Data Prep → EDA → Test Selection → Assumptions Check → Test Execution → P-value Interpretation → Effect Size → Summary |
| **Classification** | Data Prep → Class Distribution → Feature Engineering → Train/Test Split → Model Training → Evaluation Metrics → Model Comparison → Summary |
| **Clustering** | Data Prep → Feature Scaling → Elbow Method → Silhouette Analysis → Model Fitting → Cluster Profiling → Visualization → Summary |
| **Time Series** | Data Prep → Decomposition → Stationarity Tests → ACF/PACF → Model Selection → Fitting → Forecast → Residual Diagnostics → Summary |
| **PCA** | Data Prep → Scaling → Correlation Heatmap → Eigenvalues → Scree Plot → Loadings → Biplot → Variance Explained → Summary |

---

## Tips for Best Results

1. **Be specific with concepts** — 5–8 key concepts gives enough detail for
   thorough explanations without padding.
2. **Write real learning objectives** — "interpret odds ratios" is better than
   "learn logistic regression."
3. **Name prerequisites** — enables "As we saw in `05_simple_linear_regression`…"
   cross-references.
4. **SAS comparison mode** — maps SAS PROC output layout to Python equivalents
   (most useful for PROC REG, PROC LOGISTIC, PROC GLM).
5. **Run the notebook after generation** — review outputs, then ask for tweaks.
6. **Iterate** — "add a Step between 6 and 7 covering interaction terms" works.
7. **Answer the Knowledge Check yourself** — then compare with the Answer Key
   to test your understanding.
8. **Check target/method compatibility** — continuous target = regression methods;
   categorical target = classification methods. The template validates this
   but double-check your concepts list.
