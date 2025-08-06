-- Write your PostgreSQL query statement below
with filtered as(
    select id, visit_date, people,
    row_number() over(order by id) as rnk
    from Stadium
    where people >= 100
),
numbered as(
    select id, visit_date, people,
    id - rnk as grp
    from filtered
),
grouped as(
    select grp, count(*)
    from numbered
    group by grp
    having count(*) >= 3
)


select n.id, n.visit_date, n.people
from numbered n
inner join grouped g on n.grp = g.grp
order by n.visit_date;