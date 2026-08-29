# Multiple Regression Analysis with Stepwise Selection - Complete Guide

## Overview

This comprehensive notebook demonstrates **multiple linear regression** with **stepwise variable selection using AIC (Akaike Information Criterion)** on the PVA Donors dataset. The analysis predicts donation amounts based on donor characteristics.

## What You'll Learn

### 1. **Multiple Regression Fundamentals**
   - Why use multiple regression instead of simple regression
   - How to handle categorical variables (encoding)
   - Understanding regression coefficients and their interpretation

### 2. **Stepwise Variable Selection with AIC**
   - Forward selection algorithm
   - AIC criterion for model comparison
   - Trade-off between model fit and complexity
   - Advantages and limitations of stepwise selection

### 3. **Model Diagnostics & Assumption Checking**
   - Linearity, independence, homoscedasticity, normality
   - Multicollinearity detection (VIF)
   - Residual analysis and outlier detection
   - Diagnostic plots interpretation

## Notebook Structure

### **Step 1: Data Preparation & Cleaning**
- Load and explore the donor dataset
- Identify missing values
- Remove incomplete records
- Encode categorical variables using one-hot encoding

**Key Concept**: Clean data is essential for reliable regression results. Missing values can bias estimates, and categorical variables must be converted to numeric form.

### **Step 2: Observations Summary (Table 1)**
Shows:
- Total observations read
- Observations used in analysis
- Observations excluded due to missing values

**Why It Matters**: Helps assess data quality and sample size adequacy.

### **Step 3: Class Variables Summary (Table 2)**
Lists all categorical variables and their levels:
- Original variable names
- Number of unique categories
- Actual category values

**Why It Matters**: Understanding categorical structure is crucial for interpreting dummy variable coefficients.

### **Step 4: Model Dimensions (Table 3)**
Displays:
- Number of predictor variables
- Number of parameters to estimate (including intercept)
- Observations-to-parameters ratio

**Why It Matters**: Ensures adequate sample size relative to model complexity (rule of thumb: 10-20 observations per parameter).

### **Step 5: Stepwise Selection with AIC (Table 4)**
Forward selection process showing:
- Step number
- Variable entered at each step
- Number of effects and parameters in model
- AIC value at each step

**Key Concepts**:
- **Forward Selection**: Start with no variables, add one at a time
- **AIC**: Balances model fit with complexity (lower is better)
- **Stopping Rule**: Stop when adding more variables doesn't improve AIC

**Alternatives**:
- Backward elimination (start with all, remove one at a time)
- Best subset selection (test all combinations)
- Ridge/Lasso regression (shrinkage methods)

### **Step 6: Stop Details (Table 5)**
Shows candidates that were NOT selected:
- Variables considered but not added
- Their AIC if they were added
- Comparison with current model AIC

**Why It Matters**: Explains why selection stopped and which variables were close to being selected.

### **Step 7: Fit Criteria Visualization**
Four plots showing:
1. **AIC by Step**: How AIC improves as variables are added
2. **Model Complexity**: Number of parameters at each step
3. **AIC Improvement**: Magnitude of improvement at each step
4. **Summary Statistics**: Final model characteristics

**What to Look For**:
- Steep decline in AIC = variables significantly improve model
- Flat line = additional variables not helping much
- Elbow point = optimal model complexity

### **Step 8: Final Model Summary**
Complete regression output including:
- Coefficients and standard errors
- t-statistics and p-values
- Model fit statistics (R², Adjusted R², AIC, BIC)

### **Step 9: ANOVA Table (Table 6)**
Tests overall model significance:
- **F-statistic**: Tests if model explains variation better than mean
- **p-value**: Probability of observing this F-statistic by chance
- **R-squared**: Proportion of variation explained (0 to 1)
- **Adjusted R-squared**: R² penalized for model complexity

**Interpretation**:
- F-statistic > 1 and p-value < 0.05 = Model is significant
- Higher R² = Better fit (but watch for overfitting)
- Adjusted R² accounts for number of parameters

### **Step 10: Parameter Estimates (Table 7)**
Regression coefficients with:
- **Estimate**: Coefficient value (change in Y per unit change in X)
- **Std Error**: Uncertainty in estimate
- **t Value**: Estimate / Std Error
- **Pr > |t|**: P-value for significance test
- **95% Confidence Intervals**: Range of plausible values

