import unittest

import pandas as pd
from pandas.io.json import json_normalize

from joblib import load

class TestDataintegrity(unittest.TestCase):

    def setUp(self):
        self.data = {
            'title' : 'Excel Wizard',
            'score' : 50,
            'id' : 'fg73za',
            'url' : 'https://i.redd.it/0c9louclfrl41.jpg,59',
            'comms_num' : 0,
            'body' : 'Microsoft Excel is the ultimate data science tool!!',
            'gilded' : 0,
        }
        self.raw = pd.read_csv("/home/ecast229/Predict_Reddit_Score_App/data/raw/raw_reddit_raw.csv")
        self.features = pd.read_csv("/home/ecast229/Predict_Reddit_Score_App/data/features_added/features_added_reddit.csv")

    def test_data_structure(self):
        """
        The nested data structure should be flattened
        into a single record. We'll just use pandas
        for this.
        """

        expected_columns = ['title', 'score', 'id', 'url', 'comms_num', 'body', 'gilded']

        dataframe = json_normalize(self.data)
        actual_columns = dataframe.columns
        self.assertEqual(set(expected_columns), set(actual_columns))

    def test_data_structure_raw(self):
        expected_columns = ['title', 'score', 'id', 'url', 'comms_num', 'body', 'gilded']
        data = self.raw
        self.assertEqual(data.columns.tolist(), expected_columns)

    def test_data_structure_features(self):
        expected_columns = ['title', 'score', 'id', 'url', 'comms_num', 'body', 'gilded', 'subjectivity', 'word_count', 'sentiment', 'senti_pos', 'senti_neg', 'senti_comp']
        data = self.features
        self.assertEqual(data.columns.tolist(), expected_columns)

class TestModelIntegrity(unittest.TestCase):

    def setUp(self):
        self.model = load("/home/ecast229/Predict_Reddit_Score_App/models/Linear Regression.joblib")

    def test_model_coeffs(self):
        self.assertEqual(len(model.coef_),5)

    




    