import torch
from transformers import pipeline
import pyttsx3
import sounddevice as sd
import numpy as np
import wavio
import time

# Use GPU if available
device = 0 if torch.cuda.is_available() else -1
print("Using device:", "GPU" if device == 0 else "CPU")

# Load pipelines
asr = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h", device=device)
sentiment = pipeline("sentiment-analysis", device=device) # pyright: ignore[reportArgumentType, reportCallIssue]

# Initialize TTS
engine = pyttsx3.init()

def record_audio(duration=10, fs=16000, filename="recorded.wav"):
    print(f"Recording for {duration} seconds...")
    for i in range(duration, 0, -1):
        print(f"{i}...", end="\r")
        time.sleep(1)
    print("Recording now...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    wavio.write(filename, audio, fs, sampwidth=2)
    print("Recording finished.")
    return filename

def transcribe_audio(file_path):
    return asr(file_path)["text"] # pyright: ignore[reportCallIssue, reportArgumentType]

def analyze_sentiment(text):
    result = sentiment(text)[0]
    return f"Label: {result['label']}, Score: {result['score']:.2f}"

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def process(record=True, file_path=None):
    if record:
        file_path = record_audio(duration=10)
    text = transcribe_audio(file_path)
    print("Transcribed Text:", text)
    sentiment_result = analyze_sentiment(text)
    print("Sentiment Analysis:", sentiment_result)
    speak_text(sentiment_result)

# Example usage:
process(record=True)   # Record 10 sec from mic and analyze
# process(record=False, file_path="my_audio.mp3")  # Analyze from file
