#!/usr/bin/env python3

# Requires PyAudio and PySpeech.
#git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
#sudo python setup.py install
#brew install portaudio
#conda config --add channels conda-forge
#conda install speechrecognition
import speech_recognition as sr


def recordaudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    str data = ""
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        data = data+r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return data


    # Abbreviated commands in voice to code; for example, "curly open"  should return '{'
    def TLDT(data):

         # types of brackets
        if "curly open" in data:
            data.replace("curly open","{")
        if "curly close" in data:
            data.replace("curly close", "}")
        if "paren open" in data:
            data.replace( "paren open","(")
        if "paren close" in data:
            data.replace("paren close" ,")")
        if "bracket open" in data:
            data.replace("bracket open","[")
        if "bracket close" in data:
            data.replace("bracket open","]")

        if "enter" in data:
            data.replace("enter"+"\n")
        if "quote" or "unquote" in data:
            data.replace("quote", "\"")
            data.replace("unquote", "\"")
        if "backslash" in data:
            data.replace("backslash", "\\")
        if "to" in data:
            data.replace("to",":")

        #numbers
         
        #numerical operators

        #conditionals


        #commands for variables
        if "string" in data:
            data.replace("string","str")
        if ("integer" in data):
                data.replace("integer", "int ")
        if "float" in data:
                data.replace("float", "float ")

        #commands to define functions
         if "define" in data:
             data.replace("define", "\n" + "\t" + "def")
        return data


    #Saving our transcribed code into a .txt file
        def savecode(code):
            return code
        with open("code_transcribed.txt", "w") as out:
            out.write(savecode(code)+"\n")

 

