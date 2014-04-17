#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, unicode_literals

from fabric.api import *
from fabric.colors import *


@task
def mail_server():
    local('python -m smtpd -n -c DebuggingServer localhost:1025')


@task
def init_migration():
    local('python ./manage.py schemamigration question --initial')
    local('sudo chmod +x manage.py ')


@task
def dump():
    local('python ./manage.py dumpdata > question/fixtures/initial_data.json')


@task
def m():
    local('python ./manage.py schemamigration question --auto')
    local('python ./manage.py migrate question')


@task
def mn(appname):
    local('python ./manage.py schemamigration {} --auto'.format(appname))
    local('python ./manage.py migrate {}'.format(appname))


@task
def push(comment=False):
    if comment == False:
        return red('Commit comment is requred!')
    #local('workon djangoggg')
    local('rm requirements.txt')
    local('pip freeze >> requirements.txt')
    local('find . -name "*.py" -exec isort {} \\;')
    local('autopep8 --in-place -r . ')
    local('git add .')
    local('git status', capture=False)
    local('git commit -m "{}"'.format(comment), capture=False)
    local('git push', capture=False)
    green('All ok')


@task
def db_setup():
    local(';\n'.join([
        'python ./manage.py syncdb',
        'python ./manage.py migrate',
        'python ./manage.py createsuperuser',
    ]))


@task
def run():
    local(';\n'.join([
        'python ./manage.py syncdb',
        'python ./manage.py migrate',
        'python ./manage.py collectstatic --noinput',
        'python ./manage.py run_gunicorn',
    ]))
