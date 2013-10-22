from sys import argv, stdout

import nltk
import jsonpickle

from seedrecruit.classifier import KeywordClassifier, JobTitleClassifier
from seedrecruit.data.candidate import Candidate
from seedrecruit.data.job import JobDescription
from seedrecruit.data.keyword import WordNetKeywordPool


class Calculator(object):
    def __init__(self, job_file, candidates):
        self.job_desc = JobDescription(job_file)
        self.candidates = map(lambda x: Candidate(x), candidates)

    def run(self):
        print "Checking NLTK deps"
        nltk.download("wordnet")
        nltk.download("punkt")

        keywords = WordNetKeywordPool()
        classifiers = [KeywordClassifier(keywords), JobTitleClassifier(keywords)]
        for candidate in self.candidates:
            stdout.write("Processing candidate \"%s, %s\"... " %
                         (candidate.last_name, candidate.first_name))
            scores = map(lambda x: x.get_score(self.job_desc, candidate), classifiers)
            average = float(reduce(lambda x, y: x + y, scores)) / len(scores)
            stdout.write("%f\n" % average)
            candidate.score = average
        top_three = sorted(self.candidates, key=lambda x: -x.score)
        print jsonpickle.encode(top_three[:3])


if __name__ == "__main__":
    if len(argv) < 2:
        print "Usage: ./calculator.py <path_to_jobdesc> [<candidate_file>]"
        exit(255)
    instance = Calculator(argv[1], argv[2:])
    instance.run()