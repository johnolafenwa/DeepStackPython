from deepstack_sdk import ServerConfig, SceneRecognition

config = ServerConfig("http://localhost:89")
scene = SceneRecognition(config)

response = scene.recognizeSceneVideo("video.mp4", output="scene.mp4")

"""
--- Available Paramaters

:: scene.recognizeSceneVideo("media/park.jpg",output="face_output.jpg")

- video (file, Camera video feed IP, integer for OpenCV Camera e.g 0, 1, 2)
- min_confidence (0.1 to 1.0)
- callback (function name, parses in image_byte [without label and boxes] and detections into the function)
- output (file path of none if you don't want to save to file)
- output_font (cv2 font)
- output_font_color ( r, g, b )
"""