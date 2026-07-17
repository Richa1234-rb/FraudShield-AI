import pandas as pd
from pathlib import Path


# Base directory
BASE_DIR = Path(__file__).resolve().parent

# Dataset path
DATASET_PATH = BASE_DIR / "dataset" / "creditcard.csv"

# Output path
OUTPUT_PATH = BASE_DIR / "dataset" / "processed_creditcard.csv"


def preprocess_data():
    print("=" * 50)
    print("Loading dataset...")
    print("=" * 50)

    df = pd.read_csv(DATASET_PATH)

    print(f"Dataset Shape : {df.shape}")
    print()

    # Remove duplicate rows
    before = len(df)
    df.drop_duplicates(inplace=True)
    after = len(df)

    print(f"Removed {before - after} duplicate rows")

    # Check missing values
    print("\nMissing Values:")
    print(df.isnull().sum().sum())

    # Save processed dataset
    df.to_csv(OUTPUT_PATH, index=False)

    print("\nProcessed dataset saved successfully!")
    print(OUTPUT_PATH)

    print("=" * 50)
    print("Preprocessing Completed")
    print("=" * 50)


if __name__ == "__main__":
    preprocess_data()