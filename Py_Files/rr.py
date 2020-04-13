# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rr.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!



from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.patches as mpatches
import numpy as np


import matplotlib.pyplot as plt
import tkinter
from tkinter import messagebox

class Queue:
    def __init__(self,l=None):
        if(l == None):
            self.q=[]
        else:
            self.q = list(l)

    def __str__(self):
        return str(self.q)
    def __repr__(self):
        return self.q

    def push(self,elem):
        self.q.append(elem)

    def pop(self):
        temp = self.q[0]
        self.q = self.q[1:]
        return temp

    def empty(self):
        if(len(self.q) == 0): return 1
        return 0


class rr(object):
    def fig_init(self, processes_name, total_burst):
        self.fig, self.gnt = plt.subplots()  # must be global

        self.gnt.set_ylim(0, len(processes_name))
        self.gnt.set_xlim(0, total_burst)
        self.gnt.set_ylabel('Processes')
        self.gnt.set_xlabel('Time Taken By Each Process')

        ytick = [(i + 1) * 10 for i in range(len(processes_name) + 1)]

        self.gnt.set_xticks(np.arange(0, total_burst + 1, 1))
        self.gnt.set_yticks(ytick)
        self.gnt.set_yticklabels(processes_name)
        self.gnt.grid(True)

    def draw(self, name, start_time, end_time):
        no = int(name[1:])
        self.gnt.broken_barh([(start_time, end_time - start_time)], ((no * 10) - 4, 7), facecolors=('tab:orange'))



    def Round_Robin(self, Processes_Names, Burst_Time_List, Arrival_Time_List, Number_Of_Processes, quantum):
        turn_around = [i for i in range(len(Processes_Names))]
        total = sum(Burst_Time_List) + 10 + max(Arrival_Time_List)
        self.fig_init(Processes_Names, total)
        ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # algorithim
        # first sort
        swapped = None
        for i in range(Number_Of_Processes):
            swapping = False
            for j in range(Number_Of_Processes - i - 1):
                if (Arrival_Time_List[j] > Arrival_Time_List[j + 1]):
                    Arrival_Time_List[j], Arrival_Time_List[j + 1] = Arrival_Time_List[j + 1], Arrival_Time_List[j]
                    Processes_Names[j], Processes_Names[j + 1] = Processes_Names[j + 1], Processes_Names[j]
                    Burst_Time_List[j], Burst_Time_List[j + 1] = Burst_Time_List[j + 1], Burst_Time_List[j]
                    swapping = True
                elif (Arrival_Time_List[j] == Arrival_Time_List[j + 1]):
                    if (int(Processes_Names[j][1:]) > int(Processes_Names[j + 1][1:])):
                        Arrival_Time_List[j], Arrival_Time_List[j + 1] = Arrival_Time_List[j + 1], Arrival_Time_List[j]
                        Processes_Names[j], Processes_Names[j + 1] = Processes_Names[j + 1], Processes_Names[j]
                        Burst_Time_List[j], Burst_Time_List[j + 1] = Burst_Time_List[j + 1], Burst_Time_List[j]
                        swapped = True
            if (swapping == False): break
        ################
        Burst_Copy = list(Burst_Time_List)
        #########
        termination =0
        i=0

        queue = Queue()

        flag=[0 for i in range (Number_Of_Processes)]
        first_time=1
        while(termination < Number_Of_Processes):
            last_x = Arrival_Time_List[i]
            queue.push([Processes_Names[i], Burst_Time_List[i]])

            while( not queue.empty()):

                temp = queue.pop()
                if(temp[1] <= quantum):
                    duration = min(temp[1],quantum)
                    self.draw(temp[0] , last_x, last_x +duration )
                    old_x=last_x
                    last_x=last_x+duration
                    turn_around[ Processes_Names.index(temp[0])] = last_x-Arrival_Time_List[ Processes_Names.index(temp[0])]
                    termination=termination+1
                    flag[ Processes_Names.index(temp[0]) ] =1
                    if (first_time):
                        for it in range(1, len(Arrival_Time_List)):
                            if (Arrival_Time_List[it] > last_x): break
                            if (Arrival_Time_List[it] >= old_x and Arrival_Time_List[it] <= last_x and temp[0] !=
                                    Processes_Names[it]):
                                queue.push(
                                    [Processes_Names[it], Burst_Time_List[it]])
                    else:
                        for it in range(len(Arrival_Time_List)):
                            if (Arrival_Time_List[it] > last_x): break
                            if (Arrival_Time_List[it] > old_x and Arrival_Time_List[it] <= last_x and temp[0] !=
                                    Processes_Names[it]):
                                queue.push(
                                    [Processes_Names[it], Burst_Time_List[it]])


                else:
                    duration=quantum
                    self.draw(temp[0] , last_x, last_x +duration)
                    old_x=last_x
                    last_x=last_x+duration
                    temp[1] = temp[1]-quantum

                    if (first_time):
                        for it in range(1,len(Arrival_Time_List)):
                            if (Arrival_Time_List[it] > last_x): break
                            if (Arrival_Time_List[it] >= old_x and Arrival_Time_List[it] <= last_x and temp[0] != Processes_Names[it]):
                                queue.push(
                                    [Processes_Names[it], Burst_Time_List[it]])
                    else:
                        for it in range(len(Arrival_Time_List)):
                            if (Arrival_Time_List[it] > last_x): break
                            if (Arrival_Time_List[it] > old_x and Arrival_Time_List[it] <= last_x and temp[0] != Processes_Names[it]):
                                queue.push(
                                    [Processes_Names[it], Burst_Time_List[it]])

                    queue.push(temp)
                    first_time = 0

            ##if queue is empty
            if (termination == Number_Of_Processes): break
            else:
                for f in range(Number_Of_Processes):
                    if(flag[f] == 0):
                        i=f
                        break;










        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        waiting = []
        for i in range(len(Processes_Names)):
            waiting.append(turn_around[i] - Burst_Copy[i])

        average_waiting = sum(waiting) / len(waiting)  ##put it in message box

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

            quantum = float(self.textEdit_4.toPlainText())
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
            # Number_Of_Processess
            # quantum

            # Put your code here
            ##############
            if (x != 1):
                self.Round_Robin(Processes_Names, Burst_Time_List, Arrival_Time_List, Number_Of_Processes, quantum)
        except:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror("Error", "Error in input!!")
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1044, 641)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 331, 61))
        self.label.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"background:red;\n"
"border-radius:12;")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(380, 30, 101, 61))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 271, 71))
        self.label_2.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"background:red;\n"
"border-radius:12;")
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(40, 210, 241, 401))
        self.textEdit_2.setStyleSheet("font: 75 20pt \"Nirmala UI\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(690, 30, 281, 61))
        self.pushButton.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color:white;\n"
"background:red;\n"
"border-radius:12;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(390, 210, 231, 401))
        self.textEdit_3.setStyleSheet("font: 75 20pt \"Nirmala UI\";")
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 140, 261, 71))
        self.label_3.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"background:red;\n"
"border-radius:12;")
        self.label_3.setObjectName("label_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(760, 210, 200, 50))
        self.textEdit_4.setStyleSheet("font: 75 20pt \"Nirmala UI\";")
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(750, 140, 241, 71))
        self.label_4.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"background:red;\n"
"border-radius:12;")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.click)
        MainWindow.setFixedSize(1044, 641)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "  Number of process :"))
        self.label_2.setText(_translate("MainWindow", "   Arrival Time"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.label_3.setText(_translate("MainWindow", "  Burst Time"))
        self.label_4.setText(_translate("MainWindow", "   quantem"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = rr()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
