from deepstack_sdk import ServerConfig, Detection


def detection_callback(input_image_byte, detection_result):
    # Get detected image byte and save
    with open("detected_image.jpg", "wb") as writer:
        writer.write(input_image_byte)
    
    # Process detection result
    for obj in detection_result:
        print("Name: {}, Confidence: {}".format(obj.label, obj.confidence))

    # You can do other stuffs with the image and the detection results in this function
    

config = ServerConfig("http://localhost:89")
detection = Detection(config)

image_byte = open("image.jpg", "rb").read()
response = detection.detectObject(image_byte, callback=detection_callback)