import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random 
import config

form_class = uic.loadUiType("UI1.ui")[0]

NameList = config.NameList
  
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        
        self.List = [str(i) + '. ' + str(NameList[i-1]) for i in range (1, 27)]

        # 주문 버튼 정의
        self.pushButton.clicked.connect(self.shuffleList)

        # 기본 텍스트 상자 설정
        self.set_label()

       
    # 갯수 더하기 함수 
    def shuffleList (self) :
        random.shuffle(self.List)
        self.set_label()
    
    # 항목 별 갯수 정의
    def set_label (self) :
        self.SEAT1.setText(self.List[0])
        self.SEAT2.setText(self.List[1])
        self.SEAT3.setText(self.List[2])
        self.SEAT4.setText(self.List[3])
        self.SEAT5.setText(self.List[4])
        self.SEAT6.setText(self.List[5])
        self.SEAT7.setText(self.List[6])
        self.SEAT8.setText(self.List[7])
        self.SEAT9.setText(self.List[8])
        self.SEAT10.setText(self.List[9])
        self.SEAT11.setText(self.List[10])
        self.SEAT12.setText(self.List[11])
        self.SEAT13.setText(self.List[12])
        self.SEAT14.setText(self.List[13])
        self.SEAT15.setText(self.List[14])
        self.SEAT16.setText(self.List[15])
        self.SEAT17.setText(self.List[16])
        self.SEAT18.setText(self.List[17])
        self.SEAT19.setText(self.List[18])
        self.SEAT20.setText(self.List[19])
        self.SEAT21.setText(self.List[20])
        self.SEAT22.setText(self.List[21])
        self.SEAT23.setText(self.List[22])
        self.SEAT24.setText(self.List[23])
        self.SEAT25.setText(self.List[24])
        self.SEAT26.setText(self.List[25])


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()