class ServerConfig(object):
    def __init__(self,server_url: str,api_key: str=None,admin_key: str=None):
        self.server_url = server_url
        if not self.server_url.endswith("/"):
            self.server_url = self.server_url+"/"
        self.api_key = api_key
        self.admin_key = admin_key