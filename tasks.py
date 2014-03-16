import sys
from os import path, chdir
from invoke import run, task

if sys.version_info[0] < 3:
    import SimpleHTTPServer as httpserver
    import SocketServer as socketserver
else:
    import http.server as httpserver
    import socketserver

languages = ['en', 'de']

BASE_DIR = path.realpath(path.dirname(__file__))
BUILD_DIR = path.join(BASE_DIR, 'build')
SOURCE_DIR = path.join(BASE_DIR, 'source')
LOCALE_DIR = path.join(SOURCE_DIR, 'locale',
                       '%s', 'LC_MESSAGES')
LANGUAGES = set(['en', 'de'])
MAIN_TARGET = 'html'
REPOSITORY = 'git@github.com:OpenTechSchool/html-css-beginners.git'
SERVE_PORT = 8000


@task
def clean(language=None, target=MAIN_TARGET):
    if language is not None:
        run('rm -rf %s' % path.join(BUILD_DIR, target, language))
    else:
        run('rm -rf %s' % path.join(BUILD_DIR, target))


@task('clean')
def setup():
    target_dir = path.join(BUILD_DIR, MAIN_TARGET)
    run('mkdir -p %s' % target_dir)
    run('git clone %s -b %s --single-branch %s' %
        (REPOSITORY, 'gh-pages', target_dir))


@task
def build(language=None, target=MAIN_TARGET):
    if language is None:
        print('Please build a specific language; one of: %s' %
              ', '.join(LANGUAGES))
        print('e.g: invoke build -l en')
        exit()
    elif language not in LANGUAGES:
        exit('Language %s not available.' % language)
    args = [
        'sphinx-build',
        '-b', target,  # builder type
        '-d', path.join(BUILD_DIR, 'doctrees'),  # doctree path
        '-D', 'language=%s' % language,  # language
        SOURCE_DIR,
        path.join(BUILD_DIR, target, language),  # output path
    ]
    run(' '.join(args))
    if 'html' in target:
        static_files = path.join(BASE_DIR, '_static', '*')
        target_dir = path.join(BUILD_DIR, target)
        run('cp %s %s' % (static_files, target_dir))


def serve(port=SERVE_PORT, serve_dir=None):
    """Run a web server to serve the built project"""
    if serve_dir is None:
        serve_dir = path.join(BUILD_DIR, MAIN_TARGET)
    port = int(port)
    chdir(serve_dir)
    handler = httpserver.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)
    print("serving on http://%s:%s" % httpd.server_address)
    httpd.serve_forever()
