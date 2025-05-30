from flask import Flask
import logging

app = Flask(__name__)

logger = logging.getLogger(__name__)
logger.setLevel("INFO")
# logger.propagate = True
if not logger.handlers:
    handler = logging.StreamHandler()
    # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    # handler.setFormatter(formatter)
    logger.addHandler(handler)

@app.route('/hello/')
def hello_world():
    logger.info("test info log")
    logger.warning("test warning log")
    logger.error("test error log")
    return 'Hello World!'

# if __name__ == '__main__':
    # app.run(debug=True)


# running with gunicorn:
# gunicorn -b 127.0.0.1:8000 -c gunicorn.config.py --threads 2 --workers 4 app:app
