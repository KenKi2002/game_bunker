# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_game.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(325, 360)
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
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 325, 360))
        self.stackedWidget.setStyleSheet("background-color: green;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.create_page = QtWidgets.QWidget()
        self.create_page.setObjectName("create_page")
        self.game_id = QtWidgets.QLineEdit(self.create_page)
        self.game_id.setGeometry(QtCore.QRect(50, 90, 220, 50))
        self.game_id.setStyleSheet("text-align: center;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color: black;")
        self.game_id.setObjectName("game_id")
        self.label = QtWidgets.QLabel(self.create_page)
        self.label.setGeometry(QtCore.QRect(50, 10, 220, 60))
        self.label.setStyleSheet("text-align: center;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color: black;")
        self.label.setObjectName("label")
        self.game_password = QtWidgets.QLineEdit(self.create_page)
        self.game_password.setEnabled(True)
        self.game_password.setGeometry(QtCore.QRect(50, 160, 220, 50))
        self.game_password.setStyleSheet("text-align: center;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color: black;")
        self.game_password.setObjectName("game_password")
        self.create = QtWidgets.QPushButton(self.create_page)
        self.create.setGeometry(QtCore.QRect(80, 230, 160, 30))
        self.create.setObjectName("create")
        self.game_settings = QtWidgets.QPushButton(self.create_page)
        self.game_settings.setGeometry(QtCore.QRect(80, 280, 160, 30))
        self.game_settings.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.create_page)
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.player_q = QtWidgets.QComboBox(self.settings)
        self.player_q.setGeometry(QtCore.QRect(230, 30, 41, 22))
        self.player_q.setStyleSheet("background-color: white;")
        self.player_q.setObjectName("player_q")
        self.player_q.addItem("")
        self.player_q.addItem("")
        self.player_q.addItem("")
        self.label_2 = QtWidgets.QLabel(self.settings)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 111, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.settings)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 181, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.settings)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 191, 16))
        self.label_4.setObjectName("label_4")
        self.duration = QtWidgets.QLineEdit(self.settings)
        self.duration.setGeometry(QtCore.QRect(230, 70, 41, 20))
        self.duration.setStyleSheet("font-size: 12px;\n"
"color: black;\n"
"qproperty-alignment: AlignCenter;\n"
"background-color: white;")
        self.duration.setObjectName("duration")
        self.vote_duration = QtWidgets.QLineEdit(self.settings)
        self.vote_duration.setGeometry(QtCore.QRect(230, 110, 41, 20))
        self.vote_duration.setStyleSheet("font-size: 12px;\n"
"color: black;\n"
"qproperty-alignment: AlignCenter;\n"
"background-color: white;")
        self.vote_duration.setObjectName("vote_duration")
        self.save_changes = QtWidgets.QPushButton(self.settings)
        self.save_changes.setGeometry(QtCore.QRect(80, 200, 160, 30))
        self.save_changes.setObjectName("save_changes")
        self.cancel = QtWidgets.QPushButton(self.settings)
        self.cancel.setGeometry(QtCore.QRect(80, 250, 160, 30))
        self.cancel.setObjectName("cancel")
        self.stackedWidget.addWidget(self.settings)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 325, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Создать новую игру</span></p></body></html>"))
        self.create.setText(_translate("MainWindow", "Создать"))
        self.game_settings.setText(_translate("MainWindow", "Настройки"))
        self.player_q.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>10</p></body></html>"))
        self.player_q.setItemText(0, _translate("MainWindow", "12"))
        self.player_q.setItemText(1, _translate("MainWindow", "10"))
        self.player_q.setItemText(2, _translate("MainWindow", "8"))
        self.label_2.setText(_translate("MainWindow", "Количество игроков"))
        self.label_3.setText(_translate("MainWindow", "Длительность хода при вскрытии"))
        self.label_4.setText(_translate("MainWindow", "Длительность хода при голосовании"))
        self.duration.setText(_translate("MainWindow", "60"))
        self.vote_duration.setText(_translate("MainWindow", "60"))
        self.save_changes.setText(_translate("MainWindow", "Сохранить"))
        self.cancel.setText(_translate("MainWindow", "Отмена"))
