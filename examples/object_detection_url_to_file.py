from deepstack_sdk import ServerConfig, Detection

config = ServerConfig("http://localhost:89")
detection = Detection(config)

response = detection.detectObject("https://miro.medium.com/max/3600/1*J1L3J2SYyBiDQeEOY8KLLQ.jpeg",output="output.jpg")

for obj in response:
    print("Name: {}, Confidence: {}".format(obj.label, obj.confidence))