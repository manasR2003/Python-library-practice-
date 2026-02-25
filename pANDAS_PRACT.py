import pandas as pd

data = {
    "EmpID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Karan", "Anita", "Vikram", "Pooja"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "IT"],
    "Salary": [60000, 45000, 70000, 50000, 48000, 75000, 52000, 68000],
    "Experience": [2, 4, 5, 3, 6, 7, 2, 4],
    "City": ["Bangalore", "Mumbai", "Delhi", "Mumbai", "Delhi", "Bangalore", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)
print(df.to_string())

# Display first 5 rows.
print(df.head())

# Show column names.
print(df.columns)

# Find total number of employees.
print(len(df))

# Get employees from IT department.
print(df.loc[df["Department"]=="IT"])

# Find average salary.
print(df["Salary"].mean())

# Find highest salary employee.
print(df["Salary"].max())

# Find employees with salary > 60000.
print(df.loc[df["Salary"]>60000])

# Count employees in each department.
print(df.groupby("Department").size())

# Find average salary department-wise.
print(df.groupby("Department")["Salary"].mean())

# Sort employees by experience (descending).
print(df.sort_values(by="Experience", ascending=False))

# Add new column Bonus (10% of Salary).
df["Bonus"]=df["Salary"]*0.2
print(df.to_string())

# Increase salary by 5% for IT department.
df["Salary"]=df["Salary"]+df["Salary"]*0.05
print(df.to_string())

# Find second highest salary.
print(df.sort_values(by="Salary",ascending=False).iloc[1])

# Group by City and find total salary.
print(df.groupby("City")["Salary"].sum())

# Find employees whose experience is above average.
print(df["Experience"].mean())
print(df.loc[df["Experience"]>df["Experience"].mean()])

import pandas as pd

sales_data = {
    "OrderID": [1,2,3,4,5,6,7,8,9,10],
    "Product": ["Laptop","Mobile","Tablet","Laptop","Mobile","Tablet","Laptop","Mobile","Tablet","Laptop"],
    "Category": ["Electronics","Electronics","Electronics","Electronics","Electronics","Electronics","Electronics","Electronics","Electronics","Electronics"],
    "Price": [55000,20000,15000,60000,22000,14000,58000,21000,16000,62000],
    "Quantity": [1,2,1,1,3,2,1,2,1,1],
    "City": ["Delhi","Mumbai","Delhi","Bangalore","Mumbai","Delhi","Bangalore","Mumbai","Delhi","Bangalore"]
}

sales_df = pd.DataFrame(sales_data)
print(sales_df.to_string())

# Calculate total revenue (Price × Quantity).
print(sales_df["Price"]*sales_df["Quantity"])

# Find total sales per product.
print(sales_df.groupby("Product")["Quantity"].sum())

# Show unique cities.
print(sales_df["City"].unique())

# Find city with highest sales.
print(sales_df.groupby("City").max().iloc[0])

# Find most sold product (by quantity).
print(sales_df.groupby("Product")["Quantity"].sum().idxmax())

# Find average price of products.
print(sales_df.groupby("Product")["Price"].mean())

# Add column TotalAmount.
sales_df["TotalAmount"]=sales_df["Price"]*sales_df["Quantity"]
print(sales_df.to_string())

# Find top 3 highest revenue orders.
print(sales_df.sort_values(by="TotalAmount",ascending=False).head(3))

# Group by City and Product and calculate total revenue.
print(sales_df.groupby(["City","Product"])["TotalAmount"].sum())

# Find percentage contribution of each product in total sales.
result = (
    sales_df.groupby("Product")["Quantity"]
    .sum()
    .reset_index()
)

result["Percentage"] = (result["Quantity"] / result["Quantity"].sum()) * 100

print(result)                                                                                                         