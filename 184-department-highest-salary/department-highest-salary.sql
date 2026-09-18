# Write your MySQL query statement below
with t as(
select  
d.name as Department,
e.name as Employee,
e.Salary as Salary
from Employee e
left join department d
on e.departmentId=d.id 
)
,t1 as(
select Department,Employee,Salary,
dense_rank() over(partition by department order by salary desc ) r
from t
)
select Department,Employee,Salary
from t1
where r=1