# -*- coding: utf-8 -*-
"""

@author: Samantha
"""

import numpy as  np
import cv2
import os 

 
img_path = 'doggos/'
for images in os.listdir(img_path):
    print('_______________________', images, '________________________________')
    input_path = os.path.join(img_path, images)
    #img = load_img(input_path)
    img_to_detect = cv2.imread(input_path)
    img_height = img_to_detect.shape[0]
    img_width = img_to_detect.shape[1]
    
   
    img_blob = cv2.dnn.blobFromImage(img_to_detect, 0.003922, (608, 608), swapRB=True, crop=False)
    
    
    class_labels = ["person","bicycle","car","motorcycle","airplane","bus","train","truck","boat",
                    "trafficlight","firehydrant","stopsign","parkingmeter","bench","bird","cat",
                    "dog","horse","sheep","cow","elephant","bear","zebra","giraffe","backpack",
                    "umbrella","handbag","tie","suitcase","frisbee","skis","snowboard","sportsball",
                    "kite","baseballbat","baseballglove","skateboard","surfboard","tennisracket",
                    "bottle","wineglass","cup","fork","knife","spoon","bowl","banana","apple",
                    "sandwich","orange","broccoli","carrot","hotdog","pizza","donut","cake","chair",
                    "sofa","pottedplant","bed","diningtable","toilet","tvmonitor","laptop","mouse",
                    "remote","keyboard","cellphone","microwave","oven","toaster","sink","refrigerator",
                    "book","clock","vase","scissors","teddybear","hairdrier","toothbrush"]
    
   
    class_colors = ["0,255,0","0,0,255","255,0,0","255,255,0","0,255,255"]
    class_colors = [np.array(every_color.split(",")).astype("int") for every_color in class_colors]
    class_colors = np.array(class_colors)
    class_colors = np.tile(class_colors,(16,1))
    
    
    yolo_model = cv2.dnn.readNetFromDarknet('dataset/yolov3.cfg','dataset/yolov3.weights')
    
     
    yolo_layers = yolo_model.getLayerNames()
    yolo_output_layer = [yolo_layers[yolo_layer - 1] for yolo_layer in yolo_model.getUnconnectedOutLayers()]
    
    yolo_model.setInput(img_blob)
   
    obj_detection_layers = yolo_model.forward(yolo_output_layer)
    
    

    for object_detection_layer in obj_detection_layers:
    	
        for object_detection in object_detection_layer:
            
            
            all_scores = object_detection[5:]
            predicted_class_id = np.argmax(all_scores)
            prediction_confidence = all_scores[predicted_class_id]
        
            if prediction_confidence > 0.50:
                
                predicted_class_label = class_labels[predicted_class_id]
               
                bounding_box = object_detection[0:4] * np.array([img_width, img_height, img_width, img_height])
                (box_center_x_pt, box_center_y_pt, box_width, box_height) = bounding_box.astype("int")
                start_x_pt = int(box_center_x_pt - (box_width / 2))
                start_y_pt = int(box_center_y_pt - (box_height / 2))
                end_x_pt = start_x_pt + box_width
                end_y_pt = start_y_pt + box_height
                
               
                box_color = class_colors[predicted_class_id]
                
               
                box_color = [int(c) for c in box_color]
                
               
                predicted_class_label = "{}: {:.2f}%".format(predicted_class_label, prediction_confidence * 100)
                print("predicted object {}".format(predicted_class_label,))
                
               
                cv2.rectangle(img_to_detect, (start_x_pt, start_y_pt), (end_x_pt, end_y_pt), box_color, 3)
                cv2.putText(img_to_detect, predicted_class_label, (start_x_pt, start_y_pt-5), cv2.FONT_HERSHEY_SIMPLEX, 3, box_color, 2)
                cv2.imwrite('yolo-img/YOLO'+images+'.jpg', img_to_detect)









