import PyPDF2
import pyttsx3

engine = pyttsx3.init()     # initiali
voices = engine.getProperty("voices")   #getting details of current voice
engine.setProperty("voice",voices[1].id) #changing index, changes voices. o for male and 1 for female
engine.setProperty('rate', 125) #setting up new voice rate

pdf_file = open('joke.pdf','rb')     # read the  file 
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
pageObj = pdf_reader.getPage(6) # page you want to listen here it's read the page 6 
content = pageObj.extractText()


def speak(text):
    engine.say(text)
    engine.runAndWait()

speak(content)