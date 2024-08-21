import streamlit as st
import requests
from bs4 import BeautifulSoup

url = 'https://www.journalism.cuny.edu/events/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify)