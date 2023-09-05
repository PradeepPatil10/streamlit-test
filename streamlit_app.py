import streamlit as st
import pandas as pd

# Create a pandas DataFrame from the given data
data = {
    'product_category_name': ['abchfbb', 'hkkrbjkvjbrjf', 'agro_industria_e_comercio', 'agro_industria_e_comercio', 'alimentos',
                              'alimentos_bebidas', 'artes', 'artes_e_artesanato', 'artigos_de_festas', 'artigos_de_natal'],
    'order_status': ['delivered', 'invoiced', 'delivered', 'shipped', 'delivered', 'delivered', 'delivered', 'delivered', 'delivered', 'delivered'],
    'total_payment': [5006.36, 1504.91, 3790.92, 614.63, 2479.89, 724.61, 765.18, 204.56, 205.76, 397.48]
}

df = pd.DataFrame(data)

# Streamlit app
st.title("Product Data Visualization")

# Group by 'product_category_name' and 'order_status' and sum 'total_payment'
grouped_df = df.groupby(['product_category_name', 'order_status']).sum().reset_index()

# Create a Streamlit bar chart
st.bar_chart(grouped_df.pivot(index='product_category_name', columns='order_status', values='total_payment').fillna(0))
