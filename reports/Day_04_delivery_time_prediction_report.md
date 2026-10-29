# Uber Eats Operational & Customer Intelligence System

## Day 4: Delivery-Time Prediction

**Analysis:** Delivery-time prediction using regression models\
**Status:** Model comparison completed; add the actual residual and
feature-analysis findings from the notebook before final submission.

## 1. Executive Summary

This analysis compares a mean-prediction baseline, Ridge Regression,
Lasso Regression, and Random Forest to estimate delivery time in
minutes.

On the current held-out test set, **Ridge Regression performed best**
among the tested models, with MAE of 3.232 minutes, RMSE of 4.114
minutes, and R² of 0.944. Five-fold cross-validation also favored Ridge
Regression, with CV MAE of 3.241 minutes, CV RMSE of 4.055 minutes, and
CV R² of 0.945.

These results are promising for this dataset, but they should not be
treated as guaranteed real-world performance until feature timing,
synthetic-data patterns, and possible data leakage have been checked.

## 2. Business Problem

Delivery-time estimates can help a food-delivery platform set customer
expectations, support operational planning, and identify orders that may
need attention.

**Business question:** Can order, preparation, traffic, weather, and
distance information be used to estimate delivery time?

## 3. Dataset and Preparation

The merged modelling dataset contained **4,410 rows and 34 columns**
before selecting model features. The target variable was
`delivery_time_minutes`, observed at approximately 10--114 minutes, with
a mean near 59.8 minutes in the initial inspection.

Model inputs used: - Numeric: `distance_km`, `prep_time_minutes`,
`item_count`, `order_amount` - Categorical: `weather`, `traffic`

The workflow used a train/test split, numeric imputation and scaling,
categorical imputation and one-hot encoding, and regression pipelines.

**Validation note:** Confirm that every feature would be available at
the intended prediction time. In particular, `prep_time_minutes` must be
known or estimated at that point. Avoid information that becomes
available only after delivery has progressed or completed.

## 4. Models Compared

1.  **Baseline (Dummy Regression):** predicts the training-set average
    target value.
2.  **Ridge Regression:** linear regression with L2 regularization.
3.  **Lasso Regression:** linear regression with L1 regularization,
    which can shrink some coefficients to zero.
4.  **Random Forest Regression:** combines decision trees to model
    nonlinear relationships.

## 5. Test-Set Results

  Model                MAE (minutes)   RMSE (minutes)                    R²
  ------------------ --------------- ---------------- ---------------------
  Ridge Regression         **3.232**        **4.114**             **0.944**
  Lasso Regression             3.240            4.124                 0.943
  Random Forest                3.600            4.562                 0.931
  Baseline                    14.033           17.307   approximately 0.000

-   **MAE:** average absolute prediction error; lower is better.
-   **RMSE:** penalizes large errors more strongly; lower is better.
-   **R²:** measures variation explained relative to a mean-based
    reference; higher is generally better. It is not the percentage of
    predictions that are exactly correct.

Ridge reduced test MAE by approximately 77% compared with the baseline
on this test split.

## 6. Cross-Validation Results

  Model                   CV MAE     CV RMSE    CV R²
  ------------------ ----------- ----------- --------
  Ridge Regression     **3.241**   **4.055**    0.945
  Lasso Regression         3.257       4.075    0.944
  Random Forest            3.706       4.658    0.927
  Baseline                14.101      17.267   -0.002

Ridge had the lowest average CV MAE and RMSE in the reported comparison.
Its CV scores were close to the test scores, which is encouraging
evidence of consistency across these splits.

## 7. Random Forest Overfitting Check

  Metric            Training    Test
  --------------- ---------- -------
  MAE (minutes)         1.84    3.60
  R²                   0.981   0.931

Random Forest performed better on training data than on test data. This
gap suggests some overfitting, although test performance remained
strong. It did not outperform Ridge or Lasso in this experiment.

## 8. Visual Analysis

Include the actual notebook plots and explain them based on observed
evidence:

-   **Actual vs. predicted:** points close to the diagonal indicate
    predictions close to actual delivery times.
-   **Ridge coefficient plot:** positive coefficients are associated
    with higher predictions and negative coefficients with lower
    predictions, holding other model inputs constant. Scaling and
    one-hot encoding affect comparisons.
-   **Residual plot:** residual = actual − predicted. Positive residuals
    mean underprediction; negative residuals mean overprediction.
-   **Residual distribution:** check whether errors are centered around
    zero and whether there are extreme errors or patterns.



## 9. Business Recommendations

1.  **Use Ridge as the current candidate model** for further validation
    because it performed best on the reported test and cross-validation
    metrics.
2.  Consider using predictions to support customer-facing ETA estimates
    only after realistic operational validation.
3.  Monitor errors by traffic, weather, distance, and preparation time
    to identify segments where estimates are less reliable.
4.  Review large residuals to understand cases with substantial
    underprediction or overprediction.
5.  Keep a simple baseline so model complexity must demonstrate
    measurable improvement.



## 10. Conclusion

Among the models tested on the current dataset, **Ridge Regression is
the preferred candidate**. It achieved test MAE of 3.232 minutes, RMSE
of 4.114 minutes, and R² of 0.944, and it also performed best on
reported cross-validation MAE and RMSE. Lasso was close behind, while
Random Forest did not outperform the linear models.

The findings are promising, but the model should be described as a
candidate for further validation rather than deployment-ready. Feature
timing, leakage, and generalization to real delivery operations must be
checked first.

