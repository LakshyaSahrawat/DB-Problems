-- Write your PostgreSQL query statement below
with cte as(
    select p.product_id, u.units, p.price * u.units as amount
    from Prices p left join UnitsSold u on p.product_id = u.product_id and u.purchase_date between p.start_date and p.end_date
)

-- select * from cte

select product_id, case when round(sum(amount)::numeric/sum(units), 2) is null then 0 else round(sum(amount)::numeric/sum(units), 2) end as average_price
from cte
group by product_id