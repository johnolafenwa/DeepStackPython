from deepstack_sdk import ServerConfig, Face

config = ServerConfig("http://localhost:89")
face = Face(config)

response = face.recognizeFaceVideo("video.mp4", output="webcam.mp4" )
print(response)

"""
:: face.recognizeFaceVideo()

--- Available Paramaters

- video (file, Camera video feed IP, integer for OpenCV Camera e.g 0, 1, 2)
- min_confidence (0.1 to 1.0)
- callback (function name, parses in image_byte [without label and boxes] and detections into the function)
- output (file path, cv2.VideoWriter)
- output_font (cv2 font)
- output_font_color ( r, g, b )
"""