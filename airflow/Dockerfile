FROM docker.io/bitnami/airflow:1.10.10

USER root

ADD airflow/requirements.txt /requirements.txt
ADD data /opt/bitnami/airflow/data
ADD models /opt/bitnami/airflow/models

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y vim && \
    rm -r /var/lib/apt/lists /var/cache/apt/archives
    
RUN bash -c "source /opt/bitnami/airflow/venv/bin/activate && \
    pip install -r requirements.txt && \
    deactivate"
