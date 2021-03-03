from deepstack_sdk import ServerConfig, Face

config = ServerConfig("http://localhost:80")
face = Face(config)

images = ["face_image1.jpg","face_image12.jpg", "face_image3.jpg", "face_imageN.jpg"]
response = face.registerFace(images=images,userid="Moses")
print(response)

"""
:: face.registerFace()

--- Available Paramaters

- images (a list of file path, numpy array, PIL Image, image bytes, url)
- format (jpg, png)
- user_id
"""