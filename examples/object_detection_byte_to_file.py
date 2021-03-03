from deepstack_sdk import ServerConfig, Detection

config = ServerConfig("http://localhost:89")
detection = Detection(config)

image_byte = open("image.jpg", "rb").read()
response = detection.detectObject(image_byte,output="image_output.jpg")

for obj in response:
    print("Name: {}, Confidence: {}".format(obj.label, obj.confidence))