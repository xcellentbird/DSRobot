import csv
import numpy as np
import pandas as pd

jja = 'Jja-jang-myeon'
jjam = 'Jjam-bbong'
tang = 'Tang-su-yuk'
menu = [jja, jjam, tang]

def table2serve(food, csv_name='order_pandas.csv'):
    data = pd.read_csv(csv_name, names=['table number', 'food'])
    flg = False
    table = 0
    data = data.values.tolist()
    for i, row in enumerate(data):
        if food in row:
            #print(food +" is in ",i,"th order")
            table = row[0]
            del data[i]
            flg = True
            break
    if not flg:
        print(food + " is not in order!!")
        return -1
    
    data = pd.DataFrame(np.array(data))
    data.to_csv(csv_name, index=False, header=False)
    print("order updated")
    return table

if __name__ == "__main__":
    print("key 'q' - exit")
    while True:
        print("menu: Jja-jang-myeon, Jjam-bbong, Tang-su-yuk")
        print("menu input: ")
        ipt = input()
        if ipt == 'q':
            print("exit~")
        elif ipt not in menu:
            print(ipt,"is not on the list")
        else:
            t2s = table2serve(ipt)
            if t2s == -1:
                print("There is no table ordered ",ipt)
            else:
                print(t2s,"번 테이블로 서빙합니다")
        
