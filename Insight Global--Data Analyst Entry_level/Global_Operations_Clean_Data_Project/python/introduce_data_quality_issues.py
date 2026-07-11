import pandas as pd
import random

# Load clean dataset
df = pd.read_csv("data/raw/operational_data.csv")

# ----------------------------------------
# 1. Add Duplicate Records
# ----------------------------------------
duplicate_rows = df.sample(20, random_state=42)
df = pd.concat([df, duplicate_rows], ignore_index=True)

# ----------------------------------------
# 2. Missing Employee IDs
# ----------------------------------------
missing_index = df.sample(15, random_state=1).index
df.loc[missing_index, "Employee ID"] = None

# ----------------------------------------
# 3. Invalid Employee IDs
# ----------------------------------------
invalid_index = df.sample(10, random_state=2).index
df.loc[invalid_index, "Employee ID"] = "EMP9999"

# ----------------------------------------
# 4. Invalid Departments
# ----------------------------------------
dept_map = {
    "IT": "it",
    "Finance": "FIN",
    "Operations": "Operation",
    "Procurement": "Procure"
}

for old, new in dept_map.items():
    rows = df[df["Department"] == old].sample(5, random_state=3).index
    df.loc[rows, "Department"] = new

# ----------------------------------------
# 5. Invalid Priorities
# ----------------------------------------
priority_map = {
    "High": "HIGH",
    "Medium": "medium",
    "Critical": "CRITICAL"
}

for old, new in priority_map.items():
    rows = df[df["Priority"] == old].sample(5, random_state=4).index
    df.loc[rows, "Priority"] = new

# ----------------------------------------
# 6. Extra Spaces
# ----------------------------------------
space_rows = df.sample(20, random_state=5).index
df.loc[space_rows, "Assignment Group"] = (
    " " + df.loc[space_rows, "Assignment Group"] + " "
)

# ----------------------------------------
# 7. Invalid Dates
# Closed Date earlier than Created Date
# ----------------------------------------
date_rows = df.sample(10, random_state=6).index

df["Created Date"] = pd.to_datetime(df["Created Date"])
df["Closed Date"] = pd.to_datetime(df["Closed Date"])

for i in date_rows:
    df.loc[i, "Closed Date"] = df.loc[i, "Created Date"] - pd.Timedelta(days=2)

# Convert dates back to string
df["Created Date"] = df["Created Date"].dt.strftime("%Y-%m-%d")
df["Closed Date"] = df["Closed Date"].dt.strftime("%Y-%m-%d")

# ----------------------------------------
# Save Dirty Dataset
# ----------------------------------------
df.to_csv(r"data/raw/operational_data_dirty.csv", index=False)

print("Dirty dataset created successfully.")
print("Total Records:", len(df))
print(df.head())