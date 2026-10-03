import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file from backend directory or project root
backend_dir = Path(__file__).resolve().parent.parent
env_path = backend_dir / '.env'

if env_path.exists():
    load_dotenv(dotenv_path=env_path)
else:
    load_dotenv()


class Settings:
    # AWS service regions
    AWS_S3_REGION: str = os.getenv('AWS_S3_REGION', 'ap-south-1')
    AWS_DATA_REGION: str = os.getenv('AWS_DATA_REGION', 'ap-south-2')
    AWS_BEDROCK_REGION: str = os.getenv('AWS_BEDROCK_REGION', 'us-east-1')

    # AWS resources
    AWS_GLUE_DATABASE: str = os.getenv(
        'AWS_GLUE_DATABASE',
        'medical_operations_db'
    )

    AWS_S3_BUCKET: str = os.getenv(
        'AWS_S3_BUCKET',
        'medical-operations-bharath-2026'
    )

    AWS_ATHENA_WORKGROUP: str = os.getenv(
        'AWS_ATHENA_WORKGROUP',
        'primary'
    )

    AWS_ATHENA_OUTPUT: str = os.getenv(
        'AWS_ATHENA_OUTPUT',
        's3://medical-operations-athena-results-bharath-2026/'
    )

    AWS_BEDROCK_MODEL: str = os.getenv(
        'AWS_BEDROCK_MODEL',
        'anthropic.claude-3-5-sonnet-20240620-v1:0'
    )

    # Optional explicit credentials.
    # In deployment, prefer the platform's IAM/credential mechanism.
    AWS_ACCESS_KEY_ID: str = os.getenv('AWS_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY: str = os.getenv('AWS_SECRET_ACCESS_KEY', '')
    AWS_SESSION_TOKEN: str = os.getenv('AWS_SESSION_TOKEN', '')


settings = Settings()