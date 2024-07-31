import re
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#These lines allow us to work with updated Python
#import time
#time.clock = time.time

gandalf_train = []

with open("The_Lord_of_the_Rings.txt", "r", encoding = "utf-8") as file:
    lines = file.readlines()
    with open("LoR_re.txt", "w") as file2:
        for line in lines:
            new_line = re.sub("^[\s]+ | [\s]+$", "", lines)
            file2.write(new_line)
            # if line[0] == "[Gandalf:]":
            #     gandalf_train.append(' '.join(line[1:]))

# gandalfbot = ChatBot("Gandalf", storage_adapter = "chatterbot.storage.SQLStorageAdapter", database_uri = ("sqlite:///gandalf.squlite3"))