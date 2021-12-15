#part1 : take user voice and convert into text
#part2 : process the text and give some results->text
#part3 : convert results(text) into voice

#part1(speech recognition)

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
from _datetime import datetime
import pyjokes

def speak(answer):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(answer)
    engine.runAndWait()

def processQuestion(question):
    if 'what are you doing ' in question:
        print("im waiting for your question")
        speak("im waiting for your question")
        return True

    elif 'how are you' in question:
        print('im god thankyou for asking')
        speak("im god thankyou for asking")
        return True

    elif 'play' in question:
        question = question.replace('play',' ')
        pywhatkit.playonyt(question)
        return True
    elif 'who is' in question:
        question = question.replace('who is',' ')
        about = wikipedia.summary(question, 2)
        print(about)
        speak(about)
        return True

    elif 'time' in question:
        time = datetime.today().time().strftime("%I:%M %p")
        print(time)
        speak(time)
        return True

    elif 'joke' in question:
        joke = pyjokes.get_jokes()
        print(joke)
        speak(joke)
        return True

    elif 'love ' in question:
        speak('i love you too gannu')
        return True

    elif 'bye' in question:
        speak("bye gannu , please take care , will meet you again")
        return False

    else:
        print("i didnt get your question, please say again")
        return True


def getQuestion():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('hello gannu jaguar')
        audio = r.listen(source)

    try:
        print(r.recognize_google(audio))
        question = r.recognize_google(audio)
        if 'Alexa' in question:
            question.replace('Alexa',' ')
            print(question)
            return question

        else:
            print('your not talking with me please carry on')
            return "notwithme"

    except sr.UnknownValueError:
        print("sorry, i cant get  your question")

canAskquestion = True
while canAskquestion:
    question = getQuestion()
    if (question == "notwithme"):
        speak("ok carry on with your friends, bye!")
        canAskquestion = False
    else:
        canAskquestion = processQuestion(question)

