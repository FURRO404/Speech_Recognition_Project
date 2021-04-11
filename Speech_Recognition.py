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
    
def Listen():
    global text
    with sr.Microphone() as source:
        print("\nListening")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print('You said', text)
            if text is int:
                bruh()
        except:
            print('Sorry could not recognize your voice')
            text = "ERR"
            bruh()
            
        return text
#===============MATH===============#
#------------------------Addition------------------------#
def Add():
    print("First Number?")
    Listen()
    
    if text == "random":
        fnum = random.randint(0, 100000)
        print("Your random number is ", fnum)
    else:
        fnum = int(text)


    print("Second Number?")
    Listen()
    
    if text == "random":
        snum = random.randint(0, 100000)
        print("Your random number is ", snum)
    else:
        snum = int(text)
        
    print("The sum is: ", fnum + snum)
    playsound('YAY.mp3')
    time.sleep(2)
    print("\n\n")
#------------------------Subtraction------------------------#
def Subtraction():
    print("First Number?")
    Listen()
    
    if text == "random":
        fnum = random.randint(0, 100000)
        print("Your random number is ", fnum)
    else:
        fnum = int(text)


    print("Second Number?")
    Listen()
    
    if text == "random":
        snum = random.randint(0, 100000)
        print("Your random number is ", snum)
    else:
        snum = int(text)
        
    print("The difference is: ", fnum - snum)
    playsound('YAY.mp3')
    time.sleep(2)
    print("\n\n")
#------------------------Division------------------------#
def Divide():
    print("First Number?")
    Listen()
    
    if text == "random":
        fnum = random.randint(0, 100000)
        print("Your random number is ", fnum)
    else:
        fnum = int(text)


    print("Second Number?")
    Listen()
    
    if text == "random":
        snum = random.randint(0, 100000)
        print("Your random number is ", snum)
    else:
        snum = int(text)
        
    print("The quotient is: ", fnum / snum)
    playsound('YAY.mp3')
    time.sleep(2)
    print("\n\n")
#------------------------Multiplication------------------------#
def Multiply():
    print("First Number?")
    Listen()
    
    if text == "random":
        fnum = random.randint(0, 100000)
        print("Your random number is ", fnum)
    else:
        fnum = int(text)


    print("Second Number?")
    Listen()
    
    if text == "random":
        snum = random.randint(0, 100000)
        print("Your random number is ", snum)
    else:
        snum = int(text)
        
    print("The product is: ", fnum * snum)
    playsound('YAY.mp3')
    time.sleep(2)
    print("\n\n")
#^^^^^^^^^^^^^^^MATH^^^^^^^^^^^^^^^#
#----------------------------#
while True:
    print("Command: ")
    Listen()
#----------------------------#
    if text == 'add':
        Add()

    elif text == 'subtract':
        Subtract()
                                                        #Math Section by FURRO404
    elif text == 'divide':
        Divide()
        
    elif text == 'multiply':
        Multiply()
#----------------------------#
    elif text == 'exit':
        quit()

    elif text == 'quit':                      #Exit Section by FURRO404
        quit()
        
    elif text == 'close':
        quit()
#----------------------------#
    elif text == 'Jake Paul':
        playsound('BRUH.mp3')
                                                        #Meme Section by FURRO404 && Sonic26
#==============FURRO404==============#
