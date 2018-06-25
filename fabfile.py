import os
import shutil
from fabric.api import local, lcd


def clean():
    with lcd(os.path.dirname(__file__)):
        local("find . | grep -E \"(__pycache__|\.pyc$)\" | xargs rm -rf")

def deploy():
    # test()
    # make()
    local("nikola github_deploy")


def test():
    local("python3.6 -m unittest")
