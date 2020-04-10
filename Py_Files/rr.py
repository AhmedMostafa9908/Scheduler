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
                        swapping = True
            if (swapping == False): break

        ########
        Burst_Copy = list(Burst_Time_List)
        #########
        count = [(1) for i in range(Number_Of_Processes)]
        last_x = Arrival_Time_List[0]
        taken = []
        taken_count = 0
        flag = 0
        index = None
        x = 0
        while (sum(count) != 0):
            i = 0
            while (i < len(Processes_Names)):
                if (last_x < Arrival_Time_List[i] and taken_count == 0):  # **************************8
                    last_x = Arrival_Time_List[i]

                    ################
                    if (Burst_Time_List[i] == 0):
                        count[i] = 0
                    else:
                        if (Burst_Time_List[i] < quantum):
                            duration = Burst_Time_List[i]
                            Burst_Time_List[i] = 0
                            self.draw(Processes_Names[i], last_x, last_x + duration)
                            last_x = last_x + duration
                            turn_around[i] = last_x - Arrival_Time_List[i]
                            if (i in taken):
                                # taken.remove(i)
                                taken_count = taken_count - 1
                        else:
                            duration = quantum
                            Burst_Time_List[i] = Burst_Time_List[i] - quantum
                            taken.append(i)
                            taken_count = taken_count + 1
                            ###
                            if (flag == 0):
                                index = i
                                flag = 1
                            ####
                            self.draw(Processes_Names[i], last_x, last_x + duration)
                            last_x = last_x + duration
                            if (Burst_Time_List[i] == 0):
                                turn_around[i] = last_x - Arrival_Time_List[i]
                                if (i in taken):
                                    # taken.remove(i)
                                    taken_count = taken_count - 1
                    i = i + 1
                elif (last_x >= Arrival_Time_List[i]):  # *********************************************************
                    ################
                    if (Burst_Time_List[i] == 0):
                        count[i] = 0
                    else:
                        if (Burst_Time_List[i] < quantum):
                            duration = Burst_Time_List[i]
                            Burst_Time_List[i] = 0
                            self.draw(Processes_Names[i], last_x, last_x + duration)
                            last_x = last_x + duration
                            turn_around[i] = last_x - Arrival_Time_List[i]
                            if (i in taken):
                                # taken.remove(i)
                                taken_count = taken_count - 1
                        else:
                            duration = quantum
                            Burst_Time_List[i] = Burst_Time_List[i] - quantum
                            taken.append(i)
                            taken_count = taken_count + 1
                            ###
                            if (flag == 0):
                                index = i
                                flag = 1
                            ####
                            self.draw(Processes_Names[i], last_x, last_x + duration)
                            last_x = last_x + duration
                            if (Burst_Time_List[i] == 0):
                                turn_around[i] = last_x - Arrival_Time_List[i]
                                if (i in taken):
                                    # taken.remove(i)
                                    taken_count = taken_count - 1
                    i = i + 1
                elif (last_x < Arrival_Time_List[i] and taken_count > 0):  # ***********************************

                    if (Burst_Time_List[index] == 0):
                        count[index] = 0
                    else:
                        ################
                        if (Burst_Time_List[index] < quantum):
                            duration = Burst_Time_List[index]
                            Burst_Time_List[index] = 0
                            self.draw(Processes_Names[index], last_x, last_x + duration)
                            last_x = last_x + duration
                            turn_around[index] = last_x - Arrival_Time_List[index]
                            taken.remove(index)
                            taken_count = taken_count - 1
                        else:
                            duration = quantum
                            Burst_Time_List[index] = Burst_Time_List[index] - quantum
                            self.draw(Processes_Names[index], last_x, last_x + duration)
                            last_x = last_x + duration
                            if (Burst_Time_List[index] == 0):
                                turn_around[index] = last_x - Arrival_Time_List[index]
                                # taken.remove(index)
                                taken_count = taken_count - 1

                        if (taken_count == 0):
                            flag = 0
                            x = 0
                        else:
                            x = ((x + 1) % len(taken))
                            index = taken[x]

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
        self.textEdit_4.setGeometry(QtCore.QRect(760, 210, 211, 401))
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
