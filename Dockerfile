FROM tensorflow/tensorflow:2.0.0-py3
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

WORKDIR /app/src
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
