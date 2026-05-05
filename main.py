import requests
import json
import os
from datetime import datetime
import time

url = f'https://api.tfl.gov.uk/BikePoint'
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
response = requests.get(url)
data = response.json()

if response.status_code == 200:

    dir = 'data'
    os.makedirs(dir, exist_ok=True)
    filename = f'{dir}/{timestamp}.json'
    with open(filename, 'w') as file:
        json.dump(data, file)

    print(f'File {filename} was succesfully created.')

else:
    print(f'Error: {response.status_code} {data.get("message", "no message found")}')
