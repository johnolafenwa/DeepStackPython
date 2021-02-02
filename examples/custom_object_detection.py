from deepstack import ServerConfig, Detection
import json

config = ServerConfig("http://localhost:80")
detection = Detection(config,"openlogo")

response = detection.detectObject("detection.jpg",output="output_image.jpg")

for obj in response:
    print("Name: {}, Confidence: {}".format(obj.label, obj.confidence))