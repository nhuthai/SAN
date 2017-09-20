pos_ = ['NOUN','VERB','ADJ','ADV']
dep_ = []
sen_ = ['.','?','...','!']

def isPoS(PoS: Union[str,dict]):
    """
        Check whether PoS is correct format

        :param PoS: string is Part of Speech, dict is full information.
        """
    if (type(PoS) is str and PoS in pos_) or PoS is None:
        return True

    if len(PoS) > 0 and PoS['pos_'] in pos_:
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
