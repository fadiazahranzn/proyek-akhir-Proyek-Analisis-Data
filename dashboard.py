# Import libraries
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('final_combined_data.csv')

# Convert order_purchase_timestamp to datetime
data['order_purchase_timestamp'] = pd.to_datetime(data['order_purchase_timestamp'])

# Streamlit app title
st.title("E-Commerce Data Dashboard")
st.title("by:Fadia Zahran Zain")

# Sidebar for navigation
st.sidebar.header("Navigation")
options = st.sidebar.selectbox("Select an option:", 
                                 ["Overview", "Sales Performance", "Product Insights", "Customer Insights"])

# Overview page
if options == "Overview":
    st.header("Overview")
    st.write(data.head())
    st.write("Total records:", data.shape[0])

# Sales Performance page
elif options == "Sales Performance":
    st.header("Sales Performance")
    
    # Monthly sales revenue
    monthly_sales_revenue = data.resample('M', on='order_purchase_timestamp').agg({
        'order_id': 'nunique',
        'price': 'sum'
    }).reset_index()
    
    monthly_sales_revenue.columns = ['Order Date', 'Total Orders', 'Total Revenue']
    
    # Plotting
    st.line_chart(monthly_sales_revenue.set_index('Order Date')[['Total Orders', 'Total Revenue']])
    st.write(monthly_sales_revenue)

# Product Insights page
elif options == "Product Insights":
    st.header("Product Insights")
    
    # Top 10 products by sales
    product_sales = data.groupby('product_id').agg({
        'order_id': 'nunique',
        'price': 'sum'
    }).reset_index()
    
    product_sales.columns = ['Product ID', 'Total Orders', 'Total Revenue']
    top_products = product_sales.sort_values(by='Total Orders', ascending=False).head(10)
    
    st.bar_chart(top_products.set_index('Product ID')['Total Orders'])
    st.write(top_products)

# Customer Insights page
elif options == "Customer Insights":
    st.header("Customer Insights")
    
    # Customer distribution by city
    customer_city_counts = data['customer_city'].value_counts().head(10)
    
    st.bar_chart(customer_city_counts)
    st.write(customer_city_counts)

# Run the app
if __name__ == "__main__":
    st.write("Dashboard is running...")