import requests
import json
from datetime import datetime

#variable
url = 'https://api.tfl.gov.uk/BikePoint/BikePoints_888'
response = requests.get(url)
data = response.json()
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
filename = f'bikepoint_888_{timestamp}.json'

if response.status_code == 200:
    with open(filename, 'w') as file:
        json.dump(data, file)
    print(f'File {filename} was succesfully created!')
else:
    error_message = data.get('message', 'no message given')
    print(f'Error creating {filename}: {response.status_code} {error_message}')

#Hint
#error_message = data.get('message', 'no message given')
#print(error_message)


