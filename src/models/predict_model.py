import sys
sys.path.insert(0, "C:\\Users\\588175\\Projects\\ML_Flask_App\\ml_flask\\src\\models")
sys.path.insert(0, "C:\\Users\\588175\\Projects\\ML_Flask_App\\ml_flask\\src\\features\\build_features.py")

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

