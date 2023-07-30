from Backend import get_audio


def main(audio, frames):
    """This function takes audio frames and returns final audio"""
    audio_file = get_audio.save_audio_to_wav(audio, frames)
    print("Generated audio file for further processing \n\n")
    print("storing frames in db")