**Interpretation**:
- Positive coefficient = Variable increases donation amount
- Negative coefficient = Variable decreases donation amount
- p-value < 0.05 = Coefficient is statistically significant
- Larger |t value| = Stronger evidence coefficient ≠ 0

### **Step 11: Model Diagnostics (Table 8 & Plots)**

#### **Diagnostic Statistics**:
- Residuals (errors) for each observation
- Standardized residuals (residuals / std dev)
- Leverage (influence of each observation)
- Cook's Distance (overall influence on model)

#### **Diagnostic Plots**:

1. **Residuals vs Fitted Values**
   - Check: Random scatter around 0 (no pattern)
   - Problem: Curved pattern suggests non-linearity
   - Solution: Add polynomial terms or transform variables

2. **Q-Q Plot (Quantile-Quantile)**
   - Check: Points close to diagonal line
   - Problem: Deviations at tails suggest non-normality
   - Solution: Transform response variable (log, sqrt, etc.)

3. **Scale-Location Plot**
   - Check: Horizontal line with random scatter
   - Problem: Increasing/decreasing trend suggests heteroscedasticity
   - Solution: Weighted least squares or transformation

4. **Residuals vs Leverage**
   - Check: No extreme points
   - Problem: Points far from center with large residuals are influential
   - Solution: Investigate outliers, consider robust regression

5. **Cook's Distance**
   - Check: No points above threshold (4/n)
   - Problem: High values indicate influential observations
   - Solution: Investigate outliers, consider robust regression

6. **Histogram of Residuals**
   - Check: Bell-shaped, symmetric distribution
   - Problem: Skewed or multi-modal distribution
   - Solution: Transform response variable

7. **Actual vs Predicted**
   - Check: Points close to diagonal line
   - Problem: Systematic deviations suggest model misspecification
   - Solution: Add interaction terms or non-linear terms

8. **Residuals Over Time**
   - Check: Random pattern, no trends
   - Problem: Autocorrelation suggests dependence
   - Solution: Use time series methods or add lagged variables

9. **Autocorrelation Function (ACF)**
   - Check: Spikes within confidence bands
   - Problem: Significant spikes suggest autocorrelation
   - Solution: Add lagged variables or use time series methods

#### **Statistical Tests**:

1. **Normality Tests** (Shapiro-Wilk, Jarque-Bera)
   - H₀: Residuals are normally distributed
   - p-value > 0.05 = Residuals are normal (good)
   - p-value < 0.05 = Residuals deviate from normality

2. **Heteroscedasticity Test** (Breusch-Pagan)
   - H₀: Constant variance (homoscedasticity)
   - p-value > 0.05 = Constant variance (good)
   - p-value < 0.05 = Non-constant variance (heteroscedasticity)

3. **Multicollinearity Check** (VIF - Variance Inflation Factor)
   - VIF = 1: No correlation with other variables (ideal)
   - VIF < 5: Generally acceptable
   - VIF > 10: Problematic multicollinearity
   - VIF > 5: May warrant investigation

## Key Concepts Explained

### **Regression Equation**
```
Donation_Amt = β₀ + β₁X₁ + β₂X₂ + ... + βₚXₚ + ε

Where:
- β₀ = Intercept (expected value when all X = 0)
- β₁, β₂, ..., βₚ = Coefficients (effect of each variable)
- ε = Error term (unexplained variation)
```

### **AIC (Akaike Information Criterion)**
```
AIC = 2k + n*ln(RSS/n)

Where:
- k = Number of parameters
- n = Number of observations
- RSS = Residual sum of squares

Lower AIC = Better model (balances fit and complexity)
```

### **R-squared (Coefficient of Determination)**
```
R² = SS_Model / SS_Total = 1 - (SS_Error / SS_Total)

Where:
- SS_Model = Variation explained by model
- SS_Error = Unexplained variation (residuals)
- SS_Total = Total variation in Y

Range: 0 to 1
- R² = 0: Model explains none of the variation
- R² = 1: Model explains all variation (perfect fit)
- Higher R² = Better fit (but watch for overfitting)
```

### **Adjusted R-squared**
```
Adj R² = 1 - [(1 - R²) * (n - 1) / (n - p - 1)]

Where:
- n = Number of observations
- p = Number of parameters

Penalizes adding unnecessary variables
Better for comparing models with different numbers of parameters
```

### **F-statistic**
```
F = MS_Model / MS_Error = (SS_Model / p) / (SS_Error / (n - p - 1))

Tests: H₀: All coefficients = 0 (model has no effect)
- F > 1: Model explains more variation than error
- p-value < 0.05: Model is statistically significant
```

