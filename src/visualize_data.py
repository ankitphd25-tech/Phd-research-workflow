import os
import pandas as pd
import matplotlib.pyplot as plt

# ----- Paths -----
data_path = "data/cleaned_data.csv"
output_dir = "results"

# Create results directory if not exists
os.makedirs(output_dir, exist_ok=True)

# ----- Load Data -----
df = pd.read_csv(data_path)

# ----- Basic Check -----
print("Dataset shape:", df.shape)
print("Columns:", df.columns.tolist())

# ----- Plot 1: Histogram (first numeric column) -----
numeric_cols = df.select_dtypes(include=['number']).columns

if len(numeric_cols) > 0:
    col = numeric_cols[0]
    
    plt.figure()
    df[col].hist()
    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    
    plt.savefig(f"{output_dir}/histogram_{col}.png")
    plt.close()

# ----- Plot 2: Scatter Plot (first two numeric columns) -----
if len(numeric_cols) >= 2:
    col1, col2 = numeric_cols[:2]
    
    plt.figure()
    plt.scatter(df[col1], df[col2])
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.title(f"{col1} vs {col2}")
    
    plt.savefig(f"{output_dir}/scatter_{col1}_vs_{col2}.png")
    plt.close()

print("Plots saved in 'results/' folder.")