from abc import ABCMeta, abstractmethod
import nltk


class AbstractKeywordPool(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_similar(self, word):
        pass

    @abstractmethod
    def extract_from(self, text):
        pass


class CSVKeywordPool(AbstractKeywordPool):
    def __init__(self, input_file):
        self.keywords = dict()
        with open(input_file) as csv:
            for line in csv.readlines():
                if not line.startswith("//"):
                    fmt_line = line.lower().replace("\n", "")
                    self.__create_entry(fmt_line.split(","))

    def __create_entry(self, words):
        for word in words:
            self.keywords[word] = filter(lambda x: not x == word, words)

    def get_similar(self, word):
        try:
            return self.keywords[word.lower()]
        except IndexError:
            return []

    def extract_from(self, text):
        words = text.replace("\n", "").lower().split(" ")
        return set(filter(lambda x: x in self.keywords, words))


class WordNetKeywordPool(AbstractKeywordPool):
    """ A keyword pool that uses NLTK and the WordNet corpus
        to determine similarity between words.
    """

    def __init__(self):
        nltk.download("wordnet")
        self.corpus = nltk.corpus.wordnet

    def get_similar(self, word):
        synsets = self.corpus.synsets(word.lower()) # Assuming it's a noun atm..
        results = [word.lower()]
        for synset in synsets:
            for lemma in synset.lemmas:
                results.append(lemma.name)
        return set(results)

    def extract_from(self, text):
        sentences = nltk.sent_tokenize(text)
        tokens = [word for sent in sentences for word in
                  nltk.word_tokenize(sent)]
        return tokens