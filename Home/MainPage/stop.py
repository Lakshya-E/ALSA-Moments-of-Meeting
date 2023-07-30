import threading
import streamlit as st
from Backend import main_process
from Backend import get_audio


def main(frames):
    print("Generating final audio...")
    audio = get_audio.save_audio_to_wav(frames)
    print("Generated audio file for further processing \n\n")
