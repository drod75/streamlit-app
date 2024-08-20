import streamlit as st
import pandas as pd

df = pd.read_csv('data sources\Data-Science-Jobs.csv')
df.head(20)