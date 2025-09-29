import openai
import os

# --- Configuration ---
openai.api_base = "http://localhost:4891/v1"
openai.api_key = "not needed"
model_name = "DeepSeek-R1-Distill-Qwen-7B.gguf"

def generate_completion(user_prompt):
    """
    Sends a chat completion request to the GPT4All API server.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model_name,
            messages=[{"role": "user", "content": user_prompt}],
            max_tokens=200,
            temperature=0.28,
            stream=False,
        )

        # Correctly access the message content from the response
        # The 'choices' list contains a dictionary at index 0
        return response["choices"][0]["message"]["content"]

    except openai.error.APIError as e:
        return f"Error connecting to GPT4All API: {e}"
