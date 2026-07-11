import pandas as pd

print("=" * 70)
print("GLOBAL OPERATIONS - DATA CLEANING")
print("=" * 70)

# ---------------------------------------------------
# Load Dirty Dataset
# ---------------------------------------------------

df = pd.read_csv(r"data\raw\operational_data_dirty.csv")

print("\nRecords Before Cleaning:", len(df))

# ---------------------------------------------------
# 1. Remove Duplicate Rows
# ---------------------------------------------------

duplicates_before = df["Ticket Number"].duplicated().sum()

df = df.drop_duplicates(subset="Ticket Number", keep="first")

print("Duplicate Ticket Numbers Removed:", duplicates_before)
# Verify
print("\nRemaining Duplicate Ticket Numbers:")
print(df["Ticket Number"].duplicated().sum())

# ---------------------------------------------------
# 2. Fill Missing Employee IDs
# ---------------------------------------------------

missing_before = df["Employee ID"].isnull().sum()

df["Employee ID"] = df["Employee ID"].fillna("UNKNOWN")

print("Missing Employee IDs Filled:", missing_before)

# ---------------------------------------------------
# 3. Correct Invalid Employee IDs
# ---------------------------------------------------

invalid_emp = df["Employee ID"] == "EMP9999"

invalid_count = invalid_emp.sum()

df.loc[invalid_emp, "Employee ID"] = "UNKNOWN"

print("Invalid Employee IDs Corrected:", invalid_count)

# ---------------------------------------------------
# 4. Standardize Department Names
# ---------------------------------------------------

department_mapping = {
    "it": "IT",
    "FIN": "Finance",
    "Operation": "Operations",
    "Procure": "Procurement"
}

df["Department"] = df["Department"].replace(department_mapping)

print("Department Names Standardized")

# ---------------------------------------------------
# 5. Standardize Priority
# ---------------------------------------------------

priority_mapping = {
    "HIGH": "High",
    "medium": "Medium",
    "CRITICAL": "Critical"
}

df["Priority"] = df["Priority"].replace(priority_mapping)

print("Priority Values Standardized")

# ---------------------------------------------------
# 6. Remove Extra Spaces
# ---------------------------------------------------

object_columns = df.select_dtypes(include="object").columns

for col in object_columns:
    df[col] = df[col].str.strip()

print("Extra Spaces Removed")

# ---------------------------------------------------
# 7. Correct Invalid Dates
# ---------------------------------------------------

df["Created Date"] = pd.to_datetime(df["Created Date"])
df["Closed Date"] = pd.to_datetime(df["Closed Date"])

invalid_dates = df["Closed Date"] < df["Created Date"]

invalid_date_count = invalid_dates.sum()

df.loc[invalid_dates, "Closed Date"] = (
    df.loc[invalid_dates, "Created Date"] + pd.Timedelta(days=1)
)

print("Invalid Dates Corrected:", invalid_date_count)

# ---------------------------------------------------
# 8. Format Text Columns
# ---------------------------------------------------

df["Employee Name"] = df["Employee Name"].str.title()
df["Location"] = df["Location"].str.title()
df["Country"] = df["Country"].str.title()

print("Text Formatting Completed")

# ---------------------------------------------------
# 9. Final Data Quality Check
# ---------------------------------------------------

print("\nFinal Validation")
print("-" * 40)

print("Missing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

# ---------------------------------------------------
# 10. Save Clean Dataset
# ---------------------------------------------------

df["Created Date"] = df["Created Date"].dt.strftime("%Y-%m-%d")
df["Closed Date"] = df["Closed Date"].dt.strftime("%Y-%m-%d")

df.to_csv(r"data\processed\clean_operational_data.csv", index=False)

print("\nRecords After Cleaning:", len(df))

print("\nClean Dataset Saved Successfully!")

