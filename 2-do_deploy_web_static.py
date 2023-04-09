#!/usr/bin/env python3
"""
Fabric script that distributes an archive to web servers
"""

import os.path
from fabric.api import env, put, run, sudo


env.hosts = ['54.175.198.234', '54.90.19.199']


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    # Upload the archive to the web server
    put(archive_path, '/tmp/')

    # Get the archive filename without extension
    archive_filename = os.path.basename(archive_path)
    archive_name = os.path.splitext(archive_filename)[0]

    # Create the release directory
    run('mkdir -p /data/web_static/releases/{}'.format(archive_name))

    # Uncompress the archive to the release directory
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'
        .format(archive_filename, archive_name))

    # Delete the archive from the web server
    run('rm /tmp/{}'.format(archive_filename))

    # Move the files to the final location
    run('mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/'.format(archive_name, archive_name))

    # Remove the empty directory
    run('rm -rf /data/web_static/releases/{}/web_static'
        .format(archive_name))

    # Delete the symbolic link
    run('rm -f /data/web_static/current')

    # Create a new symbolic link
    run('ln -s /data/web_static/releases/{} /data/web_static/current'
        .format(archive_name))

    print("New version deployed!")
    return True

