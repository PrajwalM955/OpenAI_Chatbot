import os
from dotenv import load_dotenv
from openai import OpenAI, error
import time

load_dotenv()

# Load all API keys from environment variables
API_KEYS = list(filter(None, [
    os.getenv("OPENAI_API_KEY"),
    os.getenv("OPENAI_API_KEY_1"),
    os.getenv("OPENAI_API_KEY_2"),
    os.getenv("OPENAI_API_KEY_3"),
]))

if not API_KEYS:
    raise ValueError("No OpenAI API keys found in environment variables!")

MODELS = ["gpt-3.5-turbo", "gpt-5-mini", "gpt-5-nano"]

class ChatManager:
    def __init__(self, keys, models):
        self.keys = keys
        self.models = models
        self.api_index = 0
        self.model_index = 0
        self.client = OpenAI(api_key=self.keys[self.api_index])
        self.model = self.models[self.model_index]

    def switch_api(self):
        self.api_index = (self.api_index + 1) % len(self.keys)
        self.client = OpenAI(api_key=self.keys[self.api_index])
        print(f"[INFO] Switched API key to index {self.api_index}")

    def switch_model(self):
        self.model_index = (self.model_index + 1) % len(self.models)
        self.model = self.models[self.model_index]
        print(f"[INFO] Switched model to {self.model}")

    def chat(self, prompt):
        attempts = 0
        max_attempts = len(self.keys) * len(self.models)

        while attempts < max_attempts:
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=150,
                )
                return response.choices[0].message.content.strip()
            except error.RateLimitError:
                print(f"[INFO] Rate limit reached, trying next API key and model...")
                self.switch_api()
                self.switch_model()
                attempts += 1
                time.sleep(2)
            except error.APIError as e:
                print(f"[INFO] API error occurred: {e}, switching API key and model...")
                self.switch_api()
                self.switch_model()
                attempts += 1
                time.sleep(2)
            except error.OpenAIError as e:
                print(f"[INFO] OpenAI error: {e}, switching API key and model...")
                self.switch_api()
                self.switch_model()
                attempts += 1
                time.sleep(2)
            except Exception as e:
                print(f"[ERROR] Unexpected error: {e}, switching API key and model...")
                self.switch_api()
                self.switch_model()
                attempts += 1
                time.sleep(2)

        return "[INFO] All API keys/models exhausted or over quota."

def main():
    manager = ChatManager(API_KEYS, MODELS)
    print("Chatbot running! Type 'quit'/'exit'/'bye' to stop.")

    while True:
        query = input("You: ")
        if query.lower() in ["quit", "exit", "bye"]:
            break

        response = manager.chat(query)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
