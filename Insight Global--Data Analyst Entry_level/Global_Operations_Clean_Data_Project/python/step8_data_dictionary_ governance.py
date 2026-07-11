# step8_data_dictionary_ governance.py
import pandas as pd


print("="*70)
print("GLOBAL OPERATIONS - DATA DICTIONARY CREATION")
print("="*70)

# ------------------------------------------------
# Load Dataset
# ------------------------------------------------

df = pd.read_csv("data/processed/mapped_operational_data.csv")

print("\nDataset Loaded")

print("Columns:", len(df.columns))

# ------------------------------------------------
# Define Governance Metadata
# ------------------------------------------------


dictionary_rules = {


"Ticket Number": {

"Business Definition":
"Unique identifier assigned to each operational ticket",

"Source System":
"ServiceNow",

"Validation Rule":
"Must be unique and cannot be null",

"Data Owner":
"IT Operations"

},


"Employee ID": {

"Business Definition":
"Unique employee identifier associated with ticket",

"Source System":
"HR Master System",

"Validation Rule":
"Must exist in Employee Master",

"Data Owner":
"Human Resources"

},


"Employee Name": {

"Business Definition":
"Employee who submitted the request",

"Source System":
"HR Master System",

"Validation Rule":
"Required field",

"Data Owner":
"Human Resources"

},


"Department": {

"Business Definition":
"Business department associated with employee",

"Source System":
"HR Master System",

"Validation Rule":
"Must match approved department master",

"Data Owner":
"HR Governance"

},


"Priority": {

"Business Definition":
"Business impact level of operational ticket",

"Source System":
"ServiceNow",

"Validation Rule":
"Allowed values: LOW, MEDIUM, HIGH, CRITICAL",

"Data Owner":
"IT Service Management"

},


"Status": {

"Business Definition":
"Current lifecycle status of ticket",

"Source System":
"ServiceNow",

"Validation Rule":
"Must follow approved workflow states",

"Data Owner":
"IT Operations"

},


"Category": {

"Business Definition":
"High-level classification of ticket",

"Source System":
"ServiceNow",

"Validation Rule":
"Must use approved category list",

"Data Owner":
"IT Operations"

},


"Assignment Group": {

"Business Definition":
"Support team responsible for resolution",

"Source System":
"ServiceNow",

"Validation Rule":
"Must match support group master",

"Data Owner":
"Service Management"

},


"System": {

"Business Definition":
"Application or platform impacted",

"Source System":
"Application Inventory",

"Validation Rule":
"Must match application catalog",

"Data Owner":
"Application Owners"

},


"Vendor": {

"Business Definition":
"External technology provider",

"Source System":
"Vendor Management",

"Validation Rule":
"Must match approved vendor list",

"Data Owner":
"Procurement"

},


"Created Date": {

"Business Definition":
"Date ticket was created",

"Source System":
"ServiceNow",

"Validation Rule":
"Valid date format",

"Data Owner":
"IT Operations"

},


"Closed Date": {

"Business Definition":
"Date ticket was resolved",

"Source System":
"ServiceNow",

"Validation Rule":
"Must be greater than Created Date",

"Data Owner":
"IT Operations"

},


"Resolution Code": {

"Business Definition":
"Method used to resolve ticket",

"Source System":
"ServiceNow",

"Validation Rule":
"Must use approved resolution values",

"Data Owner":
"IT Operations"

},


"Comments": {

"Business Definition":
"Additional ticket notes and resolution details",

"Source System":
"ServiceNow",

"Validation Rule":
"Text field",

"Data Owner":
"IT Operations"

}

}


# ------------------------------------------------
# Build Data Dictionary
# ------------------------------------------------


dictionary = []


for column in df.columns:


    if column in dictionary_rules:

        dictionary.append({

        "Column Name":
        column,

        "Data Type":
        str(df[column].dtype),

        "Business Definition":
        dictionary_rules[column]["Business Definition"],

        "Source System":
        dictionary_rules[column]["Source System"],

        "Validation Rule":
        dictionary_rules[column]["Validation Rule"],

        "Data Owner":
        dictionary_rules[column]["Data Owner"]

        })


    else:

        dictionary.append({

        "Column Name":
        column,

        "Data Type":
        str(df[column].dtype),

        "Business Definition":
        "Mapped or standardized operational attribute",

        "Source System":
        "ServiceNow",

        "Validation Rule":
        "Follow governance standards",

        "Data Owner":
        "Global Operations"

        })


# ------------------------------------------------
# Save Dictionary
# ------------------------------------------------


data_dictionary = pd.DataFrame(dictionary)


data_dictionary.to_csv("data/governance/data_dictionary_ governance.csv",index=False)


print("\nData Dictionary Created Successfully")

print("\nFile Created:")
print("data/governance/data_dictionary_ governance.csv")


print("\nPreview:")

print(data_dictionary.head())