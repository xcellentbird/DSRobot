import os

datadir = './Learning_dataset'

files = os.listdir(datadir)
categories=[]
path = 'C:/Yolo_v4/darknet/build/darknet/x64/dsrobot_food_data/Learning_dataset/'
for i in files:
    categories.append(path+i)

files=list(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1  or x.find('.PNG') != -1 or x.find('.JPG') != -1, categories))

print(files)

filePath = './food_training.txt'

with open(filePath, 'w+') as lf:
    lf.write('\n'.join(files))



datadir = './Valid_dataset'

files = os.listdir(datadir)
categories=[]
path = 'C:/Yolo_v4/darknet/build/darknet/x64/dsrobot_food_data/Valid_dataset/'
for i in files:
    categories.append(path+i)

files=list(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1  or x.find('.PNG') != -1 or x.find('.JPG') != -1, categories))

print(files)

filePath = './food_testing.txt'

with open(filePath, 'w+') as lf:
    lf.write('\n'.join(files))
