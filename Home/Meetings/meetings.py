import streamlit as st
# from user_conversations import answer_user_question
from Frontend.htmlTemplate import  css, bot_template, user_template
from st_pages import add_page_title

st.write(css, unsafe_allow_html=True)
add_page_title()

user_question = st.text_input("Your questions")
if user_question:
    # answer_user_question(user_question)
    pass

st.write(bot_template.replace("{{MSG}}", "Hello Human!"), unsafe_allow_html=True)
st.write(user_template.replace("{{MSG}}", "Hello ALSA"), unsafe_allow_html=True)
