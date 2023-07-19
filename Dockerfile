FROM ubuntu:22.04

COPY backend /

RUN apt-get update && apt-get install -y python3 python3-pip python3-dev curl 

RUN curl -sSL https://install.python-poetry.org | python3 -

# export PATH=$PATH:/root/.local/bin

WORKDIR /backend

RUN /root/.local/bin/poetry install

EXPOSE 3000
EXPOSE 27017 
CMD ["/root/.local/bin/poetry", "run", "backend"]
