#!/usr/bin/env python
# Author: Alex Ksikes 

# TODO :
# - move to production server
# - add google ads
# - domain name wikitrivia.net, contact wade for .com
# - add analytics
# - add testimonials

import web
import config
import app.controllers

urls = (
    '/?',                                   'app.controllers.wikitrivia.index',
    '/quiz/?',                              'app.controllers.wikitrivia.quiz',
    '/answer/?',                            'app.controllers.wikitrivia.answer',
    '/public/.+',                           'app.controllers.public.public',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
