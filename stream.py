import streamlit as st
from Frontend.htmlTemplate import css
from st_pages import Page, show_pages

st.write(css, unsafe_allow_html=True)

if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = None

with st.echo("below"):
    show_pages(
        [
            Page("Home/MainPage/home.py", "Home", "🏠"),
            Page("Home/Meetings/meetings.py", "Meeting", ":books:"),
        ]
    )

# with st.sidebar:
#     selected = st.selectbox("Mode", ('Home', 'Meetings'))
#
#     st.subheader("Enter audio texts")
#

