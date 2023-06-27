# General

This is a simple example of a REST API implemented with FastAPI and used to manage (spaw, kill, restart) a process in the host machine from a docker container.

# Testing

Run server using 

    $ python -m uvicorn main:app --reload --host 0.0.0.0


Start container using 

    $ docker run -it --add-host=host.docker.internal:host-gateway <container_name> bash

From within the container execute

    $ python client.py

Alternatevely, you can also use

    $ docker run -it --add-host=host.docker.internal:host-gateway client:lastest bash
