import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import signal

from config.options import mainOptions

from requestHandler import webhook_serv

WEBHOOK_CERT = mainOptions.cert
WEBHOOK_PKEY = mainOptions.key
WEBHOOK_HOST = mainOptions.host
WEBHOOK_SECRET = mainOptions.secret
WEBHOOK_PORT = mainOptions.port
WEBHOOK_URL_BASE = mainOptions.getWebhookUrlBase()

# openssl genrsa -out pkey.pem 2048
# openssl req -new -x509 -days 3650 -key pkey.pem -out cert.pem
#
# When asked for "Common Name (e.g. server FQDN or YOUR name)" you should reply
# with the same value in you put in WEBHOOK_HOST

tornado.options.define("port", default=WEBHOOK_PORT,
                       help="run on the given port", type=int)

is_closing = False


def signal_handler(signum, frame):
    global is_closing
    print("Exiting...")
    is_closing = True


def try_exit():
    global is_closing
    if is_closing:
        tornado.ioloop.IOLoop.instance().stop()
        print("Exit success!")


tornado.options.options.logging = None
tornado.options.parse_command_line()
signal.signal(signal.SIGINT, signal_handler)

application = tornado.web.Application([
    (r"/" + WEBHOOK_SECRET, webhook_serv)
])

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application, ssl_options={
        "certfile": WEBHOOK_CERT,
        "keyfile": WEBHOOK_PKEY,
    })
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.PeriodicCallback(try_exit, 100).start()
    tornado.ioloop.IOLoop.instance().start()
