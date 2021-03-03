from deepstack_sdk import ServerConfig, Detection
import cv2

config = ServerConfig("http://localhost:80")
detection = Detection(config)

cv2_image = cv2.imread("image.jpg");
response = detection.detectObject(cv2_image,output="image_output.jpg")

for obj in response:
    print("Name: {}, Confidence: {}, x_min: {}, y_min: {}, x_max: {}, y_max: {}".format(obj.label, obj.confidence, obj.x_min, obj.y_min, obj.x_max, obj.y_max))