"""This is the meetings page for streamlit meetings button"""
import streamlit as st
from Backend import main_process
from Frontend.htmlTemplate import css, bot_template, user_template
from st_pages import add_page_title


def meeting_ended(frames):
    pass


st.write(css, unsafe_allow_html=True)
add_page_title()

user_question = st.text_input("Your questions")
if user_question:
    main_process.main_process_meetings(user_question)

st.write(bot_template.replace("{{MSG}}", "Hello Human!"), unsafe_allow_html=True)
st.write(user_template.replace("{{MSG}}", "Hello ALSA"), unsafe_allow_html=True)
