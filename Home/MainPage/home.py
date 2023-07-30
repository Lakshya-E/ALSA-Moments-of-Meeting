import streamlit as st
from Backend import get_audio
import threading
from st_pages import add_page_title


st.set_page_config(page_title="ALSA Meets", page_icon="🏠")


st.header("i-Meets :left_speech_bubble:")

start_btn = st.button("Start")
summary_btn = st.button("Summary")
questions_btn = st.button("Questions")
stop_btn = st.button("Stop")

if start_btn:
    print("meeting started")
    thread1 = threading.Thread(target=get_audio.record())
    thread1.start()
if summary_btn:
    print("summary button clicked")
    get_audio.is_summary = True
if questions_btn:
    print("questions button clicked")
    get_audio.is_question = True
if stop_btn:
    print("stop button clicked")
    get_audio.is_stop = True


