-- Write your PostgreSQL query statement below
select * 
from Cinema where description not ilike 'boring' and id % 2 != 0 
order by rating desc;