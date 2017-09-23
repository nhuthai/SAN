"""
SAN.T2V
~~~
Use the given API of Windows 10 or use our methods to generate audio
:copyright: 2017 by Nhut Hai Huynh.
:license: MIT, see LICENSE for more details.
"""

from .talkWin10 import talkInWin10
from .text import term, sentence, text
from .learning import *

def read(txt: str):
    isWin10 = False
    the_text = text(txt)

    # for Windows 10
    if isWin10:
        talkInWin10(the_text.plain_text)
    else:
        # FIXME: link sound between consonant (in the end of the previous word) and vowel (at the begining of the next word)
        print(the_text.plain_text)
