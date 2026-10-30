# Uber Eats Operational & Customer Intelligence System

## 1. Project Overview

The **Uber Eats Operational & Customer Intelligence System** is an end-to-end data analytics and machine learning project designed to understand customer behaviour, evaluate restaurant performance, analyse customer sentiment, predict delivery times and forecast order demand.

The project uses synthetic datasets to demonstrate how machine learning can support operational decisions and improve customer experience in a food delivery platform.

### Business Objectives

- Identify valuable customer segments and understand their ordering behaviour.
- Group restaurants based on operational performance.
- Analyse customer reviews and identify dissatisfaction patterns.
- Predict food delivery time using machine learning.
- Forecast hourly order demand.
- Convert analytical findings into actionable business recommendations.

## 2. Dataset Overview

The project uses synthetically generated datasets representing:

| Dataset | Description |
|---|---|
| customers.csv | Customer details and customer-related information |
| restaurants.csv | Restaurant information and operational attributes |
| orders.csv | Order details, order values and timestamps |
| deliveries.csv | Delivery information, delivery duration and related factors |
| reviews.csv | Customer ratings, review text and sentiment-related information |

### Dataset Scale

- 5,000 orders
- 500 customers
- 50 restaurants
- 100 drivers
- 5 cities
- Six months of order history

**Note:** These are synthetic datasets created for learning and demonstration. They do not represent actual Uber Eats operational data.

## 3. Project Workflow

The project follows an end-to-end machine learning workflow:

1. Synthetic data generation
2. Data loading and cleaning
3. Exploratory Data Analysis (EDA)
4. Feature engineering
5. Customer and restaurant segmentation
6. Review sentiment classification
7. Delivery-time prediction
8. Demand forecasting
9. Model evaluation and comparison
10. Business insights and recommendations

## 4. Machine Learning Implementation

### A. Customer and Restaurant Segmentation

**Objective:** Identify groups of customers and restaurants with similar behavioural and operational characteristics.

**Algorithms implemented:**
- K-Means Clustering
- DBSCAN Clustering
- Principal Component Analysis (PCA)

**Customer features include:**
- Total orders
- Average order value
- Total spending
- Ordering frequency
- Average rating
- Weekend orders
- Late-night orders

**Restaurant features include:**
- Total orders
- Revenue
- Average rating
- Average preparation time
- Cancellation rate
- Average delivery time

PCA is used to reduce the feature dimensions to two principal components for visualizing the clusters.

**Reported results:**
- Customer segmentation: 4 K-Means groups, with a separation score of 0.16.
- Restaurant segmentation: 3 K-Means groups, with a separation score of 0.26.

The customer clusters overlap, so they should be interpreted as behavioural tendencies rather than strict customer categories.

### B. Customer Sentiment Analysis

**Objective:** Analyse customer reviews and identify positive, negative and neutral sentiment.

**Implementation steps:**
1. Text preprocessing and cleaning.
2. Sentiment label preparation.
3. Text vectorization using TF-IDF.
4. Sentiment classification using Naive Bayes and a second classification model.
5. Model evaluation using classification metrics and a confusion matrix.

The final model names and scores should match the models actually executed in the final notebook. The executive report compares Naive Bayes and Linear SVM.

**Important limitation:** The sentiment scores are inflated because the synthetic reviews contain repeated phrases and sentiment labels are derived from star ratings.

### C. Delivery-Time Prediction

**Objective:** Predict delivery duration using order and operational information.

**Target variable:** `delivery_time_minutes`

**Features include:**
- Distance
- Restaurant preparation time
- Item count
- Order amount
- Weather conditions
- Traffic conditions

**Models implemented:**
- Ridge Regression
- Lasso Regression
- Random Forest Regressor
- Average-only baseline

**Reported model comparison:**

| Model | MAE (minutes) | RMSE (minutes) | R² |
|---|---:|---:|---:|
| Ridge Regression | 3.23 | 4.11 | 0.944 |
| Lasso Regression | 3.24 | 4.12 | 0.943 |
| Random Forest | 3.60 | 4.56 | 0.931 |
| Average baseline | 14.03 | 17.31 | 0.000 |

