import pandas as pd

# Load your uploaded CSV
df = pd.read_csv("data\processed\mapped_operational_data.csv")

# -----------------------------
# 1. CREATE EMPLOYEE MASTER
# -----------------------------
employee_master = (
    df[["Employee ID", "Employee Name", "Department", "Location", "Country"]]
    .drop_duplicates()
    .sort_values("Employee ID")
    .reset_index(drop=True)
)

# Save employee master
employee_master.to_csv("data\master\employee_master.csv",index=False)

# -----------------------------
# 2. CREATE DEPARTMENT MASTER
# -----------------------------
department_master = (
    df[["Department"]]
    .drop_duplicates()
    .sort_values("Department")
    .reset_index(drop=True)
)

# Create Department_ID (D001, D002, ...)
department_master["Department_ID"] = [
    f"D{str(i+1).zfill(3)}"
    for i in range(len(department_master))
]

# Reorder columns
department_master = department_master[["Department_ID", "Department"]]

# Save department master
department_master.to_csv("data\master\department_master.csv",index=False)

print("Employee and Department master files created successfully!")
