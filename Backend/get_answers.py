import streamlit as st
from Frontend.htmlTemplate import bot_template, user_template


def answer_user_question_home(question):
    """This function takes the question and returns the response on the basis of
    conversation chain created"""
    try:
        response = st.session_state.conversation({'question': question})
        st.session_state.chat_history = response['chat_history']

        length = len(st.session_state.chat_history)
        print(st.session_state.chat_history)

    except (KeyError, AttributeError):
        st.write("Enter Some data first")


def answer_user_question_meetings(question):
    """This function takes the question and returns the response on the basis of
        conversation chain created"""
    try:
        response = st.session_state.conversation({'question': question})
        st.session_state.chat_history = response['chat_history']

        length = len(st.session_state.chat_history)
        print(st.session_state.chat_history)
        for i in range(length-1, -1, -1):
            if i % 2 == 0:
                st.write(user_template.replace("{{MSG}}", st.session_state.chat_history[i].content), unsafe_allow_html=True)
            else:
                st.write(bot_template.replace("{{MSG}}", st.session_state.chat_history[i].content), unsafe_allow_html=True)

    except (KeyError, AttributeError):
        st.write("Enter Some data first")