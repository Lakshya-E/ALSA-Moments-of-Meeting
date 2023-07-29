import streamlit as st
from Backend import main_process
import threading
from Backend.get_audio import save_audio_to_wav


def main(frames):
    thread_summary = threading.Thread(target=save_audio_to_wav(frames))
    audio = thread_summary.start()
    summary_main = main_process.main_process_home(audio, "give me summary")
    print(summary_main)

