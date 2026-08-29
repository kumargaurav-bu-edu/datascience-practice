# Candidate Models Comparison Guide

## Overview

The Candidate Models table compares different variable selection methods and criteria to help you choose the best model for your specific needs. Each method produces a different model with different trade-offs between complexity and fit.

## Table Structure

### Columns

| Column | Description |
|--------|-------------|
| **Method** | Variable selection method (Stepwise, Backwards) |
| **Select** | Selection criterion (AIC, SBC, Adj R-square, SL) |
| **# inputs** | Number of predictor variables in model |
| **MSE** | Mean Squared Error (lower = better prediction) |
| **R-square** | Proportion of variation explained (0-1) |
| **Adj R-square** | R² adjusted for number of parameters |
| **AIC** | Akaike Information Criterion (lower = better) |
| **SBC** | Schwarz Bayesian Criterion (lower = better) |

## Selection Methods

### 1. Stepwise with AIC (RECOMMENDED)

**Our Chosen Model**

**Characteristics:**
- 11 input variables
- MSE: 302.96
- Adj R²: 0.539
- AIC: 20837 (lowest)

**Why Choose:**
- Best balance between fit and complexity
- AIC criterion penalizes model complexity appropriately
- Good predictive performance
- Reasonable number of variables for interpretation

**When to Use:**
- When you want the best overall model
- When you need a balance between fit and simplicity
- When prediction accuracy is important

### 2. Stepwise with SBC

**Simplest Model**

**Characteristics:**
- 6 input variables (simplest)
- MSE: 307.05
- Adj R²: 0.532
- SBC: 17809 (lowest)

**Why Choose:**
- Fewest variables (easiest to interpret)
- SBC criterion strongly penalizes complexity
- Minimal overfitting risk
- Easier to implement in practice

**When to Use:**
- When simplicity is a priority
- When you want maximum interpretability
- When you have limited resources for data collection
- When you want to avoid overfitting

### 3. Backwards with Adj R-square

**Most Complex Model**

**Characteristics:**
- 15 input variables (most complex)
- MSE: 301.76 (lowest)
- Adj R²: 0.541 (highest)
- AIC: 20880

**Why Choose:**
- Best fit to the data
- Highest adjusted R-square
- Lowest MSE (best predictions)
- Captures most relationships

**When to Use:**
- When prediction accuracy is paramount
- When you have sufficient data
- When you can handle model complexity
- When you want to capture all relationships

### 4. Stepwise with SL (α = 0.01)

**Significance-Based Model**

**Characteristics:**
- 8 input variables
- MSE: 303.48
- Adj R²: 0.538
- AIC: 20839

**Why Choose:**
- Uses statistical significance threshold
- Moderate complexity (8 variables)
- All variables are statistically significant
- Good balance of significance and fit

**When to Use:**
- When statistical significance is important
- When you want all variables to be significant
- When you prefer hypothesis-driven selection
- When you need to justify each variable

## Comparison Analysis

### Complexity vs Fit Trade-off

```
Simplest ←────────────────────────────────→ Most Complex
SBC (6)  →  SL (8)  →  AIC (11)  →  Backwards (15)

MSE:     307.05  →  303.48  →  302.96  →  301.76 (lower = better)
Adj R²:  0.532   →  0.538   →  0.539   →  0.541  (higher = better)
```

### Performance Differences

**MSE Range:** 301.76 to 307.05 (difference: 5.29)
- Backwards model has 1.7% better MSE than SBC
- AIC model is 0.04% better than Backwards

**Adj R² Range:** 0.532 to 0.541 (difference: 0.009)
- Backwards model has 1.7% better Adj R² than SBC
- AIC model is 0.2% better than Backwards

**Complexity Range:** 6 to 15 variables (difference: 9 variables)
- SBC uses 60% fewer variables than Backwards
- AIC uses 27% fewer variables than Backwards

### Key Insights

1. **Diminishing Returns:**
   - Going from 6 to 11 variables: 0.7% improvement in Adj R²
   - Going from 11 to 15 variables: 0.4% improvement in Adj R²
   - Adding more variables gives smaller improvements

