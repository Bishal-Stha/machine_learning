# import sounddevice as sd
# import wavio
# import pyttsx3
# import tkinter as tk
# from tkinter import messagebox
# from transformers import pipeline
# import torch
# import threading
# from typing import Any, Dict, List, Union

# # -----------------------------
# # Global Initialization
# # -----------------------------
# DEVICE = 0 if torch.cuda.is_available() else -1

# # Load pipelines once at startup for performance
# ASR_PIPELINE = pipeline(
#     "automatic-speech-recognition",
#     model="openai/whisper-small",
#     device=DEVICE
# )
# SENTIMENT_PIPELINE = pipeline("sentiment-analysis", device=DEVICE)

# # Initialize pyttsx3 engine once
# ENGINE = pyttsx3.init()

# # -----------------------------
# # 1. Record audio
# # -----------------------------
# def record_audio(filename: str = "audio.wav", duration: int = 10, fs: int = 16000) -> None:
#     """Record audio from microphone and save to WAV file."""
#     print("Recording... Speak now!")
#     recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
#     sd.wait()
#     wavio.write(filename, recording, fs, sampwidth=2)
#     print(f"Audio recorded and saved as {filename}")

# # -----------------------------
# # 2. Transcribe audio
# # -----------------------------
# def transcribe_audio(filename: str = "audio.wav") -> str:
#     """Transcribe audio to text using preloaded ASR pipeline."""
#     out: Union[Dict[str, Any], str] = ASR_PIPELINE(filename) # type: ignore
#     text: str = out.get("text", "") if isinstance(out, dict) else str(out)
#     print(f"Transcribed Text: {text}")
#     return text

# # -----------------------------
# # 3. Sentiment analysis
# # -----------------------------
# def analyze_sentiment(text: str) -> Dict[str, Any]:
#     """Perform sentiment analysis on text using preloaded pipeline."""
#     result_list: List[Dict[str, Any]] = SENTIMENT_PIPELINE(text) # type: ignore

#     if isinstance(result_list, list) and len(result_list) > 0:
#         result: Dict[str, Any] = result_list[0]
#     else:
#         result = {"label": "Unknown", "score": 0.0}
#     print(f"Sentiment: {result}")
#     return result

# # -----------------------------
# # 4. Speak the result
# # -----------------------------
# def speak_sentiment(result: Dict[str, Any]) -> None:
#     """Speak the sentiment result using preloaded pyttsx3 engine."""
#     label: str = result.get("label", "Unknown").lower()
#     if label == "positive":
#         ENGINE.say("Positive")
#     elif label == "negative":
#         ENGINE.say("Negative")
#     else:
#         ENGINE.say("Unknown sentiment")
#     ENGINE.runAndWait()

# # -----------------------------
# # Pipeline runner
# # -----------------------------
# def run_pipeline() -> None:
#     """Record, transcribe, analyze, speak, and show result in GUI."""
#     try:
#         # 1. Record
#         record_audio(duration=10)

#         # 2. Transcribe
#         text = transcribe_audio()

#         # 3. Analyze sentiment
#         sentiment_result = analyze_sentiment(text)

#         # 4. Speak sentiment
#         speak_sentiment(sentiment_result)

#         # 5. Show result in messagebox
#         messagebox.showinfo(
#             "Result",
#             f"Transcribed Text:\n{text}\n\nSentiment: {sentiment_result.get('label', 'Unknown')}"
#         )
#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# # -----------------------------
# # Threaded runner to avoid GUI freeze
# # -----------------------------
# def run_pipeline_thread() -> None:
#     threading.Thread(target=run_pipeline).start()

# # -----------------------------
# # GUI Setup
# # -----------------------------
# root = tk.Tk()
# root.title("Audio Sentiment Analyzer")

# frame = tk.Frame(root, padx=20, pady=20)
# frame.pack()

# label = tk.Label(
#     frame,
#     text="Click the button to record your voice (10 sec) and analyze sentiment:"
# )
# label.pack(pady=10)

# btn = tk.Button(frame, text="Start Recording & Analyze", command=run_pipeline_thread)
# btn.pack(pady=10)

# root.mainloop()
