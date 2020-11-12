from datetime import timedelta

from airflow import DAG

from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator 

from airflow.utils.dates import days_ago

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

# define taks
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

t2 = BashOperator(
    task_id='sleep',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)

# execute DAG
t1 >> t2