from google.cloud import storage
import os

BUCKET_NAME = os.environ.get('GCP_BUCKET_NAME')

def upload_to_gcp(image):
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)

    blob = bucket.blob('avatar/image.png')

    blob.upload_from_file(image)