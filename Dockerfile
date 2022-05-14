FROM python:3.8

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
RUN mkdir app

COPY *.py /app
ENV PYTHONPATH=/app
WORKDIR /app/
EXPOSE 5001