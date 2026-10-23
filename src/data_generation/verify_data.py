
from pathlib import Path
import pandas as pd

# Project data folder
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "raw"

# Files we expect to find
files = [
    "customers.csv",
    "restaurants.csv",
    "drivers.csv",
    "orders.csv",
    "deliveries.csv",
    "payments.csv",
    "reviews.csv"
]

print("=" * 55)
print("UBER EATS DATASET VERIFICATION")
print("=" * 55)

for filename in files:
    file_path = DATA_DIR / filename

    if not file_path.exists():
        print(f"\nMISSING: {filename}")
        continue

    df = pd.read_csv(file_path)

    print(f"\nFile: {filename}")
    print(f"Rows: {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]}")
    print("Column names:", list(df.columns))
    print("Duplicate rows:", df.duplicated().sum())
    print("Missing cells:", df.isna().sum().sum())

    print("\nSample records:")
    print(df.head(3).to_string(index=False))

print("\nVerification complete.")
