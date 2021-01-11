# Face Recognition and Detection
**Face detection** is based on 68 face landmark points. Landmarks like eye brows, lips, nose, mouth like that. If these landmark points matches with landmark of general face, then that can be considered as a face. But **Face recognition** relies on 128 points or 128 numbers called as face embeddings and these embeddings are used to compare our face with what we already have i.e. the embeddings that we already have in the database.

## Prerequisites
**Cmake (Cross Platform Make)** :- It is a free and open-source software tool for building software using a compiler-independent method.We use cmake to compile and install Dlib Library.<br />
**Numpy**<br/>
**OpenCV** :- It is a library of programming functions mainly aimed at real-time computer vision.<br />
**Dlib** :- Dlib is a C++ toolkit containing machine learning algorithms and tools.We will use dlib for face-detection and facial landmark detection.The frontal face in dlib is simple,fast and powerful.<br />
**face_recognition** :- It recognize faces from python or from the command line.Built using dlib's face recognition feature.Bulit with deep learning model with accuracy of 99.38%.<br />
**Pillow** :- Python Image Library<br />

## Installation
* Install Cmake via anaconda: `pip install cmake`<br />
* Install Numpy via anaconda: `pip install numpy`<br />
* Install OpenCV via anaconda: `pip install opencv-python`<br />
* Install Dlib via anaconda: `pip install dlib`<br />
* Install face-recognition via anaconda: `pip install face-recognition`<br />
* Install Pillow via anaconda: `pip install Pillow`<br />
