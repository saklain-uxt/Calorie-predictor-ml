import logging
import os
import datetime as dt

LOG_FILE = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.log'

logs_path_ = os.path.join(os.getcwd(), 'logs')

os.makedirs(logs_path_, exist_ok=True)

file_path = os.path.join(logs_path_, LOG_FILE)


def logging_config():
    logging.basicConfig(
        filename=file_path,
        level=logging.INFO,
        format='%(asctime)s:%(levelname)s:%(message)s:%(name)s:%(lineno)d'
    )

logging_config()    
