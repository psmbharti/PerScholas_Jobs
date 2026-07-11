\# Global Operations Clean Data Project



\## Project Overview



This project demonstrates an end-to-end \*\*Global Operations Data Quality Initiative\*\* similar to work performed by a Data Analyst supporting enterprise operational systems such as \*\*ServiceNow\*\*.



The objective is to improve the quality, consistency, and governance of operational data by analyzing existing data, identifying quality issues, cleaning and standardizing records, validating against master data, documenting governance rules, assessing risks, and delivering executive reporting.



\---



\# Business Problem



Operational data collected from multiple systems often contains:



\- Duplicate records

\- Missing values

\- Invalid employee IDs

\- Inconsistent department names

\- Incorrect priority values

\- Invalid ticket status values

\- Data governance issues

\- Poor reporting quality



Poor-quality data impacts:



\- Operational reporting

\- Automation

\- Decision-making

\- SLA reporting

\- Executive dashboards



This project demonstrates how those issues can be identified and resolved using Python, SQL, and Power BI.



\---



\# Project Objectives



\- Generate operational ticket data

\- Simulate real-world data quality issues

\- Profile operational data

\- Assess data quality

\- Clean and standardize records

\- Normalize operational data

\- Validate against master data

\- Perform UAT testing

\- Create governance documentation

\- Perform risk analysis

\- Generate KPI reports

\- Build an executive Power BI dashboard



\---



\# Technologies Used



\- Python

\- Pandas

\- Faker

\- ReportLab

\- MySQL

\- GitHub



\---



\# Project Structure



GLOBAL\_OPERATIONS\_CLEAN\_DATA\_PROJECT



│

├── data

│

│   ├── raw

│   │     operational\_data.csv

│   │     operational\_data\_dirty.csv

│   │

│   ├── processed

│   │     clean\_operational\_data.csv

│   │     mapped\_operational\_data.csv

│   │

│   ├── master

│   │     employee\_master.csv

│   │     department\_master.csv

│   │

│   ├── quality

│   │     data\_profile\_report.csv

│   │     data\_quality\_report.csv

│   │     validation\_report.csv

│   │     uat\_test\_results.csv

│   │

│   ├── governance

│   │     data\_dictionary\_governance.csv

│   │     data\_risk\_register.csv

│   │

│   └── reporting

│         kpi\_summary.csv

│         Department Ticket Report.csv

│

├── python

│     generate\_dataset.py

│     introduce\_data\_quality\_issues.py

│     generate\_master\_data.py

│

│     step1\_analysis.py

│     step2\_data\_profiling.py

│     step3\_data\_quality.py

│     step4\_data\_cleaning.py

│     step5\_mapping.py

│     step6\_validation.py

│     step7\_testing.py

│     step8\_data\_dictionary\_governance.py

│     step9\_risk\_analysis.py

│     step10\_reporting.py

│     create\_reports.py

│

├── sql

│     database.sql

│     load\_data.sql

│     queries.sql

│

├── ClaudeAI

│     Dashboard.HTML

│

├── reports

│     Data\_Quality\_Report.pdf

│     UAT\_Test\_Report.pdf

│     Risk\_Assessment\_Report.pdf

│

├── requirements.txt

│

└── README.md

```



\---



\# Workflow



```

Generate Operational Data

&#x20;           │

&#x20;           ▼

Introduce Data Quality Issues

&#x20;           │

&#x20;           ▼

Data Profiling

&#x20;           │

&#x20;           ▼

Data Quality Assessment

&#x20;           │

&#x20;           ▼

Data Cleaning

&#x20;           │

&#x20;           ▼

Data Mapping

&#x20;           │

&#x20;           ▼

Master Data Validation

&#x20;           │

&#x20;           ▼

UAT Testing

&#x20;           │

&#x20;           ▼

Data Dictionary \& Governance

&#x20;           │

&#x20;           ▼

Risk Assessment

&#x20;           │

&#x20;           ▼

Reporting Automation

&#x20;           │

&#x20;           ▼

HTML Dashboard(ClaudeAI)

