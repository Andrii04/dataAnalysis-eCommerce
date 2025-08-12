
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from db_config import DB_CONFIG

engine = create_engine(
  f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)


#queries and visualization

#-- total and average revenue of each country
query1 = """
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
"""

df_countries = pd.read_sql_query(query1, engine)
df_top = df_countries.head(10)

plt.figure(figsize=(12, 6))
bars = plt.bar(df_top["country"], df_top["total_revenue"], color="skyblue")
plt.xlabel("Country")
plt.ylabel("Total Revenue")
plt.title("Top 10 Countries based on Total Revenue")
plt.xticks(rotation=45)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{int(yval):,}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()

#-- top 10 most sold products
query2 = """
SELECT stockcode, SUM(quantity) AS total_sold
FROM onlineretail_cleaned
GROUP BY stockcode
ORDER BY total_sold DESC
LIMIT 10;
"""

df_prod = pd.read_sql_query(query2, engine)

plt.figure(figsize=(12, 6))
bars = plt.barh(df_prod["stockcode"], df_prod["total_sold"], color="purple")
plt.xlabel("Total Sold")
plt.ylabel("Product Code")
plt.title("Top 10 Most Sold Products")
plt.gca().invert_yaxis()

for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{int(bar.get_width()):,}', va='center', ha='left', fontsize=9)

plt.tight_layout()

#-- pie chart: distribution of total spent between the 10 most sold products
query3 = """
SELECT stockcode, SUM(quantity) AS total_sold
FROM onlineretail_cleaned
GROUP BY stockcode
ORDER BY total_sold DESC
LIMIT 10;
"""

df_pie_prod = pd.read_sql_query(query3, engine)

explode = [0.15] + [0]*(len(df_pie_prod["total_sold"])-1)
plt.figure(figsize=(12, 6))
plt.pie(
    df_pie_prod["total_sold"],
    labels=df_pie_prod["stockcode"],
    autopct="%1.1f%%",
    startangle=140,
    colors=plt.cm.Set3.colors,
    explode=explode
)

plt.title("Distribution of total spent between the 10 Most Sold Products")
plt.tight_layout()
plt.show()
