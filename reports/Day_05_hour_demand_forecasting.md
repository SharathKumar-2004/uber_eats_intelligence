# Day 5: Hourly Demand Forecasting
## Uber Eats Operational & Customer Intelligence System

## 1. Executive Summary

The objective of Day 5 was to analyze hourly order demand and develop time-series forecasting models to predict future order volumes.

The analysis included hourly aggregation, exploratory data analysis (EDA), time-series decomposition, stationarity testing using the Augmented Dickey-Fuller (ADF) test, and forecasting using ARIMA and Prophet.

A seasonal-naive forecasting model was also evaluated as a baseline.

ARIMA achieved the lowest test error among the three evaluated models, with a Mean Absolute Error (MAE) of **0.860** and a Root Mean Squared Error (RMSE) of **1.122**. Prophet produced very similar results, while the seasonal-naive baseline had higher errors.

These results suggest that ARIMA is the strongest candidate among the tested models on this particular test period. Additional validation is recommended before using forecasts for operational decisions.

## 2. Business Context

Food delivery platforms need to understand how order demand changes over time. Forecasting hourly demand can help operations teams plan restaurant preparation capacity, delivery-driver availability, and staffing requirements.

This project investigates historical order demand to understand time-series patterns and evaluate whether forecasting models can predict future hourly order volumes.

The dataset used in this exercise is project data and should not be interpreted as actual Uber Eats operational data.

## 3. Project Objectives

The objectives were to:

- Aggregate order records into hourly demand counts.
- Inspect the dataset for missing timestamps and data-quality issues.
- Explore demand patterns over time, by hour, and by day of the week.
- Decompose the time series into trend, seasonal, and residual components.
- Test stationarity using the ADF test.
- Build ARIMA and Prophet forecasting models.
- Compare model performance using MAE, RMSE, and MAPE.
- Evaluate the models against a seasonal-naive baseline.
- Translate the findings into business recommendations.

## 4. Dataset Overview and Cleaning


### Data preparation

The timestamp column was converted into datetime format to support time-based analysis.

Records with missing or invalid timestamps were excluded from hourly aggregation because they could not be assigned reliably to a time interval.

Duplicate rows were checked. Duplicate records should only be removed after confirming that they are genuine duplicates rather than separate valid orders.

The hourly demand dataset was created by resampling the order records into hourly intervals and counting the available records in each interval.

The resulting dataset contained 4,392 hourly observations, covering 183 days with 24 hours per day.

### Key observation

The average demand was 1.14 orders per hour, with a maximum of 7 orders in an hour. This indicates that the analyzed dataset has relatively low order counts, which is important when interpreting forecasting errors and percentage-based metrics.

## 5. Exploratory Data Analysis

Exploratory data analysis was performed to understand how order demand varied over time.

The analysis included:

- A time-series plot of hourly demand.
- Average demand by hour of the day.
- Average demand by day of the week.
- Inspection of minimum, maximum, and average hourly order counts.

These visualizations help identify potential recurring patterns and changes in demand.

**Observation to complete from the notebook:** Record the specific peak hours, busiest days, or other patterns only after confirming them from the generated plots and summary statistics.

## 6. Time-Series Decomposition

Time-series decomposition was performed using an additive model with a seasonal period of 24 observations.

The decomposition separates the observed series into three components:

### Trend

The trend represents the longer-term direction of demand over time.

### Seasonality

The seasonal component represents patterns that repeat at regular intervals. A period of 24 was used to investigate potential daily patterns in hourly demand.

### Residual

The residual component represents the variation that remains after accounting for the estimated trend and seasonal components.

Decomposition helps explain the structure of the time series and can reveal patterns that may be useful for forecasting.

**Observation to complete:** Describe the actual trend, seasonal, and residual patterns visible in the decomposition plot. No specific pattern should be claimed without inspecting the plot.

## 7. Stationarity Testing Using the ADF Test

The Augmented Dickey-Fuller test was used to investigate whether the original hourly demand series exhibited a unit root.

### ADF test results

| Metric | Value |
|---|---:|
| ADF statistic | -34.3815 |
| p-value as displayed | 0.0 |
| 1% critical value | -3.4318 |
| 5% critical value | -2.8622 |
| 10% critical value | -2.5671 |

The p-value displayed as `0.0` is a rounded numerical output and should not be interpreted as a literal probability of zero.

### Interpretation

The ADF statistic was more negative than the reported critical values, and the p-value was below the 0.05 significance level.

Therefore, the unit-root null hypothesis was rejected. The original hourly demand series appears stationary according to this test.

Stationarity does not imply that demand is constant or that all seasonal patterns are absent. Additional examination of the seasonal and residual components remains important.

## 8. Forecasting Methodology

A chronological train/test split was used instead of randomly shuffling observations. This approach preserves time order and prevents future observations from being used to train a model that predicts the past.

| Dataset portion | Observations |
|---|---:|
| Training set | 3,513 |
| Testing set | 879 |
| Total | 4,392 |

