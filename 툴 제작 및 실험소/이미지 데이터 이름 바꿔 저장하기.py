import os
import cv2
import numpy as np

# 바탕화면 절대 경로
desktop = "C:/Users/USER/Desktop/"
fn = ["Tang-su-yuk", "Jjam-bbong", "Jja-jang-myeon"] # 불러올 이미지 데이터 담긴 폴더들

# imread 한글 경로 처리 함수
def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None

# 폴더 내의 이미지 이름들을 모두 담는다
folders = []
folders.append(os.listdir(desktop+fn[0]))
folders.append(os.listdir(desktop+fn[1]))
folders.append(os.listdir(desktop+fn[2]))

# 새로 저장할 폴더
new_folder = "C:/Users/USER\Desktop/food_dataset/"
cnt = 1
for i, folder in enumerate(folders):
    n = desktop + fn[i] + "/"
    print(n)
    for img_name in folder:
        try:
            img = imread(n + img_name) # 이미지를 읽고
            cv2.imwrite(new_folder+str(cnt)+".jpg", img) # 숫자를 이름으로 하여 저장
            cnt+=1
        except:
            print("Didn't saved",fn[i],"-",img_name)
