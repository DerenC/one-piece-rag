from dotenv import load_dotenv
import requests
import os

load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/models"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

for model_data in response.json().get("data"):
    print(model_data.get("id"))

"meta-llama/llama-prompt-guard-2-86m"   # Unusable as the context window is too short
"meta-llama/llama-prompt-guard-2-22m"   # Unusable as the context window is too short