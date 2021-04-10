#==============FURRO404==============#
import speech_recognition as sr
import time
import random
#---------------------------------#
r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print('Command: ')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
        except:
            print('Sorry could not recognize your voice')

    if text == 'add':
        with sr.Microphone() as source:
            print('\nFirst number: ')
            audio = r.listen(source)
                
            try:
                text = r.recognize_google(audio)
                if text == "random":
                    fnum = random.randint(0, 100)
                    print('Your random number is: ', fnum)
                else:
                    fnum = int(text)
                    print('You said: ', fnum)
            except:
                print('Sorry could not recognize your voice')

        with sr.Microphone() as source:
            print('\nSecond number: ')
            audio = r.listen(source)
                
            try:
                text = r.recognize_google(audio)
                if text == "random":
                    snum = random.randint(0, 100)
                    print('Your random number is: ', snum)
                else:
                    snum = int(text)
                    print('You said: ', snum)
            except:
                print('Sorry could not recognize your voice')

        print(fnum + snum)
        time.sleep(2)
        print("\n\n")
#==============FURRO404==============#
