#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, unicode_literals

from fabric.api import cd, env, lcd, local, run, sudo, task
from fabric.colors import green, red
from fabric.contrib.project import rsync_project
from fabric.operations import prompt

from fabtools import require

env.use_ssh_config = True
env.hosts = ['web@singularity.su']
env.shell = "/bin/bash -l -i -c"
env.key_filename = "/home/ihor/.ssh/id_rsa"
env.rsync_excludes = ['*.pyc', '*.db', '*~']


@task
def make_m():
    with lcd('question'):
        local('django-admin.py makemessages -l ua')


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


def venv_command(command='help', virtualenv='stackoverflow'):
    run("/bin/bash -l -c 'source /usr/local/bin/virtualenvwrapper.sh && workon " +
        virtualenv + " && " + command + " '")


@task
def restart():

    with cd('stackoverflow'):
        run('workon stackoverflow')
        run('hg pull')
        run('hg update')
    venv_command('python manage.py collectstatic -y')
    run('touch /home/web/stackoverflow/uwsgi.ini')
    sudo('ln -s nginx.conf /etc/nginx/conf.d/stackoeverflow.conf ')
    sudo('service nginx restart')


@task
def push(comment=False):
    if comment == False:
        print(red('Commit comment is requred!'))
        comment = prompt('Enter commit: ', default='spam & eggs')
    green(comment)
    local('find . -name "*.py" -exec isort {} \\;')
    local('autopep8 --in-place -r . ')
    local('hg add .')
    local('hg ci -m "{}"'.format(comment), capture=False)
    local('hg push')
    green('All ok')
    restart()


@task
def db_setup():
    local(';\n'.join([
        'python ./manage.py syncdb',
        'python ./manage.py migrate',
        'python ./manage.py createsuperuser',
    ]))


@task
def r():
    local('python ./manage.py runserver')


@task
def setup_python():
    require.deb.packages([
        'python-pip',
        'python-dev',
        'build-essential',
        'uwsgi',
        'uwsgi-plugin-python',
        'libssl-dev',
        'libffi-dev',
    ])


def setup_sass():
    local('sudo apt-add-repository ppa:chris-lea/node.js -y')
    local('sudo apt-get update')
    local('sudo apt-get install ruby rubygems yui-compressor nodejs -y')
    local('sudo npm install -g bower')
    local('sudo gem install compass sass foundation')
    print('foundation new PROJECT_NAM \n sass watch')


@task
def install_pillow():
    require.deb.packages([
        'libtiff4-dev',
        'libjpeg8-dev',
        'zlib1g-dev',
        'libfreetype6-dev',
        'liblcms2-dev',
        'libwebp-dev',
    ])


@task
def setup_python_packeges():
    require.python.packages(['fabric', 'virtualenvwrapper'], use_sudo=True)


@task
def pip_wraper():
    with lcd('/home/ihor/.pip'):
        require.directory('~/.pip', owner='web')
        #require.file('~/.pip/pip.conf', source='pip.conf')
    text = """ 
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
"""
    require.directory('~/.virtualenvs', owner='web')
    require.file('~/.bashrc', contents=text)


@task
def test_connect():
    run('uname -s')
    run('ls -l')
