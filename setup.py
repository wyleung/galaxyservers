# -*- coding: utf-8 -
#
# This file is part of galaxyserver released under the MIT license.
# See the NOTICE for more information.


import os
from setuptools import setup, find_packages, Command
import sys

version_info = (0, 1, 0)
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

# read long description
with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    long_description = f.read()

# read dev requirements
# fname = os.path.join(os.path.dirname(__file__), 'requirements_dev.txt')
# with open(fname) as f:
#     tests_require = list(map(lambda l: l.strip(), f.readlines()))

class PyTest(Command):
    user_options = [
        ("cov", None, "measure coverage")
    ]

    def initialize_options(self):
        self.cov = None

    def finalize_options(self):
        pass

    def run(self):
        import sys,subprocess
        basecmd = [sys.executable, '-m', 'pytest']
        if self.cov:
            basecmd += ['--cov', 'gunicorn']
        errno = subprocess.call(basecmd + ['tests'])
        raise SystemExit(errno)


setup(
    name = 'galaxyservers',
    version = __version__,

    description = 'Runners for Galaxyproject',
    # long_description = long_description,
    author = 'Wai Yi Leung',
    author_email = 'w.y.leung@e-sensei.nl',
    license = 'MIT',
    url = 'https://github.com/wyleung/galaxyservers',

    classifiers = CLASSIFIERS,
    zip_safe = False,
    packages = find_packages(exclude=['examples', 'tests']),
    include_package_data = True,

    # tests_require = tests_require,
    # cmdclass = {'test': PyTest},

    entry_points="""
    [paste.server_runner]
    tornado=galaxyservers.servers.tornado_runner:paste_server
    gunicorn=galaxyservers.servers.gunicorn_runner:paste_server
    fapws3=galaxyservers.servers.fapws3_runner:paste_server
    """
)
