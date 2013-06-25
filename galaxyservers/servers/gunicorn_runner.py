# -*- coding: utf-8 -
#
# This file is part of gunicorn released under the MIT license.
# See the NOTICE for more information.

# copied from https://github.com/benoitc/gunicorn/commits/master#e77d47cb97

def paste_server(app, gcfg=None, host="127.0.0.1", port=None, *args, **kwargs):
    """\
    A paster server.

    Then entry point in your paster ini file should looks like this:

    [server:main]
    use = egg:gunicorn#main
    host = 127.0.0.1
    port = 5000

    """
    import os, pprint
    pprint.pprint(os.environ)
    from gunicorn.app.pasterapp import PasterServerApplication
    PasterServerApplication(app, gcfg=gcfg, host=host, port=port, *args, **kwargs).run()
