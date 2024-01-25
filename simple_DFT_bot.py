import nltk
from nltk.chat.util import Chat, reflections

patterns = [
    (r'Hi|hello|hey', ["Hi there! Are you ready to learn about Density Functional Theory?",
                      "Hello! Are you ready to learn about Density Functional Theory?",
                      "Hey! Are you ready to learn about Density Functional Theory?"]),
]

chatbot = Chat(patterns, reflections)

print("Hello! I am a Density Functional Theory (DFT) chatbot.")
print("If you want to quit, please type 'quit' or 'exit.' ")

response_list = []  # Variable to store responses

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit" or user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    
    response = chatbot.respond(user_input)
    response_list.append(response)
    if response:
        print("Chatbot:", response)
    if user_input == "no" and "Are you ready to learn about Density Functional Theory?" in response_list[ len(response_list) - 2]:
        print("I am sorry but I am only trained to talk about DFT. Goodbye!")
        break
