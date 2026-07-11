import pandas as pd


print("="*70)
print("GLOBAL OPERATIONS - UAT TESTING")
print("="*70)


# ------------------------------------------------
# Load Data
# ------------------------------------------------

df = pd.read_csv( "data/processed/mapped_operational_data.csv")

employee_master = pd.read_csv( "data/master/employee_master.csv")

department_master = pd.read_csv("data/master/department_master.csv")

print("\nData Loaded")

print("Records:", len(df))

# ------------------------------------------------
# UAT Test Results Container
# ------------------------------------------------

uat_results = []

# ------------------------------------------------
# Test Case 1
# Ticket Number Uniqueness
# ------------------------------------------------

duplicate_tickets = (
    df["Ticket Number"]
    .duplicated()
    .sum()
)


uat_results.append({

"Test Case ID":
"UAT001",

"Test Scenario":
"Validate Ticket Number uniqueness",

"Expected Result":
"No duplicate ticket numbers",

"Actual Result":
duplicate_tickets,

"Status":
"PASS" if duplicate_tickets == 0 else "FAIL"

})


# ------------------------------------------------
# Test Case 2
# Employee Master Relationship
# ------------------------------------------------

invalid_employee = (

~df["Employee ID"]
.isin(employee_master["Employee ID"])

).sum()



uat_results.append({

"Test Case ID":
"UAT002",

"Test Scenario":
"Employee IDs exist in HR Master",

"Expected Result":
"All Employee IDs valid",

"Actual Result":
invalid_employee,

"Status":
"PASS" if invalid_employee == 0 else "FAIL"

})


# ------------------------------------------------
# Test Case 3
# Department Mapping
# ------------------------------------------------


invalid_department = (

~df["Department"]
.isin(
department_master["Department"]
)

).sum()



uat_results.append({

"Test Case ID":
"UAT003",

"Test Scenario":
"Department follows governance standard",

"Expected Result":
"Approved departments only",

"Actual Result":
invalid_department,

"Status":
"PASS" if invalid_department == 0 else "FAIL"

})


# ------------------------------------------------
# Test Case 4
# Priority Values
# ------------------------------------------------

approved_priority = [

"LOW",
"MEDIUM",
"HIGH",
"CRITICAL"

]


invalid_priority = (

~df["Priority_Standard"]
.isin(
approved_priority
)

).sum()



uat_results.append({

"Test Case ID":
"UAT004",

"Test Scenario":
"Priority standardization",

"Expected Result":
"Only approved priority values",

"Actual Result":
invalid_priority,

"Status":
"PASS" if invalid_priority == 0 else "FAIL"

})


# ------------------------------------------------
# Test Case 5
# Status Workflow
# ------------------------------------------------

approved_status = [

"NEW",
"WORKING",
"RESOLVED",
"CLOSED"

]


invalid_status = (

~df["Status_Standard"]
.isin(
approved_status
)

).sum()



uat_results.append({

"Test Case ID":
"UAT005",

"Test Scenario":
"Status workflow validation",

"Expected Result":
"Approved status lifecycle",

"Actual Result":
invalid_status,

"Status":
"PASS" if invalid_status == 0 else "FAIL"

})


# ------------------------------------------------
# Test Case 6
# Date Validation
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



uat_results.append({

"Test Case ID":
"UAT006",

"Test Scenario":
"Ticket closure date validation",

"Expected Result":
"Closed date after created date",

"Actual Result":
invalid_dates,

"Status":
"PASS" if invalid_dates == 0 else "FAIL"

})


# ------------------------------------------------
# Test Case 7
# Required Fields
# ------------------------------------------------


required_columns = [

"Ticket Number",
"Employee ID",
"Department",
"Priority",
"Status"

]


missing_values = (

df[required_columns]
.isnull()
.sum()
.sum()

)



uat_results.append({

"Test Case ID":
"UAT007",

"Test Scenario":
"Required operational fields",

"Expected Result":
"No missing mandatory fields",

"Actual Result":
missing_values,

"Status":
"PASS" if missing_values == 0 else "FAIL"

})


# ------------------------------------------------
# Create UAT Report
# ------------------------------------------------


uat_report = pd.DataFrame(uat_results)

uat_report.to_csv("data/quality/uat_test_results.csv",index=False)

print("\nUAT Testing Results")
print("-----------------------------")

print(uat_report)

print("\nUAT Test Report Generated Successfully")