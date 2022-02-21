from deepstack_sdk import ServerConfig, Enhance
import cv2

config = ServerConfig("http://localhost:80")
enhancer = Enhance(config)

cv2_image = cv2.imread("sky.jpg")
response = enhancer.enhanceObject(cv2_image, output="sky-4X.jpg")

for obj in response:
    print("Base64: {}, width: {}, height: {}".format(obj.base64, obj.width, obj.height))
