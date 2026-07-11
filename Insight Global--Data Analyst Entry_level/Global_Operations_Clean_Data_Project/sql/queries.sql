USE global_operations;

-- ============================================
-- 1. Total Tickets
-- ============================================

SELECT
COUNT(*) AS Total_Tickets

FROM tickets;

-- ============================================
-- 2. Ticket Status Summary
-- ============================================

SELECT

statusN,

COUNT(*) AS Ticket_Count

FROM tickets

GROUP BY statusN;




-- ============================================
-- 3. Priority Analysis
-- ============================================


SELECT

priority,

COUNT(*) AS Ticket_Count

FROM tickets

GROUP BY priority

ORDER BY Ticket_Count DESC;



-- ============================================
-- 4. Department Workload
-- ============================================


SELECT
department,
COUNT(*) AS Total_Tickets
FROM tickets
GROUP BY department
ORDER BY Total_Tickets DESC;



-- ============================================
-- 5. Monthly Ticket Trend
-- ============================================


SELECT
MONTH(CreatedDate) AS Month,
COUNT(*) AS Ticket_Count
FROM tickets
GROUP BY MONTH(CreatedDate)
ORDER BY Month;



-- ============================================
-- 6. Closed Ticket Percentage
-- ============================================


SELECT
ROUND(
SUM(
CASE
WHEN statusN IN ('CLOSED','RESOLVED')
THEN 1
ELSE 0
END
)
/
COUNT(*) * 100,2) AS Resolution_Percentage
FROM tickets;



-- ============================================
-- 7. High Priority Tickets
-- ============================================


SELECT *
FROM tickets
WHERE priority IN
(
'HIGH',
'CRITICAL'
);

-- ============================================
-- 8. Employee Validation
-- Find tickets with invalid employees
-- ============================================

SELECT
t.TicketNumber,
t.EmployeeID
FROM tickets t
LEFT JOIN employee_master e
ON t.EmployeeID=e.EmployeeID
WHERE e.EmployeeID IS NULL;

-- ============================================
-- 9. Department Governance Check
-- ============================================

SELECT
t.Department
FROM tickets t
LEFT JOIN department_master d
ON t.Department=d.Department
WHERE d.Department IS NULL;

-- ============================================
-- 10. Duplicate Ticket Check
-- ============================================

SELECT

TicketNumber,
COUNT(*) AS Duplicate_Count

FROM tickets

GROUP BY TicketNumber

HAVING COUNT(*) > 1;



-- ============================================
-- 11. Date Quality Check
-- ============================================


SELECT *
FROM tickets
WHERE ClosedDate < CreatedDate;



-- ============================================
-- 12. Risk Summary
-- ============================================


SELECT
RiskCategory,
severity,
COUNT(*) AS Risk_Count
FROM risk_register
GROUP BY
RiskCategory,
severity;