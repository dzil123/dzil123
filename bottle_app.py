from bottle import *
import beaker.middleware

from web_app import *

session_opts = {
    'session.type': 'file',
    'session.data_dir': '/home/dzil123/mysite/session/',
    'session.auto': True,
}

@hook('before_request') # adds easier cookie sessions
def setup_request():
    request.session = request.environ['beaker.session']

os.chdir('/home/dzil123/mysite') # for static files

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
