# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 10:01:49 2022

@author: Samantha
"""

from keras.applications import ResNet50
from keras.applications import imagenet_utils
from tensorflow.keras.utils import img_to_array, load_img
import numpy as np
import cv2
import os
import pandas as pd
from PIL import Image

img_path = 'doggos/'
pred_obj = []
percent1 = []
for images in os.listdir(img_path):
    input_path = os.path.join(img_path, images)
    img = load_img(input_path)

    img = img.resize((224,224))
    img_array = img_to_array(img)
    
    
    img_array = np.expand_dims(img_array, axis = 0)
    
    img_array = imagenet_utils.preprocess_input(img_array)
    
    pretrained_model = ResNet50(weights="imagenet")
    
    prediction = pretrained_model.predict(img_array)
    
    actual_prediction = imagenet_utils.decode_predictions(prediction)
    
    print("Prepredicted object is:" + images)
    print(actual_prediction[0][0][1])
    print("With accuracy:")
    print(actual_prediction[0][0][2]*100)
    
    pred_obj.append(actual_prediction[0][0][1]) 
    percent1.append(actual_prediction[0][0][2]*100)
    
    disp_img = cv2.imread(input_path)
    disp_img = cv2.resize(disp_img, (1200,1200))
    cv2.putText(disp_img, actual_prediction[0][0][1], (20,20), cv2.FONT_HERSHEY_TRIPLEX, 0.8, (255,0,0))


    cv2.imwrite('resnet-img/RESNET'+images+'.jpg', disp_img)
    
    

data = {'Prediction': pred_obj, 'Accuracy': percent1}
df = pd.DataFrame(data)
df.to_excel('resnet_result.xlsx')




