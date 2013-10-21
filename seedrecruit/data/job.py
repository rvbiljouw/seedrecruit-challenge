from lxml import etree

from seedrecruit.util.solr import get_solr_str


class JobDescription(object):
    """ A class that wraps a job description document
    """

    def __init__(self, input_file):
        dom = etree.parse(input_file)
        doc = dom.xpath("/response/result/doc")[0]
        self.id = get_solr_str(doc, 'id')
        self.type = get_solr_str(doc, 'job_type')
        self.title = get_solr_str(doc, 'job_title')
        self.company = get_solr_str(doc, 'job_company')
        self.location = get_solr_str(doc, 'job_location')
        self.description = get_solr_str(doc, 'job_description')
        self.min_salary = get_solr_str(doc, 'salary_bracket_min')
        self.max_salary = get_solr_str(doc, 'salary_bracket_max')


class NoJobDescriptionFoundException(Exception):
    """ An exception thrown when there is no information
    about the job found in the XML document it was supposed
    to load from. """

    def __str__(self):
        return ": No 'doc' element was found in the XML document"