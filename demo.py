# from deepstack_sdk import ServerConfig, Detection

# config = ServerConfig("http://localhost:80")
# detection = Detection(config)

# response = detection.detectObject("image.jpg",output="image_output.jpg", show_label=True, draw_bounding_box=True, show_conf=False)

# for obj in response:
#    print("Name: {}, Confidence: {}, x_min: {}, y_min: {}, x_max: {}, y_max: {}"\
#     .format(obj.label, obj.confidence, obj.x_min, obj.y_min, obj.x_max, obj.y_max))

from deepstack_sdk import ServerConfig, Detection

config = ServerConfig("http://localhost:80")
detection = Detection(config)

detection.detectObjectVideo("video.mp4",output="video_output.mp4",show_label=True, draw_bounding_box=True, show_conf=False)