from PIL import Image
from deepstack import SceneRecognition,ServerConfig, displayResponse
import cv2 

img = Image.open(r"C:\Users\johnolafenwa\Documents\AI\DeepStackPython\tests\images\scene.jpg")
#print(type(img))
    
config = ServerConfig("http://localhost:89")
scene = SceneRecognition(config)

def c(image_data,res):
    print("from callback",res.label)

res = scene.processImage(r"C:\Users\johnolafenwa\Documents\AI\DeepStackPython\tests\images\scene.jpg",callback=c)
displayResponse(r"C:\Users\johnolafenwa\Documents\AI\DeepStackPython\tests\images\scene.jpg",res)

scene.processVideo(r"C:\Users\johnolafenwa\Videos\2020-12-16-15-00-14.flv",output="out6.mp4",display=True,callback=c)

v = cv2.VideoCapture("out6.mp4")

totalframecount= int(v.get(cv2.CAP_PROP_FRAME_COUNT))

print(totalframecount)



