from PIL import Image
import cv2 
from .config import ServerConfig
from .utils import cv2ToBytes, pilToBytes, printError
from .structs import SceneResponse
import requests
import os
import validators
import numpy

class SceneRecognition(object):
    def __init__(self,config: ServerConfig):
        self.config = config

    def __process_image(self,image_data: bytes):
        response = requests.post(self.config.server_url+"v1/vision/scene",
        files={"image": image_data},
        data={"api_key": self.config.api_key}
        )

        return response

    #allow folder input, with exts param specifying comma separated exts
    def processImage(self, image,format="jpg", callback=None):
        if isinstance(image,str):
            if os.path.isfile(image):
                image_data = open(image,"rb").read()
            elif validators.url(image):
                image_data = requests.get(image).content
            else:
                raise Exception("file {} does not exist".format(image))
        elif isinstance(image,numpy.ndarray):
            image_data = cv2ToBytes(image,format=format)
        elif isinstance(image,Image.Image):
            image_data = pilToBytes(image,format=format)
        elif isinstance(image,bytes):
            image_data = image
        else:
            raise Exception("Unsupported input type: {}".format(type(image)))

        response = self.__process_image(image_data)

        if response.status_code == 200:
            data = SceneResponse(response.json())
            if callback is not None:
                callback(image_data,data)
            return data
        elif response.status_code == 403:
            raise Exception("The scene endpoint is not enabled on the DeepStack server")
        elif response.status_code == 400:
            raise Exception("Invalid image")
        elif response.status_code == 500:
            raise Exception("An error occured on the DeepStack server")
        else:
            raise Exception("Unknown error : {} occured".format(response.status_code))

    def processVideo(self,video,output=None,codec=cv2.VideoWriter_fourcc(*'mp4v'),fps=24,callback=None, continue_on_error=False,output_font=cv2.FONT_HERSHEY_SIMPLEX, output_pos=(50,50),output_font_scale=1,output_font_color=(0,0,255),output_line_type=cv2.LINE_4):
        if not isinstance(video,cv2.VideoCapture):
            video = cv2.VideoCapture(video)
        width  = video.get(3) 
        height = video.get(4)
        if output is not None:
            if isinstance(output,cv2.VideoWriter):
                out = output 
            else:   
                out = cv2.VideoWriter(output,codec,fps,((int(width), int(height))))
        
        while video.isOpened():
            valid, frame = video.read()
            if valid:
                frame_data = cv2ToBytes(frame)
                response = self.__process_image(frame_data)
                
                if response.status_code == 200:
                    data = SceneResponse(response.json())
                    if callback is not None:
                        callback(frame_data,data)
                   
                    if output is not None:
                        frame = cv2.putText(
                            frame,
                            data.label + " " + str(data.confidence),
                            output_pos,
                            output_font,
                            output_font_scale,
                            output_font_color,
                            output_line_type
                        )

                        out.write(frame)
                elif response.status_code == 403:
                    if continue_on_error:
                        printError("The scene endpoint is not enabled on the DeepStack server")
                    else:
                        raise Exception("The scene endpoint is not enabled on the DeepStack server")
                elif response.status_code == 400:
                    if continue_on_error:
                        printError("Invalid image")
                    else:
                        raise Exception("Invalid image")
                elif response.status_code == 500:
                    if continue_on_error:
                        printError("An error occured on the DeepStack server")
                    else:
                        raise Exception("An error occured on the DeepStack server")
                else:
                    if continue_on_error:
                        printError("Unknown error : {} occured".format(response.status_code))
                    else:
                        raise Exception("Unknown error : {} occured".format(response.status_code))
            else:
                break

        video.release()
        out.release()
                




        




        

