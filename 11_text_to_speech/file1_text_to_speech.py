from gtts import gTTS

def text_to_speech(text, filename="audio.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    print("Audio saved!")
