import os
import time
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from your .env file in project root
load_dotenv()

# Collect all API keys from environment variables, filtering None values
API_KEYS = list(filter(None, [
    os.getenv("OPENAI_API_KEY"),
    os.getenv("OPENAI_API_KEY_1"),
    os.getenv("OPENAI_API_KEY_2"),
    os.getenv("OPENAI_API_KEY_3"),
    os.getenv("OPENAI_API_KEY_4"),
    os.getenv("OPENAI_API_KEY_5"),
    os.getenv("OPENAI_API_KEY_6"),
    os.getenv("OPENAI_API_KEY_7"),
]))

if not API_KEYS:
    raise ValueError("No OpenAI API keys found in environment variables!")

# We just use a single model here, but you can add more to rotate models if you want
MODELS = ["gpt-3.5-turbo"]

class ChatManager:
    def __init__(self, keys, models):
        self.keys = keys
        self.models = models
        self.api_index = 0
        self.model_index = 0
        self.client = OpenAI(api_key=self.keys[self.api_index])
        self.model = self.models[self.model_index]

    def switch_api(self):
        # Switch to next API key, cycle back if at the end
        self.api_index = (self.api_index + 1) % len(self.keys)
        self.client = OpenAI(api_key=self.keys[self.api_index])
        print(f"[INFO] Switched to API key {self.api_index}")

    def switch_model(self):
        # Switch to next model (optional, here only one model)
        self.model_index = (self.model_index + 1) % len(self.models)
        self.model = self.models[self.model_index]
        print(f"[INFO] Switched to model {self.model}")

    def chat(self, prompt):
        attempts = 0
        max_attempts = len(self.keys) * len(self.models)
        delay = 1  # Initial delay for exponential backoff retry

        while attempts < max_attempts:
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=150,
                )
                return response.choices[0].message.content.strip()

            except Exception as e:
                print(f"[WARNING] OpenAI API error: {e}. Retrying after {delay} seconds...")
                time.sleep(delay)
                delay = min(delay * 2, 60)  # Exponential backoff max 60 seconds
                self.switch_api()
                self.switch_model()
                attempts += 1

        return "[INFO] All API keys and models exhausted or quota exceeded. Please try again later."

def main():
    print("🤖 Chatbot started! Type 'quit', 'exit', or 'bye' to stop.\n")
    chat_manager = ChatManager(API_KEYS, MODELS)

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("🤖 Goodbye!")
            break

        bot_response = chat_manager.chat(user_input)
        print(f"Bot: {bot_response}\n")

if __name__ == "__main__":
    main()
