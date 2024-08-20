import streamlit as st
import pandas as pd

df = pd.read_csv('data sources\Data-Science-Jobs.csv')
st.dataframe(df)
st.table()