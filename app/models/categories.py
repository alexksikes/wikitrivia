# Author: Alex Ksikes

lang = 'en'
base_query = '/wiki/ site:' + lang + '.wikipedia.org -disambiguation -"up to conform" -"a stub" \
-"is the * day" -"was a * year" -"list of years"'

yahoo_queries = dict(
    comics = '"comic books" OR "comic book" OR "manga" OR "comics" OR "graphic novel"',
    movies = 'tv OR movie OR movies OR cinema OR actor OR actress OR director',
    scifi = '"science fiction" OR "sci fi"',
    sports = 'baseball OR football OR basketball OR sport OR sports',
    blogs = '"web log" OR blog OR blogging OR waxy OR weblog OR blogger OR weblogs OR "boing boing"',
    politics = 'political politician',
    art = 'painter OR painting',
    science = 'physics OR chemistry OR math OR astronomy OR medicine OR science',
    food = 'food OR dish OR recipe OR drink OR cocktail',
    literature = 'author OR writer novel',
    programming = 'programming OR programmer',
    geography = '"is a city" OR "is a country"',
    music = 'singer OR band OR pop',
    philosophy = 'philosopher',
    fantasy = 'fantasy OR "lord of the rings" -"final fantasy"',
    animals = 'animal family',
    computers = 'computer OR internet',
    games = '"computer game" OR "video game" OR "pc game" OR "amiga 500" OR atari OR c64',
    cars = 'car',
    detectives = '"miss marple" OR "secret agent"  OR "austin powers" OR detective OR "sherlock holmes" OR "james bond" OR "inspector clouseau" OR "agatha christie" OR "conan doyle"',
    legends = '"fairy tale" OR "urban legend" OR "conspiracy theory" OR scam OR spoof OR fake',
    crime = 'murder OR criminal OR mafia OR assassination OR thief',
    search = '"search engine" OR seo OR google -groups.google -maps.google',
    searchde = 'suchmaschine -groups.google -maps.google',
    misc = 'wikipedia',
)    

def get_yahoo_query(category):
    """Get a search query to return a random wikipedia article."""
    return yahoo_queries[category] + ' ' + base_query

def get_categories():    
    """Return a list of categories for the quiz."""
    return [('comics', 'Comics'), ('movies', 'Movies'), ('sports', 'Sports'), ('scifi', 'Sci-fi'), 
        ('blogs', 'Blogs'), ('politics', 'Politics'), ('science', 'Science'), ('literature', 'Literature'), 
        ('music', 'Music'), ('art', 'Art'), ('geography', 'Geography'), ('programming', 'Programming'), 
        ('food', 'Food'), ('philosophy', 'Philosophy'), ('fantasy', 'Fantasy'), ('animals', 'Animals'), 
        ('computers', 'Computers'), ('games', 'Video&nbsp;Games'), ('cars', 'Cars'), 
        ('detectives', 'Detectives'), ('legends', 'Legends'), ('crime', 'Crime'), ('misc', 'Misc.')]

def get_category_name(category):
    """Return the pretty name of a category."""
    for c, c_name in get_categories():
        if c == category:
            return c_name

def is_valid_category(category):
    return category in yahoo_queries.keys()