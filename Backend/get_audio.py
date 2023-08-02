"""In this file we work with audio recording in the background"""
import time
from threading import Thread
import pyaudio
import wave
import io
from Home.MainPage import summary, questions, stop

is_summary = False
is_question = False
is_stop = False

with open("data_files/audio_to_text.txt", "r") as f:
    text = f.read().replace('\n', '')


def save_audio_to_wav(audio, frame):
    wav_file = io.BytesIO()
    sound_file = wave.open(wav_file, "wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frame))
    sound_file.close()
    wav_file.seek(0)
    return wav_file


def record():
    print("opening audio and stream to start recording...\n")
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    frames = []

    global is_stop
    global is_summary
    global is_question

    while True:
        data = stream.read(1024)
        frames.append(data)
        if is_summary:
            print("*****Entering is_summary loop  to get audio*****\n\n")
            is_summary = False
            # summary_thread = Thread(target=summary.main, args=[audio, frames])
            summary_thread = Thread(target=summary.main, args=[text])
            summary_thread.start()

        elif is_question:
            print("*****Entering is_question loop to get audio*****\n\n")
            is_question = False
            # question_thread = Thread(target=questions.main, args=[audio, frames])
            question_thread = Thread(target=questions.main, args=[text])
            question_thread.start()

        elif is_stop:
            print("*****Entering is_stop loop to get audio*****\n\n")
            is_stop = False
            stop.main(audio, frames)
            break

    stream.stop_stream()
    stream.close()
    audio.terminate()
    print("Recording stopped! \n")
    print("################################## \n\n")
