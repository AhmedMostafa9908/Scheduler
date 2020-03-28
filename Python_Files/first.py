# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import matplotlib.pyplot as plt



from PyQt5 import QtCore, QtGui, QtWidgets
from  FCFS import FCFS
from SJF import SJF
from rr import  rr
from priority import priority

class Ui_MainWindow(object):
    def Fcfs(self):
        self.window =QtWidgets.QMainWindow()
        self.ui= FCFS()
        self.ui.setupUi(self.window)
        self.window.show()

    def SJF(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = SJF()
        self.ui.setupUi(self.window)
        self.window.show()

    def rr(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = rr()
        self.ui.setupUi(self.window)
        self.window.show()

    def priority(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = priority()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 895)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background: grey;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 390, 211, 91))
        self.pushButton.setStyleSheet("font: 30pt \"MV Boli\";\n"
"background: red;\n"
"border-radius: 12;\n"
"color:white;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(810, 560, 211, 91))
        self.pushButton_2.setStyleSheet("font: 30pt \"MV Boli\";color:white;\n"
"background: red;\n"
"border-radius: 12;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 570, 211, 91))
        self.pushButton_3.setStyleSheet("\n"
"color:white;font: 30pt \"MV Boli\";\n"
"background: red;\n"
"border-radius: 12;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 400, 271, 91))
        self.pushButton_4.setStyleSheet("font: 30pt \"MV Boli\";\n"
"background: red;\n"
"border-radius: 12;\n"
"color:white;")

        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 90, 1271, 111))
        self.label.setStyleSheet("font: 36pt \"MV Boli\";\n"
"color: white;\n"
"background: red;")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.Fcfs)
        self.pushButton_2.clicked.connect(self.priority)
        self.pushButton_3.clicked.connect(self.SJF)
        self.pushButton_4.clicked.connect(self.rr)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "FCFS"))
        self.pushButton_2.setText(_translate("MainWindow", "Priority"))
        self.pushButton_3.setText(_translate("MainWindow", "SJC"))
        self.pushButton_4.setText(_translate("MainWindow", "Round Robin"))
        self.label.setText(_translate("MainWindow", "Choose the scheduler type :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
