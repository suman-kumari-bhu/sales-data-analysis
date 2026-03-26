import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
# (You can replace this with your own CSV file)
df = pd.read_csv("sales_data.csv")

# Preview data
print("First 5 rows:")
print(df.head())

# Basic info
print("\nDataset Info:")
print(df.info())

# Total sales
total_sales = df["Revenue"].sum()
print(f"\nTotal Revenue: {total_sales}")

# Sales by product
sales_by_product = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
print("\nSales by Product:")
print(sales_by_product)

# Sales by region
sales_by_region = df.groupby("Region")["Revenue"].sum()
print("\nSales by Region:")
print(sales_by_region)

# Plot: Sales by Product
sales_by_product.plot(kind="bar", title="Sales by Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_by_product.png")
plt.show()
