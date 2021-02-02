from deepstack import ServerConfig, Detection, SceneRecognition, drawResponse, saveResponse, Face
import json

config = ServerConfig("http://localhost:89")
detection = Detection(config)

response = detection.detectObject(r"C:\Users\johnolafenwa\Documents\AI\DeepStackPython\tests\data\detection.jpg","output.jpg")

for obj in response:
    print("Name: {}, Confidence: {}".format(obj.label, obj.confidence))