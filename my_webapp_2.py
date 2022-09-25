import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px

df_iris=sns.load_dataset("iris")

st.write("""
# Iris Dataset
- This is a relation between sepal length, sepal width and petal width
""")

fig = px.scatter_3d(df_iris, x='sepal_length', y='sepal_width', z='petal_width',
              color='species')
fig.show()