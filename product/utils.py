import boto3
from django.conf import settings

import boto3


def generate_presigned_url(file_key, expiration=3600):
    """
    Generate a presigned URL to share an S3 object
    :param file_key: S3 object key (e.g. "products/img1.jpg")
    :param expiration: Time in seconds for the presigned URL to remain valid
    """
    s3_client = boto3.client(
        "s3",
        region_name=settings.AWS_S3_REGION_NAME,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )
    try:
        response = s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": settings.AWS_STORAGE_BUCKET_NAME, "Key": file_key},
            ExpiresIn=expiration,
        )
    except Exception as e:
        print(e)
        return None

    return response
