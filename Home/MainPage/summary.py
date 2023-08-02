from Backend import get_audio
from Backend import main_process
import streamlit as st
from Frontend.htmlTemplate import css, summary_template, question_template
from threading import Thread
from streamlit.runtime.scriptrunner import get_script_run_ctx, add_script_run_ctx

st.write(css, unsafe_allow_html=True)


def main(text):
    """This function takes audio frames and returns summary"""
    summary_main = Thread(target=main_process.main_process_home,
                          args=[text,
                                "give the whole context, with every major points discussed"
                                ]
                          )
    add_script_run_ctx(summary_main)
    summary_main.start()


# def main(audio, frames):
#     """This function takes audio frames and returns summary"""
#     audio_file = get_audio.save_audio_to_wav(audio, frames)
#     summary_main = Thread(target=main_process.main_process_home,
#                           args=[audio_file,
#                                 "give the whole summary of the context, with every major points discussed"
#                                 ]
#                           )
#     add_script_run_ctx(summary_main)
#     summary_main.start()
