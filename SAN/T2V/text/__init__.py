"""
SAN.T2V.text
~~~
An object text consisting of a text of sentences,
each contains speech of sentence, other data to learn and terms,
each has information to learn and play.
:copyright: 2017 by Nhut Hai Huynh.
:license: MIT, see LICENSE for more details.
"""

from typing import Optional, Union
from .utils import isPoS, isToneLabel, isTypeSentence, searchDatabase, sen_,saveDataBase
from .part_of_speech import get_tags_of_sentence
from .stop_word import checkStopWords
from .higher_or_lower import isHigher
from .levenshtein_distance import nearlyEquals, nearlyContains

class term:
    @property
    def PoS(self):
        return self._PoS

    @PoS.setter
    def PoS(self,value):
        assert isPoS(value)
        self._PoS = value

    @property
    def higher_or_lower(self):
        return self._higher_or_lower

    @higher_or_lower.setter
    def higher_or_lower(self,value):
        assert isToneLabel(value)
        self._higher_or_lower = value

    @property
    def time_label(self):
        return self._time_label

    @time_label.setter
    def time_label(self,value):
        assert value >= 0
        self._time_label = value

    def convertJson(self):
        """
        Convert from term object to json object

        Example:
        {'went': {'link': None, 'higher_or_lower': 'N', 'PoS': 'VERB',
                  'stopword': False},
        'went away': {'link': None, 'higher_or_lower': False, 'PoS': 'PHRASE',
                      'stopword': False},
        'went away from': {'link': None, 'higher_or_lower': 'N', 'PoS': 'PHRASE',
                           'stopword': False}}
        """
        tmp = {self.plain_term: {'sound': self.sound,
               'higher_or_lower': self.higher_or_lower, 'PoS': self.PoS,
               'stopword': self.isStopWord}}

        return tmp

    def convertFromJson(self, jsonObj):
        """
        Create a term after search in Database (use in
        sentence.breakSentenceIntoTerms function) including sound link, stopword
        ,higher_or_lower, PoS information
        """
        for key in jsonObj:
            assert isPoS(jsonObj[key]['PoS'])
            assert isToneLabel(jsonObj[key]['higher_or_lower'])

            self.plain_term = key
            self.sound = jsonObj[key]['sound']

            self.isStopWord = jsonObj[key]['stopword']
            self.PoS = jsonObj[key]['PoS']
            self.isWord = False if self.PoS == 'PHRASE' else True

            self.higher_or_lower = jsonObj[key]['higher_or_lower']
            self.time_label = 0

            break

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
        assert time_label >= 0

        self.plain_term = plain_term
        self.sound = sound if sound is not None else None

        self.isWord = isWord
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
        tmp = self.plain_sentence[-1]
        if isTypeSentence(tmp):
            self.type = tmp
            self.plain_sentence=self.plain_sentence[:-1]

    def parsePoS(self, the_terms):
        """
        Part of speech -> different noun and verb pronounce

        :param the_terms: the list of term objects
        """
        labeled_terms = get_tags_of_sentence(self.plain_sentence)
        for a_term in the_terms:
            for a_lbl_term in labeled_terms:
                if a_term.plain_term == a_lbl_term[0]:
                    a_term.PoS = a_lbl_term[1]
                    break

        return the_terms

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
            if len(patterns_) > 0:
                max_tmp = word
                for pattern_ in patterns_:
                    tmp = word
                    skip = 0
                    for next in range(index + 1, len(word_list)):
                        if nearlyContains(tmp + ' ' + word_list[next], pattern_):
                            tmp += ' ' + word_list[next]
                            skip += 1
                        else:
                            break

                    tmp = pattern_ if nearlyEquals(tmp, pattern_) else word
                    tmp_tone = isHigher(tmp.split()[-1],word_list,self.type)
                    if len(tmp) > len(max_tmp) and \
                       patterns_[pattern_]['higher_or_lower'] == tmp_tone:
                        max_tmp = tmp
                        max_skip = skip
                new_word = term()
                new_word.convertFromJson({max_tmp: patterns_[max_tmp]})
                term_list.append(new_word)
            else:
                new_word = term(plain_term=word, isWord=True,
                                isStopWord=checkStopWords(word),
                                higher_or_lower=isHigher(word,word_list,self.type),
                                time_label=0)
                term_list.append(new_word)

        return self.parsePoS(term_list)

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
                the_symbol = symbols[-1]
                the_list = my_str.split(the_symbol)
                for index, aChunk in enumerate(the_list):
                    if index < len(the_list) - 1:
                        aChunk += the_symbol
                    chunks.extend(breakEachSymbol(aChunk, symbols[:-1]))
            else:
                for aPlain in my_str.split(symbols[0]):
                    if len(aPlain) > 0:
                        chunks.append(sentence(plain_sentence=aPlain))
            return chunks

        self.sentences = breakEachSymbol(self.plain_text, sen_)

        for index, aSentence in enumerate(self.sentences):
            self.sentences[index].plain_sentence = aSentence.plain_sentence.strip()
