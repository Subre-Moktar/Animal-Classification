# -*- coding: utf-8 -*-
"""Untitled30.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oXikTezyUMdcVqDbuCgxyAnLdUUcSbw0
"""



import os
import shlex
import shutil
import subprocess
from pytube import YouTube
import gradio as gr


curr = os.getcwd()
SAVE_PATH = os.path.join(curr,"temp")
VID_NAME = "temp.mp4"
print(curr)
def downloadAndDetect(link):
    print(SAVE_PATH)

    if os.path.exists(SAVE_PATH):
        try:
            shutil.rmtree(SAVE_PATH)
        except:
            print('Error3')

    try:
        yt = YouTube(link)
    except:
        print("Error")
    streams = yt.streams.filter(progressive=True).all()
    d_video = streams[-1]
    try:
        down = d_video.download(output_path=SAVE_PATH, filename = VID_NAME)
    except:
        print('Error2')

    # sanitized_title = ''.join(c if c.isalnum() else '_' for c in yt.title)
    command = f"python detect.py --weights best_200_epochs.pt --conf 0.2 --source {SAVE_PATH}\{VID_NAME} --device 0 --name animal_detect --project temp/detect"
    print(command)
    try:
        subprocess.run(command, shell=True, check=True)
    except:
        print('error4')

    outputVideo = f"temp\detect\\animal_detect\{VID_NAME}"
    OUTPUTVIDEO = os.path.join(curr, outputVideo)

    print(OUTPUTVIDEO)
    return OUTPUTVIDEO

ytDownload = gr.Interface(
    fn=downloadAndDetect,
    inputs=[gr.Textbox(label="Enter Video URL")],
    outputs=[gr.Video(label = "Video Downloaded")],
)

ytDownload.launch()

# Commented out IPython magic to ensure Python compatibility.
# %ls

# Commented out IPython magic to ensure Python compatibility.
# %cd yolov7/