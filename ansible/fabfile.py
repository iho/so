#!/usr/bin/env python
# coding: utf-8

from fabric.api import run, env
env.use_ssh_config = True
env.shell = "/bin/bash -l -i -c" 
env.hosts = ['root@singularity.su']
env.key_filename = "~/.ssh/id_rsa"
def test():
    run('uname -s')
