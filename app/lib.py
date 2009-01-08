# Author: Alex Ksikes 

import re, urllib, pycurl, cStringIO, string, random
from lxml import etree

def yahoo_search(query, start, results):
    appid = 'your app id'
    url = 'http://search.yahooapis.com/WebSearchService/V1/webSearch?appid=%s&query=%s&results=%s&start=%s' % \
    (appid, urllib.quote(query), results, start)
    xml = parse_xml(dnl(url))
    
    results = []
    for r in xml.findall('Result'):
        result = {}
        for f in ['Title', 'Summary', 'Url']:
            result[f.lower()] = r.findtext(f)
        results.append(result)
        
    return results

def parse_xml(txt):
    xml = re.sub('xmlns\s*=\s*["\'].*?["\']', ' ', txt) # we remove the xmlns for simplicity
    return etree.fromstring(xml, parser=etree.XMLParser(resolve_entities=False))

def curl_init():
    curl = pycurl.Curl()
    curl.setopt(pycurl.USERAGENT, "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)")
    #curl.setopt(pycurl.CONNECTTIMEOUT, 3)
    #curl.setopt(pycurl.TIMEOUT, 30)
    return curl

# TODO: some urls such as http://en.wikipedia.org/wiki/List_of_Tamil-language_films return garbage for some reason.       
def open_url(curl, url, referer = None):
    curl.setopt(pycurl.URL, url)
    if referer:
        curl.setopt(pycurl.REFERER, referer)
    
    f = cStringIO.StringIO()
    curl.setopt(pycurl.WRITEFUNCTION, f.write)
    curl.perform()
    
    html = f.getvalue()
    f.close()
    return html

def dnl(url, referer = None):
    c = curl_init()
    return open_url(c, url, referer)

def capitalize_first(str):
    if not str:
        str = ''
    return ' '.join(map(string.capitalize, str.lower().split()))

def get_pub_id():
    pub_ids = dict(alex = 'pub-1431948349807205', philipp = 'pub-4135663670627621')
    return pub_ids.values()[random.randint(0,1)]
    
# we may want to use this in order to preserve some of html of wikipedia
def strip_tags(html, ignore_tags='<b>|<i>|&#?\w+;'):
    skip_p = re.compile(ignore_tags, re.I)
    def fixup(m):
        text = m.group(0)
        if skip_p.match(text):
            return text
        if text[:1] == "<" or text[:1] == "&" or text[:2] == "&#":
            return ""
        return text
    return re.sub("(?s)<[^>]*>|&#?\w+;", fixup, text)
