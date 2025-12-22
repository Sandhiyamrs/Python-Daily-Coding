def is_spam(email_text):
    spam_words = ["win", "free", "prize", "click", "urgent"]
    for word in spam_words:
        if word in email_text.lower():
            return "Spam"
    return "Not Spam"

# Example
print(is_spam("You won a free prize!"))
