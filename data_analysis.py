#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Create example data
data = [
    [1, "2023-11-24", "CUST001", "Male", 34, "Beauty", 3, 50, 150],
    [2, "2023-11-25", "CUST002", "Female", 28, "Electronics", 1, 500, 500],
    [3, "2023-11-26", "CUST003", "Male", 40, "Clothing", 2, 300, 600],
    [4, "2023-11-27", "CUST004", "Female", 31, "Beauty", 5, 45, 225],
    [5, "2023-12-01", "CUST005", "Male", 25, "Electronics", 2, 450, 900],
    [6, "2023-12-02", "CUST006", "Female", 29, "Clothing", 4, 250, 1000],
]

columns = ["Transaction ID","Date","Customer ID","Gender","Age","Product Category","Quantity","Price per Unit","Total Amount"]

df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv("sales_data.csv", index=False)

print("Sample sales_data.csv created!")


# In[2]:


df = pd.read_csv("sales_data.csv", parse_dates=["Date"])
df.head()


# In[3]:


print(df.info())
print(df.describe())
print(df.isnull().sum())


# In[4]:


# Total sales by product category
sales_by_category = df.groupby("Product Category")["Total Amount"].sum()
print(sales_by_category)

# Total sales by gender
sales_by_gender = df.groupby("Gender")["Total Amount"].sum()
print(sales_by_gender)


# In[5]:


df["Month"] = df["Date"].dt.to_period("M").astype(str)

sales_by_month = df.groupby("Month")["Total Amount"].sum()
print(sales_by_month)


# In[6]:


import matplotlib.pyplot as plt

# Sales by product category (bar chart)
sales_by_category.plot(kind="bar", title="Total Sales by Product Category", ylabel="Total Amount", xlabel="Product Category")
plt.show()

# Sales by month (line chart)
sales_by_month.plot(kind="line", marker="o", title="Monthly Sales Trend", ylabel="Total Amount", xlabel="Month")
plt.show()


# In[7]:


sales_by_category.to_csv("sales_by_category.csv")
sales_by_month.to_csv("sales_by_month.csv")


# In[ ]:




