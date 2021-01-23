import darknet
import numpy as np
import cv2
import time

class yolo4food:
    def __init__(self, cfg='/home/dsnx/DSRobot/darknet/y4_food.cfg', data='/home/dsnx/DSRobot/darknet/y4_food.data', weights='/home/dsnx/DSRobot/darknet/y4_food_final.weights'):
        self.net, self.cn, self.color = darknet.load_network(cfg, data, weights)
        self.width = darknet.network_width(self.net)
        self.height = darknet.network_height(self.net)
        self.darknet_image = darknet.make_image(self.width, self.height, 3)
        self.foods=''

    def cam_on(self, cam_num=0, txt='food_out', showmode=False, writemode=False, detect_term = 5):
        cap = cv2.VideoCapture(cam_num)
        past = time.time()
        while(cap.isOpened()):
            ret, frame = cap.read() # read capture video frame
            if ret: # true: read frame successed, false: read frame failed

                #### Image Preprocessing, Detect, Draw Box ####
                frame_resized = cv2.resize(frame, (self.width, self.height), interpolation=cv2.INTER_LINEAR) # resize image
                frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB) # change bgr image 2 rgb image
                darknet.copy_image_from_bytes(self.darknet_image, frame_rgb.tobytes())
                r = darknet.detect_image(self.net, self.cn, self.darknet_image) # detect obj from image
                
                if showmode:
                    image = darknet.draw_boxes(r, frame_resized, self.color) # draw box on the image
                    image = cv2.resize(image, (len(frame[0]), len(frame)))
                    cv2.imshow('show',image)
                else:
                    cv2.destroyAllWindows()        

                now = time.time()
                if now - past >= detect_term: 
                    self.foods=''
                    for found in r: # for all detected obj
                        label_name, prob, loc = found[0], found[1], found[2] # get label name, probablility, location
                        print(label_name)
                        self.foods += (" "+label_name)

                    if writemode:
                        with open(txt,mode='w+') as f:
                            print("file_wrote")
                            f.write(self.foods)
                    past = now

                if cv2.waitKey(1) != -1:
                    break
            else:
                print('No Frame')
                break
        cap.release()

    def get_food(self):
        #print(self.foods, " is returned")
        return self.foods

if __name__ == '__main__':
    y = yolo4food()
    y.cam_on(cam_num=0, showmode=True)
