from deepstack_sdk import ServerConfig, Detection
from PIL import Image

config = ServerConfig("http://localhost:80")
detection = Detection(config)

pil_image = Image.open("image.jpg")
response = detection.detectObject(pil_image,output="image_output.jpg")

for obj in response:
    print("Name: {}, Confidence: {}, x_min: {}, y_min: {}, x_max: {}, y_max: {}".format(obj.label, obj.confidence, obj.x_min, obj.y_min, obj.x_max, obj.y_max))