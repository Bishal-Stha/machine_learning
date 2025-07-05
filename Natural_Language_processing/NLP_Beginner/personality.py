import random

weather_today = "rainy"

responses = {
    "what's your name?": 
                [
                "my name is EchoBot",
                "they call me EchoBot",
                "the name's Bot, Echo Bot"
                ],

    "what's the weather today?": "it's {}!".format(weather_today)

             }

def respond(message):
    if message in responses:
        return random.choice(responses[message])
    
msg = input("👦: ")
print(respond(msg))
