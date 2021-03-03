from deepstack_sdk import ServerConfig, Detection
import cv2

config = ServerConfig("http://localhost:89")
detection = Detection(config)

cv2_image = cv2.imread("image.jpg");
response = detection.detectObject(cv2_image,output="image_output.jpg")

for obj in response:
    print("Name: {}, Confidence: {}".format(obj.label, obj.confidence))