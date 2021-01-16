import os
import random
import cv2

dataset = [f for f in os.listdir(os.getcwd()) if ('.txt' in f or '.jpg' in f) and len(f) < 9]
img_datas = [f for f in dataset if '.jpg' in f]
txt_datas = [f for f in dataset if '.txt' in f]

valid_per = 0.2
num_valid = int(len(img_datas) * valid_per)
num_learning = len(img_datas) - num_valid

valid_img_datas = random.sample(img_datas, num_valid)
learning_img_datas = [img for img in img_datas if img not in valid_img_datas]

valid_data_names = [img.split('.')[0] for img in valid_img_datas]

valid_txt_datas = [ txt for txt in txt_datas if txt.split('.')[0] in valid_data_names]
learning_txt_datas = [txt for txt in txt_datas if txt not in valid_txt_datas]


now = os.getcwd()
# valid
valid_folder = now + "\\Valid_dataset\\"
for img in valid_img_datas:
    tmp = cv2.imread(img)
    cv2.imwrite(valid_folder + img, tmp)

for txt in valid_txt_datas:
    content = []
    with open(txt, mode='r') as f:
        content = f.readlines()
    with open(valid_folder + txt, mode='w') as f:
        f.writelines(content)

# learning
learning_folder = now + "\\Learning_dataset\\"
for img in learning_img_datas:
    tmp = cv2.imread(img)
    cv2.imwrite(learning_folder + img, tmp)

for txt in learning_txt_datas:
    content = []
    with open(txt, mode='r') as f:
        content = f.readlines()
    with open(learning_folder + txt, mode='w') as f:
        f.writelines(content)
