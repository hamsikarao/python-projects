# Import the required module for text
# to speech conversion
"""
from gtts import gTTS

# this isn't working to take continuous inputs, I dont know why!!
# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
while True:
    mytext = input("enter the text that you want me to speak:")

    # Language in which you want to convert
    
    if(mytext == "q"):
        break

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang='en', slow=False)

    # Saving the converted audio in a mp3 file named
    # yourspeech
    myobj.save("yourspeech.mp3")

    # Playing the converted file
   
    os.system("yourspeech.mp3")


        """

import pyttsx3
import time

if __name__ == '__main__':
    text_to_speech = pyttsx3.init()
    time.sleep(1)
    while(True):
        word = input("Enter your command: ")
        if word == 'q':
            break
        # convert this text to speech  
        text_to_speech.say(word)
        text_to_speech.runAndWait() 

