import streamlit as st
import urllib2
from bs4 import BeautifulSoup

url = 'https://www.journalism.cuny.edu/events/'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')