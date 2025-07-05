import time

def respond(message):
    print(f"\n🔊 Bot: I can hear you, you said: '{message}'\n")

def send_message(message):
    time.sleep(0.6)
    respond(message)

while True:
    message = input("🧑 Bishal: ")
    if message.lower() == "stop":
        break
    send_message(message)
