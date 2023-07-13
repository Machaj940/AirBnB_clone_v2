#!/usr/bin/python3
''' Fabric script that generates a .tgz archive from the contents of the web_
    static
'''
from fabric.api import local
from datetime import datetime


def do_pack():
    ''' Fabric script that generates a .tgz archive from the contents of the
        web_static
    '''
    now = datetime.now()
    filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(now.year,
                                                             now.month,
                                                             now.day,
                                                             now.hour,
                                                             now.minute,
                                                             now.second)
    print("Packing web_static to versions/{}".format(filename))
    local("mkdir -p versions")
    local("tar -zcvf {} web_static".format(filename))
