# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playgame_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1600, 900))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton_5 = QtWidgets.QPushButton(self.page)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 136, 75, 22))
        self.pushButton_5.setObjectName("pushButton_5")
        self.open = QtWidgets.QPushButton(self.page)
        self.open.setGeometry(QtCore.QRect(350, 40, 75, 22))
        self.open.setObjectName("open")
        self.player_10 = QtWidgets.QPushButton(self.page)
        self.player_10.setGeometry(QtCore.QRect(836, 610, 200, 200))
        self.player_10.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"")
        self.player_10.setText("")
        self.player_10.setObjectName("player_10")
        self.pushButton_7 = QtWidgets.QPushButton(self.page)
        self.pushButton_7.setGeometry(QtCore.QRect(350, 184, 75, 22))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setGeometry(QtCore.QRect(20, 208, 330, 22))
        self.label_9.setObjectName("label_9")
        self.player_12 = QtWidgets.QPushButton(self.page)
        self.player_12.setGeometry(QtCore.QRect(1384, 610, 200, 200))
        self.player_12.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"\n"
"")
        self.player_12.setText("")
        self.player_12.setObjectName("player_12")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 330, 22))
        self.label_2.setObjectName("label_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.page)
        self.pushButton_10.setGeometry(QtCore.QRect(1459, 190, 120, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(20, 64, 330, 22))
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setGeometry(QtCore.QRect(1105, 40, 120, 120))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(1282, 40, 120, 120))
        self.label_11.setObjectName("label_11")
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(20, 160, 330, 22))
        self.label_7.setObjectName("label_7")
        self.player_1 = QtWidgets.QPushButton(self.page)
        self.player_1.setGeometry(QtCore.QRect(20, 340, 200, 200))
        self.player_1.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"\n"
"")
        self.player_1.setText("")
        self.player_1.setObjectName("player_1")
        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setGeometry(QtCore.QRect(20, 184, 330, 22))
        self.label_8.setObjectName("label_8")
        self.player_6 = QtWidgets.QPushButton(self.page)
        self.player_6.setGeometry(QtCore.QRect(1384, 340, 200, 200))
        self.player_6.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"\n"
"")
        self.player_6.setText("")
        self.player_6.setObjectName("player_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.page)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 112, 75, 22))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(1105, 190, 120, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(20, 88, 330, 22))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(20, 136, 330, 22))
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(515, 40, 570, 200))
        self.label.setStyleSheet("background-color: silver;")
        self.label.setObjectName("label")
        self.player_8 = QtWidgets.QPushButton(self.page)
        self.player_8.setGeometry(QtCore.QRect(292, 610, 200, 200))
        self.player_8.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"")
        self.player_8.setText("")
        self.player_8.setObjectName("player_8")
        self.player_5 = QtWidgets.QPushButton(self.page)
        self.player_5.setGeometry(QtCore.QRect(1110, 340, 200, 200))
        self.player_5.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"\n"
"")
        self.player_5.setText("")
        self.player_5.setObjectName("player_5")
        self.player_7 = QtWidgets.QPushButton(self.page)
        self.player_7.setGeometry(QtCore.QRect(20, 610, 200, 200))
        self.player_7.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"")
        self.player_7.setText("")
        self.player_7.setObjectName("player_7")
        self.pushButton_6 = QtWidgets.QPushButton(self.page)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 160, 75, 22))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(20, 112, 330, 22))
        self.label_5.setObjectName("label_5")
        self.player_4 = QtWidgets.QPushButton(self.page)
        self.player_4.setGeometry(QtCore.QRect(836, 340, 200, 200))
        self.player_4.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"\n"
"")
        self.player_4.setText("")
        self.player_4.setObjectName("player_4")
        self.player_11 = QtWidgets.QPushButton(self.page)
        self.player_11.setGeometry(QtCore.QRect(1110, 610, 200, 200))
        self.player_11.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"")
        self.player_11.setText("")
        self.player_11.setObjectName("player_11")
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 64, 75, 22))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.page)
        self.pushButton_8.setGeometry(QtCore.QRect(350, 208, 75, 22))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.page)
        self.pushButton_9.setGeometry(QtCore.QRect(1282, 190, 120, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_12 = QtWidgets.QLabel(self.page)
        self.label_12.setGeometry(QtCore.QRect(1459, 40, 120, 120))
        self.label_12.setObjectName("label_12")
        self.pushButton_3 = QtWidgets.QPushButton(self.page)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 88, 75, 22))
        self.pushButton_3.setObjectName("pushButton_3")
        self.player_3 = QtWidgets.QPushButton(self.page)
        self.player_3.setGeometry(QtCore.QRect(564, 340, 200, 200))
        self.player_3.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"\n"
"")
        self.player_3.setText("")
        self.player_3.setObjectName("player_3")
        self.player_9 = QtWidgets.QPushButton(self.page)
        self.player_9.setGeometry(QtCore.QRect(564, 610, 200, 200))
        self.player_9.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"\n"
"\n"
"")
        self.player_9.setText("")
        self.player_9.setObjectName("player_9")
        self.player_2 = QtWidgets.QPushButton(self.page)
        self.player_2.setGeometry(QtCore.QRect(292, 340, 200, 200))
        self.player_2.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"\n"
