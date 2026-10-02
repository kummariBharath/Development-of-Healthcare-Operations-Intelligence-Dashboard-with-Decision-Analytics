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
    AWS_REGION: str = os.getenv('AWS_REGION', 'ap-south-1')
    AWS_GLUE_DATABASE: str = os.getenv('AWS_GLUE_DATABASE', 'medical_operations_db')
    AWS_S3_BUCKET: str = os.getenv('AWS_S3_BUCKET', 'medical-operations-bharath-2026')
    AWS_ATHENA_WORKGROUP: str = os.getenv('AWS_ATHENA_WORKGROUP', 'primary')
    AWS_ATHENA_OUTPUT: str = os.getenv('AWS_ATHENA_OUTPUT', 's3://medical-operations-bharath-2026/athena-query-results/')
    AWS_BEDROCK_MODEL: str = os.getenv('AWS_BEDROCK_MODEL', 'anthropic.claude-3-5-sonnet-20240620-v1:0')
    
    AWS_ACCESS_KEY_ID: str = os.getenv('AWS_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY: str = os.getenv('AWS_SECRET_ACCESS_KEY', '')
    AWS_SESSION_TOKEN: str = os.getenv('AWS_SESSION_TOKEN', '')

settings = Settings()
