from deepstack_sdk import ServerConfig, Enhance

config = ServerConfig("http://localhost:80")
enhancer = Enhance(config)

pil_image = Image.open("supermarket.jpg")
response = enhancer.enhanceObject(pil_image,output="supermarket_4X.jpg")

for obj in response:
    print("Base64: {}, width: {}, height: {}".format(obj.base64, obj.width, obj.height))