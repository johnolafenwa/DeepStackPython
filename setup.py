from setuptools import setup,find_packages

setup(name= "deepstack-sdk",
      version='0.1.1',
      description='DeepStack Python SDK',
      url="https://github.com/johnolafenwa/DeepStackPython",
      author='John Olafenwa and Moses Olafenwa',
      license='MIT',
      packages= find_packages(),
      install_requires=['pillow','scikit-image','opencv-python','matplotlib',"requests","pytest","validators"],
      zip_safe=False,
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
      )