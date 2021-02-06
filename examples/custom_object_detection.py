from deepstack_sdk import ServerConfig, Detection

config = ServerConfig("http://localhost:89")
detection = Detection(config)

response = detection.detectObject("detection.jpg",output="output_image.jpg")

for obj in response:
    print("Name: {}, Confidence: {}".format(obj.label, obj.confidence))