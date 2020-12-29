import threading
from what_food import yolo4food


if __name__=='__main__':
    yolo = yolo4food()
    # cam_num=4, txt='food_out', showmode=False, writemode=False, detect_term = 5
    cam_thrd = threading.Thread(target=yolo.cam_on, args=(2, 'food_out.txt', True, False, 2))
    cam_thrd.start()