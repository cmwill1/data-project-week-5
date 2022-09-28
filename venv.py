import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.title('Unit 5 Project, Supermarket Sales')
st.text('Performances of Supermarket Areas in Store')

st.image('https://th.bing.com/th/id/R.31a519f5480fa22a9dd5c82a35461040?rik=5SF%2fdtkz%2bD4ocQ&pid=ImgRaw&r=0')


df = pd.read_csv('supermarket.csv')
st.subheader('Top 5 Performing areas')
st.checkbox('Check')
df.sort_values(["store_area"], axis=0, ascending=[False], inplace=True)
st.dataframe(df[["store_id","store_area"]].head(n=10))

st.subheader('Lowest 5 performing areas')
df.sort_values(["store_area"], axis=0, ascending=[True], inplace=True)
st.dataframe(df[["store_id","store_area"]].head(n=10))


st.subheader("Total Sales")

df.sort_values(["store_sales"], axis=0, ascending=[False], inplace=True)
st.dataframe(df[['store_id','store_sales']].head(n=10))

