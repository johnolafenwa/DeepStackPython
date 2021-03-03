from deepstack_sdk import ServerConfig, Detection

config = ServerConfig("http://localhost:80")
detection = Detection(config)

response = detection.detectObject("image.jpg",output="image_output.jpg")

for obj in response:
    print("Name: {}, Confidence: {}, x_min: {}, y_min: {}, x_max: {}, y_max: {}".format(obj.label, obj.confidence, obj.x_min, obj.y_min, obj.x_max, obj.y_max))

"""
:: detection.detectObject()

--- Available Paramaters

- image (file, numpy array, PIL Image, image bytes, url)
- format (jpg, png)
- min_confidence (0.1 to 1.0)
- callback (function name, parses in image_byte [without label and boxes] and detections into the function)
- output (file path of none if you don't want to save to file)
- output_font (cv2 font)
- output_font_color ( r, g, b )
"""