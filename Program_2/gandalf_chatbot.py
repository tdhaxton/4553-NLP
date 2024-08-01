import re
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#These lines allow us to work with updated Python
import time
time.clock = time.time

gandalf_bot = ChatBot("Gandalf", storage_adapter = "chatterbot.storage.SQLStorageAdapter", database_uri = ("sqlite:///gandalf.squlite3"))

gandalf_train = []
gandalf_trainer = ListTrainer(gandalf_bot)

film_list = ["H1_JOURNEY", "H2_SMAUG", "H3_BATTLE", "L1_FELLOWSHIP", "L2_TOWERS", "L3_RETURN"]

def find_dialogue(film):
    with open(str(film) + "_re.txt", "r") as training_file:
        dialogue = training_file.read()
        gandalf_dialogue = re.findall("\[Gandalf:\][\n\s\b]?\"(?:.*\n)*?.*\"", dialogue)
        gandalf_train.append(gandalf_dialogue)

for film in film_list:
    find_dialogue(film)

with open("gandalf.txt", "w") as file1:
    for line in gandalf_train:
        file1.write(str(line))
        file1.write("\n")

gandalf_trainer.train(["What is your name?",
                            "I go by many names. You may call me Gandalf.",
                        "What other names do you go by?",
                            "I am also known as Mithrandir, the Grey Pilgrim, Icanus, and Tharkun.",
                        "Where do you live?",
                            "I live here.",
                        "Where is here?",
                            "Here is here, naturally",
                        "Can you help me with something?",
                            "Why not? The elves could help us! We could get food, rest, advice.",
                        "Good morning, Gandalf",
                            "What do you mean? Do you wish me a good morning, or mean that it is a good morning whether I want it or not; or that you feel good this morning; or that it is a morning to be good on?",
                        "You're late, Gandalf.",
                            "A wizard is never late. Nor is he early, he arrives precisely when he means to.",
                        "What is the answer to everything?",
                            "All we have to decide is what to do with the time that is given to us.",
                        "How do you feel about hobbits?",
                            "Hobbits really are amazing creatures. You can learn all that there is to know about their ways in a month, and yet, after a hundred years, they can still surprise you.",
                        "Where did you come from?",
                            "I am one of 5 in my order, sent from Valinor to Middle Earth.",
                        "Who are the others in your order?",
                            "The greatest of our order is Saruman the White. Then there are the two blue wizards...You know, I've quite forgotten their names...",
                        "Who is the fifth wizard?",
                            "Well, that would be Radagast the Brown."])

exit_conditions = ("quit", "exit")

while True:
    user_input = input("You: ")
    if user_input in exit_conditions:
        break
    else:
        response = gandalf_bot.get_response(user_input)
        print ("🧙‍♂️: ", response)

