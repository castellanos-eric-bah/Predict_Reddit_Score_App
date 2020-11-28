import logging

import boto3
from botocore.exceptions import NoCredentialsError

from joblib import load

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)

ACCESS_KEY = 'AKIAJ4DZW6GBKCD7PVOA'
SECRET_KEY = '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'

def upload_to_aws(local_file='/ml_models/Linear Regression.joblib', bucket='flaksmlmodels', s3_file='LinearRegressionModel'):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        LOG.info("Upload Successful")
        return True
    except FileNotFoundError:
        LOG.error("The file was not found")
        return False
    except NoCredentialsError:
        LOG.error("Credentials not available")
        return False

if __name__ == "__main__":
    upload_to_aws('/home/ecast229/Predict_Reddit_Score_App/models/Linear Regression.joblib', 'flaksmlmodels', 'LinearRegressionModel')