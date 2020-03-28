# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FCFS.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


import matplotlib.patches as mpatches
from PyQt5 import QtCore, QtGui, QtWidgets



import matplotlib.pyplot as plt
import tkinter
from tkinter import messagebox



class FCFS(object):
    def fig_init(self, processes_name, total_burst):
        self.fig, self.gnt = plt.subplots()  # must be global

        self.gnt.set_ylim(0, len(processes_name))
        self.gnt.set_xlim(0, total_burst)
        self.gnt.set_ylabel('Processes')
        self.gnt.set_xlabel('Time Taken By Each Process')

        ytick = [(i + 1) * 10 for i in range(len(processes_name) + 1)]

        self.gnt.set_yticks(ytick)
        self.gnt.set_yticklabels(processes_name)
        self.gnt.grid(True)

    def draw(self, name, start_time, end_time):
        no = int(name[1:])
        self.gnt.broken_barh([(start_time, end_time - start_time)], ((no * 10) - 4, 7), facecolors=('tab:orange'))

    def fcfs(self,Processes_Names,Burst_Time_List,Arrival_Time_List,Number_Of_Processes):
        turn_around = []
        ####
        self.fig_init(Processes_Names, sum(Burst_Time_List) + 20 + max(Arrival_Time_List))
        # sorrrrrrt
        arrival_copy = list(Arrival_Time_List)
        ##
        link1 = zip(Arrival_Time_List, Processes_Names)  # [ (0,'p1') , (0.2,'p2')_,(0.1,'p3'),(0.8,'p4'),(1,'p5') ]
        sorted_link = sorted(link1)
        tuples = zip(*sorted_link)
        Arrival_Time_List, Processes_Names = [list(i) for i in tuples]

        link2 = zip(arrival_copy, Burst_Time_List)
        sorted_link2 = sorted(link2)
        tuples2 = zip(*sorted_link2)
        arrival_copy, Burst_Time_List = [list(j) for j in tuples2]

        #####
        last_x = Arrival_Time_List[0]
        for i in range(len(Processes_Names)):
            if (last_x < Arrival_Time_List[i]):
                last_x = Arrival_Time_List[i]

            self.draw(Processes_Names[i], last_x, Burst_Time_List[i] + last_x)
            last_x = last_x + Burst_Time_List[i]
            turn_around.append(last_x - Arrival_Time_List[i])

        waiting_time = []
        for k in range(len(turn_around)):
            waiting_time.append(turn_around[k] - Burst_Time_List[k])

        average_waiting = sum(waiting_time) / len(Processes_Names)

        red_patch = mpatches.Patch(label="The Average Waiting Time is: {}".format(average_waiting), fill=False)
        plt.legend(handles=[red_patch])
        plt.show()
    def click(self):
        try:
            Number_Of_Processes = int(self.textEdit.toPlainText())

            value_of_textedit_2 = self.textEdit_2.toPlainText()
            Arrival_Time_List = value_of_textedit_2.splitlines()

            value_of_textedit_3 = self.textEdit_3.toPlainText()
            Burst_Time_List = value_of_textedit_3.splitlines()

            Processes_Names = []
            i = 0
            x = 0
            for i in range(Number_Of_Processes):
                try:
                    Arrival_Time_List[i] = float(Arrival_Time_List[i])
                except ValueError:
                    root = tkinter.Tk()
                    root.withdraw()

                    # message box display
                    messagebox.showerror("Error in Arrival_Time_List :",
                                         " this value  " + Arrival_Time_List[i] + "  in line " + str(
                                             i + 1) + "   isn't allowed""")

                    x = 1

                try:
                    Burst_Time_List[i] = float(Burst_Time_List[i])
                except ValueError:
                    # hide main window
                    root = tkinter.Tk()
                    root.withdraw()

                    # message box display
                    messagebox.showerror("Error in Burst_time_List :",
                                         " this value  " + Burst_Time_List[i] + "  in line " + str(
                                             i + 1) + "  isn't allowed""")
                    x = 1
                Processes_Names.append("p" + str(i + 1))

            # there is our variables:
            # Processes_Names
            # Burst_Time_List
            # Arrival_Time_List
            # Number_Of_Processes

            # Put your code here
            if (x != 1):
                self.fcfs(Processes_Names, Burst_Time_List, Arrival_Time_List, Number_Of_Processes)
        except ValueError:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror("Error", "Error in input!!")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1176, 793)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 90, 331, 61))
        self.label.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"background:red;\n"
"border-radius:12;")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(390, 90, 101, 61))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 270, 291, 71))
        self.label_2.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"background:red;\n"
"border-radius:12;")
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 340, 261, 411))
        self.textEdit_2.setStyleSheet("font: 75 20pt \"Nirmala UI\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(800, 630, 281, 61))
        self.pushButton.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color:white;\n"
"background:red;\n"
"border-radius:12;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(370, 340, 261, 411))
        self.textEdit_3.setStyleSheet("font: 75 20pt \"Nirmala UI\";")
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 270, 291, 71))
        self.label_3.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"background:red;\n"
"border-radius:12;")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "  Number of process :"))
        self.label_2.setText(_translate("MainWindow", "   Arrival Time"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.label_3.setText(_translate("MainWindow", "  Burst Time"))
        self.pushButton.clicked.connect(self.click)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FCFS()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
