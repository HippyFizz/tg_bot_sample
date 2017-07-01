from configparser import RawConfigParser

configuration = RawConfigParser()
configuration.read("./config/configuration.ini")


class Options:
    token = None
    cert = None
    key = None
    host = None
    secret = None
    port = None

    def __init__(self):
        self.getBotToken()
        self.getWebhookCert()
        self.getWebhookKey()
        self.getWebhookHost()
        self.getWebhookSecret()
        self.getWebhookPort()
        
        self.test()

    def getBotToken(self, from_file=True):
        if from_file and not self.token:
            self.token = configuration.get("Telegram", "token")

    def getWebhookCert(self, from_file=True):
        if from_file and not self.cert:
            self.cert = configuration.get("Webhook", "cert")

    def getWebhookKey(self, from_file=True):
        if from_file and not self.key:
            self.key = configuration.get("Webhook", "key")

    def getWebhookHost(self, from_file=True):
        if from_file and not self.host:
            self.host = configuration.get("Webhook", "host")

    def getWebhookSecret(self, from_file=True):
        if from_file and not self.secret:
            self.secret = configuration.get("Webhook", "secret")

    def getWebhookPort(self, from_file=True):
        if from_file and not self.port:
            self.port = configuration.get("Webhook", "port")

    def getWebhookUrlBase(self, from_file=True):
        if not self.host:
            self.getWebhookHost()
        if not self.port:
            self.getWebhookPort()
        if not self.secret:
            self.getWebhookSecret()

        if from_file and self.host and self.port and self.secret:
            return "https://{0}:{1}/{2}".format(self.host, str(self.port), self.secret)

    def test(self):
        if self.token == None:
            raise "Can't load token"
        if self.cert == None:
            raise "Can't load cert path"
        if self.key == None:
            raise "Can't load key path"
        if self.host == None:
            raise "Can't load host"
        if self.secret == None:
            raise "Can't load secret"
        if self.port == None:
            raise "Can't load port"


mainOptions = Options()
