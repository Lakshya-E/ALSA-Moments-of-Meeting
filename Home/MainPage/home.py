"""This is the home page for streamlit home button"""
import streamlit as st
# from streamlit
from Backend import get_audio
from threading import Thread

st.set_page_config(page_title="ALSA Meets", page_icon="🏠")

st.header("i-Meets :left_speech_bubble:")

start_btn = st.button("Start")
summary_btn = st.button("Summary")
questions_btn = st.button("Questions")
stop_btn = st.button("Stop")

if start_btn:
    print("********************************")
    print("Start button clicked")

    record_thread = Thread(target=get_audio.record())

if summary_btn:
    print("summary button clicked")
    get_audio.is_summary = True

if questions_btn:
    print("questions button clicked")
    st.write("gref")
    get_audio.is_question = True

if stop_btn:
    print("stop button clicked")
    get_audio.is_stop = True