**Selected model:** Ridge Regression.

Ridge achieved the best reported performance and offers a relatively simple, interpretable approach.

### D. Hourly Demand Forecasting

**Objective:** Understand and forecast order demand over time.

**Forecasting workflow:**
1. Convert order timestamps into hourly demand.
2. Resample the data into hourly frequency.
3. Visualize demand trends.
4. Perform time-series decomposition.
5. Test stationarity using the Augmented Dickey-Fuller (ADF) test.
6. Train and evaluate forecasting models.
7. Compare forecasts against actual demand.

**Models explored in the project:**
- ARIMA
- Prophet
- Seasonal Naive baseline

The executive report's documented comparison selects a flat-average forecast over repeating the previous week's demand.

| Forecast approach | MAE (orders/hour) |
|---|---:|
| Flat average | 0.86 |
| Repeat previous week | 1.23 |

The report concludes that hourly and weekday differences are not sufficiently reliable to support fixed time-based staffing decisions.

Use the actual notebook results when documenting the final ARIMA and Prophet scores.

## 5. Key Business Insights

### Customer Insights

- Premium Frequent Diners contribute 41% of delivered order value.
- Weekend High-Ticket customers contribute 22% of order value but have a negative-review rate of 29%.
- Weekend High-Ticket customers have the lowest average rating among the customer segments.

### Restaurant Insights

- High-Demand Slow-Preparation restaurants handle 42% of orders.
- Their average delivery time is approximately 68 minutes.
- Around 68% of their orders take more than one hour.

### Customer Experience Insights

- Slow or late delivery accounts for 35% of negative-review themes.
- Food quality issues account for 28%.
- The remaining 37% are general or unspecified complaints.

### Delivery Insights

- Each additional kilometre adds approximately 3 minutes to delivery time.
- Each additional minute of kitchen preparation adds approximately 1 minute.
- Heavy traffic adds approximately 16 minutes.
- Rain adds approximately 12 minutes.

### Demand Insights

- Average demand is approximately 1.1 orders per hour.
- Delhi and Mumbai account for 53% of order volume.
- No statistically reliable hourly or weekday demand peak was identified in the analysis.

## 6. Business Recommendations

1. Introduce a retention programme for Weekend High-Ticket customers.
2. Set preparation-time improvement targets for slow-preparation restaurants.
3. Deploy additional delivery capacity during rain and heavy traffic.
4. Improve dispatch allocation for long-distance orders.
5. Introduce food-quality improvement plans for lower-rated restaurants.
6. Use delivery-time predictions to provide more realistic estimated arrival times.
7. Prioritize operational monitoring in Delhi and Mumbai and investigate delays in Pune.
8. Investigate cancelled and failed orders to identify recoverable order value.

## 7. Model Limitations

- The project uses synthetic rather than real marketplace data.
- The customer segments have overlapping characteristics.
- The sentiment dataset contains repeated review phrases, which can inflate model performance.
- Six months of historical data is insufficient to establish annual seasonality.
- Hourly demand is relatively low, making precise short-term forecasts difficult.
- The delivery model does not include live traffic, rider availability or restaurant queue information.
- The analysis identifies patterns and associations, not proven causal relationships.

## 8. Future Scope

- Integrate real operational data.
- Add live traffic, weather and rider availability.
- Improve sentiment analysis using more varied, real-world review text.
- Develop customer churn and lifetime-value prediction models.
- Forecast demand by city and delivery zone.
- Include festivals, holidays and promotional campaigns.
- Automate model retraining and performance monitoring.
- Conduct controlled business experiments to measure the impact of recommendations.

## 9. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Statsmodels
- Prophet
- Jupyter Notebook
- Git and GitHub

## 10. Running the Project

Clone the repository:

```bash
git clone https://github.com/SharathKumar-2004/uber_eats_intelligence.git
cd uber_eats_intelligence
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open the notebooks in the `notebooks/` directory and execute the project workflow.

Ensure the required CSV files are available in `data/raw/` before running the notebooks.

