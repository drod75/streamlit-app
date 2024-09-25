import streamlit as st
from st_login.authentication import *
with open( "app/styles/fonts.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)
st.markdown('# Streamlit App')

if st.session_state.get('authentication_status'):
    st.write('Hello and welcome!')
else:
    st.warning('PLEASE LOGIN TO USE FEATURE', icon=':material/priority_high:')