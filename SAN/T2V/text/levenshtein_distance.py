"""
SAN.T2V.text.levenshtein_distance
~~~
Because of the typing mistake, we can use Levenshtein distance to compare
the input terms and the terms in Database.
:copyright: 2017 by Nhut Hai Huynh.
:license: MIT, see LICENSE for more details.
"""

from Levenshtein import *
from functools import reduce

def getChunk(the_list: list, num: int):
    """
    Example:
    if the_list: ['a', 'b', 'c', 'd', 'e', 'f'] and num: 3
    ['a', 'b', 'c', 'd', 'e', 'f'] -> ['a b c', 'b c d', 'c d e', 'd e f']

    :param the_list: ['a', 'b', 'c', 'd', 'e', 'f'].
    :param num: the number of words in a chunk.
    """
    i = range(num)

    def generate_list(shift: int):
        """
        Example:
        if shift: 1
        ['a', 'b', 'c', 'd', 'e', 'f'] -> ['b', 'c', 'd', 'e', 'f', '']

        :param num: the number of words in a chunk.
        """
        if shift == 0:
            return the_list
        ox=['']*len(the_list)
        ox[:-shift]=the_list[shift:]
        return ox

    # Create shifted lists from a given list
    r = list(map(generate_list,i))
    # Combine shifted lists into a list containing chunks
    combined = list(reduce(lambda x,y: map(lambda i,j: i + ' ' + j,x,y),r))
    # Cut list
    ending = combined[:-(num-1)] if num > 1 else combined

    return ending

def nearlyContains(_pattern: str, _search: str):
    """
    Whether _search nearly contains _pattern
    nearly: the ratio between Levenshtein distance and total possible operations
    is less than 20% (or distance is very small and the ratio is less than 50%)
    and difference of length of strings is not too different to the distance
    since difference between to strings should be modifying, not inserting or
    deleting.

    :param _pattern: the given word or term.
    :param _search: the word or term which we have in database.
    """
    num = len(_pattern.split())
    pre_chunk = _search.split()

    if num > len(pre_chunk):
        return False

    chunks = getChunk(pre_chunk, num)
    score = [distance(_pattern, e) for e in chunks]

    the_min = min(score)
    min_term = chunks[score.index(the_min)]

    len1 = len(_pattern)
    len2 = len(min_term)

    ratio = the_min / max(len1, len2)

    if(_pattern == 'home'):
        print('{} has {} with {}, {} and {}'.format(chunks,min_term,the_min, len1, len2))

    return the_min == 0 or (((the_min < 2 and ratio < 0.5) or ratio < 0.2) \
           and abs(len1-len2) / the_min < 0.4)

def nearlyEquals(_pattern: str, _search: str):
    """
    Whether _search nearly equals _pttern
    nearly: the ratio between Levenshtein distance and total possible operations
    is less than 20% (or distance is very small and the ratio is less than 50%)
    and difference of length of strings is not too different to the distance
    since difference between to strings should be modifying, not inserting or
    deleting.

    :param _pattern: the given word or term.
    :param _search: the word or term which we have in database.
    """
    score = distance(_search, _pattern)
    len1 = len(_pattern)
    len2 = len(_search)
    ratio = score / max(len1, len2)

    return score == 0 or (((score < 2 and ratio < 0.5) or ratio < 0.2) \
           and abs(len1-len2) / score < 0.4)
