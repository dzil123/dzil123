#import bottle
from bottle import *
import beaker.middleware

# begin /*

@route('/', method='ANY')
def index():
    return site_map() # just return function here, dont do any coding

@route('/site_map', method='ANY')
@route('/sitemap', method='ANY')
@route('/map', method='ANY')
def site_map():
    site = [['Cookie Counter', '/cookie'], ['See the Source Code of this website', '/source']]

    html = '<head><title>Daniel\'s Website</title><link rel="icon" href="/favicon.ico"></head><h1>Welcome to my Hand-Coded Website</h1>' # header
    html += "<ul>" # begin list

    for x in site:
        html += '<li><a href="%s">%s</a></li>' % (x[1], x[0])

    html += '</ul>'

    return html

@route('/cookie', method='ANY')
def cookie_counter():
    if 'counter' not in request.session.keys():
        request.session['counter'] = 0
    request.session['counter'] += 1
    return '<h1>You visited this page %s time%s</h1><br/><a href="%s">Back to start</a>' % (str(request.session['counter']), ('s' if request.session['counter'] > 1 else ''), '/')

@route('/<name>/', method='ANY')
def slash_main(name):
    redirect('/%s' % name)

# end /*

s = [['python', '/'], ['coolapp', '/'], ['danielz', '/']]
