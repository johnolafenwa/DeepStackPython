from deepstack_sdk import Detection,ServerConfig

config = ServerConfig("http://localhost:80")
detector = Detection(config=config)

detections = detector.detectObject("detection.jpg",output="detection_output.jpg")

for detection in detections:
    print("Name: {}".format(detection.label))
    print("Confidence: {}".format(detection.confidence))
    print("x_min: {}".format(detection.x_min))
    print("x_max: {}".format(detection.x_max))
    print("y_min: {}".format(detection.y_min))
    print("y_max: {}".format(detection.y_max))
    print("-----------------------")