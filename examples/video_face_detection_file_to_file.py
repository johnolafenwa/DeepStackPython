from deepstack_sdk import ServerConfig, Face

config = ServerConfig("http://localhost:89")
face = Face(config)

response = face.detectFaceVideo("video.mp4",output="face_detected.mp4")

for obj in response:
    print("Face Detected, Confidence: {}".format(obj.confidence))

"""
:: detection.detectFaceVideo()

--- Available Paramaters

- video (file, Camera video feed IP, integer for OpenCV Camera e.g 0, 1, 2)
- min_confidence (0.1 to 1.0)
- codec (Default: cv2.VideoWriter_fourcc(*'mp4v') )
- fps (frames per second)
- continue_on_error (Default: false)
- output (file path, cv2.VideoWriter)
- output_font (cv2 font)
- output_font_color ( r, g, b )
"""