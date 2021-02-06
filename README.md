# DeepStackPython
Official Python SDK for DeepStack

![DevTest](https://github.com/johnolafenwa/DeepStackPython/workflows/DevTest/badge.svg)

# DeepStack
[DeepStack](https://deepstack.cc) is an AI server that allows deploying object detection, face detection, face recognition, scene recognition and detection of custom objects on the edge and in production servers. 
DeepStack Runs on Docker, Windows, Linux, Mac, Nvidia Jetson and ARM64 devices.
And it is entirely free and Open Source 

The DeepStack Python SDK makes it easy to perform all of the above awesome AI magic on Images and Videos in few lines of code,
Just Install DeepStack and the Python SDK and you are good to go!

# Object Detection Sample

![object detection](examples/detection.jpg)

```python
from deepstack_sdk import ServerConfig, Detection

config = ServerConfig("http://localhost:80")
detection = Detection(config)

response = detection.detectObject("detection.jpg",output="detection_output.jpg")

```

![object detection output](examples/detection_output.jpg)

# Installation Instructions

## Install DeepStack on Windows
You can install DeepStack via docker on windows, note that this does not support GPU acceleration

```docker pull deepquestai/deepstack:cpu-2021.02.1```

You can also install the Native Windows Version of DeepStack, this supports GPU acceleration

#### CPU Version
Download and run [DeepStack CPU Installer](https://github.com/johnolafenwa/DeepStack/releases/download/0.2-beta/DeepStack-Installer-CPU.2021.01.beta.exe)

### GPU Version
- Download and Install CUDA 10.1 from here https://developer.nvidia.com/cuda-10.1-download-archive-base
- Download and install Cudnn from here https://developer.nvidia.com/cudnn'
- Download and run [DeepStack GPU Installer](https://github.com/johnolafenwa/DeepStack/releases/download/0.2-beta/DeepStack-Installer-GPU.2021.01.beta.exe)

## Install DeepStack on Linux
Linux Support is via Docker, hence you must install docker first

```sudo apt-get update && sudo apt-get install docker.io```

### CPU Version
```sudo docker pull deepquestai/deepstack:cpu-2021.02.1```

### GPU Version
```sudo docker pull deepquestai/deepstack:gpu-2021.02.1```

## Install DeepStack on MacOS
MacOS support is via Docker, install docker on Mac and run

```sudo docker pull deepquestai/deepstack:cpu-2020.02.1```
Note that GPU acceleration is not available for Mac at the moment

## Install DeepStack on Nvidia Jetson
```sudo docker pull deepquestai/deepstack:jetpack-2021.02.1```

## Install DeepStack on ARM64 Devices
```sudo docker pull deepquestai/deepstack:arm64-2021.02.1```

# Install DeepStack Python SDK
```pip3 install deepstack-sdk```

# Examples

## Object Detection

## Start DeepStack
To use the Object Detection API, start DeepStack with the command appropriate for your platform as below.

### On Windows Native Version CPU and GPU

```deepstack --VISION-DETECTION True --PORT 80```

### On Docker CPU Version

```sudo docker run -e VISION-DETECTION=True -v localstorage:/datastore -p 80:5000 deepquestai/deepstack:cpu-2021.02.1```

### On Docker GPU Version

```sudo docker run --gpus all -e VISION-DETECTION=True -v localstorage:/datastore -p 80:5000 deepquestai/deepstack:gpu-2021.02.1```

### On Nvidia Jetson

```sudo docker run --runtime nvidia -e VISION-DETECTION=True -v localstorage:/datastore -p 80:5000 deepquestai/deepstack:jetpack-2021.02.1```

### On ARM64 Devices

```sudo docker run -e VISION-DETECTION=True -v localstorage:/datastore -p 80:5000 deepquestai/deepstack:arm64-2021.02.1```

## Object Detection in Images
![object detection](examples/detection.jpg)

```python
from deepstack_sdk import Detection,ServerConfig

config = ServerConfig("http://localhost:80")
detector = Detection(config=config)

detections = detector.detectObject("detection.jpg",output="detection_output.jpg")

for detection in detections:
    print("Name: {}".format(detection.label))
    print("Confidence: {}".format(detection.confidence))
    print("x_min: {}".format(detection.x_min))
    print("x_max: {}".format(detection.x_max))
    print("y_min: {}".format(detection.y_min))
    print("y_max: {}".format(detection.y_max))
    print("-----------------------")
```

![object detection output](examples/detection_output.jpg)

<pre>
Name: dog
Confidence: 0.90205514
x_min: 650
x_max: 792
y_min: 348
y_max: 539
-----------------------
Name: person
Confidence: 0.9278088
x_min: 443
x_max: 606
y_min: 114
y_max: 522
-----------------------
Name: person
Confidence: 0.95218855
x_min: 295
x_max: 442
y_min: 83
y_max: 520
-----------------------
</pre>




 

    
