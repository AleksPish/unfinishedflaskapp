FROM python:3.8-slim-buster
WORKDIR /app
COPY app.py ./
COPY index.html ./templates/index.html
COPY requirements.txt ./
EXPOSE 5000
RUN pip install -r ./requirements.txt
CMD ["python","app.py"]
