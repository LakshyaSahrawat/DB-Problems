-- Write your PostgreSQL query statement below
-- select project_id, Round(sum(experience_years)::numeric/count(project_id)::numeric, 2) as average_years
-- from Project p left join Employee e on p.employee_id = e.employee_id
-- group by project_id order by project_id


select project_id, Round(AVG(e.experience_years), 2) as average_years
from Project p inner join Employee e on p.employee_id = e.employee_id
group by project_id