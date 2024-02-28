# Animal-Classification
We will be training a model for animal classfication for video object detection. We will be using youtube videos to detect animals off of that video, with a front end development, so that the user just needs to paste the video link inside. A collaborative Project

We will be using the YOLOv7 model, with using youtube videos as the input, or personal videos

Steps:

Install python3.11

Install Virtual Environment

Install Dependinces from requirements.txt file

Git Clone yolov7 - https://github.com/WongKinYiu/yolov7 

There are other ways to get the model if needed

Test - (See if they can run the model off laptops using camera)

Collecting The images off of Kaggle - https://www.kaggle.com/datasets/iamsouravbanerjee/animal-image-dataset-90-different-animals.

Train and test the Model off of these images.

Use Pytube to have the model run on youtube videos / mp4 videos also

Create an interface so that people could interact with the model

  If possible also include time stamps of when the animal comes into view and when it leaves on the video.

upload the model

# Fine Tuning YOLO v7 on Custom Data Set
Link to see the code: https://colab.research.google.com/drive/18sYcWbWg431Vc78qZuyc8R9dGjCoOlx-?usp=sharing

The first code cell is to clone YOLOv7 and download all the necessary requirements into google colab

Next you want to change your runtime like so:

  -Click on the arrow next to Connect GPU
  ![image](https://github.com/Subre-Moktar/Animal-Classification/assets/106625128/30661786-49b0-40d1-bf6e-e7ecd3621e79)

  -Select Change Runtime Type > T4 GPU
  ![image](https://github.com/Subre-Moktar/Animal-Classification/assets/106625128/aff6fd04-f3b4-43d3-8c96-187945d63c8a)

  -Save Selection

The Second Cell will make sure that the right runtime in google colab is being used

Now you want to get your Roboflow API

  -Go to Roboflow Link:
  -https://roboflow.com

  -Sign in or Create an Account

  -Select Public Plan (Free) and name your workspace (You do not need to upload any data set or invite any friends)
  ![image](https://github.com/Subre-Moktar/Animal-Classification/assets/106625128/1c71f361-a177-4118-94c9-fd629e179930)

  -Click on the top right where the arrow is
  ![image](https://github.com/Subre-Moktar/Animal-Classification/assets/106625128/820ec41e-f95a-4854-9838-cb145bb8cc85)

  -Select Setting > Your Created Workspace > Roboflow API 
  -Copy Your private API but do not share this with anyone
  ![image](https://github.com/Subre-Moktar/Animal-Classification/assets/106625128/c13dcadc-c909-40b1-8e01-91262d05966b)

Run the Third Cell and paste your API

The Fourth Cell will install the proper dataset for fine tuning

The Fifth Cell will allow you to use transfer learning with the yolov7 model

The Sixth Cell is to train the model on your training data
  -We will go over the different parameters and how they affect training

The Seventh Cell is to run the new model on our test data

The Eighth Cell is to view the images with object detection bounding boxes


