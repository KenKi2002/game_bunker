import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import wel_window
import signup
import login
import game_window
import create_game
import join_game
import playgame_window
import requests

from PyQt5.QtWidgets import QFileDialog

from Game_bunker.Bunker.project_db import DataBase

#session = requests.Session()
#session.get('http://localhost:8000/connect/')

class Wel_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui_wel = wel_window.Ui_MainWindow()
        self.ui_wel.setupUi(self)

        self.ui_wel.login.clicked.connect(lambda: self.log())
        self.ui_wel.signup.clicked.connect(lambda: self.sign())

    def log(self):
        log_window.show()

    def sign(self):
        sign_window.show()


class Sign_up(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui_sign = signup.Ui_MainWindow()
        self.ui_sign.setupUi(self)
        self.init_Sign_Ui()

        self.ui_sign.reg.clicked.connect(lambda: self.reg_clicked())
        self.ui_sign.email.returnPressed.connect(lambda: self.ui_sign.password.setFocus())
        self.ui_sign.password.returnPressed.connect(lambda: self.ui_sign.password.clearFocus())

    def reg_clicked(self):
        user_info = {'login': self.ui_sign.email.text(), 'password': self.ui_sign.password.text()}
        r = requests.get('http://localhost:8000/user/signup/', json=user_info).json()
        if r['success']:
            msg = QtWidgets.QMessageBox.information(None, 'Регистрация!','Регистрация прошла успешно')
            sign_window.close()
        else:
            msg = QtWidgets.QMessageBox.information(None, 'Регистрация!','Введите другой логин')
            self.ui_sign.email.setText('')
            self.ui_sign.email.setFocus()

    def init_Sign_Ui(self):
        self.ui_sign.email.setFocus()
        self.ui_sign.email.setPlaceholderText('Введите login')
        self.ui_sign.password.setPlaceholderText('Введите пароль')


class Log_in(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui_log = login.Ui_MainWindow()
        self.ui_log.setupUi(self)
        self.init_Log_Ui()

        self.ui_log.login.returnPressed.connect(lambda: self.ui_log.password.setFocus())
        self.ui_log.password.returnPressed.connect(lambda: self.ui_log.password.clearFocus())
        self.ui_log.reg.clicked.connect(lambda: self.log_clicked())


    def init_Log_Ui(self):
        self.ui_log.login.setFocus()
        self.ui_log.login.setPlaceholderText('Введите login')
        self.ui_log.password.setPlaceholderText('Введите пароль')

    def log_clicked(self):
        self.user_info = {'login': self.ui_log.login.text(), 'password': self.ui_log.password.text()}
        self.r = requests.get('http://localhost:8000/user/login/', json=self.user_info).json()
        if self.r['success']:
            msg = QtWidgets.QMessageBox.information(None, 'Вход!','Вы вошли в свой аккаунт')
            self.prof_log = self.ui_log.login.text()
            self.load_from_server_profile_image()
            log_window.close()
            wel_window.close()
            game_wel_win.init_log()
            game_wel_win.show()
        else:
            msg = QtWidgets.QMessageBox.information(None, 'Вход!','Неправильный логин или пароль')

    def load_from_server_profile_image(self):
        user_info = {'login': self.prof_log}
        r = requests.get('http://localhost:8000/user/return_path/', json=user_info).json()
        if r['success']:
            game_wel_win.ui_game.prof_img.setPixmap(QtGui.QPixmap(r['path']))


class Create_game(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui_create = create_game.Ui_MainWindow()
        self.ui_create.setupUi(self)
        self.init_Create_Ui()

        self.ui_create.save_changes.clicked.connect(lambda: self.save_settings())
        self.ui_create.cancel.clicked.connect(lambda: self.ui_create.stackedWidget.setCurrentWidget(self.ui_create.create_page))
        self.ui_create.create.clicked.connect(lambda: self.create_clicked())
        self.ui_create.game_settings.clicked.connect(lambda: self.ui_create.stackedWidget.setCurrentWidget(self.ui_create.settings))
        self.ui_create.game_id.returnPressed.connect(lambda: self.ui_create.game_password.setFocus())
        self.ui_create.game_id.returnPressed.connect(lambda: self.ui_create.game_password.clearFocus())

    def init_Create_Ui(self):
        self.players_quantities = 12
        self.time_duration = 60
        self.vote_duration = 60
        self.ui_create.stackedWidget.setCurrentWidget(self.ui_create.create_page)
        self.ui_create.game_id.setFocus()
        self.ui_create.game_id.setPlaceholderText('Введите название комнаты')
        self.ui_create.game_password.setPlaceholderText('Введите пароль комнаты')

    def create_clicked(self):
        self.room_info = {'name': self.ui_create.game_id.text(),
                     'password': self.ui_create.game_password.text(),
                     'player_quantities': self.players_quantities,
                     'duration': self.time_duration,
                     'vote_duration': self.vote_duration,
                     'creator_login': log_window.user_info['login']}
        self.r = requests.get('http://localhost:8000/room/create/', json=self.room_info).json()
        if self.r['success']:
            msg = QtWidgets.QMessageBox.information(None, 'Создание комнаты!',f'Вы создали комнату с id {self.ui_create.game_id.text()}')
            create_game_win.close()
        else:
            msg = QtWidgets.QMessageBox.information(None, 'Создание комнаты!','Неправильный id или пароль')
            self.ui_create.game_id.setText('')
            self.ui_create.game_id.setFocus()
            self.ui_create.game_password.setText('')

    def save_settings(self):
        self.players_quantities = int(self.ui_create.player_q.currentText())
        self.time_duration = int(self.ui_create.duration.text())
        self.vote_duration = int(self.ui_create.vote_duration.text())
        msg = QtWidgets.QMessageBox.information(None, 'Настройки!', 'Настройки успешно сохранены')
        self.ui_create.stackedWidget.setCurrentWidget(self.ui_create.create_page)



class Join_game(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui_join = join_game.Ui_MainWindow()
        self.ui_join.setupUi(self)
        self.init_Join_Ui()

        self.ui_join.join.clicked.connect(lambda: self.join_clicked())
        self.ui_join.game_id.returnPressed.connect(lambda: self.ui_join.game_password.setFocus())
        self.ui_join.game_id.returnPressed.connect(lambda: self.ui_join.game_password.clearFocus())

    def init_Join_Ui(self):
        self.ui_join.game_id.setFocus()
        self.ui_join.game_id.setPlaceholderText('Введите название комнаты')
        self.ui_join.game_password.setPlaceholderText('Введите пароль комнаты')

    def join_clicked(self):
        self.request_info = {'name': self.ui_join.game_id.text(),
                             'password': self.ui_join.game_password.text(),
                             'incoming_login': log_window.user_info['login']}
        self.r = requests.get('http://localhost:8000/room/join/', json=self.request_info).json()
        print(self.r['players'])
        if self.r['success']:
            msg = QtWidgets.QMessageBox.information(None, 'Вход в комнату!',f'Вы вошли в комнату с названием {self.ui_join.game_id.text()}')
            join_game_win.close()
            game_wel_win.close()
            playgame_win.show()
        else:
            msg = QtWidgets.QMessageBox.information(None, 'Вход в комнату!','Неправильный id или пароль')
            self.ui_create.game_id.setText('')
            self.ui_create.game_id.setFocus()
            self.ui_create.game_password.setText('')


class Game_wel_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui_game = game_window.Ui_MainWindow()
        self.ui_game.setupUi(self)
        self.ui_game.create_game.clicked.connect(lambda: create_game_win.show())
        self.ui_game.enter_game.clicked.connect(lambda: join_game_win.show())
        self.ui_game.change_prof_img.clicked.connect(lambda: self.load_prof_img())

    def init_log(self):
        self.ui_game.prof_login.setText(log_window.prof_log)

    def load_prof_img(self):
        self.image = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        self.image_name = self.image.split('/')[-1]
        self.image_type = self.image_name.split('.')[-1]
        self.ui_game.prof_img.setPixmap(QtGui.QPixmap(self.image))
        files = {'image': (self.image_name, open(self.image, 'rb').read(), 'image/jpeg')}
        data = {'login': log_window.user_info['login'], 'image_name': self.image}
        r = requests.post('http://localhost:8000/load_image/', data=data, files=files).json()
        print(r['success'])

class PlayGame_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui_playgame = playgame_window.Ui_MainWindow()
        self.ui_playgame.setupUi(self)
        self.ui_playgame.stackedWidget.setCurrentWidget(self.ui_playgame.page_5)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wel_window = Wel_Window()
    wel_window.show()
    sign_window = Sign_up()
    log_window = Log_in()
    game_wel_win = Game_wel_window()
    create_game_win = Create_game()
    join_game_win = Join_game()
    playgame_win = PlayGame_Window()
    base = DataBase()
    sys.exit(app.exec_())