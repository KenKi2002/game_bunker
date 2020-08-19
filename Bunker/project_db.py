import sqlite3


class DataBase():
	def __init__(self):
		self.db = sqlite3.connect('base.db')
		self.cursor = self.db.cursor()

		self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
			login TEXT,
			password TEXT
			)""")
		self.db.commit()
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS rooms(
			room_id TEXT,
			room_password TEXT
			)""")
		self.db.commit()

	def reg_user(self,login,password):
		self.log = login
		self.pas = password
		self.cursor.execute(f"SELECT login FROM users WHERE login = '{self.log}'")
		if self.cursor.fetchone() is None:
			self.cursor.execute("INSERT INTO users VALUES(?,?)",(self.log,self.pas))
			self.db.commit()
			return True
		else:
			return False

	def log_user(self,login,password):
		self.log = login
		self.pas = password
		self.cursor.execute(f"SELECT login FROM users WHERE login = '{self.log}'")
		if self.cursor.fetchone() is None:
			return False
		else:
			self.cursor.execute(f"SELECT password FROM users where login = '{self.log}'")
			value = self.cursor.fetchone()
			if value[0] == self.pas:
				return True
				self.db.commit()
			else:
				return False

	def create_room(self,r_id,password):
		self.r_id = r_id
		self.password = password
		self.cursor.execute(f"SELECT room_id FROM rooms WHERE room_id = '{self.r_id}'")
		if self.cursor.fetchone() is None:
			self.cursor.execute("INSERT INTO rooms VALUES(?,?)",(self.r_id,self.password))
			self.db.commit()
			return True
		else:
			return False

	def join_room(self,r_id,password):
		self.r_id = r_id
		self.password = password
		self.cursor.execute(f"SELECT room_id FROM rooms WHERE room_id = '{self.r_id}'")
		if self.cursor.fetchone() is None:
			return False
		else:
			self.cursor.execute(f"SELECT room_password FROM rooms WHERE room_id = '{self.r_id}'")
			value = self.cursor.fetchone()
			if value[0] == self.password:
				return True
				self.db.commit()
			else:
				return False

