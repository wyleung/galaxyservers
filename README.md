Galaxyservers
=============

This package is a release supporting the poster presentation at GCC2013/Oslo.
The work is still in progres, we will incremently add servers and installation
instructions to this package.

Installation
--------------

To install this package you will need either root access or preferabel install into
your virtualenv. 

### Installation of WSGI-servers

Some of the WSGI-server require supplementary installation of supporting software/libraries.

One common package to install is **python-dev**, this can be installed by:

    sudo apt-get install python-dev build-essential

On Debian/Ubuntu based systems.

#### Fapws3
In order to install Fapws3, you need to install 1 system package called 'libev'. This packages handles the event-based system calls.

    sudo apt-get install libev libev-dev

Inside your virtualenv, installation of Fapws3 is done by:

    pip install fapws3

Thats all! Once installed, proceed with configuring your Galaxy instance

#### Gunicorn

Installation of Gunicorn also requires the installation of the **python-dev** library headers. Install the following into your virtualenv: (or even system-wide)

    pip install greenlet gunicorn

That's all!

#### Tornado

    pip install tornado

#### uWSGI

    pip install uwsgi

### Configuring your Galaxy instance

Open **universe_wsgi.ini** and search for the following section:

    [server:main]
    use = egg:Paste#http

You can replace the **egg:Paste#http** by any server supported by this package:

    [server:main]
    use = egg:galaxyservers#gunicorn
	# you can replace gunicorn by: fapws3/tornado

##### one exception
uWSGI requires a slightly different setup.

