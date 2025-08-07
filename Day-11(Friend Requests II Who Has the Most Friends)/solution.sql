-- Write your PostgreSQL query statement below
with all_friends as(
    select requester_id as user_id
    from RequestAccepted
    union all
    select accepter_id as user_id
    from RequestAccepted 
),
count_friends as(
    select user_id, count(*) as frd_count
    from all_friends
    group by user_id
),
max_count as(
    select max(frd_count) as max_frd_count
    from count_friends
    )

select user_id as id, frd_count as num
from count_friends, max_count
where frd_count = max_frd_count;