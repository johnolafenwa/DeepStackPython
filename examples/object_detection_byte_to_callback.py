from deepstack_sdk import ServerConfig, Detection


def detection_callback(input_image_byte, detection_result):
    # Get detected image byte and save
    with open("detected_image.jpg", "wb") as writer:
        writer.write(input_image_byte)
    
    # Process detection result
    for obj in detection_result:
        print("Name: {}, Confidence: {}, x_min: {}, y_min: {}, x_max: {}, y_max: {}".format(obj.label, obj.confidence, obj.x_min, obj.y_min, obj.x_max, obj.y_max))

    # You can do other stuffs with the image and the detection results in this function
    

config = ServerConfig("http://localhost:80")
detection = Detection(config)

image_byte = open("image.jpg", "rb").read()
response = detection.detectObject(image_byte, callback=detection_callback)