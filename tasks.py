from os import path
from invoke import run, task

languages = ['en', 'de']

BASE_DIR = path.realpath(path.dirname(__file__))
BUILD_DIR = path.join(BASE_DIR, 'build')
SOURCE_DIR = path.join(BASE_DIR, 'source')
LOCALE_DIR = path.join(SOURCE_DIR, 'locale',
                       '%s', 'LC_MESSAGES')
LANGUAGES = set(['en', 'de'])
MAIN_TARGET = 'html'
REPOSITORY = 'git@github.com:OpenTechSchool/python-beginners.git'
SERVE_PORT = 8000


@task
def clean(language=None):
    if language is None:
        langs = languages
    elif language in languages:
        langs = [language]
    else:
        exit('Invalid language %s' % language)
    for l in langs:
        run("rm -rf %s" % path.join('build', l))


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
