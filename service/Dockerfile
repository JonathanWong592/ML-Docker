FROM python:3.6-stretch

RUN apt-get update && \
	apt-get install -y gcc make apt-transport-https ca-certificates build-essential

# check our python environment
RUN python3 --version
RUN pip3 --version

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app

COPY requirements.txt /usr/src/app

WORKDIR /usr/src/app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"]