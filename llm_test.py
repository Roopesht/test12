import requests
import os
from dotenv import load_dotenv

load_dotenv()

def call_openai_api(prompt, model="gpt-4.1"):
    """Call OpenAI API with proper error handling"""
    api_key = os.getenv('OPENAI_API_KEY')
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    data = {
        'model': model,
        'input': prompt
    }
    print (f"Data: {data}")
    print (f"Headers: {headers}")
    try:
        response = requests.post(
            'https://api.openai.com/v1/responses',
            headers=headers,
            json=data
        )
        response.raise_for_status()  # Raise exception for bad status
        return response.json()['output'][0]['content'][0]['text']
    
    except requests.exceptions.RequestException as e:
        print(f"API call failed: {e}")
        return "Sorry, I couldn't process your request."

# Usage
result = call_openai_api("What is your name?")
print("\nResult: ", result)
