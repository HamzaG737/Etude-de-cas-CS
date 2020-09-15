
 # This file transforms the original data from the DEFT tweet classification challenge into a csv file
# this csv contains : the id of the tweet, its polarity (pos, neg, neutral or mixt), the nature of the tweets and a finer classification of the sentiment or emotion

import pandas as pd


# opening the original files

def from_text_to_csv(in_path):
    # simple functions which turns a space separated text file into a csv
    out_path = ''
    txt_file = open(in_path)
    out_file = open(out_path)
    for line in txt_file:
        (id, polarity) = line.strip().split(' ')
        out_file.write(','.join([id, polarity]) + '\n')
    txt_file.close()
    out_file.close()



"""polarity = open('Data/Train_References-22042015/Train_References/T1.txt', 'r')
polarity_csv = open('Data/Train_References-22042015/Train_References/T1.csv', 'w')
polarity.readline() # skip first line
for line in polarity:
    (id, pol) = line.strip().split('\t')
    polarity_csv.write(','.join([id, pol]) + '\n')
polarity.close()
polarity_csv.close()"""

#polarity = pd.read_csv('Data/Train_References-22042015/Train_References/T1.csv')
#print(polarity)

"""nature = open('Data/Train_References-22042015/Train_References/T2.1.txt', 'r')
nature_csv = open('Data/Train_References-22042015/Train_References/nature_tweets.csv', 'w')
nature.readline() # skip first line
for line in nature:
    (id, nat) = line.strip().split(' ')
    nature_csv.write(','.join([id, nat]) + '\n')
nature.close()
nature_csv.close()"""

polarity = pd.read_csv('Data/Train_References-22042015/Train_References/T1.csv')
print(polarity)


nature = pd.read_csv('Data/Train_References-22042015/Train_References/nature_tweets.csv')
print(nature)

emotion = pd.read_csv('Data/Train_References-22042015/Train_References/emotion_tweets.csv')
print(emotion)

"""data_list = []
tweet_list = open('Data/TRAIN_TWEETS_ID-03042015/TRAIN_TWEETS_ID.txt')
print(tweet_list)
for tweet in tweet_list:
    pol = polarity[polarity[] == tweet].to_dict('records')
    print(pol)
    #nat =
    #em ="""

polarity.columns = ['id', 'polarity']
nature.columns = ['id', 'nature']
emotion.columns = ['id', 'emotion']

all_data = pd.merge(polarity, nature, how='outer', on='id')
all_data = pd.merge(all_data, emotion, how='outer', on='id')
print(all_data)

all_data.to_csv('labelled_train_data.csv')





















