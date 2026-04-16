import pandas as pd

try:
    # Load dataset
    df = pd.read_csv('data/sample_data.csv')

    # Detect missing values
    print("Missing values before cleaning:\n")
    print(df.isnull().sum())

    # Fill missing numeric values with mean
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    # Save cleaned data
    df.to_csv('data/cleaned_data.csv', index=False)

    # Confirm cleaning
    print("\nMissing values after cleaning:\n")
    print(df.isnull().sum())

    print("\nCleaned data saved to data/cleaned_data.csv")

except FileNotFoundError:
    print("Error: File 'data/sample_data.csv' not found. Check the file path.")
except Exception as e:
    print("An error occurred:", e)