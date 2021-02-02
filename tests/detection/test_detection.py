from deepstack import Detection,ServerConfig,pilToBytes
import os
import cv2 
from PIL import Image

DEEPSTACK_URL = os.getenv("TEST_DEEPSTACK_URL")
IMAGES_DIR = os.getenv("TEST_DATA_DIR")
config = ServerConfig(DEEPSTACK_URL)

def test_detection_file():
    
    detection = Detection(config)

    res = detection.detectObject(os.path.join(IMAGES_DIR,"detection.jpg"))
    
    assert len(res) == 3
    
def test_detection_url():
   
    
    detection = Detection(config)

    res = detection.detectObject("https://docs.deepstack.cc/_images/family-and-dog.jpg")

    assert len(res) == 3

def test_detection_cv2():

    detection = Detection(config)

    img = cv2.imread(os.path.join(IMAGES_DIR,"detection.jpg"))

    res = detection.detectObject(img)

    assert len(res) == 3

def test_detection_pil():

    detection = Detection(config)

    img = Image.open(os.path.join(IMAGES_DIR,"detection.jpg"))

    res = detection.detectObject(img)

    assert len(res) == 3

def test_detection_bytes():

    detection = Detection(config)

    img = Image.open(os.path.join(IMAGES_DIR,"detection.jpg"))

    img_data = pilToBytes(img)

    res = detection.detectObject(img_data)

    assert len(res) == 3

def test_detection_video():

    detection = Detection(config)

    video = os.path.join(IMAGES_DIR,"video.mp4")

    res = detection.detectObjectVideo(video,output="vid.mp4")

    savedVid = cv2.VideoCapture("vid.mp4")

    totalframecount= int(savedVid.get(cv2.CAP_PROP_FRAME_COUNT))

    assert totalframecount == 1193