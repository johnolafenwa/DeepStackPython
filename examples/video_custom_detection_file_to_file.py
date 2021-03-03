from deepstack_sdk import ServerConfig, Detection

config = ServerConfig("http://localhost:89")
detection = Detection(config, name="openlogo")

detection.detectObjectVideo("video.mp4",output="video_output.mp4")


"""
:: detection.detectObjectVideo()

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