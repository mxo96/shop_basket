FROM python:3.8.1
WORKDIR /app
COPY . /app


ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 5000

RUN pip install -r requirements.txt
RUN python -m unittest discover -p 'test_*.py'

ENTRYPOINT ["flask", "run"]