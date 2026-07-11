-- ============================================
-- GLOBAL OPERATIONS DATA QUALITY DATABASE
-- ============================================


CREATE DATABASE global_operations;

USE global_operations;



-- ============================================
-- Ticket Operational Table
-- ============================================
drop table operational_tickets;
CREATE TABLE tickets (
    TicketNumber        VARCHAR(20),
    EmployeeID          VARCHAR(20),
    EmployeeName        VARCHAR(100),
    Department           VARCHAR(50),
    Location             VARCHAR(50),
    Country              VARCHAR(50),
    Priority             VARCHAR(20),
    StatusN               VARCHAR(20),
    Category             VARCHAR(50),
    Subcategory          VARCHAR(50),
    AssignmentGroup     VARCHAR(50),
    SystemN              VARCHAR(50),
    Vendor               VARCHAR(50),
    CreatedDate         DATE,
    ClosedDate          DATE,
    ResolutionCode      VARCHAR(50),
    Comments             TEXT
);



-- ============================================
-- Employee Master Table
-- ============================================

drop table employee_master;
CREATE TABLE employee_master (

    EmployeeID VARCHAR(20) PRIMARY KEY,

    EmployeeName VARCHAR(100),

    Department VARCHAR(100),

    Location VARCHAR(50),

    Country VARCHAR(50)

);



-- ============================================
-- Department Master Table
-- ============================================

drop table department_master;

CREATE TABLE department_master (

    DepartmentID VARCHAR(10) PRIMARY KEY,

    Department VARCHAR(100)

  );



-- ============================================
-- Validation Report Table
-- ============================================

drop table validation_results;
CREATE TABLE validation_results (

        TestCase VARCHAR(200),

    Expected VARCHAR(200),

    Actual INT,

    statusR VARCHAR(10)

);



-- ============================================
-- UAT Testing Table
-- ============================================

drop table uat_results;
CREATE TABLE uat_results (

    TestCaseID VARCHAR(20) PRIMARY KEY,

    TestScenario VARCHAR(200),

    ExpectedResult VARCHAR(200),

    ActualResult INT,

    StatusR VARCHAR(10)

);



-- ============================================
-- Risk Register Table
-- ============================================

drop table risk_register;
CREATE TABLE risk_register (

   RiskID VARCHAR(10) PRIMARY KEY,

   RiskCategory VARCHAR(50),

    RiskDescription TEXT,

    Impact TEXT,

    Severity VARCHAR(20),

    RootCause TEXT,

    MitigationPlan TEXT,

   OwnerN VARCHAR(100)

);