-- Write your PostgreSQL query statement below
with cte as(
    select * , dense_rank() over(partition by product_id order by year asc) as rnk
    from Sales
)

select product_id, year as first_year, quantity, price from cte where rnk = 1;