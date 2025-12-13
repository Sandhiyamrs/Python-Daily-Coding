spam_keywords = ["free", "winner", "lottery", "click", "prize"]

def is_spam(email_text):
    email_text = email_text.lower()
    for word in spam_keywords:
        if word in email_text:
            return True
    return False

email = "You won a free lottery prize!"
print("Spam Email" if is_spam(email) else "Not Spam")
