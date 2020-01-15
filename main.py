import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
import pyqtgraph as pg
from Ui import Ui_Form
import sys
from PyQt5.QtCore import *
class Main(QWidget,Ui_Form):
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)          #调用父类方法
        self.ser = serial.Serial()  #生成串口对象
        self.thread = Worker()         #线程实例化

        self.datas1 = []#心率
        self.datas2 = []#血氧
        self.datas3 = []#体温

        self.setsign()  #信号与槽
        self.paint_setup() #图像初始化

    def paint_setup(self):

        self.XN=50
        self.pw1= pg.PlotWidget(enableAutoRange=True)  # 实例化一个绘图部件
        self.pw1.showGrid(x=True, y=True)  # 显示图形网格
        self.pw1.setRange(xRange=[0,self.XN],yRange=[200,800])
        self.horizontalLayout.addWidget(self.pw1)
        self.paint1= self.pw1.plot(pen='b')  # 蓝色

        self.pw2 = pg.PlotWidget(enableAutoRange=True)
        self.pw2.showGrid(x=True, y=True)
        self.pw2.setRange(xRange=[0, self.XN], yRange=[0, 130])
        self.verticalLayout.addWidget(self.pw2)
        self.paint2 = self.pw2.plot(pen='b')

        self.pw3 = pg.PlotWidget(enableAutoRange=True)
        self.pw3.showGrid(x=True, y=True)
        self.pw3.setRange(xRange=[0, self.XN], yRange=[20, 46])
        self.verticalLayout_2.addWidget(self.pw3)
        self.paint3 = self.pw3.plot(pen='b')



    def setsign(self):
        self.serachbtn.clicked.connect(self.search)     #获取串口号
        self.startbtn.clicked.connect(self.start)       #启动线程
        self.suspendbtn.clicked.connect(self.suspend)   #停止线程
        self.resetbtn.clicked.connect(self.reset)       #重置图像


        self.thread.sinOut1.connect(self.details1)      #生成图像
        self.thread.sinOut2.connect(self.details2)
        self.thread.sinOut3.connect(self.details3)
    def search(self):
        ch = list(serial.tools.list_ports.comports())
        print(ch)
        if len(ch) == 0:
            mes = QMessageBox.about(self, "错误", "无法识别串口")
        else:
            self.serport.clear()
            for ch1 in ch:
                sh = str(ch1)

                lens=sh.find('-')
                #print("len:",lens)对串口进行处理，获取COM值
                #print("串口："+sh[0:lens-1])
                self.serport.addItem(sh[0:lens-1])
    def start(self):
        try:
            self.thread.working = True
            # self.btn1.setEnabled(False)
            self.thread.start()
        except:
            me = QMessageBox.about(self, "错误", "启动失败")
    def suspend(self):
        try:
            self.thread.working = False
        except:
            me = QMessageBox.about(self, "错误", "出现错误")
    def details3(self,data):
        try:
            self.body.setText(data)
            if len(self.datas3) < self.XN:
                self.datas3.append(float(data))#字符转浮点数
            else:
                self.datas3[:-1] = self.datas3[1:]
                self.datas3[-1] = float(data)
            self.paint3.setData(self.datas3)
        except:
            print('chucuo')
    def details2(self,data):
        self.blood.setText(data)
        if len(self.datas2) < self.XN:
            self.datas2.append(int(data))
        else:
            self.datas2[:-1] = self.datas2[1:]
            self.datas2[-1] = int(data)
        self.paint2.setData(self.datas2)
    def details1(self,data):
        self.heart.setText(data)

        if len(self.datas1) < self.XN:
            self.datas1.append(int(data))
        else:
            self.datas1[:-1] = self.datas1[1:]
            self.datas1[-1] = int(data)
        self.paint1.setData(self.datas1)
    def reset(self):
        self.datas1.clear()
        self.datas2.clear()
        self.datas3.clear()




class Worker(QThread):
    sinOut1 = pyqtSignal(str)
    sinOut2 = pyqtSignal(str)
    sinOut3 = pyqtSignal(str)
    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.working = True

    def __del__(self):
        # 线程状态改变与线程终止
        self.working = False
        self.wait()

    def run(self):
        '''

        :return:
        '''
        ch = main.serport.currentText()  # 串口号
        sh = main.baud.currentText()  # 波特率
        main.ser.setPort(ch)
        main.ser.baudrate = sh
        main.ser.open()
        try:
            while self.working == True:
                num1=main.ser.readline()
                print(num1)
                nums1 = str(num1, "utf-8")
                position1 = nums1.find('\n')
                self.sinOut1[str].emit(nums1[0:position1-1])

                num2 = main.ser.readline()
                nums2=str(num2,'utf-8')
                position2=nums2.find('\n')
                if position2 == 1:
                    self.sinOut2[str].emit(nums2[0:1])
                else :
                    self.sinOut2[str].emit(nums2[0:position2-1])
                num3 = main.ser.readline()
                nums3=str(num3, "utf-8")
                position3 = nums3.find('\n')

                self.sinOut3[str].emit(nums3[0:position3-1])
                #main.ser.readline()
            main.ser.close()
        except:
            print("串口读取数据失败")




if __name__=="__main__":
    app=QApplication(sys.argv)
    main=Main()
    main.show()
    sys.exit(app.exec_())
