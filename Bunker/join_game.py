# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'join_game.ui'
#
# joind by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(325, 363)
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
"QPushButton:hover{\n"
"    background-color: silver;\n"
"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 221, 61))
        self.label.setStyleSheet("text-align: center;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color: green;")
        self.label.setObjectName("label")
        self.game_password = QtWidgets.QLineEdit(self.centralwidget)
        self.game_password.setEnabled(True)
        self.game_password.setGeometry(QtCore.QRect(50, 190, 221, 51))
        self.game_password.setObjectName("game_password")
        self.game_id = QtWidgets.QLineEdit(self.centralwidget)
        self.game_id.setGeometry(QtCore.QRect(50, 120, 221, 51))
        self.game_id.setObjectName("game_id")
        self.join = QtWidgets.QPushButton(self.centralwidget)
        self.join.setGeometry(QtCore.QRect(80, 260, 161, 31))
        self.join.setObjectName("join")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 325, 20))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Войти в игру</span></p></body></html>"))
        self.join.setText(_translate("MainWindow", "Войти"))
