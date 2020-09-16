
 # This file transforms the original data from the DEFT tweet classification challenge into a csv file
# this csv contains : the id of the tweet, its polarity (pos, neg, neutral or mixt), the nature of the tweets and a finer classification of the sentiment or emotion

import pandas as pd


# opening the original files

def from_text_to_csv(in_path, out_path):
    # simple functions which turns a space separated text file into a csv
    txt_file = open(in_path, 'r')
    out_file = open(out_path, 'w')
    txt_file.readline()
    for line in txt_file:
        (id, el) = line.strip().split('\t')
        out_file.write(','.join([id, el]) + '\n')
    txt_file.close()
    out_file.close()



polarity = open('Data/labelled_data/Test_References/T1.txt', 'r')
polarity_csv = open('Data/labelled_data/Test_References/test_polarity.csv', 'w')
polarity.readline() # skip first line
for line in polarity:
    (id, pol) = line.strip().split('\t')
    polarity_csv.write(','.join([id, pol]) + '\n')
polarity.close()
polarity_csv.close()

#polarity = pd.read_csv('Data/Train_References-22042015/Train_References/T1.csv')
#print(polarity)

nature = open('Data/labelled_data/Test_References/test_nature.txt', 'r')
nature_csv = open('Data/labelled_data/Test_References/test_nature.csv', 'w')
nature.readline() # skip first line
for line in nature:
    print(line.strip().split('\t'))
    (id, nat) = line.strip().split('\t')
    nature_csv.write(','.join([id, nat]) + '\n')
nature.close()
nature_csv.close()


from_text_to_csv('Data/labelled_data/Test_References/test_emotion.txt', 'Data/labelled_data/Test_References/test_emotion.csv')

polarity = pd.read_csv('Data/labelled_data/Test_References/test_polarity.csv')
print(polarity)

nature = pd.read_csv('Data/labelled_data/Test_References/test_nature.csv')
print(nature)

emotion = pd.read_csv('Data/labelled_data/Test_References/test_emotion.csv')
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

all_data.to_csv('labelled_test_data.csv')





















