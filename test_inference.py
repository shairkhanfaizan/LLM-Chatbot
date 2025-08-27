from huggingface_hub import InferenceClient


def get_response(messages, model, token):
    if not token:
        raise ValueError("Hugging Face API key is required.")
    client = InferenceClient(
        model=model,
        token=token
    )
    response = client.chat_completion(
        messages=messages,
        max_tokens=200
    )
    return response.choices[0].message["content"]