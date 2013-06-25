#!/usr/bin/env python

import os
import os.path
import fapws._evwsgi as evwsgi
from fapws import base
import sys
sys.setcheckinterval(100000) # since we don't use threads, internal checks are no more required

def paste_server(app, gcfg=None, host="127.0.0.1", port=None, *args, **kwargs):
    """
    A paster server.

    Then entry point in your paster ini file should looks like this:

    [server:main]
    use = egg:galaxyservers#fapws3
    host = 127.0.0.1
    port = 5000

    """
    evwsgi.start(host, port)
    evwsgi.set_base_module(base)
    evwsgi.wsgi_cb(('',app))
    evwsgi.run()
