# build from base conda container
FROM continuumio/miniconda3

# create conda environment for yml file
ADD env.yml .
RUN conda env create -f env.yml

# activate conda environment
RUN conda run -n ml_flask_env /bin/bash -c
#RUN conda activate ml_flask_env

# add paths to PYTHONPATH
ENV PYTHONPATH "${PYTHONPATH}:C:\\Users\\588175\\Projects\\ML_Flask_App\\ml_flask\\src\\models"
ENV PYTHONPATH "${PYTHONPATH}:C:\\Users\\588175\\Projects\\ML_Flask_App\\ml_flask\\src\\data\\scrapers"
ENV PYTHONPATH "${PYTHONPATH}:C:\\Users\\588175\\Projects\\ML_Flask_App\\ml_flask\\src\\data\\prrocessing" 
ENV PYTHONPATH "${PYTHONPATH}:C:\\Users\\588175\\Projects\\ML_Flask_App\\ml_flask\\src\\features"

# Add app and establish entrypoint
ENTRYPOINT ["python3", "C:\Users\588175\Projects\ML_Flask_App\ml_flask\app\app.py"]
