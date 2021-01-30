import cv2
import matplotlib.pyplot as plt 
from .structs import SceneResponse
from .utils import bytestoCV2
from PIL import Image
import numpy

def displayResponse(image,response,output_font=cv2.FONT_HERSHEY_SIMPLEX, output_pos=(50,50),output_font_scale=5,output_font_color=(0,0,255),output_line_type=cv2.LINE_4):
    if isinstance(image,Image.Image):
        image_arr = numpy.array(image)
        image_arr = cv2.cvtColor(image_arr, cv2.cv.CV_BGR2RGB)
    elif isinstance(image,numpy.ndarray):
        image_arr = image
    elif isinstance(image,bytes):
        image_arr = bytestoCV2(image)
    elif isinstance(image,str):
        image_arr = cv2.imread(image)
    else:
        raise Exception("Unsuported input type: {}".format(type(image)))

    if isinstance(response,SceneResponse):
        image_arr = cv2.putText(
                        image_arr,
                        response.label + " " + str(response.confidence),
                        output_pos,
                        output_font,
                        output_font_scale,
                        output_font_color,
                        output_line_type
                        )

    image_arr = cv2.cvtColor(image_arr, cv2.COLOR_BGR2RGB)
    plt.imshow(image_arr)
    plt.show()

