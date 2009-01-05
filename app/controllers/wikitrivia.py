# Author: Alex Ksikes 

import web
import config

from app.models import questions
from app.models import score
from app.models import categories
from config import view

class index:
    def GET(self):
        score.reset_score()
        return view.layout(view.front_page(categories.get_categories()))
    
class quiz:
    def GET(self):
        i = web.input(category='')
        if not categories.is_valid_category(i.category): 
            return web.seeother('/')
        
        question = questions.get_random_question(i.category)
        
        category, category_name = i.category, categories.get_category_name(i.category)
        return view.layout(view.question(question, score.get_score(), category, category_name), 
            title='Wikitrivia - ' + category_name)
                
class answer:
    def POST(self):
        i = web.input(category='', answer='', guess='', wiki_url='', score=0)
        
        success = questions.is_correct_guess(i.guess, i.answer)
        cscore = i.score
        if success:
            cscore = score.update_score(cscore)
        
        category_name = categories.get_category_name(i.category)
        return view.layout(view.score(cscore, i, success), title='Wikitrivia - ' + category_name)
