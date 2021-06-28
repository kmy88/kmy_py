import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
import pyautogui
import random
from datetime import datetime

screenWidth , screenHeight = pyautogui.size()

class Worker(QThread):
    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        #화면 전체 크기를 출력(화면해상도)
        print('{},{}.format(screenWidth, screenHeight')
        cnt = 0
        while True :
            ran_width = random.randint(1,screenWidth)
            ran_height = random.randint(1,screenHeight)
            pyautogui.moveTo(ran_width,ran_height,2)
            #키보드로 2초동안 'test' 글자를 입력
            pyautogui.typewrite("test", interval=2)
            cnt += 1
            print('{} 번째 동작중 {}{}'.format(cnt,ran_width, ran_height))
            time.sleep(60)
            print(datetime.now())

    def resume(self):
        self.running = True
        print('status:resume')

    def pause(self):
        self.running = False
        print('status:pause')


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker = Worker()
        self.worker.start()

        btn1 = QPushButton("resume", self)
        btn1.move(20, 20)
        btn2 = QPushButton("pause", self)
        btn2.move(20, 50)

        # 시그널-슬롯 연결하기
        btn1.clicked.connect(self.resume)
        btn2.clicked.connect(self.pause)

    def resume(self):
        self.worker.resume()
        self.worker.start()

    def pause(self):
        self.worker.pause()


app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()