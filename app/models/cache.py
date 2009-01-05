# Author: Alex Ksikes

import web
from config import db

# TODO: - This is inefficient compared to
# SELECT * FROM `table` WHERE id >= (SELECT FLOOR( MAX(id) * RAND()) FROM `table` ) ORDER BY id LIMIT 1;
def get_random_question(category):
    """Get a random quiz question from the cache."""
    return web.listget(
        db.select('wikitrivia_cache',
            vars=dict(category=category), 
            where='category = $category', limit=1, order='rand()'), 0, False)

def set_question(question):
    """Set a quiz question in the cache."""
    if not get_question(question):
        db.insert('wikitrivia_cache', **question)

def get_question(question):
    """Get a specific question from the cache."""
    return web.listget(
        db.select('wikitrivia_cache', 
            vars=dict(url=wiki_url),
            where='wiki_url = $url', limit=1), 0, False)
