import os

from gtts import gTTS

text = "तोहार स्वागत बा! तोहर नाम के बा?"
speech = gTTS(text=text, lang="hi")
speech.save("speech.mp3")

os.system("start speech.mp3")
