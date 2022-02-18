from deepstack_sdk import Enhance, ServerConfig, pilToBytes
import os
import cv2
from PIL import Image

DEEPSTACK_URL = os.getenv("TEST_DEEPSTACK_URL")
IMAGES_DIR = os.getenv("TEST_DATA_DIR")
config = ServerConfig(DEEPSTACK_URL)


def test_enhance_file():
    enhance = Enhance(config)
    res = enhance.enhanceObject(os.path.join(IMAGES_DIR, "disney.png"))
    assert res["width"] == 172
    assert res["height"] == 172


def test_enhance_cv2():
    enhance = Enhance(config)
    img = cv2.imread(os.path.join(IMAGES_DIR, "disney.png"))
    res = enhance.enhanceObject(img)
    assert res["width"] == 172
    assert res["height"] == 172


def test_enhance_url():
    enhance = Enhance(config)
    res = enhance.enhanceObject("https://docs.deepstack.cc/_images/sky.jpg")
    assert res["width"] == 1840
    assert res["height"] == 1036


def test_enhance_pil():
    enhance = Enhance(config)
    img = Image.open(os.path.join(IMAGES_DIR, "disney.png"))
    res = enhance.enhanceObject(img)
    assert res["width"] == 172
    assert res["height"] == 172


def test_enhance_bytes():
    enhance = Enhance(config)
    img = Image.open(os.path.join(IMAGES_DIR, "disney.png"))
    img_data = pilToBytes(img)
    res = enhance.enhanceObject(img_data)
    assert res["width"] == 172
    assert res["height"] == 172
