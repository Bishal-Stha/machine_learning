# Import os module
import os

# Check the folder of audio files
os.listdir("acme_audio_files")
from pydub import AudioSegment
import speech_recognition as sr
# Create function to convert audio file to wav

def convert_to_wav(filename):
  """Takes an audio file of non .wav format and converts to .wav"""
  # Import audio file
  audio = AudioSegment.from_file(filename)
  
  # Create new filename
  new_filename = filename.split(".")[0] + ".wav"
  
  # Export file as .wav
  audio.export(new_filename, format="wav")
  print(f"Converting {filename} to {new_filename}...")
  
  return new_filename
 

def show_pydub_stats(filename):
    audio_segment = AudioSegment.from_file(filename)
    print(f"Channels: {audio_segment.channels}")
    print(f"Frame rate: {audio_segment.frame_rate}")
    print(f"Frame width: {audio_segment.frame_width}")
    print(f"Sample width: {audio_segment.sample_width}")
    print(f"Max Amplitude: {audio_segment.max}")
    print(f"Length (ms): {len(audio_segment)}")
    print(f"Frame count: {audio_segment.frame_count()}")
    

def transcribe_audio(filename):
    if not filename.endswith(".wav"):
        filename = convert_to_wav(filename)
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)

    return recognizer.recognize_google(audio_data) # type: ignore