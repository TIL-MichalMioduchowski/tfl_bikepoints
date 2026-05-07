import os
import sys
from dotenv import load_dotenv
from pathlib import Path
from modules.setup_logging import setup_logging
from modules.extract_function import extract
from modules.load_function import load

logger = setup_logging('logs')
logger.info('Logger initialised.')

url = 'https://api.tfl.gov.uk/BikePoint'

load_dotenv()

AWS_KEY_ID = os.getenv('AWS_KEY_ID')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
BUCKET = os.getenv('BUCKET')

print(f'[main] BUCKET set: {bool(BUCKET)}', flush=True)
print(f'[main] AWS_KEY_ID set: {bool(AWS_KEY_ID)}', flush=True)
print(f'[main] AWS_SECRET_KEY set: {bool(AWS_SECRET_KEY)}', flush=True)

if extract(url, 3, 'data'):
    data_dir = Path('data')
    load(AWS_KEY_ID, AWS_SECRET_KEY, BUCKET, data_dir)
    print('[main] Script ran successfully.', flush=True)
    logger.info('Script ran succesfully.')
else:
    print('[main] Extract failed. Script stopped.', flush=True)
    logger.error('Extract failed. Script stopped.')
    sys.exit(1)