-- Write your PostgreSQL query statement below
with cte as(
    select actor_id, director_id , count(*) as count
    from ActorDirector
    group by actor_id, director_id
    having count(*)>=3
)

select actor_id, director_id from cte;