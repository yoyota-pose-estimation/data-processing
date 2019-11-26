FROM tensorflow/tensorflow:2.0.0-py3
WORKDIR /app

# for cache
RUN pip install tensorflow kubernetes
COPY . .
RUN python setup.py install

ENTRYPOINT [ "pair_image" ]
