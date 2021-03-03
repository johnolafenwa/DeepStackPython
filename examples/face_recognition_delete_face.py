from deepstack_sdk import ServerConfig, Face

config = ServerConfig("http://localhost:89")
face = Face(config)

response = face.deleteFace("Thanos")
print(response)