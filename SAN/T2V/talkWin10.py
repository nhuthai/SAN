"""
SAN.T2V.talkWin10
~~~
Call Win32com API to play audio
:copyright: 2017 by Nhut Hai Huynh.
:license: MIT, see LICENSE for more details.
"""

import win32com.client as wincl

def talkInWin10(sentence):
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(sentence)
