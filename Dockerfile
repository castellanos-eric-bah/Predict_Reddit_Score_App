# build from base conda container
FROM continuumio/miniconda3

# Add app to working directory
#WORKDIR /app
ADD . ./

# create conda environment for yml file
COPY env.yml ./
RUN conda env create -f env.yml

# add paths to PYTHONPATH
ENV PYTHONPATH "${PYTHONPATH}:src/models"
ENV PYTHONPATH "${PYTHONPATH}:src/data/scrapers"
ENV PYTHONPATH "${PYTHONPATH}:src/data/prrocessing" 
ENV PYTHONPATH "${PYTHONPATH}:src/features"

# create flask environment
EXPOSE 5000

# activate conda environment
RUN chmod 777 ~/.bashrc
RUN echo "source activate ml_flask_env" &gt; ~/.bashrc
ENV PATH /opt/conda/envs/ml_flask_env/bin:$PATH

# launch app
CMD ["python", "app/app.py"]
