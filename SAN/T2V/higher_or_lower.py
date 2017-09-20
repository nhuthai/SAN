def searchDatabase(word):
    # FIXME: search terms in database
    return ''

def breakSentencesIntoTerms(sentence):
    term_list = []
    word_list = sentence.split()
    for index, word in enumerate(word_list):
        pattern_ = searchDatabase(word)
        if pattern_ is not '':
            tmp = word
            for next in range(index + 1, len(word_list)):
                if word_list[next] in pattern_:
                    tmp += ' ' + word_list[next]
                else:
                    tmp = word
                    break
            term_list.append(tmp)
        else:
            term_list.append(word)
    return term_list

def isHigher_Lower(sentence):
    term_list = breakSentencesIntoTerms(sentence)
    tone_list = []
    for index, term in enumerate(term_list):
        if index < len(term_list) - 1:
            tone_list.append('N')
        elif '?' in term:
            tone_list.append('H')
        else:
            tone_list.append('L')
    return list(zip(term_list, tone_list))
