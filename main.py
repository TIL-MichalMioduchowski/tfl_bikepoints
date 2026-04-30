import requests
import json
import os
from datetime import datetime

response = requests.get('https://api.tfl.gov.uk/BikePoint')

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