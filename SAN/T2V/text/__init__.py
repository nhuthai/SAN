"""
SAN\T2V\text
~~~
An object text consisting of a text of sentences,
each contains speech of sentence, other data to learn and terms,
each has information to learn and play.
:copyright: 2017 by Nhut Hai Huynh.
:license: MIT, see LICENSE for more details.
"""

from typing import Optional, Union
from .utils import isPoS, isToneLabel, isTypeSentence, searchDatabase, sen_

class term:
    @property
    def PoS(self):
        return self.PoS

    @PoS.setter
    def PoS(self,value):
        assert isPoS(value)
        if type(PoS) is str:
            self.PoS['pos_'] = value
        else:
            self.PoS = value

    @property
    def higher_or_lower(self):
        return self.higher_or_lower

    @higher_or_lower.setter
    def higher_or_lower(self,value):
        assert isToneLabel(value)
        self.higher_or_lower = value

    @property
    def time_label(self):
        return self.time_label

    @time_label.setter
    def time_label(self,value):
        assert value > 0
        self.time_label = value

    def __init__(self, plain_term: str='', sound: Optional[str]=None,
                 isWord: bool=True, isStopWord: Optional[bool]=None,
                 PoS: Optional[Union[str,dict]]=None,
                 higher_or_lower: Union[str,bool]='N', time_label: float=0):
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
                                or normal tone ('N') in the middle of sentence.
        :param time_label: the time to play sound in the sentence (for playing
                           to merge sounds or for supervised learning).
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
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self,value):
        assert isTypeSentence(value)
        self._type = value

    def __init__(self, plain_sentence: str='', speech: Optional[str]=None,
                 the_type: str='.', terms: Optional[list]=None):
        """
        :param plain_sentence: sentence as string.
        :param speech: path to signal file (for learning).
        :param type: question '?' or normal '.' sentence.
        :param terms: terms which were broken in advanced if applicable.
        """
        assert isTypeSentence(the_type)

        self.plain_sentence = plain_sentence
        self.speech = speech if speech is not None else None

        self.type = the_type
        self.removeEndingSymbol()
        self.terms = terms if terms is not None else self.breakSentenceIntoTerms()

    def removeEndingSymbol(self):
        """
        Remove the ending symbol such as '.', '?', '!' , '...', .etc.
        """
        tmp = self.plain_sentence[len(self.plain_sentence) - 1]
        if isTypeSentence(tmp):
            self.type = tmp
            self.plain_sentence=self.plain_sentence[:len(self.plain_sentence)-1]

    def breakSentenceIntoTerms(self):
        """
        Break terms as string into a list of term.
        """
        term_list = []
        word_list = self.plain_sentence.split()
        max_skip = 0
        for index, word in enumerate(word_list):
            if max_skip > 0:
                max_skip -= 1
                continue
            patterns_ = searchDatabase(word)
            #patterns_ = ['went away', 'hope you', 'love you', 'went away from', 'fuck you', 'made a new place', 'I will kill you']
            if len(patterns_) > 0:
                max_tmp = word
                for pattern_ in patterns_:
                    tmp = word
                    skip = 0
                    for next in range(index + 1, len(word_list)):
                        if tmp + ' ' + word_list[next] in pattern_:
                            tmp += ' ' + word_list[next]
                            skip += 1
                        else:
                            break
                    if len(tmp) > len(max_tmp):
                        max_tmp = tmp
                        max_skip = skip
                term_list.append(max_tmp)
            else:
                term_list.append(word)
        return term_list

class text:
    def __init__(self, plain_text: str='', sentences: Optional[list]=None):
        """
        :param plain_text: text as string.
        :param sentences: sentences which were broken in advanced if applicable.
        """
        self.plain_text = plain_text
        if sentences is not None:
            self.sentences = sentences
        else:
            self.breakTextIntoSentences()

    def breakTextIntoSentences(self):
        """
        Break sentences as string into a list of sentence.
        """
        def breakEachSymbol(my_str: str, symbols: list):
            chunks = []
            if len(symbols) > 1:
                the_symbol = symbols[len(symbols) - 1]
                the_list = my_str.split(the_symbol)
                for index, aChunk in enumerate(the_list):
                    if index < len(the_list) - 1:
                        aChunk += the_symbol
                    chunks.extend(breakEachSymbol(aChunk, symbols[:len(symbols) - 1]))
            else:
                for aPlain in my_str.split(symbols[0]):
                    if len(aPlain) > 0:
                        chunks.append(sentence(plain_sentence=aPlain))
            return chunks

        self.sentences = breakEachSymbol(self.plain_text, sen_)

        for index, aSentence in enumerate(self.sentences):
            self.sentences[index].plain_sentence = aSentence.plain_sentence.strip()
