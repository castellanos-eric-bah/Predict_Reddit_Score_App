FROM docker.io/bitnami/airflow:1.10.10

COPY airflow/requirements.txt /requirements.txt
COPY data /task_data
COPY models /ml_models

USER root

RUN chmod -R 777 /task_data /ml_models

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y vim && \
    rm -r /var/lib/apt/lists /var/cache/apt/archives
    
RUN bash -c "source /opt/bitnami/airflow/venv/bin/activate && \
    pip install -r requirements.txt && \
    deactivate"
