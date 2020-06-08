import csv
from csv import reader
file = open('dTweet.csv', 'rU')
read_file = reader(file)
list_file = list(read_file)

tweets = []

for i in list_file[1:]:
	text = i[2]
	tweets.append(text)

text_file = open('tweets.txt', 'w+')

for tweet in tweets:
	text_file.write(tweet + "\n")

text_file.close()