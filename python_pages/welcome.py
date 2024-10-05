import streamlit as st
with open("app/styles/fonts.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)
with open('python_pages/writing/welcome.txt') as file:
    for line in file:
        st.markdown(line)
