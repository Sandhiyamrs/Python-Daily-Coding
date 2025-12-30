from file1_email_spam_detector import predict_spam

mailbox = [
    "Urgent! Your account is suspended",
    "Project update attached",
    "Earn money from home!!!"
]

spam_count = 0

for mail in mailbox:
    if predict_spam(mail):
        spam_count += 1
        print("SPAM:", mail)
    else:
        print("SAFE:", mail)

print("Total spam detected:", spam_count)
