import streamlit as st
from Backend import get_audio
import threading


def main():
    thread1 = threading.Thread(target=get_audio.record())
    thread1.start()
