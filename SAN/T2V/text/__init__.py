"""
SAN\T2V\text
~~~
An object text consisting of a text of sentences,
each contains speech of sentence, other data to learn and terms,
each has information to learn and play.
:copyright: 2017 by Nhut Hai Huynh.
:license: MIT, see LICENSE for more details.
"""

from utils import isPoS, isToneLabel, isTypeSentence

class term:
    @PoS.setter
    def PoS(self,value: Union[str,dict]):
        assert isPoS(value)
        if type(PoS) is str:
            self.PoS['pos_'] = value
        else:
            self.PoS = value

    @higher_or_lower.setter
    def higher_or_lower(self,value: Union[str,bool]):
        assert isToneLabel(value)
        self.higher_or_lower = value

    @time_label.setter
    def time_label(self,value: float):
        assert value > 0
        self.time_label = value

    def __init__(self, plain_term: str, sound: Optional[str]=None,
                 isWord: bool=True, isStopWord: Optional[bool]=None,
                 PoS: Optional[Union[str,dict]]=None,
                 higher_or_lower: Union[str,bool],
                 time_label: float=0.0)
    """
        :param plain_term: term as string.
        :param sound: path to sound file (for playing).
        :param isWord: whether word or group of words.
        :param isStopWord: whether stop word (for playing - stress keyword) if
                           isWord is True.
        :param PoS: part of speech as string or list for more detail (for
                    playing - intonation rule) if isWord is True.
        :param higher_or_lower: higher tone (True) in the end of question or
                                lower tone (False) in the end of normal sentence
                                or normal tone ('N') in the middle of sentence
        :param time_label: the time to play sound in the sentence (for playing
                           to merge sounds or for supervised learning)
        """
        assert isPoS(PoS)
        assert isToneLabel(higher_or_lower)
        assert time_label > 0

        self.plain_term = plain_term
        self.sound = sound if sound is not None else None

        self.isWord = isWord
        if isWord:
            self.isStopWord = isStopWord if isStopWord is not None else None
            self.PoS = PoS if PoS is not None else None

        self.higher_or_lower = higher_or_lower
        self.time_label = time_label

class sentence:
    @type.setter
    def type(self,value: float):
        assert isTypeSentence(value)
        self.type = value

    def __init__(self, plain_sentence: str, speech: Optional[str]=None,
                 the_type: str='.', terms: Optional[list]=None)
    """
        :param plain_sentence: sentence as string.
        :param speech: path to signal file (for learning).
        :param type: question '?' or normal '.' sentence.
        :param terms: terms which were broken in advanced if applicable.
        """
        assert isTypeSentence(type)

        self.plain_sentence = plain_sentence
        self.speech = speech if speech is not None else None

        self.type = the_type
        self.terms = terms if terms is not None else None

class text:
    def __init__(self, plain_text: str, sentences: Optional[list]=None):
    """
        :param plain_text: text as string.
        :param sentences: sentences which were broken in advanced if applicable.
        """
        self.plain_text = plain_text
        self.sentences = sentences if sentences is not None else None
