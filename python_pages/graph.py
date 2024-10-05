import streamlit as st
import time
with open( "app/styles/fonts.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)
st.markdown('# Graph Contents')

if st.session_state.get('authentication_status'):
    messages = st.container(height=1000)
    messages.chat_message('assistant').write('Please select the data from the following options:')
    time.sleep(2)
    if prompt := st.chat_input("Say something"):
        messages.chat_message("user").write(prompt)
        time.sleep(2)
        messages.chat_message("assistant").write(f'Certainly! {prompt} is executing now!')
else:
    st.warning('PLEASE LOGIN TO USE FEATURE', icon=':material/priority_high:')
    