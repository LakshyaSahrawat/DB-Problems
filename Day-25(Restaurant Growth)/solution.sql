-- Write your PostgreSQL query statement below
with daily as(
    select visited_on::date as day,
    sum(amount) as daily_amount
    from Customer 
    group by visited_on::date
),
cte as(
    select day , sum(daily_amount) 
    over(order by day range between interval '6 days' preceding and current row) as total_amount
    from daily
    --where day >= (select min(day) + interval '6 days' from daily)
)

select day as visited_on, total_amount as amount, round(total_amount::numeric/7, 2) as average_amount
from cte where day >= (select min(day) + interval '6 days' from daily)