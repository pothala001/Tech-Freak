
;with cric_overs as -------- Data preparation
(
Select 1 AS balls,2 AS runs
union all
Select 2 AS balls,3 AS runs
union all
Select 3 AS balls,4 AS runs
union all
Select 4 AS balls,6 AS runs
union all
Select 5 AS balls,1 AS runs
union all
Select 6 AS balls,1 AS runs
union all
Select 7 AS balls,2 AS runs
union all
Select 8 AS balls,3 AS runs
union all
Select 9 AS balls,4 AS runs
union all
Select 10 AS balls,4 AS runs
union all
Select 11 AS balls,2 AS runs
union all
Select 12 AS balls,6 AS runs
union all
Select 13 AS balls,2 AS runs
union all
Select 14 AS balls,1 AS runs
union all
Select 15 AS balls,4 AS runs
union all
Select 16 AS balls,1 AS runs
union all
Select 17 AS balls,2 AS runs
union all
Select 18 AS balls,4 AS runs
) ------------------------------- Data preparation
------------------ logic that solves the problem ----------
,cte_flag as 
(
Select
balls,
runs,
CASE
	when balls % 6 = 0 THEN balls / 6
	else (balls / 6) + 1
end as overs
from cric_overs
)
select overs
,SUM(runs) as TotalRunsEachOver
from cte_flag
Group by overs
Order by overs



