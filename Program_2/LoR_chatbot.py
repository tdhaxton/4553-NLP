import re
# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer

#These lines allow us to work with updated Python
#import time
#time.clock = time.time

characters = []
gandalf_train = []
film_list = ["H1_JOURNEY", "H2_SMAUG", "H3_BATTLE", "L1_FELLOWSHIP", "L2_TOWERS", "L3_RETURN"]

# def train_gandalf(file):
#     with open(file + "_re.txt", "r") as train_file:
#         gandalf_dialogue = re.findall("\[Gandalf:\]\n?\"(?:.*\n)+\"", train_file)
#         gandalf_train.append(gandalf_dialogue)

def preprocess(file):
    left_justify(file)
    find_characters(file)

def left_justify(file):
    with open(file + ".txt", "r", encoding = "utf-8") as infile:
        lines = infile.readlines()
        with open(str(file + "_re.txt"), "w") as outfile:
            for line in lines:
                l_justify = re.sub("^[\s]+ | [\s]+$", "", line)
                # rem_char = re.sub("\[[A-Z]\w+:\]\n", "", line)
                outfile.write(l_justify)

def find_characters(file):
    with open(file + "_re.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            chars = re.findall("\[[A-Z]\w+:\]\n", line)
            if chars and chars not in characters:
                characters.append(chars)

# def insert_quotes(file):

# def find_dialogue(character):
#     with open("H1_JOURNEY_re.txt", "r") as training_file:
#         dialogue = training_file.read()
#         character_dialogue = re.findall("\[Gandalf:\]\n?\"(?:.*\n)*?.*\"", dialogue)
#         character_train.append(gandalf_dialogue)

            
    # train_gandalf(file)

# with open("H1_JOURNEY.txt", "r", encoding = "utf-8") as infile:
#     lines = infile.readlines()
#     with open("H1_re.txt", "w") as outfile:
#         for line in lines:
#             left_justify = re.sub("^[\s]+ | [\s]+$", "", line)
#             outfile.write(left_justify)
# # with open("H1_re.txt", "r") as file1:
# #     lines1 = file1.readlines()
# #     with open("H1_re2.txt", "w") as file3:      
# #         for line1 in lines1:
# #             find_dialogue = re.sub("\[[A-Z]\w+:\]\n", "\[[A-Z]\w+:\]", line1)
# #             file3.write(find_dialogue)
#             # if line[0] == "[Gandalf:]":
#             #     gandalf_train.append(' '.join(line[1:]))
# with open("L1_FELLOWSHIP.txt", "r", encoding = "utf-8") as infile2:
#     lines = infile2.readlines()
#     with open("L1_re.txt", "w") as outfile2:
#         for line in lines:
#             left_justify = re.sub("^[\s]+ | [\s]+$", "", line)
#             outfile2.write(left_justify)

# with open("L2_TOWERS.txt", "r", encoding = "utf-8") as infile3:
#     lines = infile3.readlines()
#     with open("L2_re.txt", "w") as outfile3:
#         for line in lines:
#             left_justify = re.sub("^[\s]+ | [\s]+$", "", line)
#             outfile3.write(left_justify)

# with open("L3_RETURN.txt", "r", encoding = "utf-8") as infile4:
#     lines = infile4.readlines()
#     with open("L3_re.txt", "w") as outfile4:
#         for line in lines:
#             left_justify = re.sub("^[\s]+ | [\s]+$", "", line)
#             outfile4.write(left_justify)

for film in film_list:
    preprocess(film)
# preprocess("H1_JOURNEY")
# preprocess("H2_SMAUG")
# preprocess("H3_BATTLE")
# preprocess("L1_FELLOWSHIP")
# preprocess("L2_TOWERS")
# preprocess("L3_RETURN")
with open("characters.txt", "w") as file:
    for character in characters:
        file.write(str(character) + "\n")

with open("H1_JOURNEY_re.txt", "r") as training_file:
    dialogue = training_file.read()
    gandalf_dialogue = re.findall("\[Gandalf:\]\n?\"(?:.*\n)*?.*\"", dialogue)
    gandalf_train.append(gandalf_dialogue)

with open(str(character) + ".txt", "w") as file1:
    for line in gandalf_train:
        file1.write(str(line))
        file1.write("\n")

# for character in characters:
#     find_dialogue(character)

# gandalfbot = ChatBot("Gandalf", storage_adapter = "chatterbot.storage.SQLStorageAdapter", database_uri = ("sqlite:///gandalf.squlite3"))