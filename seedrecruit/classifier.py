from abc import ABCMeta, abstractmethod


class AbstractClassifier(object):
    __metaclass__ = ABCMeta

    def __init__(self, keyword_pool):
        self.keyword_pool = keyword_pool

    @abstractmethod
    def get_score(self, job, candidate):
        pass

    def has_similar(self, keywords, word):
        similars = self.keyword_pool.get_similar(word)
        return word in keywords or len(filter(lambda x: x in keywords, similars)) > 0


class KeywordClassifier(AbstractClassifier):
    """ A classifier that does the first set of classification
        and filtering based purely on keywords found in the job
        description
    """

    def __init__(self, keyword_pool):
        super(KeywordClassifier, self).__init__(keyword_pool)

    def get_score(self, job, candidate):
        keywords = self.keyword_pool.extract_from(job.description)
        resume_kw = self.keyword_pool.extract_from(candidate.resume)
        matching_kw = filter(lambda x: self.has_similar(keywords, x),
                             resume_kw)
        if len(matching_kw) > 0:
            return (float(len(matching_kw)) / float(len(resume_kw))) * 100
        return 0


class JobTitleClassifier(AbstractClassifier):
    """ A classifier that checks the candidates resume and positions
        for similar job titles to the one in the job description
    """

    def __init__(self, keyword_pool):
        super(JobTitleClassifier, self).__init__(keyword_pool)

    def get_score(self, job, candidate):
        kw = self.keyword_pool.extract_from(job.title)
        res = self.keyword_pool.extract_from(candidate.resume)
        matching_resume = filter(lambda x: self.has_similar(kw, x), res)
        pos_str = " ".join(map(lambda x: x.title, candidate.positions))
        pos = self.keyword_pool.extract_from(pos_str)
        matching_positions = filter(lambda x: self.has_similar(kw, x), pos)
        total_match = 0
        if len(matching_resume) > 0:
            total_match += (float(len(matching_resume)) / float(len(kw)) * 100)
        if len(matching_positions) > 0:
            total_match += (float(len(matching_positions)) / float(len(kw)) * 100)

        if total_match > 0:
            return total_match / 2
        return total_match


class SkillClassifier(AbstractClassifier):
    """ A classifier that scores candidates on being their skill set
        defined on LinkedIn. If the candidate has no skills on LinkedIn
        the score is set to 0. We assume that the person with the most relevant
        information is the best candidate so we can't have people not linking
        their LinkedIn info.
    """

    def __init__(self, keyword_pool):
        super(SkillClassifier, self).__init__(keyword_pool)

    def get_score(self, job, candidate):
        keywords = self.keyword_pool.extract_from(job.description)
        matching_skills = filter(lambda x: self.has_similar(keywords, x), candidate.skills)
        if len(matching_skills) > 0:
            return (float(len(matching_skills)) / float(len(candidate.skills))) * 100
        return 0


AbstractClassifier.register(KeywordClassifier)