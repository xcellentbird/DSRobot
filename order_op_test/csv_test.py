import csv
import pandas as pd

jja = 'Jja-jang-myoen'
jjam = 'Jjam-bbong'
tang = 'Tang-su-yuk'


    #for in range(len(data)):
        #writer.writerow(a)
def table2serve(food):
    tmp = []
    with open('order_list.csv','r', encoding='utf-8') as csv_rfile:
        reader = csv.reader(csv_rfile)
        tmp = list(reader)


    print("read: ",tmp)
    flg = False
    for i, row in enumerate(tmp):
        if food in row:
            print(food +" is in ",i," order")
            del tmp[i]
            flg = True
            break
    if not flg:
        print(food + " is not in order!!")
        return -1
    
    
    with open('order_list.csv','w', encoding='utf-8',newline='') as csv_wfile:
        writer = csv.writer(csv_wfile)
        print("write: ", tmp)
        writer.writerows(tmp)
        #for i in tmp:
            #writer.writerow(i)
    

table2serve(jja)
