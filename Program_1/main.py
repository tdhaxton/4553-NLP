#Name: Timothy Haxton
#Course: CMPS 4553 - NLP
#Instructor: Professor Morgan
#Assignment: Program 1 - Sentiment Analysis

#import necessary libraries
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

#create a list of tweets
tweets = []

#pull tweets out of .txt file
#open the file
with open("/home/haxtontd/projects/school/4553-NLP/Climate_change_2022-1-17_2022-7-19.txt", "r") as file:
    content = file.read()
    #open file to write comments out to
    with open("output.txt", "w") as file2:
        #pull tweets from file
        comments = re.findall("(?:Jan|Feb|Mar|Apr|May|Jun|Jul)\s\d+.*\n(?:.*\n)+?\d+", content)
        file2.write(str(comments))

#output quantity of comments found to console and set it equal to sample_size variable
print(len(comments))
sample_size = len(comments)

#write comments to list
for comment in comments:
    tweets.append(comment)

print("Tweets evaluated: " + str(len(tweets)))

#create a SentimentIntensityAnalyzer object
sia_obj = SentimentIntensityAnalyzer()
file_path = "vaderOutput.txt"
file3 = open(file_path, "w")

#create list to hold polarity scores
sentiment_analyses = []

#loop through list of tweets, write tweets to file, and compile them in sentiment_analysis list
for tweet in tweets:
    answer = sia_obj.polarity_scores(tweet)
    file3.write(str(answer))
    file3.write("\n")
    sentiment_analyses.append(answer)

#compile compound polarity scores
pos = 0
neg = 0
for scores in sentiment_analyses:
    print(scores["compound"])
    if scores["compound"] > 0:
        pos += 1
    else:
        neg += 1

#get ratio of positive tweets to negative tweets and print them to the console
total = pos + neg
pos_ratio = pos / total
neg_ratio = neg / total

print("Ratio of positive tweets: " + str(pos_ratio))
print("Ratio of negative tweets: " + str(neg_ratio))

#close the vaderOutput file
file3.close()