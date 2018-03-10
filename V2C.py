#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
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
    def lazycoder(data: str) -> str:
        str code = ""
        # types of brackets
        if "curly" in data:
            code = "{"+code+"}"
        if "parenthesis" in data:
            code = "("+code+")"
        if "bracket" in data:
            code = "["+code+"]"
        # types of arrow keys
        if "left" in data:
            code = code+'\x1b[A'
        if "enter" in data:
            code = code+"\n"
        if "define" in data:
            code = code +"\n def "
        if "argument" in data:
            code = "("+code+")"
        if "from" in data:
            code = code+":"
        if "to" in data:
            code = code+"->"
        if "string" in data:
            code = code+"str"
        if

        return code

