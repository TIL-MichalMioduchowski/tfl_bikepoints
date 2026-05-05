import requests
import json
import os
from datetime import datetime
import time

timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

url = f'https://api.tfl.gov.uk/BikePoint'
response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    folder = 'bikepoints'

    os.makedirs(folder, exist_ok=True)

    for bp in data:
        bp_id = bp['id']
        filename = os.path.join(folder, f'{bp_id}.json')
        with open(filename, 'w') as file:
            json.dump(bp, file)
        print(f'File {filename} was successfully created!')
else:
    print(f'Error:{response.status_code}')