FROM tensorflow/tensorflow:1.14.0-gpu-py3
WORKDIR /code
ENV HTTP_PROXY="http://child-prc.intel.com:913"
ENV HTTPS_PROXY="http://child-prc.intel.com:913"
RUN sed -i "s@http://.*archive.ubuntu.com@http://linux-ftp.bj.intel.com/pub/mirrors@g" /etc/apt/sources.list
RUN sed -i "s@http://.*security.ubuntu.com@http://linux-ftp.bj.intel.com/pub/mirrors@g" /etc/apt/sources.list
RUN apt-get update 
RUN apt-get install -y libsm6 libxext6 libxrender-dev
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
