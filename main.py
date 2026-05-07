from modules.setup_logging import setup_logging
from modules.extract_function import extract

logger = setup_logging('logs')

url = 'https://api.tfl.gov.uk/BikePoint'

extract(url, 3, 'data')

