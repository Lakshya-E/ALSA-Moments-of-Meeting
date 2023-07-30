import threading
<<<<<<< HEAD

import pyaudio
import wave
import io
from Home.MainPage import summary, questions, stop
=======
import pyaudio
import time
import wave
import io
from Home.MainPage import summary, questions, stop
from Home.Meetings import meetings

from Backend import main_process
>>>>>>> lakshya-branch

is_summary = False
is_stop = False
is_question = False
<<<<<<< HEAD

audio = pyaudio.PyAudio()


def save_audio_to_wav(frame):
    print("Creating virtual WAV file...")
=======
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
frames = []


def save_audio_to_wav(frame):
    """Creating virtual WAV file..."""
>>>>>>> lakshya-branch
    wav_file = io.BytesIO()
    sound_file = wave.open(wav_file, "wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frame))
    sound_file.close()
    wav_file.seek(0)
<<<<<<< HEAD
    print("Created virtual audio file which will be returned for processing...")
=======
>>>>>>> lakshya-branch
    return audio


def record():
<<<<<<< HEAD
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    frames = []
    """Record audio until the user enters 'suggest' or 'stop'."""
    print("Started recording... \n")
=======
    """Record audio until the user enters 'suggest' or 'stop'."""
    print("Started recording...")
>>>>>>> lakshya-branch
    while True:
        global is_summary
        global is_stop
        global is_question
        data = stream.read(1024)
        frames.append(data)
        if is_summary:
<<<<<<< HEAD
            print("Entering is_summary loop of get_audio")
            summary_thread = threading.Thread(target=summary.main(frames))
            summary_thread.start()
            is_summary = False
        elif is_question:
            print("Entering is_question loop of get_audio")
            questions_thread = threading.Thread(target=questions.main(frames))
            questions_thread.start()
            is_question = False
        elif is_stop:
            print("Entering is_stop loop of get_audio")
            stop_thread = threading.Thread(target=stop.main(frames))
            stop_thread.start()
            stream.stop_stream()
            stream.close()
            audio.terminate()
            print("storing frames in db \n\n")
            is_stop = False
=======
            summary.main(frames)
            is_summary = False
        elif is_question:
            questions.main(frames)
            is_question = False
        elif is_stop:
            stop.main(frames)
            stream.stop_stream()
            stream.close()
            audio.terminate()
            """storing frames in db"""
>>>>>>> lakshya-branch
            break
