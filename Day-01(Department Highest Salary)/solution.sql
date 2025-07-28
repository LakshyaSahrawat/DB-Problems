-- Write your PostgreSQL query statement below

with employees_ranked as(
    select d.name as Department, e.name as Employee, e.salary as Salary, rank() over(partition by e.departmentId order by salary desc) as Rank
    from Employee e
    inner join Department d on e.departmentId = d.id
)

select Department, Employee, Salary 
from employees_ranked where Rank = 1;



-----------------------------------------------------------------------------------------




-- Write your PostgreSQL query statement below
select Department, Employee, Salary from (
    select d.name as Department, e.name as Employee, e.salary as Salary, rank() over(partition by e.departmentId order by salary desc) as Rank
    from Employee e
    inner join Department d on e.departmentId = d.id
)
where Rank = 1;

