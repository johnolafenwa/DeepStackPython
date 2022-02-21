from deepstack_sdk import ServerConfig, Enhance

config = ServerConfig("http://localhost:80")
enhancer = Enhance(config)

response = enhancer.enhanceObject("sky.jpg", output="sky-4X.jpg")

for obj in response:
    print("Base64: {}, width: {}, height: {}".format(obj.base64, obj.width, obj.height))
