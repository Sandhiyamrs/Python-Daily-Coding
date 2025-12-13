def chatbot_response(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hi! How can I help you today?"
    elif "name" in message:
        return "I am a basic Python chatbot."
    elif "bye" in message:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that yet."

# Example
while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
    print("Bot:", chatbot_response(user))
