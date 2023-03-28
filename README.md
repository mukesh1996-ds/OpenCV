# OpenCV

What is Computer vision ?

Computer vision is a field of artificial intelligence (AI) that enables computers and systems to derive meaningful information from digital images, videos and other visual inputs — and take actions or make recommendations based on that information. Lets consider a lovely example of computer vision: Imagine you are at a coffee shop and you need to order some coffee for your self but how will you order. You will try to call waiter for a coffee but how you mind will understand that he is a waiter by looking at his costume. This is how you mind will train by looking at the patterns and then perform actions related to it or make predictions.

Def: Computer vision is a process by which we can understand the images and videos how they are stored and how we can manipulate and retrieve data from them. Computer Vision is the base or mostly used for Artificial Intelligence. Computer-Vision is playing a major role in self-driving cars, robotics as well as in photo correction apps. 

What is openCV ?

* OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products.

* OpenCV is the huge open-source library for the computer vision, machine learning, and image processing and now it plays a major role in real-time operation which is very important in today’s systems. By using it, one can process images and videos to identify objects, faces, or even handwriting of a human. When it integrated with various libraries, such as NumPy, python is capable of processing the OpenCV array structure for analysis. To Identify image pattern and its various features we use vector space and perform mathematical operations on these features. 

Applications of OpenCV: There are lots of applications which are solved using OpenCV, some of them are listed below 

* Face recognition
* Automated inspection and surveillance
* number of people – count (foot traffic in a mall, etc)
* Vehicle counting on highways along with their speeds
* Interactive art installations
* Anomaly (defect) detection in the manufacturing process (the odd defective products)
* Street view image stitching
* Video/image search and retrieval
* Robot and driver-less car navigation and control
* object recognition
* Medical image analysis

### Image-Processing

Image processing is a method to perform some operations on an image, in order to get an enhanced image and or to extract some useful information from it. 
If we talk about the basic definition of image processing then “Image processing is the analysis and manipulation of a digitized image, especially in order to improve its quality”. 

### Digital-Image : 

An image may be defined as a two-dimensional function f(x, y), where x and y are spatial(plane) coordinates, and the amplitude of fat any pair of coordinates (x, y) is called the intensity or grey level of the image at that point. 
In another word An image is nothing more than a two-dimensional matrix (3-D in case of coloured images) which is defined by the mathematical function f(x, y) at any point is giving the pixel value at that point of an image, the pixel value describes how bright that pixel is, and what colour it should be. 
Image processing is basically signal processing in which input is an image and output is image or characteristics according to requirement associated with that image. 
Image processing basically includes the following three steps: 

1. Importing the image
2. Analysing and manipulating the image
3. Output in which result can be altered image or report that is based on image analysis

For example: You can identify the your own image by looking at it, But your machine cannot identify the image because The computer reads any image as a range of values between 0 and 255. For any color image, there are 3 primary channels -red, green and blue **(RBG)**.

> attached image here

In computer there are 2 different types of image processing:
1. Grayscale: It means that the image is black and white 
2. RGB: Colored images

> attached Image here

> Note: Our image processing is nothing but converting a image into metrics as computer can understand only numbers to perfrom this we wull be using NumPy module in python.

### NumPy:
* It is a highly optimized module for numerical operations.
* Array structure is important because digital images are 2D images in case of Black and White and 3D in case of RBG.
* All openCV array structures are converted to-and-from Numpy array.
* The major advantage of using NumPy is that you can use more convenient indexing system rather than using loops.

### Let's also install openCV module in local system

You need to open your terminal and then goto the following website https://pypi.org/project/opencv-python/
copy the command from there and just run in your terminal.

> pip install opencv-python

Once done with the installation you can check it in the terminal using python 
1. type python 
2. type import cv2 

if you don't get any errors then its properly installed.

### Code time

At the time when you read the image you will come to know about an attribute name flag. It is the mode in which the image is displayed. 
1. cv2.IMREAD_COLOR --> Numerical value is 1 --> used to read the color image
2. cv2.IMREAD_GRAYSCALE --> Numerical value is 0 --> load the image in gray scale format i.e. black and white
3. cv2.IMREAD_UNCHANGED -->  Numerical value is -1 --> load the image as such including alpha channel




