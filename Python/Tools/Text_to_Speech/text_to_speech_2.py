import pyttsx3

# initialize
engine = pyttsx3.init()

# text to speech
text = "Hello, nice to meet you"

voices = engine.getProperty("voices")
print(voices)
engine.setProperty("voice", voices[1].id)
engine.say(text)
# play
engine.runAndWait()

