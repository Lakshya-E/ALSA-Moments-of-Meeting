import streamlit as st
<<<<<<< HEAD
from Backend import get_audio
import threading
from st_pages import add_page_title

=======
import start, questions, stop, summary
from st_pages import add_page_title

from Backend import get_audio
>>>>>>> lakshya-branch

st.set_page_config(page_title="ALSA Meets", page_icon="🏠")


<<<<<<< HEAD
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


=======
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
>>>>>>> lakshya-branch