2. **Efficiency:**
   - AIC model achieves 99.6% of Backwards model's fit with 27% fewer variables
   - SBC model achieves 98.3% of Backwards model's fit with 60% fewer variables

3. **Stability:**
   - All models have similar performance (Adj R² between 0.532-0.541)
   - Choice depends on your priorities, not dramatic performance differences

## Decision Framework

### Choose SBC (6 variables) if:
- ✓ Simplicity and interpretability are priorities
- ✓ You want to minimize overfitting risk
- ✓ You have limited resources
- ✓ You need a model that's easy to explain
- ✓ You want the most parsimonious model

### Choose AIC (11 variables) if:
- ✓ You want the best overall balance (RECOMMENDED)
- ✓ Prediction accuracy is important
- ✓ You can handle moderate complexity
- ✓ You want to capture most relationships
- ✓ You're unsure about trade-offs

### Choose Backwards (15 variables) if:
- ✓ Prediction accuracy is paramount
- ✓ You have sufficient data
- ✓ You can handle complexity
- ✓ You want to capture all relationships
- ✓ You're willing to sacrifice interpretability

### Choose SL (8 variables) if:
- ✓ Statistical significance is important
- ✓ You want all variables to be significant
- ✓ You prefer hypothesis-driven selection
- ✓ You need to justify each variable
- ✓ You want moderate complexity

## Practical Recommendations

### For Business Applications:
**Use AIC Model (11 variables)**
- Good balance of accuracy and interpretability
- Can explain to stakeholders
- Captures important relationships
- Reasonable number of variables to monitor

### For Research/Academic:
**Use Backwards Model (15 variables)**
- Captures all significant relationships
- Best fit to data
- Comprehensive analysis
- Can discuss trade-offs in paper

### For Production Systems:
**Use SBC Model (6 variables)**
- Simplest to implement
- Easiest to maintain
- Lowest overfitting risk
- Fastest predictions

### For Exploratory Analysis:
**Use SL Model (8 variables)**
- All variables are statistically significant
- Good balance of complexity and significance
- Easy to justify each variable
- Good for hypothesis testing

## Model Selection Criteria

### When to Prioritize Each Metric

**AIC:**
- Best for prediction accuracy
- Balances fit and complexity
- Recommended for most applications

**SBC:**
- Best for model simplicity
- Stronger penalty for complexity
- Recommended when interpretability matters

**Adj R-square:**
- Best for explaining variation
- Accounts for number of parameters
- Recommended for understanding relationships

**MSE:**
- Best for prediction error
- Direct measure of fit
- Recommended for forecasting

## Limitations and Considerations

1. **Data-Dependent:**
   - Results are specific to this dataset
   - Different data may produce different models
   - Use cross-validation to validate

2. **Assumption-Based:**
   - All methods assume linear relationships
   - May not capture non-linear patterns
   - Check diagnostic plots

3. **Multicollinearity:**
   - Correlated variables may affect selection
   - Check VIF values
   - Consider domain knowledge

4. **Generalization:**
   - Models trained on this data
   - May not generalize to new data
   - Use hold-out test set to validate

## Next Steps

1. **Validate the Chosen Model:**
   - Use cross-validation
   - Test on hold-out data
   - Check assumptions

2. **Compare with Domain Knowledge:**
   - Do selected variables make sense?
   - Are there missing important variables?
   - Should you override selection?

3. **Monitor Performance:**
   - Track model performance over time
   - Retrain periodically
   - Update as new data arrives

4. **Document Decisions:**
   - Record why you chose this model
   - Document trade-offs considered
   - Keep for future reference

## Related Sections

- **Stepwise Selection**: How variables were selected
- **Parameter Estimates**: Coefficients for selected variables
- **Model Diagnostics**: Check if assumptions are met
- **ANOVA Table**: Overall model significance

---

**Last Updated:** August 29, 2026
**Status**: ✅ Candidate Models Comparison Implemented
