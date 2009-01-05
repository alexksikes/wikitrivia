# Author: Alex Ksikes

import web

def reset_score():
    web.setcookie('score', 0)
                
def update_score(cscore):
    cscore = 10 + int(cscore)
    web.setcookie('score', cscore)
    return cscore

def get_score():
    return int(web.cookies(score=0).score)
