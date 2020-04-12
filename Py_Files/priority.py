# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'priority.ui'
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



class priority(object):
    def fig_init(self,processes_name, total_burst):
        self.fig, self.gnt = plt.subplots()  # must be global

        self.gnt.set_ylim(0, len(processes_name))
        self.gnt.set_xlim(0, total_burst)
        self.gnt.set_ylabel('Processes')
        self.gnt.set_xlabel('Time Taken By Each Process')

        ytick = [(i + 1) * 10 for i in range(len(processes_name) + 1)]

        self.gnt.set_xticks(np.arange(0,total_burst+1,1))
        self.gnt.set_yticks(ytick)
        self.gnt.set_yticklabels(processes_name)
        self.gnt.grid(True)

    def draw(self,name, start_time, end_time):
        no = int(name[1:])
        self.gnt.broken_barh([(start_time, end_time - start_time)], ((no * 10) - 4, 7), facecolors=('tab:orange'))

    def swapPositions(self,list, pos1, pos2):
         list[pos1], list[pos2] = list[pos2], list[pos1]
         return list

    def sorting(self,proc, arr, pior, Exc):
            for i in range(0, len(proc) - 1):
                for j in range(0, len(proc) - 1):

                    if (arr[j] > arr[j + 1]):
                        proc =self.swapPositions(proc, j, j + 1)
                        arr = self.swapPositions(arr, j, j + 1)
                        pior = self.swapPositions(pior, j, j + 1)
                        Exc = self.swapPositions(Exc, j, j + 1)
                    elif (arr[j] == arr[j + 1]):
                        if (pior[j] > pior[j + 1]):
                            proc = self.swapPositions(proc, j, j + 1)
                            arr = self.swapPositions(arr, j, j + 1)
                            pior = self.swapPositions(pior, j, j + 1)
                            Exc = self.swapPositions(Exc, j, j + 1)


    def get_min_pos(self, list):
        Min = 0
        for x in range(len(list)):
            Min = list[x]
            if Min > 0:
                break
        for x in range(len(list)):
            for y in range(x + 1, len(list)):
                if (list[y] < Min and list[y] > 0):
                    Min = list[y]
        return Min

    def priorit(self,Processes_Names,priority,Burst_Time_List,Arrival_Time_List,Preemptive,Number_Of_Processes):
        if not (Preemptive):
            self.sorting(Processes_Names, Arrival_Time_List, priority, Burst_Time_List)

            #########################
            last_time = []
            first_time = []
            done = []
            wt = []
            ########################## initial
            Avr_waiting_Time = []
            first_time.append(Arrival_Time_List[0])
            last_time.append(Arrival_Time_List[0] + Burst_Time_List[0])
            done.append(Processes_Names[0])
            last_x = last_time[0]
            Avr_waiting_Time.append(last_x - Arrival_Time_List[0] - Burst_Time_List[0])

            ################clear
            Processes_Names.remove(done[0])
            Arrival_Time_List.remove(Arrival_Time_List[0])
            priority.remove(priority[0])
            Burst_Time_List.remove(Burst_Time_List[0])
            #####################
            while not len(Processes_Names) == 0:

                for i in range(0, len(Processes_Names)):
                    if (Arrival_Time_List[i] <= last_x):
                        wt.append(i)
                #######wt not empty
                if not len(wt) == 0:
                    first_time.append(last_x)
                    index = wt[0]
                    min = priority[index]
                    for i in range(1, len(wt)):
                        if priority[wt[i]] < min:
                            min = priority[wt[i]]
                            index = wt[i]
                    done.append(Processes_Names[index])
                    last_x = last_x + Burst_Time_List[index]
                    last_time.append(last_x)
                    Avr_waiting_Time.append(last_x - Arrival_Time_List[index] - Burst_Time_List[index])
                    ##################
                    Processes_Names.remove(Processes_Names[index])
                    Arrival_Time_List.remove(Arrival_Time_List[index])
                    priority.remove(priority[index])
                    Burst_Time_List.remove(Burst_Time_List[index])
                    wt.clear()
                else:
                    done.append(Processes_Names[0])
                    first_time.append(Arrival_Time_List[0])
                    last_x = Arrival_Time_List[0] + Burst_Time_List[0]
                    last_time.append(last_x)
                    Avr_waiting_Time.append(last_x - Arrival_Time_List[0] - Burst_Time_List[0])
                    ################
                    Processes_Names.remove(Processes_Names[0])
                    Arrival_Time_List.remove(Arrival_Time_List[0])
                    priority.remove(priority[0])
                    Burst_Time_List.remove(Burst_Time_List[0])

            Sum_avg_time = sum(Avr_waiting_Time) / Number_Of_Processes

            for z in range(0, Number_Of_Processes):
                self.draw(done[z], first_time[z], last_time[z])
            ##########################################################################


        elif Preemptive:
            last_x = 0
            flag = 0
            New_list_burst = []
            New_list_Process = []
            Arrived_List = []
            New_priority = []
            Avr_waiting_Time = []
            #############################################################
            # Sorting Lists by Arrival Time
            ##########################################################
            for x in range(Number_Of_Processes):
                for y in range(x + 1, Number_Of_Processes):
                    if Arrival_Time_List[x] > Arrival_Time_List[y]:
                        self.swapPositions(Arrival_Time_List, x, y)
                        self.swapPositions(Burst_Time_List, x, y)
                        self.swapPositions(Processes_Names, x, y)
                        self.swapPositions(priority, x, y)
                    elif Arrival_Time_List[x] == Arrival_Time_List[y]:
                        if priority[x] > priority[y]:
                            self.swapPositions(Burst_Time_List, x, y)
                            self.swapPositions(Processes_Names, x, y)
                            self.swapPositions(priority, x, y)
            #######################################################################
            # Print Till Last Arrival Time
            #########################################################################
            for i in range(Number_Of_Processes):
                Arrived_List.append(Arrival_Time_List[i])
                New_list_burst.append(Burst_Time_List[i])
                New_list_Process.append(Processes_Names[i])
                New_priority.append(priority[i])
                while (1):
                    min_value = self.get_min_pos(New_priority)
                    index_Of_min = New_priority.index(min_value)
                    index_of_sepec_process = Processes_Names.index(New_list_Process[index_Of_min])
                    if i != len(Arrival_Time_List) - 1:
                        if last_x < Arrival_Time_List[i]:
                            if Arrival_Time_List[i + 1] > (Arrival_Time_List[i] + New_list_burst[index_Of_min]):
                                self.draw(New_list_Process[index_Of_min], Arrival_Time_List[i], Arrival_Time_List[i] +
                                          New_list_burst[index_Of_min])
                                last_x = Arrival_Time_List[i] + New_list_burst[index_Of_min]
                                New_list_burst[index_Of_min] = 0
                                New_priority[index_Of_min] = 0
                            else:
                                self.draw(New_list_Process[index_Of_min], Arrival_Time_List[i],
                                          Arrival_Time_List[i + 1])
                                last_x = Arrival_Time_List[i + 1]
                                New_list_burst[index_Of_min] = New_list_burst[index_Of_min] - (
                                        last_x - Arrival_Time_List[i])
                                if New_list_burst[index_Of_min] == 0:
                                    Avr_waiting_Time.append(last_x - Arrival_Time_List[index_of_sepec_process]
                                                            - Burst_Time_List[index_of_sepec_process])

                        else:
                            if Arrival_Time_List[i + 1] > (last_x + New_list_burst[index_Of_min]):
                                self.draw(New_list_Process[index_Of_min], last_x, last_x + New_list_burst[index_Of_min])
                                last_x = last_x + New_list_burst[index_Of_min]
                                New_list_burst[index_Of_min] = 0
                                New_priority[index_Of_min] = 0
                                Avr_waiting_Time.append(last_x - Arrival_Time_List[index_of_sepec_process]
                                                        - Burst_Time_List[index_of_sepec_process])
                            else:
                                self.draw(New_list_Process[index_Of_min], last_x, Arrival_Time_List[i + 1])
                                 New_list_burst[index_Of_min] = New_list_burst[index_Of_min] - (
                                            Arrival_Time_List[i + 1] - last_x)
                                last_x = Arrival_Time_List[i + 1]
                                if New_list_burst[index_Of_min] == 0:
                                    Avr_waiting_Time.append(last_x - Arrival_Time_List[index_of_sepec_process]
                                                            - Burst_Time_List[index_of_sepec_process])

                    elif i == len(Arrival_Time_List) - 1:
                        if last_x < Arrival_Time_List[i]:
                            self.draw(New_list_Process[index_Of_min], Arrival_Time_List[i], Arrival_Time_List[i] +
                                      New_list_burst[index_Of_min])
                            last_x = Arrival_Time_List[i] + New_list_burst[index_Of_min]
                            New_list_burst[index_Of_min] = 0
                        else:
                            self.draw(New_list_Process[index_Of_min], last_x, last_x + New_list_burst[index_Of_min])
                            last_x = last_x + New_list_burst[index_Of_min]
                            New_list_burst[index_Of_min] = 0
                            Avr_waiting_Time.append(last_x - Arrival_Time_List[index_of_sepec_process]
                                                    - Burst_Time_List[index_of_sepec_process])

                    if i == Number_Of_Processes - 1:
                        break

                    elif (Arrival_Time_List[i + 1] - last_x) == 0 or sum(New_list_burst) == 0:
                        break
            #############################################################################
            # Sorting by Priority
            #############################################################################
            for x in range(Number_Of_Processes):
                for y in range(x + 1, Number_Of_Processes):
                    if New_priority[x] > New_priority[y]:
                        self.swapPositions(New_list_burst, x, y)
                        self.swapPositions(Arrived_List, x, y)
                        self.swapPositions(New_list_Process, x, y)
                    elif New_priority[x] == New_priority[y]:
                        if Arrived_List[x] > Arrived_List[y]:
                            self.swapPositions(Arrived_List, x, y)
                            self.swapPositions(New_list_Process, x, y)
            ##########################################################################
            # Drawing after last arrival time
            ##########################################################################
            for i in range(Number_Of_Processes):
                if New_list_burst[i] > 0:
                    self.draw(New_list_Process[i], last_x, last_x + New_list_burst[i])
                    last_x = last_x + New_list_burst[i]
                    index_of_sepec_process = Processes_Names.index(New_list_Process[i])
                    Avr_waiting_Time.append(last_x - Arrival_Time_List[index_of_sepec_process]
                                            - Burst_Time_List[index_of_sepec_process])
            ###############################################################################
            Sum_avg_time = sum(Avr_waiting_Time) / Number_Of_Processes
            ###############################################################################

        #####################################################################
        red_patch = mpatches.Patch(label="The Average Waiting Time is: {}".format(Sum_avg_time), fill=False)
        plt.legend(handles=[red_patch])
        plt.show()  # must be at last

    def click(self):
        try:
            Number_Of_Processes = int(self.textEdit.toPlainText())

            value_of_textedit_2 = self.textEdit_2.toPlainText()
            Arrival_Time_List = value_of_textedit_2.splitlines()

            value_of_textedit_3 = self.textEdit_3.toPlainText()
            Burst_Time_List = value_of_textedit_3.splitlines()

            value_of_textedit_4 = self.textEdit_4.toPlainText()
            priority = value_of_textedit_4.splitlines()
            Processes_Names = []
            x=0
            i = 0
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
                try:
                    priority[i] = int(priority[i])
                except ValueError:
                    # hide main window
                    root = tkinter.Tk()
                    root.withdraw()

                    # message box display
                    messagebox.showerror("Error in priority_List :",
                                         " this value  " + priority[i] + "  in line " + str(
                                             i + 1) + "  isn't allowed""")
                    x = 1

            Preemptive = self.radioButton.isChecked()
            ####
            self.fig_init(Processes_Names, sum(Burst_Time_List) + 10 + max(Arrival_Time_List))
            # this variable value become true when we choose to be preemptive and become false if don't do anything

            # there is our variables:
            # Processes_Names
            # Burst_Time_List
            # Arrival_Time_List
            # Number_Of_Processes
            # Preemptive
            # priority
            if (x != 1):
                self.priorit(Processes_Names, priority, Burst_Time_List, Arrival_Time_List, Preemptive, Number_Of_Processes)
        except:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror("Error", "Error in input!!")
        # Put your code here
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1037, 657)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 311, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"background:red;\n"
"border-radius:12;")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(340, 40, 71, 61))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 170, 231, 71))
        self.label_2.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"background:red;\n"
