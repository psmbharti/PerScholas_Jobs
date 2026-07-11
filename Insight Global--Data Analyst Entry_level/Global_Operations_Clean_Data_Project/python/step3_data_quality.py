import pandas as pd

# ==========================================
# STEP 3 - DATA QUALITY ASSESSMENT
# ==========================================

print("=" * 70)
print("GLOBAL OPERATIONS - DATA QUALITY ASSESSMENT")
print("=" * 70)

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv(r"data\raw\operational_data_dirty.csv")

total_records = len(df)

# ------------------------------------------
# Business Rules (Governance Standards)
# ------------------------------------------

valid_departments = [
    "IT",
    "HR",
    "Finance",
    "Operations",
    "Sales",
    "Procurement"
]

valid_priorities = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

valid_status = [
    "Open",
    "In Progress",
    "Resolved",
    "Closed"
]

valid_countries = [
    "USA",
    "Canada",
    "Mexico"
]

# ------------------------------------------
# 1. Missing Values
# ------------------------------------------

missing_values = df.isnull().sum().sum()

# ------------------------------------------
# 2. Duplicate Rows
# ------------------------------------------

duplicate_rows = df.duplicated().sum()

# ------------------------------------------
# 3. Duplicate Ticket Numbers
# ------------------------------------------

duplicate_tickets = df["Ticket Number"].duplicated().sum()

# ------------------------------------------
# 4. Invalid Departments
# ------------------------------------------

invalid_department = df[
    ~df["Department"].isin(valid_departments)
]

# ------------------------------------------
# 5. Invalid Priorities
# ------------------------------------------

invalid_priority = df[
    ~df["Priority"].isin(valid_priorities)
]

# ------------------------------------------
# 6. Invalid Status
# ------------------------------------------

invalid_status = df[
    ~df["Status"].isin(valid_status)
]

# ------------------------------------------
# 7. Invalid Countries
# ------------------------------------------

invalid_country = df[
    ~df["Country"].isin(valid_countries)
]

# ------------------------------------------
# 8. Invalid Employee IDs
# ------------------------------------------

invalid_employee = df[
    df["Employee ID"] == "EMP9999"
]

# ------------------------------------------
# 9. Invalid Dates
# Closed Date cannot be before Created Date
# ------------------------------------------

df["Created Date"] = pd.to_datetime(df["Created Date"])
df["Closed Date"] = pd.to_datetime(df["Closed Date"])

invalid_dates = df[
    df["Closed Date"] < df["Created Date"]
]

# ------------------------------------------
# 10. Extra Spaces
# ------------------------------------------

space_assignment = df[
    df["Assignment Group"] !=
    df["Assignment Group"].str.strip()
]

# ------------------------------------------
# Data Quality Score
# ------------------------------------------

issue_count = (
    missing_values +
    duplicate_rows +
    duplicate_tickets +
    len(invalid_department) +
    len(invalid_priority) +
    len(invalid_status) +
    len(invalid_country) +
    len(invalid_employee) +
    len(invalid_dates) +
    len(space_assignment)
)

quality_score = (
    (1 - issue_count / (total_records * len(df.columns)))
    * 100
)

quality_score = round(max(0, quality_score), 2)

# ------------------------------------------
# Print Results
# ------------------------------------------

print("\nTotal Records :", total_records)

print("\nMissing Values :", missing_values)

print("Duplicate Rows :", duplicate_rows)

print("Duplicate Ticket Numbers :", duplicate_tickets)

print("Invalid Departments :", len(invalid_department))

print("Invalid Priorities :", len(invalid_priority))

print("Invalid Status :", len(invalid_status))

print("Invalid Countries :", len(invalid_country))

print("Invalid Employee IDs :", len(invalid_employee))

print("Invalid Dates :", len(invalid_dates))

print("Assignment Groups with Extra Spaces :", len(space_assignment))

print("\nOverall Data Quality Score :", quality_score, "%")

# ------------------------------------------
# Summary Report
# ------------------------------------------

summary = pd.DataFrame({
    "Quality Check": [
        "Missing Values",
        "Duplicate Rows",
        "Duplicate Ticket Numbers",
        "Invalid Departments",
        "Invalid Priorities",
        "Invalid Status",
        "Invalid Countries",
        "Invalid Employee IDs",
        "Invalid Dates",
        "Assignment Groups with Extra Spaces",
        "Overall Data Quality Score (%)"
    ],
    "Count": [
        missing_values,
        duplicate_rows,
        duplicate_tickets,
        len(invalid_department),
        len(invalid_priority),
        len(invalid_status),
        len(invalid_country),
        len(invalid_employee),
        len(invalid_dates),
        len(space_assignment),
        quality_score
    ]
})

summary.to_csv(r"data\quality\data_quality_report.csv", index=False)

print("\nData Quality Report Saved Successfully!")