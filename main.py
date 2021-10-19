
import logging
import os
import sys
from time import gmtime, strftime, sleep, time

from flask import Flask, json, jsonify
import psycopg2

app = Flask(__name__)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


logger.info("Starting server")

@app.route('/')
def hello_world():
    try:
        db_url = os.environ["DATABASE_URL"]
        logger.info(f"Connection to {db_url}")
        connection = psycopg2.connect(db_url)

        cursor = connection.cursor()

        cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false")

        results = cursor.fetchall()

        for result in results:
            print(result)

        return jsonify(results)
    except psycopg2.OperationalError as error:
        print("Failed to connect")
        print(error)
    except psycopg2.Error as error:
        print("Database error")
        print(error)

if __name__ == '__main__':
    logger.info('Starting application')
    app.run()
    logger.info('Application started')

