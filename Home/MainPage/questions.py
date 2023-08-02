from Backend import get_audio
from Backend import main_process
from threading import Thread
from streamlit.runtime.scriptrunner import get_script_run_ctx, add_script_run_ctx


def main(text):
    """This function takes audio frames and returns questions"""
    question_main = Thread(target=main_process.main_process_home,
                           args=[text,
                                 "create some questions from the context",
                                 "questions"
                                 ]
                           )
    add_script_run_ctx(question_main)
    question_main.start()


# def main(audio, frames):
#     """This function takes audio frames and returns questions"""
#     audio_file = get_audio.save_audio_to_wav(audio, frames)
#     questions_main = Thread(target=main_process.main_process_home,
#                             args=[audio_file, "create some questions from the context",
#                                   "questions"
#                                   ]
#                             )
#     add_script_run_ctx(questions_main)
#     questions_main.start()
