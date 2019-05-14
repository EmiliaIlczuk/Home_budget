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

    def menu(self):
        while(True):
            dec = input("Wybierz opcję: \nP - pokaż, \nW - wprowadź, \nU - usuń, \nS - szybkie podsumowanie, \nQ - wyjście").upper()
            if dec == "P":
                self.select()
            elif (dec == "W"):
                self.insert()
            #elif (dec == "U"):
                #self.delete()
            #elif(dec == "S"):
                #self.summary()
            elif dec == "Q":
                exit()
            else:
                print("Błędny wybór.")

    def select(self):
        tabela = input("Pokaż: \nW - wydatki, \nP - przychody").upper()
        miesiac = int(input("Wpisz miesiąc:"))
        rok = int(input("Wpisz rok:"))
        widok = input("Pokaż widok: \nP - pełny, \nS - skrócony, \nSUM - tylko sumę").upper()

        if tabela == "W":
            if widok == "P":
                self.kursor.execute\
                ("SELECT * FROM wydatki WHERE month(data)=%s and year(data)=%s;", (miesiac, rok))
                result = self.kursor.fetchall()
                if self.kursor.rowcount == 0:
                    print("Brak danych do wyświetlenia.")
                else:
                    i = 1
                    for row in result:
                        print(" | %4s | | %10s | | %7.2f | | %20s | | %15s | | %5s | | %30s |" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                        i = i + 1

            if widok == "S":
                self.kursor.execute\
                ("SELECT kategoria, round(sum(kwota),2) FROM wydatki WHERE month(data)=%s and year(data)=%s GROUP BY kategoria;", (miesiac, rok))
                result = self.kursor.fetchall()
                if self.kursor.rowcount == 0:
                    print("Brak danych do wyświetlenia.")
                else:
                    i = 1
                    for row in result:
                        print(" | %20s | | %10s |" % (row[0], row[1]))
                        i = i + 1

            if widok == "SUM":
                self.kursor.execute\
                ("SELECT round(sum(kwota),2) FROM wydatki WHERE month(data)=%s and year(data)=%s;", (miesiac, rok))
                result = self.kursor.fetchall()
                if self.kursor.rowcount == 0:
                    print("Brak danych do wyświetlenia.")
                else:
                    print("Wydatki w wybranym miesiącu: %7.2f zł" % result[0])

        if tabela == "P":
            if widok == "P":
                self.kursor.execute\
                ("SELECT * FROM przychody WHERE month(data)=%s and year(data)=%s;", (miesiac, rok))
                result = self.kursor.fetchall()
                if self.kursor.rowcount == 0:
                    print("Brak danych do wyświetlenia.")
                else:
                    i = 1
                    for row in result:
                        print("| %4s | | %10s | | %7.2f | | %15s | | %5s | | %30s |" % (row[0], row[1], row[2], row[3], row[4], row[5]))
                        i = i + 1

            if widok == "S":
                self.kursor.execute\
                ("SELECT kategoria, round(sum(kwota),2) FROM przychody WHERE month(data)=%s and year(data)=%s GROUP BY kategoria;",
                (miesiac, rok))
                result = self.kursor.fetchall()
                if self.kursor.rowcount == 0:
                    print("Brak danych do wyświetlenia.")
                else:
                    i = 1
                    for row in result:
                        print(" | %20s | | %10s |" % (row[0], row[1]))
                        i = i + 1

            if widok == "SUM":
                self.kursor.execute\
                ("SELECT round(sum(kwota),2) FROM przychody WHERE month(data)=%s and year(data)=%s;", (miesiac, rok))
                result = self.kursor.fetchall()
                if self.kursor.rowcount == 0:
                    print("Brak danych do wyświetlenia.")
                else:
                    print("Przychody w wybranym miesiącu: %7.2f zł" % result[0])
    def insert(self):
        tabela = input("Wprowadź: \nW - wydatki, \nP - przychody").upper()
        data = input("Wprowadź datę transakcji w formacje rrrr-mm-dd")
        kwota = input("Wprowadź kwotę")

        if tabela == "W":
            kategoria = input(
                "Wprowadź jedną z poniższych kategorii:\nŻywność, \nMieszkanie, \nPłatności, \nAuto i transport, \nZdrowie, \nHigiena, \nOdzież i obuwie, \nRozrywka, \nEdukacja, \nSpłata długów, \nInne").capitalize()
            opis = input("Wprowadź opis transkacji / miejsce zakupu")
        if tabela == "P":
            kategoria = input("Wprowadź jedną z poniższych kategorii:\nWynagrodzenie, \nPremia, \nInne").capitalize()

        kto = input("Wprowadź osobę przeprowadzającą transakcję")
        komentarz = input("Wprowadź komantarz")

        if tabela == "W":
            try:
                self.kursor.execute\
                ("INSERT INTO wydatki (data, kwota, kategoria, opis, kto, komentarz) VALUES (%s, %s, %s, %s, %s, %s)",\
                (data, kwota, kategoria, opis, kto, komentarz))
                self.conn.commit()
                print('Wprowadzono poprawnie.')
            except pymysql.MySQLError:
                print("Niepoprawne dane. Spróbuj ponownie.")
                self.insert()

        if tabela == "P":
            try:
                self.kursor.execute\
                ("INSERT INTO przychody (data, kwota, kategoria, kto, komentarz) VALUES (%s, %s, %s, %s, %s)",\
                (data, kwota, kategoria, kto, komentarz))
                self.conn.commit()
                print('Wprowadzono poprawnie.')
            except pymysql.MySQLError:
                print("Niepoprawne dane. Spróbuj ponownie.")
                self.insert()
