import streamlit as st
from Backend import main_process, get_audio


def main():
    question = "give me summary"
    get_audio.is_summary = True
    # summary = main_process.main_process_home(audio, question)
    # return summary

