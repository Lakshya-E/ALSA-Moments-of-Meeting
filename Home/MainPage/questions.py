from Backend import get_audio
from Backend import main_process
import streamlit as st


def main(audio, frames):
    """This function takes audio frames and returns questions"""
    audio_file = get_audio.save_audio_to_wav(audio, frames)
    summary_main = main_process.main_process_home(audio_file, "create some questions from the context")
    st.write(summary_main)
