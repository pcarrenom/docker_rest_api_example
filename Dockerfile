FROM python:latest

RUN pip install requests

RUN useradd -rm -d /home/worker -s /bin/bash -g root -G sudo -u 1000 worker
COPY client.py /home/worker
RUN chown -R worker /home/worker
WORKDIR /home/worker
USER 1000

CMD ["python3", "train.py"]
