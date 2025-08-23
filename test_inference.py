from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

def get_response(messages, model):
    if not HF_TOKEN:
        raise ValueError("Hugging Face API key not found. Please set the HF_TOKEN environment variable.")
    client = InferenceClient(
        model=model,
        token=HF_TOKEN
    )
    response = client.chat_completion(
        messages=messages,
        max_tokens=200
    )
    return response.choices[0].message["content"]