# build from base conda container
FROM continuumio/miniconda3

# Add app to working directory
WORKDIR /app
ADD . /app

# create conda environment for yml file
COPY env.yml /app/env.yml
RUN conda env create -f env.yml

# activate conda environment
SHELL ["conda", "run", "-n", "ml_flask_env", "/bin/bash", "-c"]

# add paths to PYTHONPATH
ENV PYTHONPATH "${PYTHONPATH}:src/models"
ENV PYTHONPATH "${PYTHONPATH}:src/data/scrapers"
ENV PYTHONPATH "${PYTHONPATH}:src/data/prrocessing" 
ENV PYTHONPATH "${PYTHONPATH}:src/features"

# establish entrypoiny
ENTRYPOINT ["conda", "run", "-n", "ml_flask_env", "python", "app/app.py"]
