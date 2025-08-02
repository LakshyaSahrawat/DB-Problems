SELECT e.name
FROM Employee e
INNER JOIN
    (
    SELECT managerId, count(*)
    FROM Employee e1
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    ) AS emp
ON emp.managerId = e.id
where emp.count >= 5