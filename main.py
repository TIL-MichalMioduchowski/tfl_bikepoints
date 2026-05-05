import requests
import json
import os
from datetime import datetime
import time
import logging

log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
log_filename = f'{log_dir}/{timestamp}.log'

logging.basicConfig(
    filename=log_filename,
    format=f'%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger()
logger.info(f'Logger initialised.')

url = f'https://api.tfl.gov.uk/BikePoint'
response = requests.get(url)
data = response.json()

count = 0
max_tries = 3

while count < max_tries:
    if 200 <= response.status_code < 300:

        dir = 'data'
        os.makedirs(dir, exist_ok=True)
        filename = f'{dir}/{timestamp}.json'
        with open(filename, 'w') as file:
            json.dump(data, file)

        print(f'File {filename} was succesfully created.')
        logger.info(f'File {filename} was succesfully created.')
        break

    elif response.status_code >= 500:
        time.sleep(10)
        count += 1
        print(f'Trying again. Attempt {count}.')
        logger.info(f'Trying again. Attempt {count}.')

    else:
        print(f'Error: {response.status_code} {data.get("message", "no message found")}')
        logger.info(f'Error: {response.status_code} {data.get("message", "no message found")}')
        break