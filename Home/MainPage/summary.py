import streamlit as st
<<<<<<< HEAD
from Backend import main_process, get_audio
import threading
from Backend import get_audio


def main(frames):
    print("Process started to generate audio...")
    audio = get_audio.save_audio_to_wav(frames)
    print("Generated audio file for further processing")
    # summary_main = main_process.main_process_home(audio, "give me summary")
    print("After processing summary will be printed here! \n\n")
=======
from Backend import main_process
import threading
from Backend.get_audio import save_audio_to_wav


def main(frames):
    thread_summary = threading.Thread(target=save_audio_to_wav(frames))
    audio = thread_summary.start()
    summary_main = main_process.main_process_home(audio, "give me summary")
    print(summary_main)
>>>>>>> lakshya-branch

