FROM python:3.9.4

RUN pip install --upgrade pip

RUN pip install -U discord.py==1.7.2

WORKDIR /bot

COPY main.py /bot

RUN ["python", "main.py"]
