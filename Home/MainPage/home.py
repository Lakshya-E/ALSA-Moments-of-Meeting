import streamlit as st
from Backend import get_audio

st.set_page_config(page_title="ALSA Meets", page_icon="🏠")

st.header("i-Meets :left_speech_bubble:")

start_btn = st.button("Start")
summary_btn = st.button("Summary")
questions_btn = st.button("Questions")
stop_btn = st.button("Stop")

if start_btn:
    print("********************************")
    print("Start button clicked")
    get_audio.record()

if summary_btn:
    print("summary button clicked")
    get_audio.is_summary = True

if questions_btn:
    print("questions button clicked")
    get_audio.is_question = True

if stop_btn:
    print("stop button clicked")
    get_audio.is_stop = True
