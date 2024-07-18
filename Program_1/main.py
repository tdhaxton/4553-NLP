#import necessary libraries
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

#create a list of tweets
tweets = []

#pull tweets out of .txt file
#open the file
with open("/home/haxtontd/projects/school/CMPS4553/Climate_change_2022-1-17_2022-7-19.txt", "r") as file:
    content = file.read()
    with open("output.txt", "w") as file2:
        for tweet in content:
            #pull tweets from file
            file2.write(re.findall("Jan\s\d{2}.*\n\d|Feb\s\d{2}|Mar\s\d{2}|Apr|\s\d{2}|May\s\d{2}|Jun\s\d{2}|Jul\s\d{2}", content))

# #close the file
# file.close()

#print(tweets)

#create a SentimentIntensityAnalyzer object
sia_obj = SentimentIntensityAnalyzer()