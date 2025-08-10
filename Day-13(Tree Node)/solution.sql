-- Write your PostgreSQL query statement below
with cte_tree as(
    select t1.id as id, t1.p_id as parent_node, t2.id as child_node
    from Tree t1 left join Tree t2 on t1.id = t2.p_id
)

select distinct id,
case when parent_node is null then 'Root'
when parent_node is not null and child_node is not null then 'Inner'
else 'Leaf' end as type
from cte_tree order by id