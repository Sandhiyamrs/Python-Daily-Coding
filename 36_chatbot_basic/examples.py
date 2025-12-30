from file1_chatbot_basic import chatbot_response

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
    print("Bot:", chatbot_response(user))
