import pyttsx3

text_speech=pyttsx3.init()
rate=text_speech.setProperty("rate",120)
#volume=text_speech.setProperty("volume",0.5)#max=1,min=0
voices=text_speech.getProperty("voices")
voices=text_speech.setProperty("voice", voices[1].id)#male=0,female=1

answer=input("insert text:")
text_speech.say(answer)
text_speech.runAndWait()