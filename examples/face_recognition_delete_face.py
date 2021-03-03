from deepstack_sdk import ServerConfig, Face

config = ServerConfig("http://localhost:80")
face = Face(config)

response = face.deleteFace("Thanos")
print(response)