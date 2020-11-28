
import sys

sys.path.append("/home/ecast229/Predict_Reddit_Score_App/src/features")
sys.path.append("/home/ecast229/Predict_Reddit_Score_App/src/models")
sys.path.append("/home/ecast229/Predict_Reddit_Score_App/src/data/prrocessing")

import numpy as np
import pandas as pd

from flask import Flask, request
from flask import render_template

from joblib import load
from sklearn.linear_model import LinearRegression

import boto3

from build_features import feature_engineering
from read_s3 import read_s3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=["POST"])
def predict():
    features = [str(x) for x in request.form.values()]
    subreddit, title, body = features[0], features[1], features[2]

    # Add features to prediction data
    commns_num, gilded = 50, 50
    prediction_data = pd.DataFrame([[body,commns_num,gilded]],columns=['body', 'comms_num', 'gilded'])
    prediction_data_features = feature_engineering(prediction_data)
    prediction_data_features = prediction_data_features[['comms_num', 'gilded', 'subjectivity', 'word_count', 'senti_comp']]

    final_features = prediction_data_features.to_numpy()
    prediction_model = read_s3()
    prediction = prediction_model.predict(final_features)

    #return 'Predicted Score for Reddit Post: {}'.format(prediction)
    return render_template('prediction.html', score=str(prediction[0]))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')