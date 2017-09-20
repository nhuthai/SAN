import win32com.client as wincl

def talkInWin10(sentence):
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(sentence)