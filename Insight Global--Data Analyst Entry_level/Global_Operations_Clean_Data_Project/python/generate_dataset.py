import pandas as pd  # pandas stores the dataset in a DataFrame
import random        # random creates random values.
from faker import Faker   # Faker generates realistic names and comments.
from datetime import datetime, timedelta   # datetime creates realistic ticket dates.

# Initialize Faker
fake = Faker()
# print(fake.name())

# Define Number of Records(create 500 operational records)
NUM_RECORDS = 500

# Create Master Lists
departments = [
    "IT",
    "HR",
    "Finance",
    "Operations",
    "Sales",
    "Procurement"
]

locations = [
    "Dallas",
    "New York",
    "Chicago",
    "Atlanta",
    "Seattle"
]

countries = [
    "USA",
    "Canada",
    "Mexico"
]

priorities = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

statuses = [
    "Open",
    "In Progress",
    "Resolved",
    "Closed"
]

categories = [
    "Incident",
    "Request",
    "Problem",
    "Change"
]

subcategories = [
    "Hardware",
    "Software",
    "Network",
    "Email"
]

assignment_groups = [
    "Service Desk",
    "Network Team",
    "Application Team",
    "Security Team"
]

systems = [
    "ServiceNow",
    "SAP",
    "Salesforce",
    "Oracle"
]

vendors = [
    "Microsoft",
    "Cisco",
    "Dell",
    "IBM"
]

# Create an Empty List
# Each generated ticket will be stored as a dictionary in this list. Later, the list will be converted into a pandas DataFrame.
records = []

# Generate Ticket Numbers(Every ticket should have a unique identifier.)
for i in range(NUM_RECORDS):
    # Generate Ticket Number
    ticket_number = f"INC{100000+i}"
    
    # Generate Employee Information (Each ticket is assigned to an employee)  
    employee_id = f"EMP{random.randint(1000,1099)}"

    employee_name = fake.name() 

    # Generate Department
    department = random.choice(departments)

    # Generate Location
    location = random.choice(locations)
    # Generate Country
    country = random.choice(countries)

    # Generate Priority
    priority = random.choice(priorities)

    # Generate Status
    status = random.choice(statuses)

    # Generate Category
    category = random.choice(categories)

   # Generate Subcategory
    subcategory = random.choice(subcategories)

   # Generate Assignment Group
    assignment_group = random.choice(assignment_groups)
 
   # Generate System
    system = random.choice(systems)

   # Generate Vendor
    vendor = random.choice(vendors)

   # Generate Dates (Tickets usually close a few days after being created.)
    created_date = fake.date_between(start_date='-365d',end_date='today')
    closed_date = created_date + timedelta(days=random.randint(1,15))

   # Generate Resolution Code
    resolution = random.choice([
    "Resolved",
    "Reboot",
    "Configuration",
    "Replaced",
    "User Error"])

   # Generate Comments (User unable to access email after password reset.)
    comments = fake.sentence()

   # Add the Record (Each iteration creates one operational ticket. After 500 iterations, we'll have 500 ticket records.)
    records.append({
        "Ticket Number": ticket_number,
        "Employee ID": employee_id,
        "Employee Name": employee_name,
        "Department": department,
        "Location": location,
        "Country": country,
        "Priority": priority,
        "Status": status,
        "Category": category,
        "Subcategory": subcategory,
        "Assignment Group": assignment_group,
        "System": system,
        "Vendor": vendor,
        "Created Date": created_date.strftime("%Y-%m-%d"),
        "Closed Date": closed_date.strftime("%Y-%m-%d"),
        "Resolution Code": resolution,
        "Comments": comments
    })

# Convert to a DataFrame(A DataFrame makes it easy to analyze, clean, filter, and export the data.)
    df = pd.DataFrame(records)

# Save the Dataset (The dataset is saved as a CSV file so it can be used in Python, SQL, Excel, and Power BI)
df.to_csv("data\\raw\\operational_data.csv", index=False)

# Preview the Data
print(df.head())

# Verify That We Really Have 500 Records
print("Total Records:", len(df))
print("Total Columns:", len(df.columns))