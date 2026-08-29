# Multiple Regression Analysis - Quick Reference

## Notebook Location
`sas_hackthon/stats_ml/06_multiple_regression.ipynb`

## What's Included

### 📊 **8 Comprehensive Tables**

| Table | Purpose | Key Info |
|-------|---------|----------|
| **Table 1** | Observations Summary | Records read, used, excluded |
| **Table 2** | Class Variables | Categorical variables and levels |
| **Table 3** | Model Dimensions | Number of effects and parameters |
| **Table 4** | Stepwise Selection | Variables added at each step with AIC |
| **Table 5** | Stop Details | Why selection stopped |
| **Table 6** | ANOVA Table | Overall model significance (F-test) |
| **Table 7** | Parameter Estimates | Coefficients, p-values, confidence intervals |
| **Table 8** | Diagnostics | Residuals, leverage, Cook's distance |

### 📈 **4 Visualization Plots**

1. **AIC by Step** - Shows model improvement
2. **Model Complexity** - Number of parameters added
3. **AIC Improvement** - Magnitude of improvement at each step
4. **Summary Statistics** - Final model characteristics

### 🔍 **9 Diagnostic Plots**

1. Residuals vs Fitted Values
2. Q-Q Plot (Normality)
3. Scale-Location Plot (Homoscedasticity)
4. Histogram of Residuals
5. Residuals vs Leverage
6. Cook's Distance
7. Actual vs Predicted
8. Residuals Over Time
9. Autocorrelation Function (ACF)

### ✅ **Statistical Tests**

- Shapiro-Wilk Test (Normality)
- Jarque-Bera Test (Normality)
- Anderson-Darling Test (Normality)
- Breusch-Pagan Test (Heteroscedasticity)
- Variance Inflation Factor (Multicollinearity)

## Key Metrics Explained

### **Model Fit**
- **R²**: Proportion of variation explained (0-1)
- **Adjusted R²**: R² penalized for complexity
- **AIC**: Lower is better (balances fit & complexity)
- **BIC**: Similar to AIC, stronger penalty for complexity
- **RMSE**: Root mean square error (prediction accuracy)

### **Significance**
- **F-statistic**: Tests if model is significant
- **t-statistic**: Tests if coefficient is significant
- **p-value**: Probability of observing by chance
  - p < 0.05: Statistically significant
  - p < 0.01: Highly significant
  - p < 0.001: Very highly significant

### **Assumptions**
- **Linearity**: Relationship is linear
- **Independence**: Observations are independent
- **Homoscedasticity**: Constant variance
- **Normality**: Residuals are normally distributed
- **No Multicollinearity**: Predictors not highly correlated

## How to Interpret Results

### **Coefficient Interpretation**
```
If GiftCnt36 coefficient = 5.2 (p < 0.05):
"For each additional gift in the last 36 months, 
donation amount increases by $5.20 on average"
```

### **Model Fit Interpretation**
```
If R² = 0.65:
"The model explains 65% of the variation in donation amounts"
```

### **Significance Interpretation**
```
If F-statistic p-value < 0.001:
"The model is highly significant - the selected variables 
collectively have a significant effect on donations"
```

## Diagnostic Checklist

- [ ] Residuals vs Fitted: Random scatter around 0?
- [ ] Q-Q Plot: Points close to diagonal line?
- [ ] Scale-Location: Horizontal line with random scatter?
- [ ] Histogram: Bell-shaped, symmetric distribution?
- [ ] Residuals vs Leverage: No extreme points?
- [ ] Cook's Distance: No points above threshold?
- [ ] Actual vs Predicted: Points close to diagonal?
- [ ] Normality Test: p-value > 0.05?
- [ ] Heteroscedasticity Test: p-value > 0.05?
- [ ] VIF: All values < 5?

## Common Issues & Solutions

| Issue | Symptom | Solution |
|-------|---------|----------|
| Non-linearity | Curved pattern in residuals | Add polynomial terms |
| Non-normality | Deviations in Q-Q plot | Transform response variable |
| Heteroscedasticity | Funnel pattern in residuals | Use weighted least squares |
| Multicollinearity | VIF > 10 | Remove correlated variables |
| Outliers | High Cook's distance | Investigate or use robust regression |
| Autocorrelation | Spikes in ACF plot | Add lagged variables |

## Running the Notebook

### **Using Conda Environment**
```bash
conda activate uiapp
jupyter notebook sas_hackthon/stats_ml/06_multiple_regression.ipynb
```

### **Execute Entire Notebook**
```bash
cd sas_hackthon/stats_ml
conda run -n uiapp jupyter nbconvert --to notebook --execute 06_multiple_regression.ipynb
```

## Key Takeaways

1. **Stepwise Selection with AIC** automatically finds optimal variables
2. **Multiple Regression** allows modeling complex relationships
3. **Categorical Encoding** converts non-numeric variables to numeric
4. **Diagnostic Plots** reveal assumption violations
5. **Statistical Tests** confirm model validity
6. **Interpretation** requires understanding both statistics and domain

## Learning Path

1. Start with **Overview** section (markdown cells)
2. Follow **Data Preparation** to understand data cleaning
3. Review **Tables 1-3** for data structure
4. Study **Stepwise Selection** (Tables 4-5) to understand variable selection
5. Examine **Fit Criteria Visualization** to see model improvement
6. Analyze **ANOVA Table** (Table 6) for overall significance
7. Interpret **Parameter Estimates** (Table 7) for individual effects
8. Review **Diagnostic Plots** (Table 8) for assumption checking
9. Read **Recommendations** for next steps

## Resources

- **Notebook**: Complete working example with all outputs
- **Guide**: Detailed explanations (`docs/06_regression_analysis_guide.md`)
- **Quick Reference**: This document (`docs/06_regression_analysis_quick_reference.md`)
- **Complete Reference**: Full documentation (`docs/06_regression_analysis.md`)
- **Images**: All diagnostic and fit criteria plots in `images/` folder

---

**Last Updated**: August 29, 2026
**Environment**: uiapp (conda)
**Status**: ✅ Fully Executed and Tested
**Images Organized**: ✅ All PNG files in dedicated images folder