The models were evaluated on the same held-out test period to support a fair comparison.

### 8.1 ARIMA

ARIMA stands for AutoRegressive Integrated Moving Average.

The model used was **ARIMA(1,0,1)**:

- `p = 1`: One autoregressive term.
- `d = 0`: No differencing was applied within the model.
- `q = 1`: One moving-average term.

The original series appeared stationary under the ADF test, so a model with `d = 0` was tested.

### 8.2 Prophet

Prophet is a time-series forecasting model designed to represent trends and recurring seasonal patterns.

The model was configured with daily and weekly seasonality enabled and yearly seasonality disabled.

Yearly seasonality was disabled because the available dataset covered approximately six months rather than a complete annual cycle.

### 8.3 Seasonal-Naive Baseline

A seasonal-naive model was used as a simple benchmark. It predicted each hour using the demand observed 168 hours earlier, corresponding to the same hour one week before.

This baseline helps determine whether the more advanced models improve upon a simple weekly-repeat assumption.

## 9. Model Evaluation Metrics

Three metrics were used to evaluate forecasting accuracy.

### Mean Absolute Error (MAE)

MAE measures the average absolute difference between actual and predicted demand.

A lower MAE indicates smaller average errors. Its unit here is orders per hour.

### Root Mean Squared Error (RMSE)

RMSE measures the square root of the average squared prediction error. It penalizes larger errors more heavily than MAE.

A lower RMSE indicates better performance under this metric.

### Mean Absolute Percentage Error (MAPE)

MAPE measures forecast errors as percentages of actual values.

Because actual demand can be zero, MAPE was calculated only for hours with positive actual demand. This limitation must be considered when interpreting the results.

## 10. Model Comparison

The following results were obtained on the chronological test set.

| Model | MAE | RMSE | MAPE on positive-demand hours |
|---|---:|---:|---:|
| ARIMA(1,0,1) | 0.860 | 1.122 | 31.712% |
| Prophet | 0.866 | 1.124 | 32.126% |
| Seasonal Naive (168-hour lag) | 1.231 | 1.614 | 71.998% |

### Results interpretation

**ARIMA(1,0,1)** achieved the lowest MAE, RMSE, and positive-demand-hour MAPE among the three evaluated models.

**Prophet** produced very similar results. The difference between ARIMA and Prophet was small:

- MAE difference: 0.006 orders per hour.
- RMSE difference: 0.002 orders per hour.
- MAPE difference: 0.414 percentage points.

**The seasonal-naive baseline** had higher errors than both forecasting models on the reported test period.

These results indicate that ARIMA and Prophet performed better than the selected baseline on this test set. However, the small difference between ARIMA and Prophet does not establish that ARIMA will always perform better on future periods.

### Why is MAPE relatively high?

The dataset has low hourly order counts. When actual demand is small, even a small absolute error can represent a large percentage of the actual value.

For example, an error of one order when actual demand is two orders represents a 50% error.

Therefore, MAE and RMSE should be emphasized alongside MAPE when evaluating this dataset.

## 11. ARIMA Model Diagnostics

The fitted ARIMA model reported the following diagnostic values:

| Diagnostic | Result |
|---|---:|
| Constant | 1.1249 |
| AR(1) coefficient p-value | 0.930 |
| MA(1) coefficient p-value | 0.895 |
| AIC | 10509.148 |
| Ljung-Box p-value at lag 1 | 0.99 |

The AR(1) and MA(1) coefficient p-values were high, indicating that these individual coefficients were not statistically significant at conventional significance levels in this fitted model.

The Ljung-Box result at lag 1 did not provide evidence of residual autocorrelation at that particular lag. It does not establish that residual autocorrelation is absent at all lags.

Residual plots and additional diagnostic checks should be reviewed before drawing stronger conclusions about model adequacy.

## 12. Business Interpretation

The forecasting results suggest that the tested ARIMA and Prophet models predicted hourly demand more accurately than the seasonal-naive baseline on the held-out test period.

Potential applications of hourly demand forecasting include:

- Planning restaurant preparation capacity.
- Supporting delivery-driver scheduling.
- Monitoring expected hourly order volume.
- Identifying periods that may require additional operational attention.
- Comparing predicted demand with available capacity.

These are potential applications. The current analysis does not quantify cost savings, improvements in delivery times, or increases in customer satisfaction.



## 13. Conclusion

The Day 5 analysis developed an hourly demand series containing 4,392 continuous observations from April through September 2026.

The ADF test provided evidence against the unit-root null hypothesis for the original series. Three forecasting approaches were compared using a chronological train/test split: ARIMA(1,0,1), Prophet, and a seasonal-naive baseline.

ARIMA achieved a test MAE of 0.860 and RMSE of 1.122, marginally outperforming Prophet and outperforming the seasonal-naive baseline on the reported metrics.

The results demonstrate a structured approach to hourly demand forecasting, including data preparation, stationarity testing, model evaluation, and business interpretation. Further validation and diagnostic checks are recommended before the forecasts are used for operational decisions.
