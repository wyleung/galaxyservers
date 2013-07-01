# -*- coding: utf-8 -
#
# This file is part of galaxyserver released under the MIT license.
# See the LICENCE for more information.

import os
from setuptools import setup, find_packages, Command
import sys

version_info = (0, 1, 1)
__version__ = ".".join([str(v) for v in version_info])

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Other Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet',
    'Topic :: Utilities',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: WSGI',
    'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content']

try:
    with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
        long_description = f.read()
except:
    long_description = 'See https://github.com/wyleung/galaxyservers/'

# read dev requirements
# fname = os.path.join(os.path.dirname(__file__), 'requirements_dev.txt')
# with open(fname) as f:
#     tests_require = list(map(lambda l: l.strip(), f.readlines()))


setup(
    name = 'galaxyservers',
    version = __version__,
    url = 'https://github.com/wyleung/galaxyservers',
    
    author = 'Wai Yi Leung',
    author_email = 'w.y.leung@e-sensei.nl',

    description = 'Runners for Galaxyproject',
    long_description = long_description,
    license = 'MIT',

    classifiers = CLASSIFIERS,
    zip_safe = False,
    packages = find_packages(exclude=['examples', 'tests']),
    data_files = [('', ['README.md'])],
    include_package_data = True,

    entry_points="""
    [paste.server_runner]
    tornado=galaxyservers.servers.tornado_runner:paste_server
    gunicorn=galaxyservers.servers.gunicorn_runner:paste_server
    fapws3=galaxyservers.servers.fapws3_runner:paste_server
    """
)