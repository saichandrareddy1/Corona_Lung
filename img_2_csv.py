import numpy as np
import pandas as pd
import cv2
import os

class COVID_IMG(object):
    
    def __init__(self, path, label):
        self.path = path
        self.label = label
        
    def images_path(self):
        li_path = [img for img in os.listdir(self.path) if img.endswith(".jpg") or img.endswith(".png") or img.endswith(".jpeg")]
        #print(len(li_path))
        return li_path

    def img_read(self, li_path):
        img_values = []
        labels = []

        for img in li_path:
            img = cv2.imread(self.path+"/"+img)
            #print(img)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (224, 224))
            #print(img.shape)
            img = img.flatten().tolist()
            img_values.append(img)
            labels.append(self.label)
        #print(len(img_values), labels)
        return labels, img_values
    
    def matrix_to_csv(self, image_array, li, labels, val):
        data = {}
        
        for i in range(len(image_array)):
            data[li[i]] = image_array[i]
        #print(data)
        print(val)

        if val == "covid":
            print(val)
            data = pd.DataFrame(data=data)
            data.T.to_csv("corona.csv")
            data = pd.read_csv("corona.csv")
            data['labels'] = labels
            data.to_csv("final_corona.csv")
            print("corona")
            os.remove("corona.csv")
            
        elif val == "normal":
            print(val)
            data = pd.DataFrame(data=data)
            data.T.to_csv("normal.csv")
            data = pd.read_csv("normal.csv")
            data['labels'] = labels
            data.to_csv("final_normal.csv")
            print("Normal")
            os.remove("normal.csv")
        else:
            pass
        
label = ["covid", "normal"]
for j in range(len(label)):
    print(label[j])
    covid = COVID_IMG(path=os.getcwd()+"/dataset/"+label[j], label=label[j])
    li_path = covid.images_path()
    labels, img_values = covid.img_read(li_path)
    covid.matrix_to_csv(img_values, li_path, labels, label[j])

