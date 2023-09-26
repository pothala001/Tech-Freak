
-- Write a SQL query to generate 'n' integers without using a loop
declare @number int = 20

;with cte_recursive(id) as
(
Select 1
union all
Select id+1 from cte_recursive where id < @number
)
select id from cte_recursive 

