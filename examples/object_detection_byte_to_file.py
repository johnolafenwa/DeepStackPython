from deepstack_sdk import ServerConfig, Detection

config = ServerConfig("http://localhost:80")
detection = Detection(config)

image_byte = open("image.jpg", "rb").read()
response = detection.detectObject(image_byte,output="image_output.jpg")

for obj in response:
    print("Name: {}, Confidence: {}, x_min: {}, y_min: {}, x_max: {}, y_max: {}".format(obj.label, obj.confidence, obj.x_min, obj.y_min, obj.x_max, obj.y_max))