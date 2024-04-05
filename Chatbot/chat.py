import random

# Define chatbot responses based on patterns
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thank you!", "I'm doing well, thanks for asking!", "All good!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "default": ["Sorry, I don't understand.", "Could you please rephrase that?", "I'm not sure I follow."]
}

# Function to generate a response based on user input
def get_response(user_input):
    for pattern, responses_list in responses.items():
        if pattern in user_input.lower():
            return random.choice(responses_list)
    return random.choice(responses["default"])

# Main function to run the chatbot
def main():
    print("Chatbot: Hi! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
