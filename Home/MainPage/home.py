import streamlit as st
import start, questions, stop, summary
from st_pages import add_page_title

st.set_page_config(page_title="ALSA Meets", page_icon="🏠")


def home():
    st.header("i-Meets :left_speech_bubble:")

    start_btn = st.button("Start")
    summary_btn = st.button("Summary")
    questions_btn = st.button("Questions")
    stop_btn = st.button("Stop")

    if start_btn:
        start.main()
    if summary_btn:
        main_summary = summary.main()
    if questions_btn:
        main_questions = questions.main()
    if stop_btn:
        stop.main()


home()
