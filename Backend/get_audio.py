import threading
import pyaudio
import time
import wave
import io
from Home.MainPage import summary, questions, stop
from Home.Meetings import meetings

from Backend import main_process

is_summary = False
is_stop = False
is_question = False
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
frames = []


def save_audio_to_wav(frame):
    """Creating virtual WAV file..."""
    wav_file = io.BytesIO()
    sound_file = wave.open(wav_file, "wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frame))
    sound_file.close()
    wav_file.seek(0)
    return audio


def record():
    """Record audio until the user enters 'suggest' or 'stop'."""
    print("Started recording...")
    while True:
        global is_summary
        global is_stop
        global is_question
        data = stream.read(1024)
        frames.append(data)
        if is_summary:
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
            break
