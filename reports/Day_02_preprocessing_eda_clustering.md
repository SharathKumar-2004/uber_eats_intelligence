# Uber Eats Operational & Customer Intelligence System

## Day 02: Data Preprocessing, Exploratory Data Analysis & Segmentation

**Status:** Preprocessing/EDA and customer/restaurant clustering were
reported as completed in the project workflow. Insert exact findings and
metrics from the notebook before submission.

------------------------------------------------------------------------

## 1. Day 02 Objectives

-   Inspect the generated datasets and understand their structure.
-   Clean and prepare data for analysis.
-   Perform exploratory data analysis (EDA).
-   Create useful features for customer and restaurant analysis.
-   Explore customer and restaurant segmentation using clustering.
-   Interpret results in business language.

## 2. Dataset Overview

The project includes these datasets:

-   `customers.csv`
-   `restaurants.csv`
-   `orders.csv`
-   `deliveries.csv`
-   `drivers.csv`
-   `reviews.csv`
-   `payments.csv`

Verify actual row counts, columns, key fields, and data types from the
current files. Do not assume that all datasets have identical row counts
or that every join is one-to-one.

## 3. Data Preprocessing

Typical preparation checks for this workflow include:

-   Inspecting shape, columns, data types, and sample records.
-   Checking missing values and duplicate rows.
-   Checking whether numeric values are plausible.
-   Reviewing category labels for inconsistent spelling or casing.
-   Validating key columns before joining datasets.
-   Choosing appropriate handling for missing values and categorical
    variables.
-   Avoiding the use of target or post-outcome information in features.


## 4. Exploratory Data Analysis (EDA)

EDA helps understand distributions, relationships, and possible
data-quality issues before modelling.

Include only visualizations actually generated in the notebook, for
example:

-   Numeric feature distributions
-   Category counts
-   Correlation heatmaps where appropriate
-   Order or customer behaviour summaries
-   Restaurant-level comparisons


## 5. Customer Segmentation

Customer clustering groups customers with similar patterns in the
selected features. The project explored **K-Means** and **DBSCAN** as
clustering approaches.

-   **K-Means:** assigns records to a chosen number of clusters based on
    distance to cluster centers.
-   **DBSCAN:** groups dense regions and can label isolated observations
    as noise.
-   **Feature scaling:** important when clustering features have
    different units or ranges.
-   **PCA:** if used, can project features into fewer dimensions for
    visualization; it does not automatically make clusters meaningful.
-   **Silhouette score:** one metric for assessing separation and
    cohesion; interpret it alongside cluster sizes and business
    usefulness.


## 6. Restaurant Segmentation

Restaurant clustering applies similar ideas to restaurant-level
features, with the goal of identifying groups that may have different
operational or business characteristics.


## 7. Business Value

When supported by the results, segmentation may help the business:

-   Understand different customer behaviour patterns.
-   Identify groups that may respond differently to engagement
    strategies.
-   Compare restaurant profiles and operational characteristics.
-   Guide further investigation and targeted experiments.

Clusters are exploratory groupings, not definitive customer types.
Validate their stability and usefulness before taking business action.



## 8. Conclusion

Day 02 focused on preparing the project datasets, exploring their
characteristics, and using clustering to investigate customer and
restaurant segments. The final report should include the actual
preprocessing decisions, feature lists, cluster settings, evaluation
metrics, and observations from the notebook. These details are necessary
to make the analysis reproducible and the business interpretation
credible.

