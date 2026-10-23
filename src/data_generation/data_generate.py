
from pathlib import Path

import numpy as np
import pandas as pd

# --------------------------------------------------
# 1. SETTINGS
# --------------------------------------------------

np.random.seed(42)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = PROJECT_ROOT / "data" / "raw"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

N_CUSTOMERS = 500
N_RESTAURANTS = 50
N_DRIVERS = 100
N_ORDERS = 5000

cities = ["Bengaluru", "Hyderabad", "Mumbai", "Delhi", "Pune"]

cuisines = [
    "Indian", "Chinese", "Italian", "Fast Food",
    "South Indian", "Biryani", "Desserts", "Healthy"
]

# --------------------------------------------------
# 2. CUSTOMERS
# --------------------------------------------------

customers = pd.DataFrame({
    "customer_id": [
        f"C{i:04d}" for i in range(1, N_CUSTOMERS + 1)
    ],
    "age": np.random.randint(18, 61, N_CUSTOMERS),
    "gender": np.random.choice(
        ["Male", "Female", "Other"], N_CUSTOMERS,
        p=[0.48, 0.48, 0.04]
    ),
    "city": np.random.choice(cities, N_CUSTOMERS),
    "membership_type": np.random.choice(
        ["Regular", "Silver", "Gold"], N_CUSTOMERS,
        p=[0.60, 0.25, 0.15]
    ),
    "signup_date": pd.to_datetime(
        np.random.choice(
            pd.date_range("2025-01-01", "2026-03-31"),
            N_CUSTOMERS
        )
    )
})

# --------------------------------------------------
# 3. RESTAURANTS
# --------------------------------------------------

restaurants = pd.DataFrame({
    "restaurant_id": [
        f"R{i:03d}" for i in range(1, N_RESTAURANTS + 1)
    ],
    "city": np.random.choice(cities, N_RESTAURANTS),
    "cuisine": np.random.choice(cuisines, N_RESTAURANTS),
    "restaurant_rating": np.round(
        np.random.uniform(2.8, 5.0, N_RESTAURANTS), 1
    ),
    "average_prep_time_minutes": np.random.randint(
        10, 41, N_RESTAURANTS
    ),
    "price_level": np.random.choice(
        ["Budget", "Moderate", "Premium"], N_RESTAURANTS
    )
})

# --------------------------------------------------
# 4. DRIVERS
# --------------------------------------------------

drivers = pd.DataFrame({
    "driver_id": [
        f"D{i:04d}" for i in range(1, N_DRIVERS + 1)
    ],
    "city": np.random.choice(cities, N_DRIVERS),
    "vehicle_type": np.random.choice(
        ["Bike", "Scooter", "Motorcycle"], N_DRIVERS
    ),
    "experience_months": np.random.randint(
        1, 61, N_DRIVERS
    ),
    "driver_rating": np.round(
        np.random.uniform(3.0, 5.0, N_DRIVERS), 1
    )
})

# --------------------------------------------------
# 5. ORDERS
# --------------------------------------------------

order_dates = (
    pd.Timestamp("2026-04-01")
    + pd.to_timedelta(
        np.random.randint(0, 183 * 24 * 60, N_ORDERS),
        unit="m"
    )
)

orders = pd.DataFrame({
    "order_id": [
        f"O{i:06d}" for i in range(1, N_ORDERS + 1)
    ],
    "customer_id": np.random.choice(
        customers["customer_id"], N_ORDERS
    ),
    "restaurant_id": np.random.choice(
        restaurants["restaurant_id"], N_ORDERS
    ),
    "order_timestamp": order_dates,
    "item_count": np.random.randint(1, 9, N_ORDERS),
    "order_status": np.random.choice(
        ["Delivered", "Cancelled", "Failed"],
        N_ORDERS,
        p=[0.88, 0.09, 0.03]
    )
})

orders["order_amount"] = np.round(
    orders["item_count"] * np.random.uniform(100, 250, N_ORDERS),
    2
)

orders["discount"] = np.round(
    orders["order_amount"]
    * np.random.choice([0, 0.05, 0.10, 0.15], N_ORDERS),
    2
)

orders["delivery_fee"] = np.random.choice(
    [20, 30, 40, 50], N_ORDERS
)

orders["tax"] = np.round(
    orders["order_amount"] * 0.05, 2
)

orders["total_amount"] = np.round(
    orders["order_amount"]
    - orders["discount"]
    + orders["delivery_fee"]
    + orders["tax"],
    2
)

orders["hour"] = orders["order_timestamp"].dt.hour
orders["day_of_week"] = orders["order_timestamp"].dt.day_name()
orders["is_weekend"] = (
    orders["order_timestamp"].dt.dayofweek >= 5
)

# --------------------------------------------------
# 6. DELIVERIES
# --------------------------------------------------

delivered_orders = orders.loc[
    orders["order_status"] == "Delivered",
    ["order_id", "restaurant_id"]
].copy()

deliveries = delivered_orders[["order_id"]].copy()

deliveries["driver_id"] = np.random.choice(
    drivers["driver_id"], len(deliveries)
)

deliveries["distance_km"] = np.round(
    np.random.uniform(1, 15, len(deliveries)), 2
)

deliveries["weather"] = np.random.choice(
    ["Clear", "Rain", "Cloudy"], len(deliveries),
    p=[0.65, 0.15, 0.20]
)

deliveries["traffic"] = np.random.choice(
    ["Low", "Medium", "High"], len(deliveries),
    p=[0.30, 0.45, 0.25]
)

