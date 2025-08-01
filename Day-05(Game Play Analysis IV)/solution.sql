-- Write your PostgreSQL query statement below

--using sub query

-- select round((
--     SELECT COUNT(*)
--     FROM Activity a1
--     INNER JOIN Activity a2 ON a1.player_id = a2.player_id
--     AND a2.event_date - a1.event_date = 1
--     WHERE a1.event_date = (
--         SELECT MIN(a3.event_date)
--         FROM Activity a3
--         where a3.player_id = a1.player_id
--     )
-- )::NUMERIC/
-- (
--     SELECT COUNT(DISTINCT player_id)
--     FROM Activity
-- ), 2) as fraction


--using cte
WITH first_logins AS(
    SELECT player_id , MIN(event_date) as event_date
    FROM Activity 
    GROUP BY player_id
),
second_logins AS(
    SELECT a.player_id
    FROM first_logins f
    JOIN Activity as a 
    on f.player_id = a.player_id
    and a.event_date - f.event_date = 1
)

SELECT ROUND(
    (
        SELECT COUNT(*) FROM second_logins
    )::NUMERIC/
    (
        SELECT COUNT(*) FROM first_logins
    ) , 2
) as fraction