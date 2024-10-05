import streamlit as st
with open( "app/styles/fonts.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)
    
pages = {
    'Main': [
        st.Page('python_pages/welcome.py', title='Welcome', icon=':material/star:', default=True),
        st.Page('python_pages\main.py', title='Home', icon=':material/home:')
    ],
    'Account': [
        st.Page('python_pages/account.py', title='Account', icon=':material/account_circle:'),
        st.Page('python_pages/history.py', title='History', icon=':material/library_books:')
    ],
    'Data': [
        st.Page('python_pages/data_cleaning.py', title='Data Cleaner', icon=':material/mop:'),
        st.Page('python_pages/graph.py', title='Graph Viewer', icon=':material/data_thresholding:')
    ]
}

pg = st.navigation(pages)
pg.run()