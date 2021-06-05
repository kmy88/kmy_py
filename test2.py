import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("test.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
         
         
        #버튼에 기능을 할당하는 코드
        self.lineEdit_2.textChanged.connect(self.lineeditTextFunction)
        self.lineEdit_2.returnPressed.connect(self.printTextFunction)
        self.pushButton.clicked.connect(self.changeTextFunction)

    def lineeditTextFunction(self) :
        self.lineEdit_1.setText(self.lineEdit_2.text())
        #pwd_type1=(self.lineEdit.text())
        #print(pwd_type1)
        

    def printTextFunction(self) :
        #self.lineedit이름.text()
        #Lineedit에 있는 글자를 가져오는 메서드
        print(self.lineEdit_2.text())

    def changeTextFunction(self) :
        #self.lineedit이름.setText("String")
        #Lineedit의 글자를 바꾸는 메서드
        pwd_type1=(self.lineEdit_2.text())
        print(pwd_type1)
        #self.lineEdit.setText("Change Text")
        

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()