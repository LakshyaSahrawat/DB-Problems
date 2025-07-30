-- Write your PostgreSQL query statement below
with duplicates as(
    select id, email, row_number() over(partition by email order by id) as row_number
    from Person
)

delete from Person where id in (select id from duplicates where row_number > 1)