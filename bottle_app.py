from bottle import *
import beaker.middleware
import os

from web_app import *

os.chdir('/home/dzil123/mysite') # for static files

session_opts = {
    'session.type': 'file',
    'session.data_dir': '/home/dzil123/mysite/session/',
    'session.auto': True,
}

@hook('before_request') # adds easier cookie sessions
def setup_request():
    request.session = request.environ['beaker.session']

def asdf(func, title='', back=True):
    def f():
        b = '<p><a href='/'>Back to Start</a></p>'
        b = b if back else ''
        html = '''<html>
<head>
<title>%s</title>
<link rel="icon" href="/favicon.ico">
</head>
<body>
<h1>%s</h1>
<div>%s</div>
%s
</body>
</html>''' % (title, title, func(), b)
        
        return html
    return f

@route('/<name>/', method='ANY')
def slash_main(name):
    redirect('/%s' % name)

# begin /* static

@route('/google61ad6ab6e35fb181.html', method='ANY') # google verification file
def google_ver():
    return static_file('google61ad6ab6e35fb181.html', '.') # robots.txt

@route('/robots.txt', method='ANY')
def robots_txt():
    return static_file('robots.txt', '.')

@route('/favicon.ico', method='ANY')
def favicon():
    return static_file('favicon.ico', '.')

@route('/source', method='ANY')
def source():
    return static_file('bottle_app.py', '.', mimetype='text/x-python', download=True)

# end /* static

# BEGIN SHORTENING LINKS

@route('/go', method='ANY') # /go/ should be handled by slash_name
def go_main():
    redirect('/')

@route('/go/<name>/', method='ANY')
def slash_go(name):
    redirect('/go/%s' % name)

for x in s: # provided by web_app
    com = '''
@route('/go/%s')
def go_%s():
    redirect('%s')''' % (x[0], x[0], x[1])

    exec(com)

# END SHORTENING LINKS

application = default_app()

application = beaker.middleware.SessionMiddleware(application, session_opts)
