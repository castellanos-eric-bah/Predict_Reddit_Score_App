FROM docker.io/bitnami/airflow-scheduler:1.10.10

COPY airflow/requirements.txt /requirements.txt
COPY data /task_data
COPY models /ml_models

USER root

RUN sudo chmod -R 777 /task_data /ml_models

RUN bash -c "source /opt/bitnami/airflow/venv/bin/activate && \
    pip install -r requirements.txt && \
    deactivate"