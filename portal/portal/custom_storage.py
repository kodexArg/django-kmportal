from storages.backends.s3boto3 import S3Boto3Storage

class DocumentStorage(S3Boto3Storage):
    location = 'documents'
