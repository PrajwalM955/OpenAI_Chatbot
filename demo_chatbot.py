import json

# Load mock responses from file
with open("mock_responses.json", "r") as f:
    mock_data = json.load(f)

def get_response(user_input):
    # A simple match to provide canned responses
    return mock_data.get(user_input.strip(), "Sorry, I don't understand that in this demo.")

def main():
    print("🤖 Demo Chatbot started! Type 'quit'/'exit'/'bye' to stop.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("🤖 Goodbye!")
            break

        response = get_response(user_input)
        print("Bot:", response, "\n")

if __name__ == "__main__":
    main()
