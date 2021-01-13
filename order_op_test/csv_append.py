#args test
import argparse
import csv

jja = 'Jja-jang-myoen'
jjam = 'Jjam-bbong'
tang = 'Tang-su-yuk'
menu = [jja, jjam, tang]
table = [1, 2, 3, 4]

def parser():
    parser = argparse.ArgumentParser(description="add order... table: 1,2,3,4  menu: Jja-jang, Jjam-bbong, Tang-su-yuk")
    parser.add_argument("table_num", type=int, default=1, help='table number')
    parser.add_argument("food_name", type=str, default='jja-jang', help='food name')
    args = parser.parse_args()
    
    return args.table_num, args.food_name

def check_parser(table_number, food_name):
    if table_number not in table:
        print("there is no {} table".format(table_number))
        print("table number: 1, 2, 3, 4")
        return False
    elif food_name not in menu:
        print("{} is not in our menu".format(food_name))
        print("menu: Jja-jang, Jjam-bbong, Tang-su-yuk")
        return False
    else:
        return True

def add_order(table_number, food_name, csv_name='order_pandas.csv'):
    with open(csv_name,'a', encoding='utf-8', newline='') as csv_file:
        appender = csv.writer(csv_file)
        appender.writerow([table_number, food_name])
    print("order added!")

if __name__=='__main__':
    tn, fn = parser()
    if check_parser(tn, fn):
        print(tn,"- table")
        print(fn,"- food")
        add_order(tn, fn)
        
