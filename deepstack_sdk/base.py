

class Endpoint(object):
    def __init__(self,server_config: str):
        self.config = server_config
    
    def processImage(self,*args):
        return NotImplementedError()
    def processVideo(self,*args):
        return NotImplementedError()
    def processCamera(self, *args):
        return NotImplementedError()