import json
import logging
from typing import Dict, Any
from app.aws.session import get_bedrock_client
from app.config import settings

logger = logging.getLogger(__name__)

def invoke_bedrock_summary(prompt: str, context_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Invokes Amazon Bedrock LLM with structured metric context and prompt.
    """
    try:
        bedrock = get_bedrock_client()
        
        full_prompt = prompt
        if context_data:
            full_prompt += f"\n\nReal Metric Context:\n{json.dumps(context_data, indent=2)}"
            
        payload = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1000,
            "messages": [
                {
                    "role": "user",
                    "content": full_prompt
                }
            ]
        }
        
        response = bedrock.invoke_model(
            modelId=settings.AWS_BEDROCK_MODEL,
            contentType="application/json",
            accept="application/json",
            body=json.dumps(payload)
        )
        
        body_bytes = response.get('body').read()
        res_json = json.loads(body_bytes.decode('utf-8'))
        text = res_json.get('content', [{}])[0].get('text', 'No AI response content returned.')
        
        return {
            'status': 'success',
            'modelId': settings.AWS_BEDROCK_MODEL,
            'summary': text,
            'errorMessage': None
        }
    except Exception as e:
        logger.error(f"Amazon Bedrock Invocation Error: {e}")
        return {
            'status': 'error',
            'modelId': settings.AWS_BEDROCK_MODEL,
            'summary': None,
            'errorMessage': str(e)
        }
