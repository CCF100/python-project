from gtts import gTTS
import os
text2electricboogaloo = input("Enter Text: ")
tts = gTTS(text=text2electricboogaloo, lang='en')
tts.save("good.mp3")
os.system("play good.mp3")