"border-radius:12;")
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(40, 240, 201, 351))
        self.textEdit_2.setStyleSheet("font: 75 20pt \"Nirmala UI\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(800, 40, 201, 61))
        self.pushButton.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color:white;\n"
"background:red;\n"
"border-radius:12;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(370, 240, 191, 351))
        self.textEdit_3.setStyleSheet("font: 75 20pt \"Nirmala UI\";")
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 170, 211, 71))
        self.label_3.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"background:red;\n"
"border-radius:12;")
        self.label_3.setObjectName("label_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(700, 240, 181, 351))
        self.textEdit_4.setStyleSheet("font: 75 20pt \"Nirmala UI\";")
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(690, 170, 211, 71))
        self.label_4.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"background:red;\n"
"border-radius:12;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(470, 40, 201, 61))
        self.label_5.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"background:red;\n"
"border-radius:12;")
        self.label_5.setObjectName("label_5")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(570, 100, 211, 61))
        self.radioButton.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: Red;\n"
"\n"
"border-radius:12;")
        self.radioButton.setObjectName("radioButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.click)
        MainWindow.setFixedSize(1037, 657)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "  Number of process :"))
        self.label_2.setText(_translate("MainWindow", "   Arrival Time"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.label_3.setText(_translate("MainWindow", "  Burst Time"))
        self.label_4.setText(_translate("MainWindow", "  priority"))
        self.label_5.setText(_translate("MainWindow", "  Execution :"))
        self.radioButton.setText(_translate("MainWindow", " Preemptive"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = priority()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
