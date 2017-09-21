from .talkWin10 import talkInWin10
from .text import term, sentence, text

def demo():
    isWin10 = False
    txt1 = text("I am David. I just want to say hello. I am a student. Nice to meet you")
    txt2 = text('I image that I had this image.')

    # for Windows 10
    if isWin10:
        talkInWin10(txt1.plain_text)
    else:
        # FIXME: link sound between consonant (in the end of the previous word) and vowel (at the begining of the next word)
        a = 0
