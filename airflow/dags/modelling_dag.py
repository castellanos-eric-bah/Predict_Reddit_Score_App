from datetime import timedelta

from airflow import DAG

from airflow.operators.http_operator import SimpleHttpOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator 

from airflow.utils.dates import days_ago

from tasks.pull_top_subreddits import get_top_subreddits
from tasks.scrape_reddit import combine_to_one
from tasks.process import process
from tasks.build_features import feature_engineering
from tasks.train_model import model
from tasks.upload_to_s3 import upload_to_aws

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
pull_top_subreddits = PythonOperator(
    task_id='pull_top_subreddits',
    provide_context=False,
    python_callable=get_top_subreddits,
    dag=dag,
)

scrape = PythonOperator(
    task_id='scrape_reddit',
    provide_context=False,
    python_callable=combine_to_one,
    dag=dag,
)

process = PythonOperator(
    task_id='process_reddit',
    provide_context=False,
    python_callable=process,
    dag=dag,
)

build_features = PythonOperator(
    task_id='build_features',
    provide_context=False,
    python_callable=feature_engineering,
    dag=dag,
)

model = PythonOperator(
    task_id='model',
    provide_context=False,
    python_callable=model,
    dag=dag,
)

upload = PythonOperator(
    task_id='upload_to_s3',
    provide_context=False,
    python_callable=upload_to_aws,
    dag=dag,
)

# execute DAG
pull_top_subreddits >> scrape >> process >> build_features >> model >> upload
