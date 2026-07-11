import pandas as pd


print("="*70)
print("GLOBAL OPERATIONS - REPORTING AUTOMATION")
print("="*70)


# ------------------------------------------------
# Load Data
# ------------------------------------------------

df = pd.read_csv("data/processed/mapped_operational_data.csv")

validation = pd.read_csv("data/quality/validation_report.csv")

uat = pd.read_csv("data/quality/uat_test_results.csv")

risk = pd.read_csv("data/governance/data_risk_register.csv")

print("\nData Loaded")

# ------------------------------------------------
# KPI Calculations
# ------------------------------------------------

total_tickets = len(df)

closed_tickets = (
    df["Status_Standard"]
    .isin(["CLOSED","RESOLVED"])
    .sum()
)


open_tickets = (
    df["Status_Standard"]
    .isin(["NEW","WORKING"])
    .sum()
)


high_priority = (
    df["Priority_Standard"]
    .isin(["HIGH","CRITICAL"])
    .sum()
)


departments = (
    df["Department"]
    .nunique()
)


systems = (
    df["System"]
    .nunique()
)


# ------------------------------------------------
# Data Quality Score
# ------------------------------------------------


total_tests = len(validation)


passed_tests = (validation["Status"] =="PASS").sum()


data_quality_score = round(
    (passed_tests / total_tests) * 100, 2)



# ------------------------------------------------
# Create KPI Report
# ------------------------------------------------


kpi = pd.DataFrame({

"KPI": [

"Total Tickets",

"Closed Tickets",

"Open Tickets",

"High Priority Tickets",

"Departments",

"Systems",

"Data Quality Score"

],


"Value":[

total_tickets,

closed_tickets,

open_tickets,

high_priority,

departments,

systems,

f"{data_quality_score}%"

]

})


kpi.to_csv("data/reporting/kpi_summary.csv",index=False)



# ------------------------------------------------
# Department Reporting
# ------------------------------------------------


department_report = (

df.groupby(
"Department"
)

.size()

.reset_index(
name="Ticket_Count"
)

.sort_values(
"Ticket_Count",
ascending=False
)

)

department_report.to_csv("data/reporting/Department Ticket Report.csv",index=False)

# ------------------------------------------------
# Print Summary
# ------------------------------------------------


print("\nKPI Summary")
print("----------------")

print(kpi)



print("\nDepartment Ticket Report")
print("----------------")

print(department_report)



print("\nReporting Files Created Successfully")