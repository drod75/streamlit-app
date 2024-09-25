import streamlit as st
with open( "app/styles/fonts.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)
st.markdown('# Account Settings')

if st.session_state.get('authentication_status'):
    pass
else:
    st.warning('PLEASE LOGIN TO USE FEATURE', icon=':material/priority_high:')