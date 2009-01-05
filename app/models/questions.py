# Author: Alex Ksikes

# TODO: 
# - We should probably have a class Question

import web

from app import lib
from app.models import cache
from app.models import categories

import random, re
from lxml import etree

question_range = 1000
snippet_size = 350
with_images_only = False
max_trials = 3
use_cache = True

def get_random_question(category, trials=max_trials):
    """Get a random quiz question using wikipedia."""
    # no more trials we failed so fetch from the cache
    if trials == 0: 
        return use_cache and cache.get_random_question(category)
    
    # maybe we have exhausted all queries from yahoo
    url = get_random_wiki_url(category)
    if not url:
        return use_cache and cache.get_random_question(category)
    
    # maybe xml parsing failed or the question we got is no good
    question = make_question(url, category)
    if not question or not is_question_valid(question):
        return get_random_question(category, trials-1)    
    
    # if we got here it is that we have a question so save it
    if use_cache and question.image_url: 
        cache.set_question(question)
    
    return question
    
def get_random_wiki_url(category):
    """Use yahoo to get a random wikipedia url."""
    wiki_url = ''
    if categories.yahoo_queries.has_key(category):
        query = categories.get_yahoo_query(category)
        wiki_url = web.listget(
            lib.yahoo_search(query, random.randint(0, question_range), 1), 0, {}).get('url', '')
    return wiki_url

def make_question(url, category):
    """Create the random question from wikipedia."""
    try:
        article = lib.dnl(url, referer='http://en.wikipedia.org/')
        xml = lib.parse_xml(article)
    except:
        return False
        raise 'Either can\'t download the wikipedia article or can\'t parse it.'
    
    answer = xml.findtext('.//h1').encode('utf-8')
    snippet = ''
    for p in xml.xpath('//div[@id="bodyContent"]/p'):
        snippet += etree.tostring(p, method='text', encoding='utf-8').strip() + ' '
#        snippet += lib.strip_tags(etree.tostring(p)) + '\n'
    snippet = snippet[0:snippet_size].replace('\n', '<br />').decode('utf-8')
    snippet = re.sub('\[\d+\]', '', snippet)
    
    snippet_secret = snippet
    for a in answer.split():
        p = re.compile(r'\b%s\b' % re.escape(a), re.I)
        snippet_secret = p.sub('<strong class="depleted">' + '?' * len(a) + '</strong>', snippet_secret)
    
    image_url = web.listget(
        xml.xpath('//img[@class="thumbimage"]//@src'), 0, '')
    
    return web.storage(
        dict(answer=answer, snippet_secret=snippet_secret, category=category,
        snippet=snippet, wiki_url=url, image_url=image_url))

def is_question_valid(question):
    """Return True if the generated question is valid."""
    if with_images_only and not question.image_url:
        return False
    return 'class="depleted"' in question.snippet_secret and len(question.snippet) == snippet_size

def is_correct_guess(guess, answer):
    """Check the user's guess in a pretty lenient way."""
    guess, answer = map(lambda x: 
        re.sub('[^a-zA-Z0-9\s]', '', x.lower().strip().encode('ascii', 'ignore')).split(), (guess, answer))
    return len([c for c in answer if c in guess]) >= (len(answer) / 2 or 1)
