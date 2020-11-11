import sys
sys.path.insert(0, "C:\\Users\\588175\\Projects\\ML_Flask_App\\ml_flask\\src\\data\\prrocessing")

import pandas as pd 
import numpy as np

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from process import DTYPE

REDDIT_DATA = pd.read_csv("C:\\Users\\588175\\Projects\\ML_Flask_App\\ml_flask\\data\\processed\\processed_reddit.csv", dtype=DTYPE)

def get_sentiment(data):
    analyser = SentimentIntensityAnalyzer()
    data['sentiment'] = data['body'].apply(lambda x: analyser.polarity_scores(x))
    return data

def feature_engineering(data):
    data['subjectivity'] = data['body'].str.count('I ') + data['body'].str.count("I'")
    data['word_count'] = data['body'].apply(lambda x: len(x.split()))
    # Add sentiment to data
    data = get_sentiment(data)
    data['senti_pos'] = data['sentiment'].apply(lambda x: x['pos'])
    data['senti_neg'] = data['sentiment'].apply(lambda x: x['neg'])
    data['senti_comp'] = data['sentiment'].apply(lambda x: x['compound'])
    data.to_csv("C:\\Users\\588175\\Projects\\ML_Flask_App\\ml_flask\\data\\features_added\\features_added_reddit.csv")
    return data

if __name__ == "__main__":
    feature_engineering(REDDIT_DATA)
