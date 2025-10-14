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
qa = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad", device=device)

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
    return asr(file_path)["text"] # type: ignore

def answer_question(context, question):
    result = qa(question=question, context=context)
    return result["answer"] # type: ignore

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def process(record=True, file_path=None):
    if record:
        file_path = record_audio(duration=10)
    # Transcribe audio
    text = transcribe_audio(file_path)
    print("Transcribed Text:", text)

    # Ask user for a query related to the text
    query = input("What do you want to know about this audio? ")
    answer = answer_question(context=text, question=query)
    print("Answer:", answer)
    speak_text(answer)

# Example usage:
process(record=True)