deliveries = deliveries.merge(
    delivered_orders, on="order_id", how="left"
)

deliveries = deliveries.merge(
    restaurants[
        ["restaurant_id", "average_prep_time_minutes"]
    ],
    on="restaurant_id",
    how="left",
    validate="many_to_one"
)

traffic_delay = deliveries["traffic"].map({
    "Low": 2, "Medium": 8, "High": 18
})

weather_delay = deliveries["weather"].map({
    "Clear": 0, "Cloudy": 3, "Rain": 12
})

deliveries["prep_time_minutes"] = (
    deliveries["average_prep_time_minutes"]
    + np.random.normal(0, 3, len(deliveries))
).round().clip(lower=5).astype(int)

deliveries["delivery_time_minutes"] = (
    deliveries["prep_time_minutes"]
    + deliveries["distance_km"] * 3
    + traffic_delay
    + weather_delay
    + np.random.normal(0, 4, len(deliveries))
).round().clip(lower=10).astype(int)

deliveries = deliveries.drop(
    columns=["restaurant_id", "average_prep_time_minutes"]
)

# --------------------------------------------------
# 7. PAYMENTS
# --------------------------------------------------

payments = orders[["order_id", "total_amount", "order_status"]].copy()

payments["payment_method"] = np.random.choice(
    ["UPI", "Credit Card", "Debit Card", "Cash", "Wallet"],
    len(payments)
)

payments["tip_amount"] = np.where(
    payments["order_status"] == "Delivered",
    np.round(
        payments["total_amount"]
        * np.random.choice([0, 0.02, 0.05, 0.10], len(payments)),
        2
    ),
    0
)

payments["payment_amount"] = np.where(
    payments["order_status"] == "Delivered",
    payments["total_amount"] + payments["tip_amount"],
    0
)

payments["payment_status"] = np.select(
    [
        payments["order_status"] == "Delivered",
        payments["order_status"] == "Cancelled"
    ],
    ["Successful", "Refunded"],
    default="Failed"
)

payments = payments.rename(
    columns={"total_amount": "order_total"}
).drop(columns=["order_status"])

# --------------------------------------------------
# 8. REVIEWS
# --------------------------------------------------

review_pool = orders.loc[
    orders["order_status"] == "Delivered",
    ["order_id", "customer_id"]
]

review_pool = review_pool.sample(
    frac=0.45, random_state=42
).reset_index(drop=True)

review_pool["review_id"] = [
    f"REV{i:05d}" for i in range(1, len(review_pool) + 1)
]

review_pool["rating"] = np.random.choice(
    [1, 2, 3, 4, 5],
    len(review_pool),
    p=[0.05, 0.08, 0.15, 0.30, 0.42]
)

review_text = {
    1: [
        "Very late delivery and cold food",
        "Terrible experience",
        "Food arrived damaged"
    ],
    2: [
        "Delivery was slow",
        "Food quality was disappointing",
        "Could be much better"
    ],
    3: [
        "Average experience",
        "Food was okay",
        "Nothing special"
    ],
    4: [
        "Good food and quick delivery",
        "Nice experience",
        "Would order again"
    ],
    5: [
        "Excellent food and service",
        "Amazing experience",
        "Fast delivery and delicious food"
    ]
}

review_pool["review_text"] = [
    np.random.choice(review_text[rating])
    for rating in review_pool["rating"]
]

review_pool["review_timestamp"] = (
    pd.to_datetime(
        np.random.choice(
            pd.date_range("2026-04-01", "2026-09-30"),
            len(review_pool)
        )
    )
)

reviews = review_pool[
    [
        "review_id", "order_id", "customer_id",
        "rating", "review_text", "review_timestamp"
    ]
].copy()

# --------------------------------------------------
# 9. SAVE CSV FILES
# --------------------------------------------------

datasets = {
    "customers.csv": customers,
    "restaurants.csv": restaurants,
    "drivers.csv": drivers,
    "orders.csv": orders,
    "deliveries.csv": deliveries,
    "payments.csv": payments,
    "reviews.csv": reviews
}

for filename, dataframe in datasets.items():
    dataframe.to_csv(OUTPUT_DIR / filename, index=False)
    print(f"Created {filename}: {len(dataframe):,} rows")

# --------------------------------------------------
# 10. BASIC DATA QUALITY CHECKS
# --------------------------------------------------

print("\n--- DATA QUALITY CHECKS ---")

for filename, dataframe in datasets.items():
    print(f"\n{filename}")
    print("Duplicate rows:", dataframe.duplicated().sum())
    print("Missing cells:", dataframe.isna().sum().sum())

assert customers["customer_id"].is_unique
assert restaurants["restaurant_id"].is_unique
assert drivers["driver_id"].is_unique
assert orders["order_id"].is_unique
assert deliveries["order_id"].is_unique
assert payments["order_id"].is_unique
assert reviews["review_id"].is_unique

assert orders["customer_id"].isin(
    customers["customer_id"]
).all()

assert orders["restaurant_id"].isin(
    restaurants["restaurant_id"]
).all()

assert deliveries["order_id"].isin(
    orders.loc[
        orders["order_status"] == "Delivered", "order_id"
    ]
).all()

assert payments["order_id"].isin(orders["order_id"]).all()

assert reviews["order_id"].isin(
    orders.loc[
        orders["order_status"] == "Delivered", "order_id"
    ]
).all()

print("\nAll data-quality assertions passed!")
print("CSV files saved in:", OUTPUT_DIR)
