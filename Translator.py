from translatepy import Translator
import pyttsx3 as pt
while True:
    translator = Translator()
    text=input("Enter your text:")
    translation=translator.translate(text,"Spanish")
    print(translation)
    a=pt.init()
    a.say(translation)
    a.runAndWait()
