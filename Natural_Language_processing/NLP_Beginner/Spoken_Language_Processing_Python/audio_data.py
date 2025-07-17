import speech_recognition as sr

recognizer = sr.Recognizer()

clean_support_call = sr.AudioFile("./clean-support-call.wav")
# print("🔥",type(clean_support_call))

with clean_support_call as source:
    clean_support_call2 = recognizer.record(source, offset=2.0, duration=1.0)
print("🔥",type(clean_support_call2))

# text = recognizer.recognize_google(audio_data=clean_support_call, language="en-US")
# # print("💎",text)

text2 = recognizer.recognize_google(audio_data=clean_support_call2, language="en-US") # type: ignore
print("💎",text2)