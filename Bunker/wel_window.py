# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wel_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(693, 451)
        MainWindow.setStyleSheet("QPushButton{\n"
"    border: 3px solid #fff;\n"
"    font-weight: bold;\n"
"    color: green;\n"
"    font-size: 14px;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border-radius: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:silver;    \n"
"}\n"
"QPushButton:active{\n"
"     background-position: 0 -64px;\n"
"}\n"
"QMainWindow{\n"
"    border: none;\n"
"    border-image: url(C:/Users/Ilsaf/PycharmProjects/first_project/Game_bunker/Bunker/images/main_img.png) 0 0 0 0 stretch stretch;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(250, 190, 201, 61))
        self.login.setStyleSheet("")
        self.login.setObjectName("login")
        self.signup = QtWidgets.QPushButton(self.centralwidget)
        self.signup.setGeometry(QtCore.QRect(250, 260, 201, 61))
        self.signup.setStyleSheet("")
        self.signup.setObjectName("signup")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 693, 20))
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
        self.login.setText(_translate("MainWindow", "Войти"))
        self.signup.setText(_translate("MainWindow", "Зарегестрироваться"))
