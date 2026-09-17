import sounddevice as sd
from faster_whisper import WhisperModel
import subprocess
import soundfile as sf

model = WhisperModel("base.en", device="cpu", compute_type="int8")

def record(seconds=4, fs=16000):
    print("Andy is listening...")
    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    return audio.flatten(), fs

def andy_speak(text):
    subprocess.run([
        "piper",
        "--model", "en_US-lessac-medium.onnx",
        "--output_file", "andy_reply.wav"
    ], input=text.encode())

    data, fs = sf.read("andy_reply.wav")
    sd.play(data, fs)
    sd.wait()

audio, fs = record()
segments, _ = model.transcribe(audio, language="en")
for seg in segments:
    print("Andy heard:", seg.text)
    andy_speak("You said: " + seg.text)