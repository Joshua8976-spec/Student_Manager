def get_response(user_message):
    if "hello" in user_message.lower():
        return "Hi there! How can I help you?"
    else:
        return "I'm not sure I understand, but I'm learning!"
