from deepstack_sdk import ServerConfig, Detection

config = ServerConfig("http://localhost:80")
detection = Detection(config)

response = detection.detectObject("https://miro.medium.com/max/3600/1*J1L3J2SYyBiDQeEOY8KLLQ.jpeg",output="output.jpg")

for obj in response:
    print("Name: {}, Confidence: {}, x_min: {}, y_min: {}, x_max: {}, y_max: {}".format(obj.label, obj.confidence, obj.x_min, obj.y_min, obj.x_max, obj.y_max))