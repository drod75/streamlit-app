import streamlit as st
with open( "app/styles/fonts.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
pages = {
    'Main': [
        st.Page('pages/main.py', title='Home', icon=':material/home:'),
        st.Page('pages/welcome.py', title='Welcome', icon=':material/star:')
    ],
    'Account': [
        st.Page('pages/account.py', title='Account', icon=':material/account_circle:'),
        st.Page('pages/account_settings.py', title='Account Settings', icon=':material/manage_accounts:')
    ],
    'Data': [
        st.Page('pages/graph.py', title='Graph Viewer', icon=':material/data_thresholding:'),
        st.Page('pages/data_cleaning.py', title='Data Cleaner', icon=':material/mop:')
    ]
}

pg = st.navigation(pages)
pg.run()