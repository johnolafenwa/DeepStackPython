from deepstack_sdk import ServerConfig, Face

config = ServerConfig("http://localhost:89")
face = Face(config)

response = face.detectFace("image.jpg",output="image_output.jpg")

for obj in response:
    print("Face Detected, Confidence: {}".format(obj.confidence))

"""

:: face.detectFace()

--- Available Paramaters ---

- image (file, numpy array, PIL Image, image bytes, url)
- format (jpg, png)
- min_confidence (0.1 to 1.0)
- callback (function name, parses in image_byte [without label and boxes] and detections into the function)
- output (file path of none if you don't want to save to file)
- output_font (cv2 font)
- output_font_color ( r, g, b )
"""