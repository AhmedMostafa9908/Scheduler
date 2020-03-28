# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rr.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.patches as mpatches


import matplotlib.pyplot as plt
import tkinter
from tkinter import messagebox



fig, gnt = plt.subplots()  # must be global

class rr(object):

    def fig_init(self,processes_name, total_burst):

        gnt.set_ylim(0, len(processes_name))
        gnt.set_xlim(0, total_burst)
        gnt.set_ylabel('Processes')
        gnt.set_xlabel('Time taked by each process')

        ytick = [(i + 1) * 10 for i in range(len(processes_name) + 1)]

        gnt.set_yticks(ytick)
        gnt.set_yticklabels(processes_name)
        gnt.grid(True)

    def draw(self,name, start_time, end_time):
        no = int(name[1:])
        gnt.broken_barh([(start_time, end_time - start_time)], ((no * 10) - 4, 7), facecolors=('tab:orange'))


    def Round_Robin(self,Processes_Names,Burst_Time_List,Arrival_Time_List,Number_Of_Processes,quantum):
        turn_around = [i for i in range(len(Processes_Names))]
        total = sum(Burst_Time_List) + 10 + max(Arrival_Time_List)
        self.fig_init(Processes_Names, total)
        ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # algorithim
        # first sort
        Arrival_Time_List_copy = list(Arrival_Time_List)

        zipped_list1 = zip(Arrival_Time_List, Processes_Names)
        sorted_pairs1 = sorted(zipped_list1)
        tuples1 = zip(*sorted_pairs1)
        Arrival_Time_List, Processes_Names = [list(tuple) for tuple in tuples1]
        ##
        zipped_list2 = zip(Arrival_Time_List_copy, Burst_Time_List)
        sorted_pairs2 = sorted(zipped_list2)
        tuples2 = zip(*sorted_pairs2)
        Arrival_Time_List_copy, Burst_Time_List = [list(tuple) for tuple in tuples2]
        ########
        count = 0
        last_x = Arrival_Time_List[0]
        while (count < len(Processes_Names)):
            for i in range(len(Processes_Names)):
                if (last_x < Arrival_Time_List[i]):
                    last_x = Arrival_Time_List[i]  ##############there is a problem here

                ################
                if (Burst_Time_List[i] == 0):
                    count = count + 1
                else:
                    if (Burst_Time_List[i] < quantum):
                        duration = Burst_Time_List[i]
                        Burst_Time_List[i] = 0
                        self.draw(Processes_Names[i], last_x, last_x + duration)
                        last_x = last_x + duration
                        turn_around[i] = last_x - Arrival_Time_List[i]
                    else:
                        duration = quantum
                        Burst_Time_List[i] = Burst_Time_List[i] - quantum
                        self.draw(Processes_Names[i], last_x, last_x + duration)
                        last_x = last_x + duration
                        if (Burst_Time_List[i] == 0):
                            turn_around[i] = last_x - Arrival_Time_List[i]

        waiting = []
        for i in range(len(Processes_Names)):
            waiting.append(turn_around[i] - Burst_Time_List[i])

        average_waiting = sum(waiting) / len(waiting)  ##put it in message box

        red_patch = mpatches.Patch(label="The Average Waiting Time is: {}".format(average_waiting), fill=False)
        plt.legend(handles=[red_patch])


    def click(self):
        try:
            Number_Of_Processes = int(self.textEdit.toPlainText())

            value_of_textedit_2 = self.textEdit_2.toPlainText()
            Arrival_Time_List = value_of_textedit_2.splitlines()

            value_of_textedit_3 = self.textEdit_3.toPlainText()
            Burst_Time_List = value_of_textedit_3.splitlines()


            quantum = float(self.textEdit_4.toPlainText())
            Processes_Names=[]
            i = 0
            x=0
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
                    messagebox.showerror("Error in Burst_time_List :", " this value  " + Burst_Time_List[i] + "  in line "+str(i+1)+"  isn't allowed""")
                    x=1
                Processes_Names.append("p"+str(i+1))

            # there is our variables:
            # Processes_Names
            # Burst_Time_List
            # Arrival_Time_List
            # Number_Of_Processess
            # quantum

            # Put your code here
            ##############
            if(x!=1):

                self.Round_Robin(Processes_Names,Burst_Time_List,Arrival_Time_List,Number_Of_Processes,quantum)
                plt.show()
        except:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror("Error","Error in input!!")



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
        self.pushButton.setGeometry(QtCore.QRect(800, 600, 281, 61))
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
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(745, 341, 170, 50))
        self.textEdit_4.setStyleSheet("font: 75 20pt \"Nirmala UI\";")
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(730, 270, 291, 71))
        self.label_4.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"background:red;\n"
"border-radius:12;")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.click)
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
