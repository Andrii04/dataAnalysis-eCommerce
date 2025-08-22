-- how many orders each day
select invoicedate, count(*)
from onlineretail_cleaned
group by invoicedate
order by count(*) desc;


-- total and average revenue of each country
WITH order_totals AS (
  SELECT 
    country,
    invoiceno,
    SUM(unitprice * quantity) AS order_revenue
  FROM onlineretail_cleaned
  GROUP BY country, invoiceno
)
SELECT
  country,
  SUM(order_revenue) AS total_revenue,
  AVG(order_revenue) AS average_order_revenue
FROM order_totals
GROUP BY country
ORDER BY total_revenue DESC;


-- top 10 most sold products
select stockcode, sum(quantity) as total_sold
from onlineretail_cleaned
group by stockcode
order by total_sold desc
limit 10;


-- top 10 clients based on total spent
select customerid, sum(unitprice * quantity) as total_spent
from onlineretail_cleaned
group by customerid
order by total_spent desc
limit 10;


-- top 10 clients based on number of orders placed
SELECT customerid, COUNT(DISTINCT invoiceno) AS order_count
FROM onlineretail_cleaned
GROUP BY customerid
ORDER BY order_count DESC
LIMIT 10;


-- top 10 clients based on average spent per order
SELECT customerid, AVG(order_total) AS average_order_cost
FROM (
    SELECT customerid, invoiceno, SUM(unitprice * quantity) AS order_total
    FROM onlineretail_cleaned
    GROUP BY customerid, invoiceno
) t
GROUP BY customerid
ORDER BY average_order_cost DESC
LIMIT 10;


-- most returned products (negative quantity)
select stockcode, sum(quantity) as quantity_sold
from onlineretail_cleaned
group by stockcode
order by quantity_sold asc
limit 10;


-- checks if there's seasonality for products, (which month they're most sold in)
with sub4 as 
(
select stockcode, extract(month from invoicedate) as month, count(*) as times_ordered
from onlineretail_cleaned
group by stockcode, extract(month from invoicedate)
order by stockcode, times_ordered desc
)
select distinct on (stockcode)
stockcode, month, times_ordered
from sub4
order by stockcode, times_ordered desc;



