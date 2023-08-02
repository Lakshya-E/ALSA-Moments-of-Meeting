"""This is the meetings page for streamlit meetings button"""
import streamlit as st
from Backend import main_process
from Frontend.htmlTemplate import css, bot_template, user_template
from st_pages import add_page_title

st.write(css, unsafe_allow_html=True)
add_page_title()

with open("data_files/meetings_data1.txt", "r", encoding='utf-8') as f:
    meeting_1 = f.read().replace('\n', '')
with open("data_files/meetings_data2.txt", "r", encoding='utf-8') as f:
    meeting_2 = f.read().replace('\n', '')

meetings = [meeting_1, meeting_2]

if "meet1" in st.session_state:
    user_question = st.text_input("Your questions")
    if user_question:
        main_process.main_process_meetings(st.session_state.meet1, user_question)

    st.write(bot_template.replace("{{MSG}}", "Hello Human!"), unsafe_allow_html=True)
    st.write(user_template.replace("{{MSG}}", "Hello ALSA"), unsafe_allow_html=True)

elif "meet2" in st.session_state:
    user_question = st.text_input("Your questions")
    if user_question:
        main_process.main_process_meetings(st.session_state.meet2, user_question)

    st.write(bot_template.replace("{{MSG}}", "Hello Human!"), unsafe_allow_html=True)
    st.write(user_template.replace("{{MSG}}", "Hello ALSA"), unsafe_allow_html=True)

else:
    meet1 = st.button("Meet 1 - Technology Podcast")
    meet2 = st.button("Meet 2 - Blockchain")

    if meet1:
        if "meet1" not in st.session_state:
            st.session_state['meet1'] = meetings[0]
        else:
            st.session_state.meet1 = meetings[0]
        st.experimental_rerun()

    if meet2:
        if "meet2" not in st.session_state:
            st.session_state['meet2'] = meetings[1]
        else:
            st.session_state.meet2 = meetings[1]
        st.experimental_rerun()


