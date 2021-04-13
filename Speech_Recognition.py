#==============FURRO404==============#
#Speech_Recognition_Project.py
import speech_recognition as sr
import time
import random
from playsound import playsound
#---------------------------------#
r = sr.Recognizer()
def bruh():
    Listen()

def Cancel_Checker():
    cancel = 'cancel'
    if any(cancel in word for word in text):    #Cancel Function
        print("CANCELLED!")
        bruh()

def Text_Deconstructor():
    global L_text
    L_text = []
    L_text = text.split(" ")
    return L_text
    
def Listen():
    global text
    with sr.Microphone() as source:
        print("\nListening")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print('You said: ', text)
            Text_Deconstructor()
            text = L_text
            Cancel_Checker()
        except:
            print('Sorry could not recognize your voice')
            bruh()
        return text
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
        
    print("The sum is: ", fnum + snum)
    playsound('YAY.mp3')
    print("\n\n")
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
        print("The difference is: ", snum - fnum)
                                                                                #Human Error Correction
    elif text[2] != "from":
        print("The difference is: ", fnum - snum)

    playsound('YAY.mp3')
    print("\n\n")
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
        
    print("The quotient is: ", fnum / snum)
    playsound('YAY.mp3')
    print("\n\n")
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
        
    print("The product is: ", fnum * snum)
    playsound('YAY.mp3')
    print("\n\n")
#^^^^^^^^^^^^^^^MATH^^^^^^^^^^^^^^^#
#----------------------------#
while True:
    Listen()
#----------------------------#
    if text[0] == 'add' or text[0] == 'Add':
        Add()

    elif text[0] == 'subtract' or text[0] == 'Subtract':
        Subtract()
                                                    #Math Section by FURRO404
    elif text[0] == 'divide' or text[0] == 'Divide':
        Divide()
        
    elif text[0] == 'multiply' or text[0] == 'Multiply':
        Multiply()
#----------------------------#
    elif text[0] == 'exit':
        quit()

    elif text[0] == 'quit':             #Exit Section by FURRO404
        quit()
        
    elif text[0] == 'close':
        quit()
#----------------------------#
    elif text[0] == 'Jake' and text[1] == 'Paul':
        playsound('BRUH.mp3')
                                                                                            #Meme Section by FURRO404 && Sonic26
    elif text[0] == 'happy' and text[1] == 'birthday':
        playsound('HappyBirthday.mp3')
#==============FURRO404==============#
