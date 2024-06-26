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

**(1) Link to see the code: https://colab.research.google.com/drive/18sYcWbWg431Vc78qZuyc8R9dGjCoOlx-?usp=sharing**
</br></br>
**(2) The first code cell is to clone YOLOv7 and download all the necessary requirements into google colab**
</br></br>
**(3) Next you want to change your runtime like so:**
</br></br>
  &emsp;&emsp;-Click on the arrow next to Connect GPU</br>
    ![image](https://github.com/Subre-Moktar/Animal-Classification/assets/106625128/30661786-49b0-40d1-bf6e-e7ecd3621e79)
  
  &emsp;&emsp;-Select Change Runtime Type > T4 GPU</br>
    ![image](https://github.com/Subre-Moktar/Animal-Classification/assets/106625128/aff6fd04-f3b4-43d3-8c96-187945d63c8a)


  &emsp;&emsp;-Save Selection
</br></br>
**(4) The Second Cell will make sure that the right runtime in google colab is being used**
</br></br>
**(5) Now you want to get your Roboflow API**
</br></br>
  &emsp;&emsp;-Go to Roboflow Link: https://roboflow.com

  &emsp;&emsp;-Sign in or Create an Account

  &emsp;&emsp;-Select Public Plan (Free) and name your workspace (You do not need to upload any data set or invite any friends)</br>
  ![image](https://github.com/Subre-Moktar/Animal-Classification/assets/106625128/1c71f361-a177-4118-94c9-fd629e179930)

  &emsp;&emsp;-Click on the top right where the arrow is</br>
  ![image](https://github.com/Subre-Moktar/Animal-Classification/assets/106625128/820ec41e-f95a-4854-9838-cb145bb8cc85)

  &emsp;&emsp;-Select Setting > Your Created Workspace > Roboflow API </br>
  &emsp;&emsp;-Copy Your private API but do not share this with anyone</br>
  ![image](https://github.com/Subre-Moktar/Animal-Classification/assets/106625128/c13dcadc-c909-40b1-8e01-91262d05966b)
</br></br>
**(6) Run the Third Cell and paste your API**
</br></br>
**(7) The Fourth Cell will install the proper dataset for fine tuning**
</br></br>
**(8) The Fifth Cell will allow you to use transfer learning with the yolov7 model**
</br></br>
**(9) The Sixth Cell is to train the model on your training data**
</br></br>
  &emsp;&emsp;-We will go over the different parameters and how they affect training
</br></br>
**(10) The Seventh Cell is to run the new model on our test data**
</br></br>
**(11) The Eighth Cell is to view the images with object detection bounding boxes**



