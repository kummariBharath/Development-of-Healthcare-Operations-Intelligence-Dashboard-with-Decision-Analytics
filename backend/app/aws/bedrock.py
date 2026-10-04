import json
import logging
from typing import Dict, Any, Optional
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

        # Safely extract text content (supports both standard text blocks and thinking blocks)
        content_blocks = res_json.get('content', [])
        text_parts = [
            b.get('text', '') for b in content_blocks
            if isinstance(b, dict) and b.get('type') == 'text' and b.get('text')
        ]
        if text_parts:
            text = "\n\n".join(text_parts)
        elif content_blocks and isinstance(content_blocks[0], dict) and 'text' in content_blocks[0]:
            text = content_blocks[0]['text']
        else:
            text = 'No AI response content returned.'
        
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
