from .. import sentence

class Testsentence:
    def test_init(self):
        sentence = sentence(plain_sentence='David went away from home and made \
                            a new place there!', the_type='!')
        assert sentence.plain_sentence == 'David went away from home and made \
                            a new place there!'
        assert sentence.type == '.'

    def test_breakSentenceIntoTerms(self):
        sentence = sentence(plain_sentence='David went away from home and made \
                            a new place there')
        sentence.breakSentenceIntoTerms()
