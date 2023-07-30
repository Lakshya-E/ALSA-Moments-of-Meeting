"""In this file we work with audio recording in the background"""
import pyaudio
import wave
import io
from Home.MainPage import summary, questions, stop

is_summary = False
is_question = False
is_stop = False

"""def test_audio(audio, tmp_frame, output_file_path):
    sound_file = wave.open(output_file_path, "wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(tmp_frame))
    sound_file.close()
    print("saving wav file")"""


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
            print("------------------------------------------------")
            print("Entering is_summary loop  to get audio")
            summary.main(audio, frames)
            # output_file_path = "summary.wav"
            # test_audio(audio, frames, output_file_path)
            print("------------------------------------------------ \n\n")
            is_summary = False
        elif is_question:
            print("------------------------------------------------")
            print("Entering is_question loop to get audio")
            questions.main(audio, frames)
            # output_file_path = "questions.wav"
            # test_audio(audio, frames, output_file_path)
            print("------------------------------------------------ \n\n")
            is_question = False
        elif is_stop:
            print("------------------------------------------------")
            print("Entering is_stop loop to get audio")
            stop.main(audio, frames)
            # output_file_path = "stop.wav"
            # test_audio(audio, frames, output_file_path)
            print("------------------------------------------------ \n\n")
            is_stop = False
            break

    stream.stop_stream()
    stream.close()
    audio.terminate()
    print("Recording stopped! \n")
    print("################################## \n\n")








