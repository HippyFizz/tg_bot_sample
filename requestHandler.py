import tornado.web
import telebot
from botLogic import bot


class webhook_serv(tornado.web.RequestHandler):
    def post(self):
        if "Content-Length" in self.request.headers and "Content-Type" in self.request.headers and self.request.headers['Content-Type'] == "application/json":
            # length = int(self.request.headers['Content-Length'])
            json_data = self.request.body.decode("utf-8")
            update = telebot.types.Update.de_json(json_data)
            bot.process_new_updates([update])
            self.write("")
            self.finish()
        else:
            self.write("What are you doing here?")
            self.set_status(400)
            self.finish()
