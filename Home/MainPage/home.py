import streamlit as st
import start, questions, stop, summary
from st_pages import add_page_title

from Backend import get_audio

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
        get_audio.is_summary = True
    if questions_btn:
        get_audio.is_question = True
    if stop_btn:
        get_audio.is_stop = True


home()
