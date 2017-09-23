"""
SAN.T2V.text.part_of_speech
~~~
Ultilize SpaCy package to parse part of speech
:copyright: 2017 by Nhut Hai Huynh.
:license: MIT, see LICENSE for more details.
"""

# Install: pip install spacy && python -m spacy download en
from spacy.en import English

def get_tags_of_sentence(text):
    parser = English()
    tokens = parser(text)
    the_terms = []
    the_pos = []
    for token in tokens:
        the_pos.append(token.pos_)
        the_terms.append(token.orth_)
        #for more detail: token.dep_,token.head
    return list(zip(the_terms, the_pos))
