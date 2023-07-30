from Backend import get_audio
from Backend import main_process


def main(audio, frames):
    audio_file = get_audio.save_audio_to_wav(audio, frames)
    # summary_main = main_process.main_process_home(audio, "give me summary")
    print("After processing summary will be printed here!")

