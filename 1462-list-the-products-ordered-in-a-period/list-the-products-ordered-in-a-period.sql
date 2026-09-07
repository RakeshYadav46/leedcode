# Write your MySQL query statement below
select product_name,SUM(e1.unit) as unit
from products p1
left join orders e1
on p1.product_id=e1.product_id
where e1.order_date >='2020-02-01' and e1.order_date <'2020-03-01'
group by e1.product_id
having sum(e1.unit)>=100 