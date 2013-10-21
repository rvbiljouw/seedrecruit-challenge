""" A set of utility methods for dealing with Solr exported XML """


def get_solr_str(doc, key):
    """ Reads an attribute for this candidate from the DOM """
    elem = doc.xpath("str[@name='%s']" % key)
    try:
        return elem[0].text
    except IndexError:
        raise SolrAttributeNotFoundException(key)


def get_solr_arr(doc, key):
    """ Reads an (array?) for this candidate from the DOM """
    elem = doc.xpath("arr[@name='%s']/str" % key)
    try:
        return elem[0].text
    except IndexError:
        raise SolrAttributeNotFoundException(key)


class SolrAttributeNotFoundException(Exception):
    """ Exception thrown when an expected attribute
        could not be found in a Solr XML document.
    """

    def __init__(self, attrib):
        self.attrib = attrib