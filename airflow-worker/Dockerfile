FROM docker.io/bitnami/airflow-worker:1.10.10

ADD airflow/requirements.txt /requirements.txt
ADD data /opt/bitnami/airflow/data
ADD models /opt/bitnami/airflow/models

RUN bash -c "source /opt/bitnami/airflow/venv/bin/activate && \
    pip install -r requirements.txt && \
    deactivate"