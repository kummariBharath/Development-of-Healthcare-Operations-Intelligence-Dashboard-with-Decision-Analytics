import boto3
from app.config import settings

def get_boto3_session():
    """
    Creates and returns a boto3 Session using configured credentials or environment defaults.
    """
    session_kwargs = {
        'region_name': settings.AWS_REGION
    }
    if settings.AWS_ACCESS_KEY_ID and settings.AWS_SECRET_ACCESS_KEY:
        session_kwargs['aws_access_key_id'] = settings.AWS_ACCESS_KEY_ID.strip()
        session_kwargs['aws_secret_access_key'] = settings.AWS_SECRET_ACCESS_KEY.strip()
        if settings.AWS_SESSION_TOKEN:
            session_kwargs['aws_session_token'] = settings.AWS_SESSION_TOKEN.strip()

    return boto3.Session(**session_kwargs)

def get_sts_client():
    return get_boto3_session().client('sts')

def get_glue_client():
    return get_boto3_session().client('glue')

def get_athena_client():
    return get_boto3_session().client('athena')

def get_s3_client():
    return get_boto3_session().client('s3')

def get_bedrock_client():
    return get_boto3_session().client('bedrock-runtime')
