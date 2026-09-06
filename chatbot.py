# CodeAlpha - AI Chatbot with NLP

import re
import random

print("===================================")
print("      CodeAlpha AI Chatbot")
print("===================================")
print("Hello! I am your AI chatbot.")
print("You can ask me simple questions.")
print("Type 'bye' to exit.\n")


responses = {
    "hello": [
        "Hello! How can I help you?",
        "Hi! Nice to meet you.",
        "Hello! What can I do for you?"
    ],

    "how are you": [
        "I am doing great! Thanks for asking.",
        "I am fine and ready to help you."
    ],

    "your name": [
        "My name is CodeAlpha AI Chatbot.",
        "You can call me CodeAlpha Bot."
    ],

    "python": [
        "Python is a popular and beginner-friendly programming language.",
        "Python is widely used for AI, data science and web development."
    ],

    "thank": [
        "You're welcome!",
        "Glad I could help!"
    ]
}


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text.strip()


def get_response(user_input):
    user_input = clean_text(user_input)

    if user_input == "bye":
        return "Goodbye! Have a great day!"

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "Sorry, I don't understand that yet. Please ask me something else."


while True:

    user_input = input("You: ")

    response = get_response(user_input)

    print("Bot:", response)

    if clean_text(user_input) == "bye":
        break