"""
SAN.T2V.text.higher_or_lower
~~~
Get higher or lower or normal tone:
Method 1: Check the type of the sentence and use different voice for different
tone.
Method 2: Check the type of the sentence and use audio coding to modify tone.
:copyright: 2017 by Nhut Hai Huynh.
:license: MIT, see LICENSE for more details.
"""
from typing import Union
from functools import reduce
from .levenshtein_distance import nearlyContains, nearlyEquals

def isHigher(term_or_index: Union[str, int], sentence: list, typ: str):
    """
    Whether term is higher or lower or normal tone

    :param term: the term(string) we want to check or the index(int) in the list
    :param sentence: the list of terms in that sentence
    :param typ: the type of the sentence
    """
    if type(term_or_index) is str:
        plain_sentence = reduce(lambda x,y: x + " " + y, sentence)
        assert nearlyContains(term_or_index, plain_sentence)
        for index, aTerm in enumerate(sentence):
            if nearlyEquals(aTerm, term_or_index) and index < len(sentence) - 1:
                return 'N'

    if type(term_or_index) is int:
        assert 0 <= term_or_index and term_or_index < len(sentence)
        if term_or_index < len(sentence) - 1:
            return 'N'

    if typ == '?':
        return True
    else:
        return False
