from deepstack_sdk import ServerConfig, Enhance

config = ServerConfig("http://localhost:80")
enhancer = Enhance(config)

pil_image = Image.open("sky.jpg")
response = enhancer.enhanceObject(pil_image,output="sky-4X.jpg")

for obj in response:
    print("Base64: {}, width: {}, height: {}".format(obj.base64, obj.width, obj.height))