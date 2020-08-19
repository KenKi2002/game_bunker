# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(282, 305)
        MainWindow.setStyleSheet("QLineEdit{\n"
"    border: 3px solid #fff;\n"
"    font-weight: bold;\n"
"    color: green;\n"
"    font-size: 14px;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border-radius: 25px;\n"
"    text-align: center;    \n"
"}\n"
"QPushButton{\n"
"    border: 3px solid #fff;\n"
"    font-weight: bold;\n"
"    border-radius: 15px;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"}\n"
"QLabel{\n"
"    text-align: center;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    color: green;\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 61, 61))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setEnabled(True)
        self.password.setGeometry(QtCore.QRect(30, 140, 221, 51))
        self.password.setObjectName("password")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(30, 80, 221, 51))
        self.login.setObjectName("login")
        self.reg = QtWidgets.QPushButton(self.centralwidget)
        self.reg.setGeometry(QtCore.QRect(60, 210, 161, 31))
        self.reg.setObjectName("reg")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 282, 20))
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
        self.label.setText(_translate("MainWindow", "Вход"))
        self.reg.setText(_translate("MainWindow", "Войти"))