### **t-statistic**
```
t = Coefficient / Standard Error

Tests: H₀: Coefficient = 0 (variable has no effect)
- |t| > 2: Roughly significant at 5% level
- p-value < 0.05: Coefficient is statistically significant
```

## Interpretation Guide

### **Coefficient Interpretation**
- **Continuous Variable**: "For each 1-unit increase in X, Y increases by β units (holding other variables constant)"
- **Categorical Variable**: "Compared to the reference category, this category has β units higher Y (holding other variables constant)"

### **Model Fit Interpretation**
- **R² = 0.75**: Model explains 75% of variation in donations
- **Adjusted R² = 0.72**: After accounting for model complexity, explains 72%
- **F-statistic p-value < 0.001**: Model is highly significant

### **Assumption Violations & Solutions**

| Assumption | Violation | Detection | Solution |
|-----------|-----------|-----------|----------|
| Linearity | Non-linear relationship | Curved pattern in residuals vs fitted | Add polynomial terms, transform variables |
| Independence | Autocorrelation | Significant spikes in ACF plot | Add lagged variables, use time series methods |
| Homoscedasticity | Non-constant variance | Funnel pattern in residuals vs fitted | Weighted least squares, transform variables |
| Normality | Non-normal residuals | Deviations in Q-Q plot | Transform response variable |
| No Multicollinearity | High correlation between predictors | VIF > 10 | Remove correlated variables, use ridge regression |

## Next Steps & Recommendations

### **Model Improvement**
1. **Variable Transformations**: Log, square root, or polynomial transformations
2. **Interaction Terms**: Include X₁*X₂ to capture combined effects
3. **Non-linear Terms**: Add polynomial terms (X², X³) for curved relationships
4. **Feature Engineering**: Create new variables from existing ones

### **Alternative Approaches**
1. **Ridge Regression**: Better for multicollinearity (shrinks coefficients)
2. **Lasso Regression**: Automatic variable selection (shrinks some to zero)
3. **Elastic Net**: Combines Ridge and Lasso benefits
4. **Generalized Linear Models (GLM)**: For non-normal response distributions
5. **Tree-based Methods**: Random Forest, Gradient Boosting for non-linear patterns

### **Model Validation**
1. **Cross-Validation**: Test model on hold-out data
2. **Bootstrap**: Assess stability of coefficient estimates
3. **Out-of-Sample Prediction**: Evaluate real-world performance
4. **Time Series Split**: For temporal data

### **Business Applications**
1. **Donor Segmentation**: Identify high-value donor segments
2. **Donation Prediction**: Predict donation amounts for new donors
3. **Marketing Prioritization**: Focus efforts on high-impact variables
4. **Model Monitoring**: Track performance over time, retrain as needed

## Common Pitfalls to Avoid

1. **Overfitting**: Too many variables relative to observations
   - Solution: Use stepwise selection, cross-validation, or regularization

2. **Multicollinearity**: Highly correlated predictors
   - Solution: Check VIF, remove correlated variables, use ridge regression

3. **Ignoring Assumptions**: Not checking diagnostic plots
   - Solution: Always examine residuals and diagnostic plots

4. **Extrapolation**: Predicting outside the range of observed data
   - Solution: Only make predictions within observed data range

5. **Causation vs Correlation**: Assuming correlation implies causation
   - Solution: Remember regression shows association, not causation

6. **Data Leakage**: Using information not available at prediction time
   - Solution: Carefully separate training and test data

## References & Further Reading

- **Regression Basics**: James et al. "An Introduction to Statistical Learning"
- **Advanced Topics**: Hastie et al. "The Elements of Statistical Learning"
- **Practical Guide**: Fox "An R Companion to Applied Regression"
- **Diagnostics**: Belsley, Kuh, Welsch "Regression Diagnostics"

## Conda Environment

This analysis uses the `uiapp` conda environment with:
- pandas: Data manipulation
- numpy: Numerical computing
- matplotlib: Visualization
- seaborn: Statistical graphics
- statsmodels: Statistical modeling and tests
- scipy: Scientific computing

To activate: `conda activate uiapp`

---

**Created**: August 29, 2026
**Dataset**: PVA Donors (Prospect Venture Analysis)
**Target Variable**: Donation Amount
**Analysis Type**: Multiple Linear Regression with Stepwise Selection