"")
        self.player_2.setText("")
        self.player_2.setObjectName("player_2")
        self.stackedWidget.addWidget(self.page)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_25 = QtWidgets.QLabel(self.page_5)
        self.label_25.setGeometry(QtCore.QRect(515, 20, 570, 300))
        self.label_25.setStyleSheet("background-color: silver;")
        self.label_25.setObjectName("label_25")
        self.pushButton_21 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_21.setGeometry(QtCore.QRect(660, 350, 280, 40))
        self.pushButton_21.setStyleSheet("QPushButton{\n"
"    border: 3px solid #fff;\n"
"    font-weight: bold;\n"
"    color: green;\n"
"    font-size: 14px;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border-radius: 20px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;    \n"
"}")
        self.pushButton_21.setObjectName("pushButton_21")
        self.player_13 = QtWidgets.QPushButton(self.page_5)
        self.player_13.setGeometry(QtCore.QRect(836, 420, 200, 200))
        self.player_13.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"\n"
"")
        self.player_13.setText("")
        self.player_13.setObjectName("player_13")
        self.player_14 = QtWidgets.QPushButton(self.page_5)
        self.player_14.setGeometry(QtCore.QRect(836, 640, 200, 200))
        self.player_14.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"\n"
"")
        self.player_14.setText("")
        self.player_14.setObjectName("player_14")
        self.player_15 = QtWidgets.QPushButton(self.page_5)
        self.player_15.setGeometry(QtCore.QRect(20, 430, 200, 200))
        self.player_15.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"\n"
"")
        self.player_15.setText("")
        self.player_15.setObjectName("player_15")
        self.player_16 = QtWidgets.QPushButton(self.page_5)
        self.player_16.setGeometry(QtCore.QRect(292, 430, 200, 200))
        self.player_16.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"\n"
"")
        self.player_16.setText("")
        self.player_16.setObjectName("player_16")
        self.player_17 = QtWidgets.QPushButton(self.page_5)
        self.player_17.setGeometry(QtCore.QRect(564, 430, 200, 200))
        self.player_17.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"\n"
"")
        self.player_17.setText("")
        self.player_17.setObjectName("player_17")
        self.player_18 = QtWidgets.QPushButton(self.page_5)
        self.player_18.setGeometry(QtCore.QRect(1110, 430, 200, 200))
        self.player_18.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"\n"
"")
        self.player_18.setText("")
        self.player_18.setObjectName("player_18")
        self.player_19 = QtWidgets.QPushButton(self.page_5)
        self.player_19.setGeometry(QtCore.QRect(1384, 430, 200, 200))
        self.player_19.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"\n"
"")
        self.player_19.setText("")
        self.player_19.setObjectName("player_19")
        self.player_20 = QtWidgets.QPushButton(self.page_5)
        self.player_20.setGeometry(QtCore.QRect(1110, 640, 200, 200))
        self.player_20.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"\n"
"")
        self.player_20.setText("")
        self.player_20.setObjectName("player_20")
        self.player_21 = QtWidgets.QPushButton(self.page_5)
        self.player_21.setGeometry(QtCore.QRect(1384, 650, 200, 200))
        self.player_21.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"\n"
"")
        self.player_21.setText("")
        self.player_21.setObjectName("player_21")
        self.player_22 = QtWidgets.QPushButton(self.page_5)
        self.player_22.setGeometry(QtCore.QRect(564, 650, 200, 200))
        self.player_22.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"\n"
"")
        self.player_22.setText("")
        self.player_22.setObjectName("player_22")
        self.player_23 = QtWidgets.QPushButton(self.page_5)
        self.player_23.setGeometry(QtCore.QRect(292, 640, 200, 200))
        self.player_23.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"\n"
"")
        self.player_23.setText("")
        self.player_23.setObjectName("player_23")
        self.player_24 = QtWidgets.QPushButton(self.page_5)
        self.player_24.setGeometry(QtCore.QRect(20, 640, 200, 200))
        self.player_24.setStyleSheet("QPushButton{\n"
"    border-image:url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/def_prof_img.png);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;\n"
"}\n"
"\n"
"")
        self.player_24.setText("")
        self.player_24.setObjectName("player_24")
        self.stackedWidget.addWidget(self.page_5)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_5.setText(_translate("MainWindow", "Вскрыть"))
        self.open.setText(_translate("MainWindow", "Вскрыть"))
        self.pushButton_7.setText(_translate("MainWindow", "Вскрыть"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_10.setText(_translate("MainWindow", "Использовать"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Карта</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Использования</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Карта</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Использования</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_4.setText(_translate("MainWindow", "Вскрыть"))
        self.pushButton.setText(_translate("MainWindow", "Использовать"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Game_Progress</span></p></body></html>"))
        self.pushButton_6.setText(_translate("MainWindow", "Вскрыть"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "Вскрыть"))
        self.pushButton_8.setText(_translate("MainWindow", "Вскрыть"))
        self.pushButton_9.setText(_translate("MainWindow", "Использовать"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Карта</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Использования</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Вскрыть"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Game_Progress</span></p></body></html>"))
        self.pushButton_21.setText(_translate("MainWindow", "Готов"))
