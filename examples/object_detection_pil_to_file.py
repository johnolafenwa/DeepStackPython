from deepstack_sdk import ServerConfig, Detection
from PIL import Image

config = ServerConfig("http://localhost:89")
detection = Detection(config)

pil_image = Image.open("image.jpg")
response = detection.detectObject(pil_image,output="image_output.jpg")

for obj in response:
    print("Name: {}, Confidence: {}".format(obj.label, obj.confidence))