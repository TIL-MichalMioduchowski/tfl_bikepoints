import requests
import json
import os
from datetime import datetime
import time
import logging

url = f'https://api.tfl.gov.uk/BikePoint'
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
response = requests.get(url)
data = response.json()

count = 0
max_tries = 3

while count < max_tries:
    if 20 <= response.status_code < 300:

        dir = 'data'
        os.makedirs(dir, exist_ok=True)
        filename = f'{dir}/{timestamp}.json'
        with open(filename, 'w') as file:
            json.dump(data, file)

        print(f'File {filename} was succesfully created.')
        break

    elif response.status_code >= 500:
        time.sleep(10)
        count += 1
        print(f'Trying again. Attempt {count}.')

    else:
        print(f'Error: {response.status_code} {data.get("message", "no message found")}')
        break