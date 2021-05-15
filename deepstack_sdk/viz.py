import cv2
import matplotlib.pyplot as plt 
from .structs import SceneResponse, DetectionResponse, FaceDetectionResponse, FaceRecognitionResponse
from .utils import bytestoCV2
from PIL import Image
import numpy

def saveResponse(image,response,output,show_label,draw_bounding_box, show_conf, output_font=cv2.FONT_HERSHEY_SIMPLEX,output_font_color=(0,146,224)):
    frame = drawResponse(image,response, show_label, draw_bounding_box, show_conf, output_font,output_font_color)
    cv2.imwrite(output,frame)

def drawResponse(image,response, show_label=True, draw_bounding_box=True, show_conf=True, output_font=cv2.FONT_HERSHEY_SIMPLEX,output_font_color=(0,146,224)):
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
    
    output_font_scale = 0.8e-3 * image_arr.shape[0]

    if isinstance(response,SceneResponse):
        image_arr = cv2.putText(
                        image_arr,
                        response.label + " ( " + str(response.confidence)+"% )",
                        (20,20),
                        output_font,
                        output_font_scale,
                        output_font_color,
                        2
                        )
    if isinstance(response,DetectionResponse) or isinstance(response,FaceDetectionResponse) or isinstance(response,FaceRecognitionResponse):
        for obj in response:
            if draw_bounding_box:
                image_arr = cv2.rectangle(
                    image_arr,
                    (obj.x_min, obj.y_min),
                    (obj.x_max, obj.y_max),
                    output_font_color,
                    2
                )
            if isinstance(response,DetectionResponse) or isinstance(response,FaceRecognitionResponse):
                if isinstance(response,DetectionResponse):
                    txt = obj.label
                elif isinstance(response,FaceRecognitionResponse):
                    txt = obj.userid

                image_arr = cv2.putText(
                    img=image_arr,
                    text=(txt + (" ( " + str(100*(obj.confidence))+"% )" if show_conf else '' ))if show_label else None,
                    org=(obj.x_min-10, obj.y_min-10),
                    fontFace=output_font,
                    fontScale=output_font_scale,
                    color=output_font_color,
                    thickness=2
                )
            
    return image_arr
