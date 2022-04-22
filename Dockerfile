FROM tensorflow/tensorflow:1.13.2-gpu-py3
WORKDIR /code
RUN apt-get update 
RUN apt-get install -y libsm6 libxext6 libxrender-dev vim
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
