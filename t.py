from deepstack import ServerConfig, Detection, SceneRecognition

config = ServerConfig("http://localhost:89")
detection = Detection(config)
scene = SceneRecognition(config)

detections = detection.processVideo(r"C:\Users\johnolafenwa\Videos\2020-12-16-15-00-14.flv",min_confidence=0.7,display=True,output="detection.mp4")

f0 = detections[0]

print(f0.label)



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


