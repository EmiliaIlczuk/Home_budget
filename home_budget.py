import pymysql
import os

class Configuration:
    def __init__(self, nazwa_pliku, host, user, haslo, baza):
        self.nazwa_pliku = nazwa_pliku
        self.__create_config(host, user, haslo, baza)

    def __create_config(self, host, user, haslo, baza):

        if(not os.path.isfile('./' + self.nazwa_pliku + '.txt')):
            self.file = open(self.nazwa_pliku + ".txt", 'w')
            config_list = [host + "\n", user, "\n", haslo, "\n", baza, "\n"]
            self.file.writelines(config_list)
            self.file.close()

    def read_data(self):
        file = open(self.nazwa_pliku + '.txt', 'r')
        data = []
        for line in file.read().splitlines():
            data.append(line)
        dictionary = {}

        dictionary["host"]      = data[0]
        dictionary["user"]      = data[1]
        dictionary["password"]  = data[2]
        dictionary["baza"]      = data[3]

        return dictionary

class DBConect:
    def __init__(self, config):
        try:
            data = config.read_data()
            self.conn = pymysql.connect(data['host'], data['user'], data['password'], data['baza'], charset="utf8")
            self.entry()
            self.conn.close()

        except pymysql.MySQLError:
            print("Błędne dane połącznia")
    def entry(self):
        dec = input("Chcesz się zalogować czy utworzyć nowe konto? \nL - logowanie, \nN - nowy użytkownik, \nQ-wyjście").upper()
        if dec == "L":
            self.log()
        elif dec == "N":
            self.reg()
        elif dec == "Q":
            exit()
        else:
            print("Błędny wybór.")
            self.entry()

    def log(self):
        login = input('Podaj login')
        haslo = input('Podaj hasło')

        self.kursor = self.conn.cursor()
        self.kursor.execute("SELECT * FROM logowanie WHERE login=%s and haslo=%s", (login, haslo))
        results = self.kursor.fetchall()

        if len(results) == 1:
            print("Zalogowano poprawnie.")
            self.menu()
        else:
            print("Niepoprawny login lub hasło. Spróbuj ponownie.")
            self.log()

    def reg(self):
        login = input('Podaj login')
        self.kursor = self.conn.cursor()
        self.kursor.execute("SELECT login FROM logowanie WHERE login=%s", login)
        if self.kursor.rowcount != 0:
            print("Użytkownik", login, "już istnieje.")
            self.entry()
        else:
            haslo = input('Podaj hasło')
            self.kursor.execute("INSERT INTO logowanie (login, haslo) VALUES (%s, %s)", (login, haslo))
            print("Utworzono nowego użytkownika: ", login)
            self.conn.commit()
            self.log()

