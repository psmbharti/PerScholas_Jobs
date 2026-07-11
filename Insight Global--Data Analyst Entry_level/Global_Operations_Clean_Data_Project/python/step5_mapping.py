import pandas as pd


print("="*70)
print("GLOBAL OPERATIONS - DATA MAPPING & STANDARDIZATION")
print("="*70)


# ------------------------------------------------
# Load Clean Dataset
# ------------------------------------------------

df = pd.read_csv(r"data\processed\clean_operational_data.csv")



print("\nDataset Loaded")
print("Records:", len(df))


# ------------------------------------------------
# 1. Department Mapping
# ------------------------------------------------

department_mapping = {

    "IT": "Information Technology",

    "Finance": "Finance",

    "Operations": "Operations",

    "Sales": "Sales",

    "HR": "Human Resources",

    "Procurement": "Procurement"

}


old_department = df["Department"].copy()


df["Department_Standard"] = (
    df["Department"]
    .map(department_mapping)
)


# ------------------------------------------------
# 2. Priority Mapping
# ------------------------------------------------

priority_mapping = {

    "Low": "LOW",

    "Medium": "MEDIUM",

    "High": "HIGH",

    "Critical": "CRITICAL"

}


df["Priority_Standard"] = (
    df["Priority"]
    .map(priority_mapping)
)



# ------------------------------------------------
# 3. Status Mapping
# ------------------------------------------------

status_mapping = {

    "Open": "NEW",

    "In Progress": "WORKING",

    "Resolved": "RESOLVED",

    "Closed": "CLOSED"

}


df["Status_Standard"] = (
    df["Status"]
    .map(status_mapping)
)



# ------------------------------------------------
# 4. Country Mapping
# ------------------------------------------------

country_mapping = {

    "USA": "United States",

    "Canada": "Canada",

    "Mexico": "Mexico"

}


df["Country_Standard"] = (
    df["Country"]
    .map(country_mapping)
)



# ------------------------------------------------
# 5. System Mapping
# ------------------------------------------------

system_mapping = {

    "ServiceNow":
        "IT Service Management Platform",

    "SAP":
        "Enterprise Resource Planning",

    "Salesforce":
        "Customer Relationship Management",

    "Oracle":
        "Database Platform"

}


df["System_Category"] = (
    df["System"]
    .map(system_mapping)
)



# ------------------------------------------------
# Create Mapping Audit Report
# ------------------------------------------------


mapping_report = pd.DataFrame({

    "Original_Department":
        old_department,

    "Standard_Department":
        df["Department_Standard"],

    "Original_Priority":
        df["Priority"],

    "Standard_Priority":
        df["Priority_Standard"],

    "Original_Status":
        df["Status"],

    "Standard_Status":
        df["Status_Standard"]

})


mapping_report.to_csv( r"data\reporting\mapping_report.csv", index=False)


# ------------------------------------------------
# Save Final Mapped Dataset
# ------------------------------------------------


df.to_csv(r"data\processed\mapped_operational_data.csv", index=False)


print("\nMapping Completed Successfully")

print("\nFiles Created:")
print("1. mapped_operational_data.csv")
print("2. mapping_report.csv")