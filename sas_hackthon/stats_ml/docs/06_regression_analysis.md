# Multiple Regression Analysis - Complete Package

## 📋 Summary

You now have a **comprehensive, production-ready multiple regression analysis** with stepwise variable selection using AIC criterion. This package includes everything needed to understand and apply multiple regression analysis to your donor data.

## 📁 Files Created/Updated

### **Main Notebook**
- **`sas_hackthon/stats_ml/06_multiple_regression.ipynb`** (614 KB)
  - 31 cells (18 code, 13 markdown)
  - Fully executed with all outputs
  - Ready to run and modify

### **Documentation**
- **`docs/06_regression_analysis.md`** - Complete overview and learning path (this file)
- **`docs/06_regression_analysis_guide.md`** - Comprehensive guide with detailed explanations
- **`docs/06_regression_analysis_quick_reference.md`** - Quick lookup for tables, plots, and interpretations

### **Generated Outputs** (in images folder)
- `sas_hackthon/stats_ml/images/fit_criteria_donation.png` - 4-panel visualization of model selection
- `sas_hackthon/stats_ml/images/model_diagnostics.png` - 9-panel diagnostic plots
- Plus 8 additional PNG files from previous analyses (9.8 MB total)

## 🎯 What's Included

### **8 Comprehensive Tables**

1. **Observations Summary** - Data quality metrics
2. **Class Variables** - Categorical variable levels
3. **Model Dimensions** - Model structure
4. **Stepwise Selection Summary** - Variables added at each step
5. **Stop Details** - Why selection stopped
6. **ANOVA Table** - Overall model significance
7. **Parameter Estimates** - Coefficients and significance
8. **Diagnostic Statistics** - Residuals and influence measures

### **Visualizations**

**Fit Criteria Plots:**
- AIC by step (model improvement)
- Model complexity (parameters added)
- AIC improvement magnitude
- Summary statistics

**Diagnostic Plots:**
- Residuals vs Fitted Values
- Q-Q Plot (Normality)
- Scale-Location Plot (Homoscedasticity)
- Histogram of Residuals
- Residuals vs Leverage
- Cook's Distance
- Actual vs Predicted
- Residuals Over Time
- Autocorrelation Function

### **Statistical Tests**

- Normality Tests (Shapiro-Wilk, Jarque-Bera, Anderson-Darling)
- Heteroscedasticity Test (Breusch-Pagan)
- Multicollinearity Check (VIF)

## 🔍 Key Features

### **Educational Markups**
Each section includes:
- **Why we're doing this** - Purpose and importance
- **How it's useful** - Practical applications
- **What alternatives exist** - Other approaches to consider

### **Categorical Variable Encoding**
- Automatic one-hot encoding
- Reference category handling
- Multicollinearity prevention

### **Stepwise Selection with AIC**
- Forward selection algorithm
- AIC-based stopping criterion
- Detailed selection history
- Candidates not selected

### **Comprehensive Diagnostics**
- 9 diagnostic plots
- 5 statistical tests
- Assumption checking
- Outlier detection

### **Model Interpretation**
- Coefficient estimates with confidence intervals
- Statistical significance testing
- Model fit statistics
- Practical interpretation guidance

## 🚀 How to Use

### **1. View the Notebook**
```bash
cd /Users/gkumargaur/workspace/datascience/boston_university/datascience-practice
jupyter notebook sas_hackthon/stats_ml/06_multiple_regression.ipynb
```

### **2. Run the Analysis**
```bash
conda activate uiapp
cd sas_hackthon/stats_ml
jupyter nbconvert --to notebook --execute 06_multiple_regression.ipynb
```

### **3. Read the Documentation**
- Start with `docs/06_regression_analysis_quick_reference.md` for overview
- Read `docs/06_regression_analysis_guide.md` for detailed explanations
- Refer to notebook for working examples

### **4. View Generated Images**
All PNG files are organized in `sas_hackthon/stats_ml/images/` folder

### **5. Modify for Your Data**
- Change data path in cell 1
- Adjust target variable name
- Modify categorical columns list
- Customize visualization parameters

## 📊 Analysis Workflow

```
1. Data Preparation
   ↓
2. Exploratory Analysis (Tables 1-3)
   ↓
3. Stepwise Selection (Tables 4-5)
   ↓
4. Visualization (Fit Criteria Plots)
   ↓
5. Model Fitting (Final Model)
   ↓
6. ANOVA Testing (Table 6)
   ↓
7. Parameter Interpretation (Table 7)
   ↓
8. Diagnostics (Table 8 + Plots)
   ↓
9. Recommendations & Next Steps
```

