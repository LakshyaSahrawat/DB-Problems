-- Write your PostgreSQL query statement below

select customer_number from (
    select customer_number , count(*)
    from Orders 
    group by customer_number
) sub
order by count desc limit 1