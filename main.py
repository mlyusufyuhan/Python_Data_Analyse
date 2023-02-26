import pandas as pd

# Load the sales data from a CSV file
sales_data = pd.read_csv('sales_data.csv')

# Add month and day_of_week columns
sales_data['order_date'] = pd.to_datetime(sales_data['order_date'])
sales_data['month'] = sales_data['order_date'].dt.month
sales_data['day_of_week'] = sales_data['order_date'].dt.day_name()

# Calculate the total revenue
total_revenue = sales_data['price'].sum()

# Identify the top 10 most popular products
popular_products = sales_data.groupby('product_name').size().nlargest(10)

# Identify the most common purchase patterns
purchase_patterns = sales_data.groupby(['month', 'day_of_week']).size().idxmax()

# Identify the customer demographics
customer_demographics = sales_data.groupby(['customer_age', 'customer_gender']).size().unstack()

# Print the results
print(f'Total revenue: ${total_revenue}')
print(f'Top 10 most popular products:\n{popular_products}')
print(f'Most common purchase pattern: {purchase_patterns}')
print(f'Customer demographics:\n{customer_demographics}')