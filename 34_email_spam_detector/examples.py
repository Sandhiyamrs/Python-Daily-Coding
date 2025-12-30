from file1_email_spam_detector import predict_spam

emails = [
    "Win a FREE iPhone now!!!",
    "Meeting scheduled at 10 AM"
]

for mail in emails:
    print(mail, "→ Spam:", predict_spam(mail))
