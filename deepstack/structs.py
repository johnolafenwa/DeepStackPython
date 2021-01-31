class SceneResponse(object):
    def __init__(self,data):
        self.label = data["label"]
        self.confidence = data["confidence"]
  
class DetectionResponseItem(object):
    def __init__(self,data):
        self.x_max = data["x_max"]
        self.x_min = data["x_min"]
        self.y_min = data["y_min"]
        self.y_max = data["y_max"]
        self.confidence = data["confidence"]
        self.label = data["label"]

class DetectionResponse(object):
    def __init__(self,data):
        predictions = data["predictions"]
        self.detections = [DetectionResponseItem(obj) for obj in predictions]
    def __getitem__(self,index):
        return self.detections[index]
    def __len__(self):
        return len(self.detections)
