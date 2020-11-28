import json
from io import BytesIO

import boto3
from joblib import load

def read_s3():
  credentials = json.load(open('/home/ecast229/Predict_Reddit_Score_App/aws_cred.json'))

  client = boto3.client('s3',
                        aws_access_key_id=credentials['ACCESS_KEY'],
                        aws_secret_access_key=credentials['SECRET_KEY']
                      )

  with BytesIO() as f:
      client.download_fileobj('flaksmlmodels','LinearRegressionModel', f)
      f.seek(0)    # move back to the beginning after writing
      model = load(f)

  return model

if __name__ == '__main__':
    print(read_s3())
