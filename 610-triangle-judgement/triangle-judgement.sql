# Write your MySQL query statement below
select x,y,z,
CASE
WHEN x+y>z
AND Y+Z>X
AND Z+X>Y
THEN 'Yes'
else 'No'  
end as triangle
from triangle