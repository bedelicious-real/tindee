from google.cloud import storage
import os
import io

BUCKET_NAME = os.environ.get('GCP_BUCKET_NAME')

def upload_to_gcp(image_content):
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)

    image = io.BytesIO(image_content)
    blob = bucket.blob('avatar/image.png')

    blob.upload_from_file(image)
    blob.make_public()
    return blob.public_url