import streamlit as st
with open( "app/styles/fonts.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)
st.markdown('# Streamlit App')
st.write('Hello and welcome!')