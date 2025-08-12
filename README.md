# International E-Commerce Sales Analysis

## 🎯 Project Objective
This project simulates the role of a Data Analyst in an international e-commerce company. The goal is to analyze sales, customers, products, and countries to answer key business questions such as:

- Who are the top customers?
- Which products are the best sellers?
- Which countries generate the most revenue?
- What are the sales trends over time?

## 📦 Dataset
**Source:** [UCI Machine Learning Repository – Online Retail Dataset (UK)](https://archive.ics.uci.edu/ml/datasets/Online+Retail)

- Real transactions from a UK-based online retailer (2010–2011)
- Fields: InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country
- Format: Provided as .xlsx, converted to PostgreSQL and pandas DataFrame for analysis

## 🔧 Project Architecture & Tools
The project follows a complete data analysis pipeline, using industry-standard tools:

1. **Data Import:** Loaded the dataset into a PostgreSQL database (SQL)
2. **Data Exploration & Cleaning:** Wrote SQL queries for initial exploration and cleaning
3. **Data Extraction:** Imported query results into Python using `pandas` and `SQLAlchemy`
4. **Data Cleaning & Transformation:** Performed further cleaning, transformation, and aggregation in `pandas`
5. **Visualization:** Created insightful visualizations using `matplotlib`
6. **Export:** Exported results to CSV for reporting and documentation
7. **Documentation:** Documented the project with a README and visualization images

## 🧠 Business Questions Answered
The analysis addresses real-world business questions, including:

### 📊 Sales
- How many orders were placed each month?
- What is the total and average revenue per country?
- What are the top 10 most sold products?

### 🧍 Customers
- Who are the top 10 customers by total spending?
- Which customers purchase most frequently?
- Which customers have the highest average order value?

### 📦 Products
- Which products are most frequently returned (negative quantity)?
- Is there seasonality in product sales?

## 📈 Example Visualizations
The project includes three visualizations:
- Top 10 countries by total revenue
- Top 10 most sold products
- Distribution of sales among top products

## 🚀 Technologies Used
- **SQL** (PostgreSQL) for data storage and querying
- **Python** (`pandas`, `sqlalchemy`, `matplotlib`)
- **CSV/Excel** for data export

## 📂 Repository Structure
- `dataCleaning.py`: Data cleaning and quality checks
- `dataVisualization.py`: Data extraction, analysis, and visualization
- `onlineRetail.sql`: SQL queries for exploration and aggregation
- `OnlineRetailCSV.csv` / `OnlineRetail_cleaned.csv`: Raw and cleaned datasets
- Visualization images: Example output charts
- `README.md`: Project documentation