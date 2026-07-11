import pandas as pd


print("="*70)
print("GLOBAL OPERATIONS - DATA RISK ANALYSIS")
print("="*70)


# ------------------------------------------------
# Load Reports
# ------------------------------------------------

validation = pd.read_csv("data/quality/validation_report.csv")


uat = pd.read_csv("data/quality/uat_test_results.csv")


print("\nReports Loaded")


# ------------------------------------------------
# Create Risk Register
# ------------------------------------------------


risks = []


# ------------------------------------------------
# Risk 1 - Duplicate Records
# ------------------------------------------------


duplicate_issue = validation.loc[
    validation["Test Case"] == "Ticket Number Unique",
    "Actual"
].values[0]


risks.append({

"Risk ID":
"R001",

"Risk Category":
"Data Quality",

"Risk Description":
"Duplicate operational tickets may exist",

"Impact":
"Incorrect reporting, duplicate workload, inaccurate KPIs",

"Severity":
"High" if duplicate_issue > 0 else "Low",

"Root Cause":
"Missing uniqueness validation during data entry",

"Mitigation Plan":
"Implement ticket number uniqueness checks",

"Owner":
"ServiceNow Administrator"

})


# ------------------------------------------------
# Risk 2 - Employee Master Integrity
# ------------------------------------------------


employee_issue = validation.loc[
validation["Test Case"]=="Employee ID Exists",
"Actual"
].values[0]


risks.append({

"Risk ID":
"R002",

"Risk Category":
"People & Data",

"Risk Description":
"Tickets linked to invalid employee records",

"Impact":
"Unable to identify request owner",

"Severity":
"High" if employee_issue > 0 else "Low",

"Root Cause":
"Employee master synchronization issues",

"Mitigation Plan":
"Daily HR master data reconciliation",

"Owner":
"HR Data Owner"

})


# ------------------------------------------------
# Risk 3 - Department Governance
# ------------------------------------------------


department_issue = validation.loc[
validation["Test Case"]=="Department Standardization",
"Actual"
].values[0]


risks.append({

"Risk ID":
"R003",

"Risk Category":
"Data Governance",

"Risk Description":
"Department values inconsistent across systems",

"Impact":
"Incorrect department reporting and analytics",

"Severity":
"High" if department_issue > 0 else "Low",

"Root Cause":
"Lack of standardized reference data",

"Mitigation Plan":
"Use department master data governance",

"Owner":
"Data Governance Team"

})


# ------------------------------------------------
# Risk 4 - Workflow Status
# ------------------------------------------------


risks.append({

"Risk ID":
"R004",

"Risk Category":
"Process",

"Risk Description":
"Incorrect ticket lifecycle status",

"Impact":
"Incorrect SLA and operational reporting",

"Severity":
"Medium",

"Root Cause":
"Users selecting incorrect workflow values",

"Mitigation Plan":
"Restrict status values using workflow rules",

"Owner":
"IT Operations"

})


# ------------------------------------------------
# Risk 5 - System Dependency
# ------------------------------------------------


risks.append({

"Risk ID":
"R005",

"Risk Category":
"Systems",

"Risk Description":
"Multiple systems create inconsistent operational data",

"Impact":
"Data mismatch between platforms",

"Severity":
"Medium",

"Root Cause":
"Lack of integrated data flow",

"Mitigation Plan":
"Create automated data synchronization",

"Owner":
"Enterprise Architecture"

})


# ------------------------------------------------
# Create Risk Register
# ------------------------------------------------


risk_register = pd.DataFrame(risks)


risk_register.to_csv("data/governance/risk_register.csv",index=False)


print("\nRisk Register Created Successfully")

print("\nFile:")
print("data/governance/risk_register.csv")


print("\nRisk Summary")

print(risk_register)