from deepstack_sdk import ServerConfig, SceneRecognition

config = ServerConfig("http://localhost:89")
scene = SceneRecognition(config)

response = scene.recognizeScene(r"scene_image.jpg")

print("Scene: {} , Confidence: {}".format(response.label, response.confidence))

"""
:: face.recognizeScene()

--- Available Paramaters

- image (file, numpy array, PIL Image, image bytes, url)
- format (jpg, png)
- callback (function name, parses in image_byte [without label and boxes] and detections into the function)
"""