import os
import tornado.httpserver
import tornado.ioloop
import tornado.wsgi
import sys

def paste_server(app, gcfg=None, host="127.0.0.1", port=None, *args, **kwargs):
    """
    A paster server.

    Then entry point in your paster ini file should looks like this:

    [server:main]
    use = egg:galaxyservers#tornado
    host = 127.0.0.1
    port = 5000

    """
    container = tornado.wsgi.WSGIContainer(app)
    http_server = tornado.httpserver.HTTPServer(container)
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
