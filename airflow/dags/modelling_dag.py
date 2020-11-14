from datetime import timedelta

from airflow import DAG

from airflow.operators.http_operator import SimpleHttpOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator 

from airflow.utils.dates import days_ago

from tasks.scrape_reddit import REDDIT, scrape
from tasks.process import process
from tasks.build_features import feature_engineering
from tasks.train_model import preparation, model
from tasks.upload_to_s3 import upload_to_aws
from tasks.predict_model import predict_func

default_args = {
    'owner' : 'airflow',
    'depends_on_past' : False,
    'start_date' : days_ago(2),
    'email' : ['ericcastellanos229@gmail.com'],
    'email_on_failure' : False,
    'email_on_retry' : False,
    'retries' : 1,
    'retry_delay' : timedelta(minutes=5),
}

dag = DAG(
    'modelling_dag',
    default_args=default_args,
    description='A DAG to create a Machine Learning Pipeline for my app',
    schedule_interval=timedelta(days=1)
)

# define tasks

scrape = PythonOperator(
    task_id='scrape_reddit',
    provide_context=True,
    python_callable=scrape,
    dag=dag,
)

process = PythonOperator(
    task_id='process_reddit',
    provide_context=True,
    python_callable=process,
    dag=dag,
)

build_features = PythonOperator(
    task_id='build_features',
    provide_context=True,
    python_callable=feature_engineering,
    dag=dag,
)

model_preparation = PythonOperator(
    task_id='preparation',
    provide_context=True,
    python_callable=preparation,
    dag=dag,
)

model = PythonOperator(
    task_id='model',
    provide_context=True,
    python_callable=model,
    dag=dag,
)

predict = PythonOperator(
    task_id='predict',
    provide_context=True,
    python_callable=predict_func,
    dag=dag,
)

# execute DAG
scrape >> process >> build_features >> model_preparation >> model >> predict
