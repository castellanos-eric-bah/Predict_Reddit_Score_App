import pandas as pd 
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer, MultiLabelBinarizer
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS

from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LassoCV
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import ElasticNetCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

from joblib import dump, load

#from modelling_helpers import model_diagnostics

MODEL_DATA = pd.read_csv("opt/bitnami/airflow/task_data/features_added/features_added_reddit.csv")
MODEL_PERFORMANCE = dict()

def model(data=MODEL_DATA,name, model_function, X_train, y_train, **kwargs): # add back X_test, y_test and performance
    y = data['score'].values
    x = data[['comms_num', 'gilded', 'subjectivity', 'word_count', 'senti_comp']]
    x = x.to_numpy()
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10)
    model = model_function(kwargs)
    model.fit(X_train,y_train)
    #performance[name] = model_diagnostics(model, X_test, y_test)
    #dump(model, 'C:\\Users\\588175\\Projects\\ML_Flask_App\\ml_flask\\models\\{}.joblib'.format(name))
    return model

if __name__ == "__main__":
    model_data = preparation(MODEL_DATA)
    X_train, X_test, y_train, y_test = model_data[0], model_data[1], model_data[2], model_data[3]
    model('Linear Regression', LinearRegression, X_train, y_train, X_test, y_test, MODEL_PERFORMANCE)
    #model('KNN Regression', KNeighborsRegressor, X_train, y_train, X_test, y_test, MODEL_PERFORMANCE)
