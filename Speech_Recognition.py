#==============FURRO404==============#
#Speech_Recognition_Project.py
#-----Misc Python Modules-----#
from googletrans import Translator
from googlesearch import search
from gtts import gTTS
import os
import os.path
from os import path
from playsound import playsound
import random
import speech_recognition as sr
import time
#-----Seperate Python Files-----#
import Languages
#---------------------------------#
def Google_Seach():
    text.remove(text[0])
    query = ""
    
    for letter in text: 
                    query += letter
                    query += ' '

    print("Googling the top 10 results for:", query)
    for result in search(query, tld="co.in", stop=10, pause=2):
        print("\n", result)
        
def Retry():
    Listen()

def Cancel_Checker():
    cancel = 'cancel'
    if any(cancel in word for word in text):    #Cancel Function
        print("CANCELLED!")
        quit()
        
def Text_Deconstructor():
    global L_text
    L_text = []
    L_text = text.split(" ")
    return L_text
    
def Listen():
    global text
    with sr.Microphone() as source:
        print("\nListening.")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print('You said: ', text)
            Text_Deconstructor()
            text = L_text
            Cancel_Checker()
        except:
            print('Sorry could not recognize your voice')
            Retry()
        return text

    
#===============LANGUAGE_TRANSLATION===============#
#------------------------Repeating------------------------#
def Lang_Listen():
    while True:
        print("\nSay repeat to listen again or speak a different command")
        wait = str(input("Press enter to speak! "))
        Listen()

        if text[0] == 'repeat':
            playsound("Sentence.mp3")
        elif text[0] != 'repeat':
            os.remove('Sentence.mp3')
            break
        else:
            print("Didn't quite catch that")
#------------------------Translation------------------------#
def Translate():
    if 'to' in text:
        translator = Translator()
        x = 1
        original = []
        user = "unsatisfied"
        
        while user == "unsatisfied":
            if text[x] != 'to':
                original.append(text[x])
                x = x + 1
                            
            elif text[x] == 'to':
                code = text[x+1]
                code = Languages.langcodes[code]
                untranslated = ""
                
                for word in original: 
                    untranslated += word #Move each untranslated word into a string from "original" list
                    untranslated += ' '
                    
                translation = translator.translate(untranslated, dest=code)
                print(translation.origin, ' -> ', translation.text)     #Translate
                
                while user == 'unsatisfied':
                    try:
                        sentence = gTTS(translation.text, lang = code)
                        sentence.save('Sentence.mp3')
                        playsound('Sentence.mp3')       #Text to Speech
                        user = "satisfied"
                    except:
                        print("Language cannot be spoken due to unsupported language choice.\n")
                        user = "satisfied"
    else:
        print("Translate function not properly used.")
#===============LANGUAGE_TRANSLATION===============#

#===============MATH===============#
#------------------------Addition------------------------#
def Add():
    if text[1] == "random":
        fnum = random.randint(0, 100000)
        print("Your random number is ", fnum)
    else:
        fnum = int(text[1])

    if text[3] == "random":
        snum = random.randint(0, 100000)
        print("Your random number is ", snum)
    else:
        snum = int(text[3])
        
    print("The sum is: ", fnum + snum, "\n")
    playsound('YAY.mp3')
#------------------------Subtraction------------------------#
def Subtract():    
    if text[1] == "random":
        fnum = random.randint(0, 100000)
        print("Your random number is ", fnum)
    else:
        fnum = int(text[1])

    if text[3] == "random":
        snum = random.randint(0, 100000)
        print("Your random number is ", snum)
    else:
        snum = int(text[3])

    if text[2] == "from":
        print("The difference is: ", snum - fnum, "\n")
                                                                                #Human Error Correction
    elif text[2] != "from":
        print("The difference is: ", fnum - snum, "\n")

    playsound('YAY.mp3')
#------------------------Division------------------------#
def Divide():
    if text[1] == "random":
        fnum = random.randint(0, 100000)
        print("Your random number is ", fnum)
    else:
        fnum = int(text[1])

    if text[3] == "random":
        snum = random.randint(0, 100000)
        print("Your random number is ", snum)
    else:
        snum = int(text[3])
        
    print("The quotient is: ", fnum / snum, "\n")
    playsound('YAY.mp3')
#------------------------Multiplication------------------------#
def Multiply():
    if text[1] == "random":
        fnum = random.randint(0, 100000)
        print("Your random number is ", fnum)
    else:
        fnum = int(text[1])

    if text[3] == "random":
        snum = random.randint(0, 100000)
        print("Your random number is ", snum)
    else:
        snum = int(text[3])
        
    print("The product is: ", fnum * snum, "\n")
    playsound('YAY.mp3')
#^^^^^^^^^^^^^^^MATH^^^^^^^^^^^^^^^#


#--------------Driver Code---------------#
r = sr.Recognizer()
if path.exists("Sentence.mp3"):             #Start by clearing old files
    os.remove('Sentence.mp3')
    
while True:
    if path.exists("Sentence.mp3"):                     #If this is true, this isn't the first iteration ;-;
        Lang_Listen()
    else:
        wait = input("Press enter to speak ")         #WE WANT THIS THE FIRST TIME
        Listen()
#----------------------------#
    if text[0] == 'add' or text[0] == 'Add':
        if text[1] == 'two':
            text[1] = '2'
                                #For some reason, saying "Add two and two" makes two turn into "two" instead of "2", causing an error. Easy fix.
        if text[3] == 'two':
            text[3] = '2'
        Add()

    elif text[0] == 'subtract' or text[0] == 'Subtract':
        Subtract()
                                                                                            #Math Section by FURRO404
    elif text[0] == 'divide' or text[0] == 'Divide':
        Divide()
        
    elif text[0] == 'multiply' or text[0] == 'Multiply':
        Multiply()
#----------------------------#
    elif text[0] == 'exit' or text[0] == 'Exit':
        quit()

    elif text[0] == 'quit' or text[0] == 'Quit':            #Exit Section by FURRO404
        quit()

    elif text[0] == 'close' or text[0] == 'Close':
        quit()
#----------------------------#
    elif text[0] == 'translate' or text[0] == 'Translate':
        Translate()                         #Translation Section by FURRO404
#----------------------------#
    elif text[0] == 'Google'  or text[0] == 'google':
        Google_Seach()
#----------------------------#
    elif text[0] == 'Jake' and text[1] == 'Paul':
        playsound('BRUH.mp3')
                                                                                            #Meme Section by FURRO404 && Sonic26
    elif text[0] == 'happy' and text[1] == 'birthday':
        playsound('HappyBirthday.mp3')
#----------------------------#
#==============FURRO404==============#
