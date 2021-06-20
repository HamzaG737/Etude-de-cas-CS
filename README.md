# ETUDE DE CAS FILIERE RECHERCHE CENTRALESUPELEC

This is the github repo for the use case study of the project 27 . The subject of this project is the tweets analysis for the prediction of covid propagation parameters.

The file **preprocessing.ipynb** transforms the input pickles into a csv file  that contains the tweet text and other relevant informations such as : datetime, language, retweets, replies and likes ,etc ... 

Since the html code of each tweet does not contain the location, you can find in **Exploration/getting_location.ipynb** a code that extracts the location using twitter api than structures it using the python library **geopy**. 

Finally, you can find in **Exploration/get_old_tweet.ipynb** a code that uses the library **GetOldTweets3** which enables the extraction of old tweets based on the parameters of the location, date, search keywords (covid for instance ),etc...  The dataset obtained via this library can complete the first one in case we have a lack of data.
