import pandas as pd


print("="*70)
print("GLOBAL OPERATIONS - DATA VALIDATION")
print("="*70)


# ------------------------------------------------
# Load Data
# ------------------------------------------------

df = pd.read_csv("data/processed/mapped_operational_data.csv")


employee_master = pd.read_csv("data/master/employee_master.csv")


department_master = pd.read_csv("data/master/department_master.csv")


print("\nDataset Loaded")

print("Operational Records:",
      len(df))


# ------------------------------------------------
# Create Validation Results
# ------------------------------------------------

validation_results = []


# ------------------------------------------------
# 1. Ticket Number Validation
# ------------------------------------------------

duplicate_ticket = (
    df["Ticket Number"]
    .duplicated()
    .sum()
)


validation_results.append({

"Test Case":
"Ticket Number Unique",

"Expected":
"No Duplicate Tickets",

"Actual":
duplicate_ticket,

"Status":
"PASS" if duplicate_ticket == 0 else "FAIL"

})


# ------------------------------------------------
# 2. Employee ID Validation
# ------------------------------------------------

invalid_employee = (
    ~df["Employee ID"]
    .isin(employee_master["Employee ID"])
).sum()


validation_results.append({

"Test Case":
"Employee ID Exists",

"Expected":
"All IDs exist in Employee Master",

"Actual":
invalid_employee,

"Status":
"PASS" if invalid_employee == 0 else "FAIL"

})


# ------------------------------------------------
# 3. Required Field Validation
# ------------------------------------------------

required_columns = [

"Ticket Number",
"Employee ID",
"Department",
"Priority",
"Status"

]


missing_required = (
    df[required_columns]
    .isnull()
    .sum()
    .sum()
)



validation_results.append({

"Test Case":
"Required Fields Complete",

"Expected":
"No Missing Values",

"Actual":
missing_required,

"Status":
"PASS" if missing_required == 0 else "FAIL"

})


# ------------------------------------------------
# 4. Department Validation
# ------------------------------------------------

approved_departments = [

    "Information Technology",
    "Finance",
    "Operations",
    "Human Resources",
    "Sales",
    "Procurement"

]


invalid_department = (

    ~df["Department_Standard"]
    .isin(approved_departments)

).sum()



validation_results.append({

    "Test Case":
    "Department Standardization",

    "Expected":
    "Valid Department",

    "Actual":
    invalid_department,

    "Status":
    "PASS" if invalid_department == 0 else "FAIL"

})


# ------------------------------------------------
# 5. Priority Validation
# ------------------------------------------------


valid_priority = [

"LOW",
"MEDIUM",
"HIGH",
"CRITICAL"

]


invalid_priority = (

~df["Priority_Standard"]
.isin(valid_priority)

).sum()



validation_results.append({

"Test Case":
"Priority Validation",

"Expected":
"Approved Priority Values",

"Actual":
invalid_priority,

"Status":
"PASS" if invalid_priority == 0 else "FAIL"

})


# ------------------------------------------------
# 6. Status Validation
# ------------------------------------------------


valid_status = [

"NEW",
"WORKING",
"RESOLVED",
"CLOSED"

]


invalid_status = (

~df["Status_Standard"]
.isin(valid_status)

).sum()



validation_results.append({

"Test Case":
"Status Validation",

"Expected":
"Approved Status Values",

"Actual":
invalid_status,

"Status":
"PASS" if invalid_status == 0 else "FAIL"

})


# ------------------------------------------------
# 7. Date Validation
# ------------------------------------------------


df["Created Date"] = pd.to_datetime(
df["Created Date"]
)


df["Closed Date"] = pd.to_datetime(
df["Closed Date"]
)



invalid_dates = (

df["Closed Date"]

<
df["Created Date"]

).sum()



validation_results.append({

"Test Case":
"Date Sequence Validation",

"Expected":
"Closed Date >= Created Date",

"Actual":
invalid_dates,

"Status":
"PASS" if invalid_dates == 0 else "FAIL"

})


# ------------------------------------------------
# Create Validation Report
# ------------------------------------------------


validation_report = pd.DataFrame(validation_results)


validation_report.to_csv("data/quality/validation_report.csv",index=False)


# ------------------------------------------------
# Display Results
# ------------------------------------------------


print("\nValidation Results")

print(validation_report)


print("\nValidation Report Created Successfully")