class SceneResponse(object):
    def __init__(self,data):
        self.label = data["label"]
        self.confidence = data["confidence"]