from Backend import get_audio
from Backend import main_process
from threading import Thread
from streamlit.runtime.scriptrunner import get_script_run_ctx, add_script_run_ctx


def main(audio, frames):
    """This function takes audio frames and saves in db"""
    audio_file = get_audio.save_audio_to_wav(audio, frames)
    stop_main = Thread(target=main_process.main_process_save,
                       args=[audio_file]
                       )
    add_script_run_ctx(stop_main)
    stop_main.start()
