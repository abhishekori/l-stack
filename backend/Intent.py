from nltk import tag, word_tokenize

class Intent:

    def __init__(self):
        print("intent")

    def getIntent(self,sentence, map):
        print("test")
        tagged_sent = tag.pos_tag(word_tokenize(sentence))
        for taged in tagged_sent:
            (word,token) = taged
            if token == 'JJ' or token == 'NN':
                map['intent'] = word
                return
        map['intent'] = sentence
