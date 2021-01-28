from PIL import Image

from deepstack import SceneRecognition,ServerConfig

img = Image.open(r"C:\Users\johnolafenwa\Documents\AI\DeepStackPython\tests\images\scene.jpg")
print(type(img))
    
config = ServerConfig("http://localhost:89")
scene = SceneRecognition(config)

res = scene.processImage(r"C:\Users\johnolafenwa\Documents\AI\DeepStackPython\tests\scene\image.jpg")
print(res.label)

