import web, os

# connect to database
db = web.database(dbn='mysql', db='wikitrivia', user='user', passwd='password')

# in development debug error messages and reloader
web.config.debug = True

# in develpment template caching is set to false
cache = False

# set global base template
view = web.template.render('app/views', cache=cache)

# used to encrypt the answer
encryption_key = 'a random string'

# your yahoo app id
yahoo_appid = ''
