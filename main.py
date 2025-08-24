import os
from dotenv import load_dotenv
from openai import OpenAI
from openai.error import OpenAIError, RateLimitError, APIError

# Load all API keys from .env
load_dotenv()

API_KEYS = [
    os.getenv("OPENAI_API_KEY"),
    os.getenv("OPENAI_API_KEY_1"),
    os.getenv("OPENAI_API_KEY_2"),
    os.getenv("OPENAI_API_KEY_3")
]

# Use lightweight models for demo purposes
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
        while attempts < len(self.keys) * len(self.models):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=150  # limit token usage for demo
                )
                return response.choices[0].message.content.strip()
            except RateLimitError:
                print(f"[INFO] Rate limit reached for API index {self.api_index}. Trying next API/model...")
                self.switch_api()
                self.switch_model()
                attempts += 1
            except APIError as e:
                print(f"[INFO] API error with API index {self.api_index}: {e}. Trying next API/model...")
                self.switch_api()
                self.switch_model()
                attempts += 1
            except OpenAIError as e:
                print(f"[INFO] OpenAI error: {e}. Trying next API/model...")
                self.switch_api()
                self.switch_model()
                attempts += 1

        return "[INFO] All API keys/models are currently over quota or failing."

def main():
    manager = ChatManager(API_KEYS, MODELS)
    print("Chatbot is running! Type 'quit', 'exit', or 'bye' to stop.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = manager.chat(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
