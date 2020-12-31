import csv

jja = 'Jja-jang-myoen'
jjam = 'Jjam-bbong'
tang = 'Tang-su-yuk'
while(True):
    print("테이블 번호(1~4)와 음식(1=짜장, 2=짬, 3=탕)을 입력하세요")
    ol = list(map(int,input().split()))

    if ol[0] == 0 or ol[1] == 0: break
    
    if ol[1] == 1: ol[1] = jja
    elif ol[1] == 1: ol[1] = jjam
    else: ol[1] = tang

    with open('order_pandas.csv','a', encoding='utf-8', newline='') as csv_file:
        appender = csv.writer(csv_file)
        appender.writerow(ol)
