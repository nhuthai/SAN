from .talkWin10 import talkInWin10
from .part_of_speech import get_tags_of_sentence
from .stop_word import checkStopWords
from .higher_or_lower import isHigher_Lower
from .text import term, sentence, text

def demo():
    isWin10 = False
    txt1 = text("I am David. I just want to say hello. I am a student. Nice to meet you")
    txt2 = text('I image that I had this image.')

    # for Windows 10
    if isWin10:
        talkInWin10(txt1.plain_text)
    else:
        # part of speech -> different noun and verb pronounce
        print(get_tags_of_sentence(txt2))
        # stop words -> stress keywords
        print(checkStopWords('the'))
        # is higher or lower or normal tone and also break into terms
        print(isHigher_Lower(txt2))
        # FIXME: link sound between consonant (in the end of the previous word) and vowel (at the begining of the next word)
