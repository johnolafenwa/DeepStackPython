from PIL import Image
from deepstack import SceneRecognition,ServerConfig
import cv2 

img = Image.open(r"C:\Users\johnolafenwa\Documents\AI\DeepStackPython\tests\images\scene.jpg")
#print(type(img))
    
config = ServerConfig("http://localhost:89")
scene = SceneRecognition(config)

def c(image_data,res):
    print("from callback",res.label)

res = scene.processImage(r"C:\Users\johnolafenwa\Documents\AI\DeepStackPython\tests\images\scene.jpg",callback=c)

scene.processVideo(r"C:\Users\johnolafenwa\Documents\AI\DeepStackPython\tests\images\video.mp4",output="out6.mp4",callback=c)

v = cv2.VideoCapture("out6.mp4")

totalframecount= int(v.get(cv2.CAP_PROP_FRAME_COUNT))

print(totalframecount)



