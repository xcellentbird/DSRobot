import threading
from food_recog import yolo4food
from table2serve import table2serve


if __name__=='__main__':
    yolo = yolo4food() # yolo init
    t2s = table2serve() 
    # cam_num=4, txt='food_out', showmode=False, writemode=False, detect_term = 5
    cam_thrd = threading.Thread(target=yolo.cam_on, args=(2, 'food_out.txt', True, False, 2))
    order_thrd = threading.Thread(target=t2s.order_update, args=(yolo.get_food()))

    cam_thrd.start()
    order_thrd.start()
