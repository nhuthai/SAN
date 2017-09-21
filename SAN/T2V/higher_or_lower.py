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
