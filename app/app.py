import sys
sys.path.append("C:\\Users\\588175\\Projects\\ML_Flask_App\\ml_flask\\src\\models")
sys.path.append("C:\\Users\\588175\\Projects\\ML_Flask_App\\ml_flask\\src\\data\\scrapers")
sys.path.append("C:\\Users\\588175\\Projects\\ML_Flask_App\\ml_flask\\src\\data\\prrocessing")
sys.path.append("C:\\Users\\588175\\Projects\\ML_Flask_App\\ml_flask\\src\\features")

import numpy as np
import pandas as pd

from flask import Flask, request
from flask import render_template
from joblib import load
from sklearn.linear_model import LinearRegression

from scrape_reddit import REDDIT, scrape
from process import process
from build_features import feature_engineering
from train_model import preparation, model
from predict_model import predict_func

app = Flask(__name__)
#model = load("C:\\Users\\588175\\Projects\\ML_Flask_App\\ml_flask\\models\\Linear Regression.joblib")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=["POST"])
def predict():
    features = [str(x) for x in request.form.values()]
    subreddit, title, body = features[0], features[1], features[2]
    reddit_data = scrape(REDDIT, subreddit)
    processed_data = process(reddit_data)
    features_added = feature_engineering(processed_data)
    model_data = preparation(features_added)
    X_train, y_train = model_data[0], model_data[2]
    prediction_model = model('Linear Regression', LinearRegression, X_train, y_train)

    # Add features to prediction data
    commns_num, gilded = reddit_data['comms_num'].mean(), reddit_data['gilded'].mean()
    prediction_data = pd.DataFrame([[body,commns_num,gilded]],columns=['body', 'comms_num', 'gilded'])
    prediction_data_features = feature_engineering(prediction_data)
    prediction_data_features = prediction_data_features[['comms_num', 'gilded', 'subjectivity', 'word_count', 'senti_comp']]

    final_features = prediction_data_features.to_numpy()
    prediction = prediction_model.predict(final_features)

    return 'Predicted Score for Reddit Post: {}'.format(prediction)

if __name__ == '__main__':
    app.run()