import csv
import numpy as np
import pandas as pd

jja = 'Jja-jang-myoen'
jjam = 'Jjam-bbong'
tang = 'Tang-su-yuk'

def table2serve(food):
    data = pd.read_csv("order_pandas.csv", names=['table number', 'food'])
    flg = False
    table = 0
    data = data.values.tolist()
    for i, row in enumerate(data):
        if food in row:
            print(food +" is in ",i," order")
            table = row[0]
            del data[i]
            flg = True
            break
    if not flg:
        print(food + " is not in order!!")
        return -1
    
    data = pd.DataFrame(np.array(data))
    data.to_csv("order_pandas.csv", index=False, header=False)
    print("order updated")
    return table
    
print(table2serve(jja),"번 테이블로 서빙합니다")
