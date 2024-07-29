#Step1: python3 -m pip install chatterbot==1.0.4 pytz
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#These lines allow us to work with updated Python
#import time
#time.clock = time.time

bobsyouruncle = ChatBot("SimpleBot")
trainer = ListTrainer(bobsyouruncle)

trainer.train(["What's your name?",
                "My name is bobsyouruncle.",
              "How are you doing?",
                "Doing great!",
              "Can you help me with something?",
                "Of course!",
              "Good bot!",
                "Thanks, human!",
              "Hello, bobsyouruncle",
                "Hello"])

#Give the user options to exit the program
exit_conditions = ("quit", "exit")

while True:
    user_input = input("You: ")
    if user_input in exit_conditions:
        break
    else:
        response = bobsyouruncle.get_response(user_input)
        print("🤖:", response)