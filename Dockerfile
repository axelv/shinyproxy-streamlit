FROM python:3.8
RUN pip install streamlit pandas numpy elasticsearch eland
COPY . /app
WORKDIR /app
EXPOSE 8501
ENV ES_HOSTS https://74e30042023542b39d86b6b3a4ba3d2d.europe-west1.gcp.cloud.es.io:9243
# ENTRYPOINT ["streamlit","run"]
CMD ["streamlit", "run", "app.py", "--server.port=8501"]