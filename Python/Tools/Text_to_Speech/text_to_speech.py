import gtts
from playsound import playsound

text = input('Text: ')

# make request to google to get synthesis
tts = gtts.gTTS(text)
# save the audio file
tts.save("text_speech.mp3")
# play the audio file
playsound("text_speech.mp3")