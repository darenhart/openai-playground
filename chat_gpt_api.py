import requests
import json
import os
from dotenv import load_dotenv


def chat_gpt_api(prompt):
    # Load environment variables from .env file
    load_dotenv()

    url = "https://api.openai.com/v1/engines/text-davinci-003/completions"
    api_key = os.getenv("CHATGPT_API_KEY")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    data = {
        "prompt": prompt,
        "max_tokens": 150,
        "temperature": 0.8,
        "n": 1,
        "stop": None,
    }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()

    if response.status_code == 200:
        message = response_json["choices"][0]["text"].strip()
        return message
    else:
        print("Error:", response.status_code)
        print(response_json)
        return None

def main():
    print("Welcome to the ChatGPT API terminal interface!")
    print("Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break

        prompt = f"User: {user_input}\nChatGPT:"
        response = chat_gpt_api(prompt)

        if response:
            print("ChatGPT:", response)

if __name__ == "__main__":
    main()