-- Write your PostgreSQL query statement below
with cte as(
    select
    tiv_2016,
    count(*) over(partition by tiv_2015) as tiv_2015_count,
    count(*) over(partition by lat, lon) as lat_lon_count
    from Insurance
)

select round(sum(tiv_2016)::Numeric, 2) as tiv_2016 from cte
where tiv_2015_count > 1 and lat_lon_count = 1