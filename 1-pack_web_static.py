#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive."""
import os
from datetime import datetime
from fabric.api import local, runs_once


def do_pack():
    """
    Creates a .tgz archive of the contents of the web_static folder and stores it in the versions directory.
    """
if not os.path.isdir("versions"):
        os.mkdir("versions")
    d_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        d_time.year,
        d_time.month,
        d_time.day,
        d_time.hour,
        d_time.minute,
        d_time.second
    )
    try:
        local("mkdir -p versions")
        timestamp = time.strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except:
        return None
