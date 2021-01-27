from PIL import Image
import cv2 
from .config import ServerConfig
from .utils import cv2ToBytes, pilToBytes
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

    
    def processImage(self, image,format="jpg", callback=None):
        if isinstance(image,str):
            if os.path.isfile(image):
                image_data = open(image,"rb").read()
            elif validators.url(image):
                image_data = requests.get(image).content
            else:
                raise Exception("String input is neigther a file nor a url")
        elif isinstance(image,numpy.ndarray):
            image_data = cv2ToBytes(image,format=format)
        elif isinstance(image,Image):
            image_data = pilToBytes(image,format=format)
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



        