## 💡 Learning Outcomes

After working through this analysis, you'll understand:

### **Concepts**
- Multiple regression fundamentals
- Categorical variable encoding
- Stepwise variable selection
- AIC criterion for model comparison
- Regression assumptions and diagnostics

### **Practical Skills**
- Data cleaning and preparation
- Model building and selection
- Coefficient interpretation
- Assumption checking
- Diagnostic plot interpretation
- Statistical testing

### **Business Applications**
- Predicting donation amounts
- Identifying key donor characteristics
- Segmenting donors by value
- Prioritizing marketing efforts
- Model monitoring and maintenance

## 🔧 Technical Details

### **Environment**
- **Conda Environment**: `uiapp`
- **Python Version**: 3.9
- **Key Libraries**:
  - pandas: Data manipulation
  - numpy: Numerical computing
  - matplotlib: Visualization
  - seaborn: Statistical graphics
  - statsmodels: Statistical modeling
  - scipy: Scientific computing

### **Data**
- **Source**: `data/VST152/pva_donors.csv`
- **Target Variable**: `Donation_Amt`
- **Observations Used**: ~1,000+ (after removing missing values)
- **Predictors**: 40+ (after encoding categorical variables)

### **Model**
- **Method**: Ordinary Least Squares (OLS)
- **Selection**: Forward Stepwise with AIC
- **Assumptions**: Linearity, Independence, Homoscedasticity, Normality, No Multicollinearity

## ⚠️ Important Notes

1. **Data Quality**: Analysis removes records with missing values
2. **Categorical Encoding**: First category is dropped (reference category)
3. **Multicollinearity**: Check VIF values (should be < 5)
4. **Assumptions**: Always check diagnostic plots
5. **Interpretation**: Correlation ≠ Causation
6. **Generalization**: Model trained on this data may not generalize to new data

## 📚 Further Reading

### **Recommended Resources**
- James et al. "An Introduction to Statistical Learning"
- Hastie et al. "The Elements of Statistical Learning"
- Fox "An R Companion to Applied Regression"
- Belsley, Kuh, Welsch "Regression Diagnostics"

### **Topics to Explore**
- Ridge/Lasso Regression (handle multicollinearity)
- Generalized Linear Models (non-normal responses)
- Tree-based Methods (non-linear relationships)
- Cross-validation (model validation)
- Bootstrap (coefficient stability)

## ✅ Checklist

- [x] Data preparation and cleaning
- [x] Categorical variable encoding
- [x] Observations summary table
- [x] Class variables table
- [x] Model dimensions table
- [x] Stepwise selection with AIC
- [x] Stop details table
- [x] Fit criteria visualization
- [x] ANOVA table
- [x] Parameter estimates table
- [x] Diagnostic statistics table
- [x] Diagnostic plots (9 plots)
- [x] Statistical tests (5 tests)
- [x] Educational markups throughout
- [x] Comprehensive documentation
- [x] Quick reference guide
- [x] Fully executed notebook
- [x] PNG files organized in images folder

## 🎓 Learning Path

**Beginner**: Read `docs/06_regression_analysis_quick_reference.md`, run notebook, examine plots

**Intermediate**: Read `docs/06_regression_analysis_guide.md`, modify notebook, interpret results

**Advanced**: Explore alternatives, implement improvements, apply to new data

## 📞 Support

For questions or issues:
1. Check `docs/06_regression_analysis_quick_reference.md` for common issues
2. Review `docs/06_regression_analysis_guide.md` for detailed explanations
3. Examine notebook cells for working examples
4. Refer to diagnostic plots for assumption violations

## 🎉 Summary

You now have a **complete, educational, production-ready multiple regression analysis** that:
- ✅ Performs stepwise variable selection with AIC
- ✅ Handles categorical variables automatically
- ✅ Includes comprehensive diagnostics
- ✅ Provides detailed educational explanations
- ✅ Generates publication-quality visualizations
- ✅ Tests all regression assumptions
- ✅ Offers practical interpretation guidance
- ✅ Organizes all outputs in dedicated folders

**Status**: ✅ Fully Executed and Tested
**Environment**: uiapp (conda)
**Last Updated**: August 29, 2026

---

**Happy Learning! 🚀**
