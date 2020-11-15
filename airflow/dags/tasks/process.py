import pandas as pd 

DTYPE = {
    'title': 'str',
    'score': 'int',
    'id': 'str',
    'url': 'str',
    'comms_num': 'int',
    'body': 'str',
    'gilded': 'int'
}

REDDIT_DATA = pd.read_csv("/opt/bitnami/data/raw/raw_reddit_raw.csv", dtype=DTYPE)

def process(data):
    data = data[(data.body != '[deleted]') | (data.body != '[removed]') | (data.body != '')]
    data = data[~(data['body'].isna() | data['body'].isna())]
    data.to_csv("/opt/bitnami/airflow/data/processed/processed_reddit.csv")
    return data

if __name__ == "__main__":
    process(REDDIT_DATA)

