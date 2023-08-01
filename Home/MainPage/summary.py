from Backend import get_audio
from Backend import main_process
import streamlit as st
from Frontend.htmlTemplate import css, summary_template, question_template
from threading import Thread

st.write(css, unsafe_allow_html=True)


def main(text):
    """This function takes audio frames and returns summary"""
    # audio_file = get_audio.save_audio_to_wav(audio, frames)
    # summary_main = main_process.main_process_home(audio_file, "give brief summary of the context")
    print("in summary")
    summary_main = Thread(target=main_process.main_process_home, args=[text, "give brief summary of the context"])
    summary_main.start()

    # st.write(summary_template.replace("{{MSG}}", "Hello ALSA"), unsafe_allow_html=True)
