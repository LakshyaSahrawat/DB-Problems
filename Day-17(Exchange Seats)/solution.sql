-- Write your PostgreSQL query statement below
-- select
-- case when id % 2 = 1 and id + 1 <= (select max(id) from Seat) then id + 1
-- when id % 2 = 0 then id - 1
-- else id end as id, student
-- from Seat 
-- order by id asc;

with cte as(
    select id,
    LAG(id) over(order by id) as prev_id,
    LEAD(id) over(order by id) as next_id,
    max(id) over() as max_id,
    student
    from Seat
)

select
case when id % 2 = 1 and id + 1 <= max_id then next_id
when id % 2 = 0 then prev_id
else id end as id, student
from cte order by id asc;