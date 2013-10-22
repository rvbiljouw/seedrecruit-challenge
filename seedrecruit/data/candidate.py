from json import loads
from lxml import etree

from seedrecruit.util.solr import get_solr_arr, get_solr_str


class Candidate(object):
    """ A class that wraps a candidate profile """

    def __init__(self, input_file):
        dom = etree.parse(input_file)
        doc = dom.xpath("/response/result/doc")[0]
        self.id = get_solr_str(doc, 'user_id')
        self.first_name = get_solr_str(doc, 'user_first_name')
        self.last_name = get_solr_str(doc, 'user_last_name')
        self.locations = get_solr_str(doc, 'user_locations')
        self.resume = get_solr_arr(doc, 'content')
        self.summary = get_solr_str(doc, 'linkedin_summary')
        self.score = 0

        positions = loads(get_solr_str(doc, 'linkedin_positions'))['values']
        self.positions = map(lambda x: Position(x), positions)
        skills = loads(get_solr_str(doc, 'linkedin_skills'))['values']
        # Nothing to do with endorsements yet, so this should be okay?
        # If we get endorsements this should probably be wrapped in a class
        # so we can count them etc.
        self.skills = map(lambda x: x['skill']['name'], skills)


class Position(object):
    """ A class that wraps a LinkedIn position
    """

    def __init__(self, values):
        self.id = values['id']
        self.company_name = values['company']['name']
        self.company_industry = values['company']['industry']
        self.start_month = values['startDate']['month']
        self.start_year = values['startDate']['year']
        self.is_current = values['isCurrent']
        if 'summary' in values:
            self.summary = values['summary']
        self.title = values['title']
