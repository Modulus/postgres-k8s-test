
FROM python:3.9-bullseye

COPY main.py ./main.py
COPY Pipfile .
COPY Pipfile.lock .

RUN pip install gunicorn pipenv && pipenv install && pipenv lock --requirements > requirements.txt && pip install -r requirements.txt


CMD ["gunicorn", "--log-level=info", "--timeout=260", "--bind", "0.0.0.0:5000",  "main:app"]

EXPOSE 5000