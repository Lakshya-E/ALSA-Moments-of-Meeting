from Backend import get_audio
from Backend import main_process


def main(audio, frames):
    """This function takes audio frames and returns questions"""
    audio_file = get_audio.save_audio_to_wav(audio, frames)
    summary_main = main_process.main_process_home(audio, "suggest me questions")
    print("After processing questions will be printed here!")
