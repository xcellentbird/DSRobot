import threading
import csv
import numpy as np
import pandas as pd
import sys
from food_recog import yolo4food
import time

jja = 'Jja-jang-myeon'
jjam = 'Jjam-bbong'
tang = 'Tang-su-yuk'
menu = [jja, jjam, tang]

def table2serve(food, csv_name='/home/dsnx/DSRobot/darknet/orders.csv'):
    data = pd.read_csv(csv_name, names=['table number', 'food'])
    flg = False
    table = 0
    data = data.values.tolist()
    l = []
    for i, row in enumerate(data):
        #print(row)
        if food in row:
            #print(food +" is in ",i,"th order")
            table = row[0]
            l.append(i)
            
            flg = True
            break
    if l:
        print(data[max(l)],"is out")
        del data[max(l)]

    if not flg:
        print(food + " is not in order!!")
        return -1
    
    data = pd.DataFrame(np.array(data))
    data.to_csv(csv_name, index=False, header=False)
    print("order updated")
    return table

if __name__=='__main__':
    yolo = yolo4food() # yolo init
    # cam_num=4, txt='food_out', showmode=False, writemode=False, detect_term = 5
    cam_thrd = threading.Thread(target=yolo.cam_on, args=(0, 'food_out.txt', True, False, 5))
    #order_thrd = threading.Thread(target=table2serve, args=(yolo.get_food(), 'orders.csv'))

    cam_thrd.start()
    #order_thrd.start()
    
    #print("key 'q' - exit")
    #print("menu: Jja-jang-myeon, Jjam-bbong, Tang-su-yuk")
    #print("menu input: ")
    while True:
        time.sleep(5)
        ipt = yolo.get_food()
        
        ipt = ipt.split()
        if ipt:
            ipt = ipt[0]
        else:
            continue
        
        if ipt == 'q':
            print("exit~")
        elif ipt not in menu:
            print(ipt,"is not", menu[0])
            print(ipt==menu[0])
            print(len(menu[0]), len(ipt))
            pass
            #print(ipt,"is not on the list")
        else:
            t2s = table2serve(ipt)
            if t2s == -1:
                print("There is no table ordered ",ipt)
            else:
                print(t2s," th table")