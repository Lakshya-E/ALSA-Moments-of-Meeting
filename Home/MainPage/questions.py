import threading
import streamlit as st
from Backend import main_process
from Backend import get_audio


def main(frames):
    print("Process started to generate questions...")
    audio = get_audio.save_audio_to_wav(frames)
    print("Generated audio file for further processing")
    # summary_main = main_process.main_process_home(audio, "suggest me questions")
    print("After processing questions will be printed here! \n\n")
