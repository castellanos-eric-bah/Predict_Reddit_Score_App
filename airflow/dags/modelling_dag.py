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
get_data = SimpleHttpOperator(
    task_id='get_data',
    http_conn_id='http://0.0.0.0:5000',
    endpoint='/predict',
    response_filter=lambda response: response.json()[0],
    dag=dag
)

scrape = PythonOperator(
    task_id='scrape_reddit',
    provide_context=True,
    python_callable=scrape,
    op_kwargs={'reddit' : REDDIT, 'subreddit' : 'datascience'},
    dag=dag,
)

process = PythonOperator(
    task_id='process_reddit',
    provide_context=True,
    python_calllable=process,
    op_kwargs={'data' : data},
    dag=dag,
)

build_features = PythonOperator(
    task_id='build_features',
    provide_context=True,
    python_calllable=feature_engineering,
    op_kwargs={'data' : data},
    dag=dag,
)

model_preparation = PythonOperator(
    task_id='preparation',
    provide_context=True,
    python_calllable=preparation,
    op_kwargs={'data' : data},
    dag=dag,
)

model = PythonOperator(
    task_id='model',
    provide_context=True,
    python_calllable=model,
    op_kwargs={'name' : name, 'model_function' : model_function, 'X_train' : X_train, 'y_train' : y_train},
    dag=dag,
)

predict = PythonOperator(
    task_id='predict',
    provide_context=True,
    python_calllable=predict,
    op_kwargs={'model' : model, 'new_post' : new_post},
    dag=dag,
)

# execute DAG
get_data >> scrape >> process >> build_features >> model_preparation >> model >> predict