```



\---



\# Project Steps



\## Step 1 – Dataset Generation



Generated \*\*500 ServiceNow-style operational ticket records\*\* including:



\- Ticket Number

\- Employee

\- Department

\- Priority

\- Status

\- Category

\- Assignment Group

\- Vendor

\- Created Date

\- Closed Date



\---



\## Step 2 – Data Profiling



Performed:



\- Row count

\- Column count

\- Missing value analysis

\- Duplicate detection

\- Data type inspection

\- Descriptive statistics



Output:



```

data\_profile\_report.csv

```



\---



\## Step 3 – Data Quality Assessment



Identified:



\- Missing values

\- Duplicate records

\- Invalid Employee IDs

\- Invalid dates

\- Department inconsistencies



Output:



```

data\_quality\_report.csv

```



\---



\## Step 4 – Data Cleaning



Performed:



\- Duplicate removal

\- Missing value treatment

\- Employee ID correction

\- Department standardization

\- Priority normalization

\- Date correction

\- Text formatting



Output:



```

clean\_operational\_data.csv

```



\---



\## Step 5 – Data Mapping



Mapped operational values into standardized governance values.



Examples:



|Original|Mapped|

|----------|--------|

|IT|Information Technology|

|High|HIGH|

|Open|NEW|



Output:



```

mapped\_operational\_data.csv

```



\---



\## Step 6 – Validation



Validation Rules:



\- Ticket uniqueness

\- Employee master validation

\- Department validation

\- Priority validation

\- Status validation

\- Date validation



Output:



```

validation\_report.csv

```



\---



\## Step 7 – UAT Testing



Created automated User Acceptance Tests.



Examples:



\- Ticket uniqueness

\- Master data validation

\- Required field validation

\- Date sequence validation



Output:



```

uat\_test\_results.csv

```



\---



\## Step 8 – Data Governance



Created:



\- Data Dictionary

\- Business Definitions

\- Validation Rules

\- Data Owners

\- Source Systems



Output:



```

data\_dictionary\_governance.csv

```



\---



\## Step 9 – Risk Assessment



Identified risks across:



\- People

\- Process

\- Data

\- Systems



Output:



```

data\_risk\_register.csv

```



\---



\## Step 10 – Reporting



Generated:



\- KPI Summary

\- Department Ticket Report

\- Automated PDF Reports



Outputs:



```

kpi\_summary.csv



Department Ticket Report.csv



Data\_Quality\_Report.pdf



UAT\_Test\_Report.pdf



Risk\_Assessment\_Report.pdf

```



\---



\## Step 11 – ClaudeAI Dashboard



Dashboard Pages:



\### Executive KPI



\- Total Tickets

\- Open Tickets

\- Closed Tickets

\- High Priority Tickets



\### Data Quality



\- Validation Results

\- UAT Results

\- Quality Score



\### Ticket Operations



\- Status Distribution

\- Priority Analysis

\- Category Analysis



\### Department Performance



\- Department Workload

\- Location Analysis

\- Assignment Group



\### Risk \& Governance



\- Risk Register

\- Severity Analysis

\- Governance Metrics



\---



\# SQL Components



Created:



\- Database

\- Operational Tables

\- Master Tables

\- Validation Queries

\- Reporting Queries



Files:



```

database.sql



load\_data.sql



queries.sql

```



\---



\# Key Skills Demonstrated



\- Data Analysis

\- Data Profiling

\- Data Cleaning

\- Data Normalization

\- Data Mapping

\- Data Validation

\- UAT Testing

\- Data Governance

\- Risk Assessment

\- SQL Query Development

\- KPI Reporting

\- Dashboard Development(ClaudeAI)

\- Python Automation



\---



\# Business Impact



This project demonstrates how a Data Analyst can:



\- Improve operational data quality

\- Reduce reporting errors

\- Standardize enterprise data

\- Strengthen governance

\- Improve operational reporting

\- Support business decision-making

\- Enable reliable analytics



\---



\# Future Enhancements



\- ServiceNow API integration

\- Automated ETL pipeline

\- Scheduled data quality monitoring

\- Email alerts for validation failures

\- Azure SQL integration

\- Azure Data Factory pipeline



\---



\# Author



\*\*Madhu Bharti\*\*



\*\*Tools:\*\* Python | Pandas |  MySQL | ClaudeAI | GitHub



