# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(771, 714)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 771, 701))
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.baud = QtWidgets.QComboBox(self.widget)
        self.baud.setGeometry(QtCore.QRect(30, 170, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.baud.setFont(font)
        self.baud.setObjectName("baud")
        self.baud.addItem("")
        self.baud.addItem("")
        self.serachbtn = QtWidgets.QPushButton(self.widget)
        self.serachbtn.setGeometry(QtCore.QRect(200, 60, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.serachbtn.setFont(font)
        self.serachbtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.serachbtn.setObjectName("serachbtn")
        self.serport = QtWidgets.QComboBox(self.widget)
        self.serport.setGeometry(QtCore.QRect(30, 60, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.serport.setFont(font)
        self.serport.setObjectName("serport")
        self.tabWidget.addTab(self.widget, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(200, -10, 631, 201))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 40, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(90, 0, 20, 491))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.heart = QtWidgets.QLabel(self.groupBox)
        self.heart.setGeometry(QtCore.QRect(10, 120, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.heart.setFont(font)
        self.heart.setText("")
        self.heart.setObjectName("heart")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(139, 9, 421, 191))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(200, 190, 631, 221))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.blood = QtWidgets.QLabel(self.groupBox_2)
        self.blood.setGeometry(QtCore.QRect(0, 130, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blood.setFont(font)
        self.blood.setText("")
        self.blood.setObjectName("blood")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 10, 421, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_2 = QtWidgets.QFrame(self.groupBox_2)
        self.line_2.setGeometry(QtCore.QRect(90, 0, 20, 221))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(200, 410, 631, 261))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.body = QtWidgets.QLabel(self.groupBox_3)
        self.body.setGeometry(QtCore.QRect(10, 110, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.body.setFont(font)
        self.body.setText("")
        self.body.setObjectName("body")
        self.line_3 = QtWidgets.QFrame(self.groupBox_3)
        self.line_3.setGeometry(QtCore.QRect(90, 0, 20, 221))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(140, 10, 421, 181))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.startbtn = QtWidgets.QPushButton(self.tab_2)
        self.startbtn.setGeometry(QtCore.QRect(20, 70, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.startbtn.setFont(font)
        self.startbtn.setObjectName("startbtn")
        self.suspendbtn = QtWidgets.QPushButton(self.tab_2)
        self.suspendbtn.setGeometry(QtCore.QRect(20, 240, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.suspendbtn.setFont(font)
        self.suspendbtn.setObjectName("suspendbtn")
        self.resetbtn = QtWidgets.QPushButton(self.tab_2)
        self.resetbtn.setGeometry(QtCore.QRect(20, 420, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.resetbtn.setFont(font)
        self.resetbtn.setObjectName("resetbtn")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.tabWidget.setObjectName("Tab1")

        qssStyle='''
            #Tab1{
                    background-color:cyan;
            }
        
        
        '''

        self.setStyleSheet(qssStyle)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.baud.setItemText(0, _translate("Form", "9600"))
        self.baud.setItemText(1, _translate("Form", "115200"))
        self.serachbtn.setText(_translate("Form", "查找串口"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("Form", "Tab 1"))
        self.label_6.setText(_translate("Form", "心率"))
        self.label_4.setText(_translate("Form", "血氧"))
        self.label_9.setText(_translate("Form", "体温"))
        self.startbtn.setText(_translate("Form", "启动"))
        self.suspendbtn.setText(_translate("Form", "停止"))
        self.resetbtn.setText(_translate("Form", "清除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))
