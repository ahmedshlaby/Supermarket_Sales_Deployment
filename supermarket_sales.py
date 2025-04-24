
import pandas as pd
import plotly.express as px
import streamlit as st

#page layout
st.set_page_config(page_title="Supermarket Sales Dashboard", layout="wide", page_icon= '🛒')


st.title("🛒 Supermarket Sales Dashboard")

#read dataframe
df = pd.read_csv("supermarket_clean_df.csv", index_col = 0)
st.dataframe(df.head())

#sidebar
st.sidebar.header("📊 Select Analysis")

analysis = st.sidebar.selectbox("Choose a question to explore:", [
    "Most Sold Product Line",
    "Gross Income by Product Line",
    "Average Spending by Gender",
    "Average Daily Sales per Branch",
    "Payment Methods",
    "Average Total Spent by Payment Method",
    "City With The Most Revenue",
    "Sales by Day of Week"
])

#visualization
if analysis == "Most Sold Product Line":
    col_1, col_2 = st.columns(2, vertical_alignment= 'center')
    col_1.subheader("Which product line is sold the most?")
    product_sales = df.groupby('Product line')['Quantity'].sum().sort_values(ascending= False).reset_index()
    col_2.plotly_chart(px.bar(product_sales, x= 'Product line', y= 'Quantity', text_auto= True))
elif analysis == "Gross Income by Product Line":
    st.header("Which product line generates the highest gross income?")
    product_income = df.groupby('Product line')['gross income'].sum().round(2).sort_values(ascending= False).reset_index()
    st.plotly_chart(px.bar(product_income, x='Product line', y='gross income', text_auto= True))

elif analysis == "Average Spending by Gender":
    st.header("Who spends more on average — males or females?")
    avg_spend = df.groupby('Gender')['Total'].mean().round(2).reset_index()
    st.plotly_chart(px.bar(data_frame= avg_spend, x= 'Gender', y= 'Total',labels = {"Total": "Average Spending"}, text_auto= True))
    st.plotly_chart(px.pie(data_frame= avg_spend, names= "Gender",values= 'Total'))

elif analysis == "Average Daily Sales per Branch":
    st.header("What is the average daily sales per branch?")
    daily_sales = df.groupby(['Branch', 'Date'])['Total'].sum().reset_index()
    avg_daily_sales = daily_sales.groupby('Branch')['Total'].mean().round(2).sort_values(ascending= False).reset_index()
    avg_daily_sales.columns = ['Branch', 'Average Daily Sales']
    st.plotly_chart(px.bar(data_frame= avg_daily_sales, x= 'Branch', y='Average Daily Sales', text='Average Daily Sales'))

elif analysis == "Payment Methods":
    st.header("What is the most common payment method?")
    payment_counts = df['Payment'].value_counts().reset_index()
    st.plotly_chart(px.bar(payment_counts, x= 'Payment', y= 'count' ,text_auto= True))

elif analysis == "Sales by Day of Week":
    st.header("Which day of the week has the highest sales?")
    day_of_the_week = df.groupby('Day')['Total'].sum().round(2).sort_values(ascending=False).reset_index()
    st.plotly_chart(px.bar(day_of_the_week, x= 'Day', y= 'Total', text_auto= '%1.2f%%'))

elif analysis == "Average Total Spent by Payment Method":
    st.header("Does the payment method affect the total amount spent?")
    payment_avg = df.groupby('Payment')['Total'].mean().round(2).reset_index()
    payment_avg.columns = ['Payment Method', 'Average Total Spent']
    st.plotly_chart(px.bar(payment_avg, x='Payment Method', y='Average Total Spent',text_auto= True))

elif analysis == "City With The Most Revenue":
    st.header("Which city generates the most revenue?")
    city_revenue = df.groupby('City')['Total'].sum().round(2).sort_values(ascending= False).reset_index()
    st.plotly_chart(px.bar(data_frame= city_revenue, x= 'City', y= 'Total', labels= {'Total' : 'Total Sales'},text_auto= True))

    
