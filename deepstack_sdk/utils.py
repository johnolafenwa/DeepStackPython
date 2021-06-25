import io
from PIL import Image
import cv2
import numpy
import os 

def printError(message):
    print(message,file=os.stderr)

def pilToBytes(image: Image,format: str="jpeg"):
    if format == "jpg":
        format = "jpeg"
    buf = io.BytesIO()
    image.save(buf,format=format)
    return buf.getvalue()

def cv2ToBytes(image: numpy.ndarray, format: str="jpg"):
    success, im_buffer = cv2.imencode("."+format,image)
    if not success:
        raise Exception("failed to convert numpy array to image")
    return im_buffer.tobytes()

def bytesToPIL(image_data):
    return Image.open(io.BytesIO(image_data))
    
def bytestoCV2(image_data):
    np_arr = numpy.asarray(bytearray(image_data),dtype=numpy.uint8)
    return cv2.imdecode(np_arr,cv2.IMREAD_COLOR)

def frameTracker(log, frame_count):
    if log:
        print("Frame {} processed".format(frame_count))