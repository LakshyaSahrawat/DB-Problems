-- Write your PostgreSQL query statement below
select Department, Employee, Salary from (
    select d.name as Department, 
    e.name as Employee, 
    e.salary as Salary, 
    dense_rank() over(partition by e.departmentId order by salary desc) as rank
    from Employee e 
    inner join Department d on e.departmentId = d.id
)
where rank in (1,2,3)
order by Salary desc;