# Importing the speech_recognition library
import speech_recognition as sr

# Create an instance of the Recognizer class
recognizer = sr.Recognizer()

# Set the energy threshold
recognizer.energy_threshold = 300

# Create a recognizer class
recognizer = sr.Recognizer()

# Load or record the audio data
with sr.AudioFile("./good_morning.wav") as source:
    audio_data = recognizer.record(source)

# Transcribe the support call audio
text = recognizer.recognize_google( # type: ignore
    audio_data,
    language="en-US"
)

print(text)