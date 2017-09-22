import json
import os
from typing import Optional, Union
from itertools import compress
from pathlib import *

pos_ = ['PROPN','NOUN','VERB','ADJ','ADV','PHRASE','CCONJ','DET']
dep_ = []
sen_ = ['.','?','...','!']

def isPoS(PoS: Union[str,dict]):
    """
    Check whether PoS is correct format

    :param PoS: string is Part of Speech, dict is full information.
    """
    print(PoS)
    if (type(PoS) is str and PoS in pos_) or PoS is None:
        return True

    if type(PoS) is dict and len(PoS) > 0 and PoS['pos_'] in pos_:
        if len(PoS) > 1:
            if PoS['dep_'] in dep_:
                return True
        else:
            return True

    return False

def isToneLabel(Tone: Union[str,bool]):
    """
    Check whether ToneLabel is correct format

    :param Tone: string is normal tone, bool is higher or lower.
    """
    if type(Tone) is bool or Tone is 'N':
        return True

    return False

def isTypeSentence(typ: str):
    """
    Check whether type of sentence is correct format

    :param typ: symbol of type of sentence.
    """
    if typ in sen_:
        return True

    return False

def searchDatabase(word):
    """
    Search database and retrieve terms which match word pattern, return json obj
    For the typing mistake, we can use Levenshtein distance to compare

    :param word: word pattern.
    """
    terms_file = findPath()

    with open(terms_file) as f:
        data = json.load(f)

    keys_list = list(data.keys())

    def doesContain(_search):
        """
        whether _search contains or nearly contains (used word distance) word
        """
        ### FIXME: Levenshtein distance
        return word in _search

    _compare = list(map(doesContain, keys_list))
    #_id = [i for i, v in _compare if v]
    # huge data
    _selected = list(compress(keys_list, _compare))

    return {aKey: data[aKey] for aKey in _selected}

def saveDataBase(term):
    """
    Save term to database

    :param term: term converted into json object.
    Example:
    {'went': {'sound': None, 'higher_or_lower': 'N', 'PoS': 'VERB',
              'stopword': False},
    'went away': {'sound': None, 'higher_or_lower': False, 'PoS': 'PHRASE',
                  'stopword': False},
    'went away from': {'sound': None, 'higher_or_lower': 'N', 'PoS': 'PHRASE',
                       'stopword': False}}
    """
    terms_file = findPath()

    with open(terms_file) as f:
        data = json.load(f)

    data.update(term, sort_keys= True)

    with open(terms_file, 'w') as f:
        json.dump(data, f)

def findPath():
    """
    Find json path
    """
    current = os.path.realpath(__file__)
    p = PurePath(current).parent
    terms_file = os.path.join(p, 'terms.json')
    return terms_file
