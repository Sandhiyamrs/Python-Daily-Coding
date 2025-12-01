text = input("Enter text: ")
emoji_dict = {"happy":"😀","sad":"😢","love":"❤️","fire":"🔥"}
for word, emoji in emoji_dict.items():
    text = text.replace(word, emoji)
print("Emoji Text:", text)
