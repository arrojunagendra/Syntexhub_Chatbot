# Simple Rule-Based Chatbot

knowledge_base = {
    "ai": "Artificial Intelligence is the simulation of human intelligence by machines.",
    "python": "Python is a programming language used for AI and data science.",
    "chatbot": "A chatbot is a program that talks with users."
}

# Log file name
log_file = "chat_history.txt"

# Function to save conversation
def log_conversation(user, bot):
    with open(log_file, "a") as file:
        file.write("User: " + user + "\n")
        file.write("Bot: " + bot + "\n")

def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hi", "hello", "hey"]:
        return "Hello! How can I help you?"

    elif "help" in user_input:
        return "You can ask me about AI, Python, or chatbot."

    elif "how are you" in user_input:
        return "I am fine!"

    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye!"

    for key in knowledge_base:
        if key in user_input:
            return knowledge_base[key]

    return "Sorry, I don't understand."

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    response = chatbot_response(user_input)

    print("Chatbot:", response)

    # Save conversation to file
    log_conversation(user_input, response)

    if user_input.lower() in ["bye", "exit", "quit"]:
        break