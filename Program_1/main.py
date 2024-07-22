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

print(len(comments))
sample_size = len(comments)

#write comments to list
for comment in comments:
    tweets.append(comment)

print(tweets[0])
print(len(tweets))

#print(tweets)

#create a SentimentIntensityAnalyzer object
sia_obj = SentimentIntensityAnalyzer()
file_path = "vaderOutput.txt"
file3 = open(file_path, "w")

sentiment_analyses = []

for tweet in tweets:
    answer = sia_obj.polarity_scores(tweet)
    file3.write(str(answer))
    file3.write("\n")
    sentiment_analyses.append(answer)
    #print(answer)

#compile compound polarity scores
total = 0
for scores in sentiment_analyses:
    total += sentiment_analyses[scores]

#calculate average sentiment
avg_sentiment = total / len(tweets)
print(avg_sentiment)

file3.close()