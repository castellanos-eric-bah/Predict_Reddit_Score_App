from joblib import load

from sklearn.datasets import make_blobs 

from build_features import feature_engineering
from train_model import preparation 

def predict_func(model, new_post):
    model = load(model)
    data = feature_engineering(new_post)
    # estimate number of comments and gilded comments based on subreddit average
    prepared = preparation(data)
    X = prepared[1]
    return model.predict(X)

