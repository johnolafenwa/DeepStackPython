from deepstack_sdk import ServerConfig, Enhance

config = ServerConfig("http://localhost:80")
enhancer = Enhance(config)

response = enhancer.enhanceObject("https://i.ibb.co/mSc8q3y/disney.jpg", output="disney_4X.jpg")

for obj in response:
    print("Base64: {}, width: {}, height: {}".format(obj.base84, obj.width, obj.height))
