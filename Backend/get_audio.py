import threading
import wave
import pyaudio
import time

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
frames = []
is_summary = False
is_stop = False
program_running = True
i = 1


def save_audio(tmp_frame):
    global i
    print("Saving audio data to a WAV file")
    sound_file = wave.open("audio" + str(i) + ".wav", "wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(tmp_frame))
    sound_file.close()
    print("saved audio")
    i += 1


def record():
    """Record audio until the user enters 'suggest'."""
    print("started recording...")
    while True:
        global is_summary
        global is_stop
        global program_running
        # print("continue recording...")
        data = stream.read(1024)
        frames.append(data)
        if is_summary:
            print("suggestion is triggered!")
            thread2 = threading.Thread(target=save_audio(frames))
            thread2.start()
            is_summary = False
        elif is_stop:
            print("stopped recording...")
            program_running = False
            stream.stop_stream()
            stream.close()
            audio.terminate()
            thread2 = threading.Thread(target=save_audio(frames))
            thread2.start()
            break


def get_input():
    global is_suggest
    global is_stop
    while program_running:
        st_r = input("Enter the string [suggest or stop]: ")
        if st_r == "suggest":
            is_suggest = True
            time.sleep(2)
        elif st_r == "stop":
            is_stop = True
            time.sleep(2)


thread3 = threading.Thread(target=get_input)
thread3.start()