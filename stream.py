"""This is the main pain for streamlit"""
import streamlit as st
from Frontend.htmlTemplate import css
from st_pages import Page, show_pages
from streamlit.runtime.scriptrunner import get_script_run_ctx

st.write(css, unsafe_allow_html=True)
# ctx = get_script_run_ctx()
# session_id = ctx.session_id
# st.session_state['ctx_session'] = session_id


# with st.echo("below"):
show_pages(
        [
            Page("Home/MainPage/home.py", "Home", "🏠"),
            Page("Home/Meetings/meetings.py", "Meeting", ":books:"),
        ]
    )

st.header("i-Meet")

with st.container():
    st.write('Click "🏠 Home" for active meeting')
    st.write('Click ":books: Meeting" for previous meetings i-Meet chatbot')
