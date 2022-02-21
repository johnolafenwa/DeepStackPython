from PIL import Image
from .config import ServerConfig
from .utils import cv2ToBytes, pilToBytes
from .structs import EnhanceResponse
import requests
import os
import validators
import numpy
import base64


class Enhance(object):
    def __init__(self, config: ServerConfig):
        self.config = config
        self.__endpoint = "v1/vision/enhance"

    def __process_image(self, image_data: bytes):
        response = requests.post(self.config.server_url + self.__endpoint,
                                 files={"image": image_data},
                                 data={"api_key": self.config.api_key}
                                 )

        return response

    # allow folder input, with exts param specifying comma separated exts
    def enhanceObject(self, image, format="jpg", output=None):
        if isinstance(image, str):
            if os.path.isfile(image):
                image_data = open(image, "rb").read()
            elif validators.url(image):
                image_data = requests.get(image).content
            else:
                raise Exception("file {} does not exist".format(image))
        elif isinstance(image, numpy.ndarray):
            image_data = cv2ToBytes(image, format=format)
        elif isinstance(image, Image.Image):
            image_data = pilToBytes(image, format=format)
        elif isinstance(image, bytes):
            image_data = image
        else:
            raise Exception("Unsupported input type: {}".format(type(image)))

        response = self.__process_image(image_data)

        if response.status_code == 200:
            data = EnhanceResponse(response.json())
            if output is not None:
                enhance_base64 = data["base64"]
                image4X_byte = base64.b64decode(enhance_base64)
                with open(output, 'wb') as f_output:
                    f_output.write(image4X_byte)

            return data
        elif response.status_code == 403:
            raise Exception("The scene endpoint is not enabled on the DeepStack server")
        elif response.status_code == 400:
            raise Exception("Invalid image")
        elif response.status_code == 500:
            raise Exception("An error occured on the DeepStack server")
        else:
            raise Exception("Unknown error : {} occured".format(response.status_code))
