import streamlit as st
from Backend import get_audio, main_process


def main():
    question = "suggest me questions"
    audio = get_audio.main()
    questions = main_process.main_process_home(audio, question)
    return questions
