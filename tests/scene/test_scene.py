from deepstack import SceneRecognition,ServerConfig

def test_scene_file():
    
    config = ServerConfig("http://localhost:89")
    scene = SceneRecognition(config)

    res = scene.processImage("image.jpg")
    
    assert res.label == "yard"

    res = scene.processImage("https://flowergardengirl.co.uk/wp-content/uploads/2017/07/Garden-Design-chelsea-screen-raised-beds-wonderful-planting-artificial-grass-olives-trees.jpg")

    assert res.label == "yard"

def test_scene_url():
    
    config = ServerConfig("http://localhost:89")
    scene = SceneRecognition(config)

    res = scene.processImage("https://flowergardengirl.co.uk/wp-content/uploads/2017/07/Garden-Design-chelsea-screen-raised-beds-wonderful-planting-artificial-grass-olives-trees.jpg")

    assert res.label == "yard"