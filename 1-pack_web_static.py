#!/usr/bin/python3
""" A Fabric script """
from fabric.api import local, lcd
from datetime import datetime


def do_pack():
    """ Generates a tgz archive """
    local("mkdir -p versions")
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local("tar cvfz versions/web_static_{}.tgz web_static/"
          .format(now))
    path = ""
    with lcd("versions"):
        path = local("pwd", capture=True)
        path += local("ls web_static_{}.tgz".format(now), capture=True)
    return path
