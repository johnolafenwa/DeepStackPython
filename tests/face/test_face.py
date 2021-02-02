from deepstack import Face,ServerConfig,pilToBytes
import os
import cv2 
from PIL import Image
import time

DEEPSTACK_URL = os.getenv("TEST_DEEPSTACK_URL")
IMAGES_DIR = os.getenv("TEST_DATA_DIR")
config = ServerConfig(DEEPSTACK_URL)

def test_face_detection():
    face = Face(config)
    detections = face.detectFace(os.path.join(IMAGES_DIR,"face.jpg"))
    assert len(detections) == 4

def test_face_detection_video():
    face = Face(config)
    video = os.path.join(IMAGES_DIR,"video.mp4")

    res = face.detectFaceVideo(video,output="face.mp4")

    savedVid = cv2.VideoCapture("face.mp4")

    totalframecount= int(savedVid.get(cv2.CAP_PROP_FRAME_COUNT))

    assert totalframecount == 1193

def test_face_register():
    face = Face(config)
    assert face.registerFace([os.path.join(IMAGES_DIR,"adele1.jpg")], userid="Adele") == True
    assert face.registerFace([os.path.join(IMAGES_DIR,"idriselba.jpg")], userid="Idris Elba") == True
    assert face.registerFace([os.path.join(IMAGES_DIR,"perri.jpg")], userid="Christina Perri") == True
    assert face.registerFace([os.path.join(IMAGES_DIR,"tomcruise.jpg")], userid="Tom Cruise") == True
    assert face.registerFace([os.path.join(IMAGES_DIR,"bradley.jpg")], userid="Bradley Cooper") == True
    assert face.registerFace([os.path.join(IMAGES_DIR,"obama1.jpg")], userid="Barrack Obama") == True

    time.sleep(5)

    faces = face.listFaces()
    assert "Adele" in faces
    assert "Idris Elba" in faces
    assert "Christina Perri" in faces
    assert "Tom Cruise" in faces
    assert "Bradley Cooper" in faces
    assert "Barrack Obama" in faces

def test_face_recognition():
    time.sleep(10)
    face = Face(config)
    detections = face.recognizeFace(os.path.join(IMAGES_DIR,"adele2.jpg"))
    assert detections[0].userid == "Adele"

def test_face_recognition_video():
    face = Face(config)
    video = os.path.join(IMAGES_DIR,"video.mp4")

    res = face.recognizeFaceVideo(video,output="face2.mp4")

    savedVid = cv2.VideoCapture("face2.mp4")

    totalframecount= int(savedVid.get(cv2.CAP_PROP_FRAME_COUNT))

    assert totalframecount == 1193

def test_face_delete():
    face = Face(config)
    assert face.deleteFace("Tom Cruise")
    time.sleep(5)

    faces = face.listFaces()
    assert "Tom Cruise" not in faces