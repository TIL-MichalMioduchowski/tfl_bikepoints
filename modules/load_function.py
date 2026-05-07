import logging
import os
import sys
import boto3

logger = logging.getLogger(__name__)

def load(AWS_KEY_ID, AWS_SECRET_KEY, BUCKET, data_dir):
    """
    This will load any json files in the data directory to a specified S3 bucket.

    Args:
        AWS_KEY_ID (string): The AWS access key ID attached to an IAM user, with relevant permissions.
        AWS_SECRET_KEY (string): The AWS secret access key attached to an IAM User, with relevant permissions.
        BUCKET (string): The name of the S3 bucket.
        data_dir (Path): Path object for the directory where the data is located e.g. Path('data')
    """

    print(f'[load] BUCKET set: {bool(BUCKET)} (len={len(BUCKET) if BUCKET else 0})', flush=True)
    print(f'[load] AWS_KEY_ID set: {bool(AWS_KEY_ID)}', flush=True)
    print(f'[load] AWS_SECRET_KEY set: {bool(AWS_SECRET_KEY)}', flush=True)
    print(f'[load] data_dir: {data_dir} exists={data_dir.exists()}', flush=True)

    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_KEY
    )

    files = list(data_dir.glob('*.json'))
    print(f'[load] Found {len(files)} json file(s): {[str(f) for f in files]}', flush=True)

    if not files:
        print('[load] No files to upload. Exiting load.', flush=True)
        return

    processed = 0

    for file in files:
        filename = os.path.basename(file)
        try:
            s3_client.upload_file(str(file), BUCKET, filename)
            print(f'[load] Uploaded {filename} to S3.', flush=True)
            logger.info(f'{file} uploaded to S3.')

            s3_client.head_object(Bucket=BUCKET, Key=filename)
            os.remove(file)
            print(f'[load] Removed local file {file}.', flush=True)
            logger.info(f'File {file} removed locally.')
            processed += 1
        except Exception as e:
            print(f'[load] UPLOAD FAILED for {filename}: {type(e).__name__}: {e}', flush=True)
            logger.error(e)

    print(f'[load] Processed {processed} of {len(files)} file(s).', flush=True)
    logger.info(f'Processed {processed} files.')

    if processed == 0:
        print('[load] Nothing was uploaded — exiting with error.', flush=True)
        sys.exit(1)