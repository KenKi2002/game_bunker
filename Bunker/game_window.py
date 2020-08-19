# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(900, 600)
        MainWindow.setBaseSize(QtCore.QSize(7, 0))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QPushButton{\n"
"    border: 3px solid #fff;\n"
"    font-weight: bold;\n"
"    color: green;\n"
"    font-size: 14px;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border-radius: 40px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;    \n"
"}\n"
"QMainWindow{\n"
"    background-image: url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/game_win_img.png);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.create_game = QtWidgets.QPushButton(self.centralwidget)
        self.create_game.setGeometry(QtCore.QRect(289, 360, 320, 80))
        self.create_game.setObjectName("create_game")
        self.enter_game = QtWidgets.QPushButton(self.centralwidget)
        self.enter_game.setGeometry(QtCore.QRect(289, 460, 320, 80))
        self.enter_game.setObjectName("enter_game")
        self.prof_img = QtWidgets.QLabel(self.centralwidget)
        self.prof_img.setGeometry(QtCore.QRect(332, 0, 236, 231))
        self.prof_img.setStyleSheet("border: 3px solid #fff;\n"
"border-radius: 20px;\n"
"background: rgba(255, 255, 255, 0.7);")
        self.prof_img.setText("")
        self.prof_img.setPixmap(QtGui.QPixmap("../images/def_prof_img.png"))
        self.prof_img.setObjectName("prof_img")
        self.prof_login = QtWidgets.QLabel(self.centralwidget)
        self.prof_login.setGeometry(QtCore.QRect(332, 240, 236, 31))
        self.prof_login.setStyleSheet("border: 3px solid #fff;\n"
"border-radius: 10px;\n"
"background: rgba(255, 255, 255, 0.7);\n"
"font-weight: bold;\n"
"color: green;\n"
"font-size: 14px;\n"
"qproperty-alignment: AlignCenter;")
        self.prof_login.setObjectName("prof_login")
        self.change_prof_img = QtWidgets.QPushButton(self.centralwidget)
        self.change_prof_img.setGeometry(QtCore.QRect(332, 280, 236, 31))
        self.change_prof_img.setStyleSheet("QPushButton{\n"
"    border: 3px solid #fff;\n"
"    font-weight: bold;\n"
"    color: green;\n"
"    font-size: 14px;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border-radius: 15px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;    \n"
"}")
        self.change_prof_img.setObjectName("change_prof_img")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.create_game.setText(_translate("MainWindow", "Создать Игру"))
        self.enter_game.setText(_translate("MainWindow", "Войти в Игру"))
        self.prof_login.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#23d508;\">LOGIN</span></p></body></html>"))
        self.change_prof_img.setText(_translate("MainWindow", "Сменить аватарку"))
