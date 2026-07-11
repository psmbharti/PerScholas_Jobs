import pandas as pd

# ==========================================
# STEP 2 - DATA PROFILING
# ==========================================

print("=" * 60)
print("GLOBAL OPERATIONS - DATA PROFILING REPORT")
print("=" * 60)

# ------------------------------------------
# Load Dirty Dataset
# ------------------------------------------

df = pd.read_csv(r"data\raw\operational_data_dirty.csv")

print("\nDataset Loaded Successfully")

# ------------------------------------------
# Dataset Shape
# ------------------------------------------

rows, columns = df.shape

print("\nDataset Shape")
print("---------------------")
print("Rows :", rows)
print("Columns :", columns)

# ------------------------------------------
# Data Types
# ------------------------------------------

print("\nData Types")
print("---------------------")
print(df.dtypes)

# ------------------------------------------
# Missing Values
# ------------------------------------------

print("\nMissing Values")
print("---------------------")

missing = df.isnull().sum()

print(missing)

# ------------------------------------------
# Missing Percentage
# ------------------------------------------

print("\nMissing Percentage")
print("---------------------")

missing_percent = (missing / len(df)) * 100

print(missing_percent.round(2))

# ------------------------------------------
# Duplicate Records
# ------------------------------------------

print("\nDuplicate Records")
print("---------------------")

duplicates = df.duplicated().sum()

print("Duplicate Rows :", duplicates)

# ------------------------------------------
# Duplicate Ticket Numbers
# ------------------------------------------

print("\nDuplicate Ticket Numbers")
print("---------------------")

duplicate_tickets = df[df.duplicated("Ticket Number", keep=False)]

print(duplicate_tickets[["Ticket Number"]])

print("Total Duplicate Tickets :", duplicate_tickets.shape[0])

# ------------------------------------------
# Unique Values
# ------------------------------------------

print("\nUnique Values")
print("---------------------")

for column in df.columns:
    print(f"{column:<25} {df[column].nunique()}")

# ------------------------------------------
# Department Distribution
# ------------------------------------------

print("\nDepartment Distribution")
print("---------------------")

print(df["Department"].value_counts())

# ------------------------------------------
# Priority Distribution
# ------------------------------------------

print("\nPriority Distribution")
print("---------------------")

print(df["Priority"].value_counts())

# ------------------------------------------
# Status Distribution
# ------------------------------------------

print("\nStatus Distribution")
print("---------------------")

print(df["Status"].value_counts())

# ------------------------------------------
# Country Distribution
# ------------------------------------------

print("\nCountry Distribution")
print("---------------------")

print(df["Country"].value_counts())

# ------------------------------------------
# Assignment Group Distribution
# ------------------------------------------

print("\nAssignment Group Distribution")
print("---------------------")

print(df["Assignment Group"].value_counts())

# ------------------------------------------
# Invalid Employee IDs
# ------------------------------------------

print("\nInvalid Employee IDs")
print("---------------------")

invalid_emp = df[df["Employee ID"] == "EMP9999"]

print(invalid_emp[["Ticket Number", "Employee ID"]])

print("Total Invalid Employee IDs :", len(invalid_emp))

# ------------------------------------------
# Summary
# ------------------------------------------

print("\nSummary")
print("---------------------")

print("Total Records :", len(df))
print("Missing Values :", df.isnull().sum().sum())
print("Duplicate Rows :", duplicates)
print("Invalid Employee IDs :", len(invalid_emp))

# ------------------------------------------
# Export Data Profile Report
# ------------------------------------------

profile = pd.DataFrame({
    "Column Name": df.columns,
    "Data Type": df.dtypes.values,
    "Missing Count": df.isnull().sum().values,
    "Unique Count": [df[col].nunique() for col in df.columns]
})

profile.to_csv("data/quality/data_profile_report.csv", index=False)

print("\nData Profile Report Saved Successfully!")