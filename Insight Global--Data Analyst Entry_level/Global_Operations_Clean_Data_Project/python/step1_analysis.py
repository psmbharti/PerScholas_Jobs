# 1 Analysis Code

import pandas as pd


# ==========================================
# 1. Load Operational Dataset
# ==========================================

df = pd.read_csv(r"data\raw\operational_data_dirty.csv")

print("========== DATASET LOADED ==========")

print(df.head())


# ==========================================
# 2. Dataset Size Analysis
# ==========================================

print("\n========== DATASET SIZE ==========")

rows, columns = df.shape

print("Total Records:", rows)

print("Total Columns:", columns)



# ==========================================
# 3. Column Information
# ==========================================

print("\n========== COLUMN INFORMATION ==========")

print(df.info())



# ==========================================
# 4. Data Type Analysis
# ==========================================

print("\n========== DATA TYPES ==========")

print(df.dtypes)



# ==========================================
# 5. Missing Value Analysis
# ==========================================

print("\n========== MISSING VALUES ==========")

missing_values = df.isnull().sum()

print(missing_values)



# Calculate Missing Percentage

missing_percentage = (
    df.isnull().sum()
    /
    len(df)
    *
    100
)


print("\n========== MISSING VALUE % ==========")

print(
    missing_percentage
)



# ==========================================
# 6. Duplicate Analysis
# ==========================================

print("\n========== DUPLICATE CHECK ==========")

duplicates = df.duplicated().sum()

print(
    "Duplicate Records:",
    duplicates
)



# ==========================================
# 7. Unique Value Analysis
# ==========================================

print("\n========== UNIQUE VALUES ==========")


for column in df.columns:

    print(
        column,
        ":",
        df[column].nunique()
    )



# ==========================================
# 8. Department Analysis
# ==========================================

print("\n========== DEPARTMENT DISTRIBUTION ==========")

print(
    df["Department"]
    .value_counts()
)



# ==========================================
# 9. Priority Analysis
# ==========================================

print("\n========== PRIORITY DISTRIBUTION ==========")

print(
    df["Priority"]
    .value_counts()
)



# ==========================================
# 10. Status Analysis
# ==========================================

print("\n========== STATUS DISTRIBUTION ==========")

print(
    df["Status"]
    .value_counts()
)



# ==========================================
# 11. Ticket System Dependency Analysis
# ==========================================

print("\n========== SYSTEM DISTRIBUTION ==========")

print(
    df["System"]
    .value_counts()
)



# ==========================================
# 12. Export Data Profile Report
# ==========================================


profile = pd.DataFrame({

    "Column_Name": df.columns,

    "Data_Type": df.dtypes.values,

    "Missing_Count": df.isnull().sum().values,

    "Unique_Count": [
        df[col].nunique()
        for col in df.columns
    ]

})


profile.to_csv("data/reporting/data_analysis_report.csv",index=False)

print(
"\nData analysis completed successfully!"
)