import threading
import time

class thd1():
    def __init__(self):
        self.cont = ''
        self.cnt = 0

    def thd_func(self, st):
        while self.cnt < 50:
            self.cnt+=1
            self.cont = str(self.cnt) + st
            time.sleep(3)

    def ret(self):
        return self.cont.split()

def funct(cl, st):
    cl.thd_func(st)

if __name__=='__main__':
    cl_th1 = thd1()
    threading.Thread(target=funct, args=(cl_th1, 'test yow~')).start()
    while True:
        print(cl_th1.ret())
        time.sleep(1)