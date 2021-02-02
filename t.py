from deepstack import ServerConfig, Detection, SceneRecognition, drawResponse, saveResponse, Face

config = ServerConfig("http://localhost:89")
detection = Detection(config)
scene = SceneRecognition(config)
face = Face(config)

#res = detection.processImage(r"C:\Users\johnolafenwa\Documents\AI\DeepStackPython\tests\images\detection.jpg",output="det1.jpg")

#saveResponse(r"C:\Users\johnolafenwa\Documents\AI\DeepStackPython\tests\images\detection.jpg",res,"det.jpg")

#face.detectFaceVideo(r"C:\Users\johnolafenwa\Videos\2020-12-16-15-00-14.flv",display=True,output="facedetection2.mp4", min_confidence=0.3)
res = face.recognizeFace(r"C:\Users\johnolafenwa\Documents\AI\DeepStackPython\tests\images\adele2.jpg",output="fdet1.jpg")
print(res[0].userid)
#f0 = detections[0]

#print(f0.label)



#displayResponse(r"C:\Users\johnolafenwa\Documents\AI\DeepStackPython\tests\images\scene.jpg",res)

#scene.processVideo(r"C:\Users\johnolafenwa\Videos\2020-12-16-15-00-14.flv",output="out6.mp4",display=False,callback=c)

'''
v = cv2.VideoCapture(0)
frame_count = 0
totalframecount = int(v.get(cv2.CAP_PROP_FRAME_COUNT))

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
if int(major_ver)  < 3 :
    fps = v.get(cv2.cv.CV_CAP_PROP_FPS)
else :
    fps = v.get(cv2.CAP_PROP_FPS)
print(fps)
while v.isOpened():
    valid, frame = v.read()
    if valid:
        frame_count = frame_count + 1
    else:
        break

v.release()

duration = frame_count/fps

print(duration)
'''


