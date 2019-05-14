DROP DATABASE IF EXISTS BUDGET;
CREATE DATABASE BUDGET;
USE BUDGET;

CREATE TABLE logowanie (
	id         int(11) NOT NULL AUTO_INCREMENT,
	login      varchar(30) NOT NULL,
	haslo	   varchar(45) NOT NULL,
	PRIMARY KEY (id));

CREATE TABLE wydatki (
	id			int(11) NOT NULL AUTO_INCREMENT,
    data		date NOT NULL,
    kwota		float NOT NULL,
    kategoria	SET ('Żywność', 'Mieszkanie', 'Płatności', 'Auto i transport', 'Zdrowie', 'Higiena', 'Odzież i obuwie', 'Rozrywka', 'Edukacja', 'Spłata długów', 'Inne') NOT NULL,
    opis		varchar(45),
    kto			varchar(15) NOT NULL,
    komentarz	varchar(50),
	PRIMARY KEY (id));
    
CREATE TABLE przychody (
	id			int(11) NOT NULL AUTO_INCREMENT,
    data		date NOT NULL,
    kwota		float NOT NULL,
    kategoria	SET ('Wynagrodzenie', 'Premia', 'Inne') NOT NULL,
    kto			varchar(15) NOT NULL,
    komentarz	varchar(50),
    PRIMARY KEY (`id`));
    
INSERT INTO logowanie VALUES 
	(NULL, 'Olga', '1234'), 
    (NULL, 'Adam', '5678');

INSERT INTO wydatki VALUES 
	(NULL, '2019-04-27', 81.50, 'Higiena', 'Rossmann', 'Olga', 'uzupełnienie zapasu kosmetyków'),
	(NULL, '2019-04-25', 131.50, 'Żywność', 'Biedronka', 'Adam', NULL),
    (NULL, '2019-04-24', 21.48, 'Żywność', 'Mango', 'Olga', 'jedzenie poza domem'),
    (NULL, '2019-04-20', 1949.50, 'Inne', 'X-KOM', 'Adam', 'iPhone 7'),
    (NULL, '2019-04-16', 60.30, 'Mieszkanie', 'Rossmann', 'Adam', 'środki czystości'),
    (NULL, '2019-04-15', 800, 'Płatności', 'Spółdzielnia', 'Olga', 'czynsz'),
    (NULL, '2019-03-15', 800, 'Płatności', 'Spółdzielnia', 'Adam', 'czynsz'),
    (NULL, '2019-02-15', 800, 'Płatności', 'Spółdzielnia', 'Olga', 'czynsz'),
    (NULL, '2019-04-15', 120, 'Płatności', 'PNGiG', 'Olga', 'opłata za prąd'),
    (NULL, '2019-03-15', 110, 'Płatności', 'PNGiG', 'Olga', 'opłata za prąd'),
    (NULL, '2019-04-12', 280, 'Auto i transport', 'ZTM', 'Adam', 'kwartalny bilet komunikacji miejskiej'),
    (NULL, '2019-04-12', 250, 'Auto i transport', 'BP', 'Olga', 'paliwo'),
    (NULL, '2019-03-12', 200, 'Zdrowie', 'LuxMed', 'Adam', 'wizyta u laryngologa'),
    (NULL, '2019-03-12', 60.90, 'Zdrowie', 'DOZ', 'Adam', 'leki'),
    (NULL, '2019-04-10', 230.49, 'Odzież i obuwie', 'Zalando', 'Adam', 'kurtka wiosenna'),
    (NULL, '2019-03-22', 36, 'Auto i transport', 'PKP', 'Olga', 'przejazd Warszawa-Białystok'),
    (NULL, '2019-03-26', 36, 'Auto i transport', 'PKP', 'Olga', 'przejazd Białystok-Warszawa'),
    (NULL, '2019-04-10', 149, 'Odzież i obuwie', 'AboutYou', 'Olga', 'sukienka wiosenna'),
    (NULL, '2019-02-10', 249, 'Odzież i obuwie', 'eobuwie', 'Olga', 'botki na obcasie'),
	(NULL, '2019-03-03', 4400, 'Edukacja', 'PWN', 'Olga', 'opłata za kurs Python'),
	(NULL, '2019-04-03', 250, 'Inne', 'Coffeedesk', 'Olga', 'prezent na urodziny Pawła'),
    (NULL, '2019-02-05', 1000, 'Spłata długów', 'abc', 'Adam', 'spłata kredytu mieszkaniowego'),
    (NULL, '2019-03-05', 1000, 'Spłata długów', 'abc', 'Adam', 'spłata kredytu mieszkaniowego'),
    (NULL, '2019-04-05', 1000, 'Spłata długów', 'abc', 'Adam', 'spłata kredytu mieszkaniowego'),
    (NULL, '2019-05-15', 800, 'Płatności', 'Spółdzielnia', 'Olga', 'czynsz'),
    (NULL, '2019-06-15', 800, 'Płatności', 'Spółdzielnia', 'Adam', 'czynsz'),
    (NULL, '2019-07-15', 800, 'Płatności', 'Spółdzielnia', 'Olga', 'czynsz'),
    (NULL, '2019-06-15', 120, 'Płatności', 'PNGiG', 'Olga', 'opłata za prąd'),
    (NULL, '2019-07-15', 110, 'Płatności', 'PNGiG', 'Olga', 'opłata za prąd'),
    (NULL, '2019-07-12', 280, 'Auto i transport', 'ZTM', 'Adam', 'kwartalny bilet komunikacji miejskiej'),
    (NULL, '2019-05-12', 300, 'Auto i transport', 'BP', 'Olga', 'paliwo'),
    (NULL, '2019-05-05', 1000, 'Spłata długów', 'abc', 'Adam', 'spłata kredytu mieszkaniowego'),
    (NULL, '2019-06-05', 1000, 'Spłata długów', 'abc', 'Adam', 'spłata kredytu mieszkaniowego'),
    (NULL, '2019-07-05', 1000, 'Spłata długów', 'abc', 'Adam', 'spłata kredytu mieszkaniowego');

INSERT INTO przychody VALUES
	(NULL, '2019-02-10', 4000, 'Wynagrodzenie', 'Olga', NULL),
    (NULL, '2019-02-10', 4000, 'Wynagrodzenie', 'Adam', NULL),
    (NULL, '2019-04-10', 6000, 'Premia', 'Olga', 'przemia za Q1'),
    (NULL, '2019-03-10', 3500, 'Wynagrodzenie', 'Olga', NULL),
    (NULL, '2019-03-10', 4000, 'Wynagrodzenie', 'Adam', NULL),
    (NULL, '2019-04-10', 2000, 'Wynagrodzenie', 'Olga', NULL),
    (NULL, '2019-04-10', 2500, 'Wynagrodzenie', 'Adam', NULL),
    (NULL, '2019-04-10', 3000, 'Premia', 'Adam', 'premia uznaniowa'),
    (NULL, '2019-04-20', 900, 'Inne', 'Adam', 'sprzedaż telefonu na allegro');

DESC wydatki;
DESC przychody;

SELECT * FROM wydatki WHERE month(data)=4 and year(data)=2019;
SELECT kategoria, round(sum(kwota),2) FROM wydatki WHERE month(data) = 4 and year(data) = 2019 GROUP BY kategoria;
SELECT round(sum(kwota),2) FROM wydatki where month(data) = 4 and year(data) = 2019;

SELECT * FROM przychody WHERE month(data)=4 and year(data)=2019;
SELECT kategoria, round(sum(kwota),2) FROM przychody WHERE month(data) = 4 and year(data) = 2019 GROUP BY kategoria;
SELECT round(sum(kwota),2) FROM przychody where month(data) = 4 and year(data) = 2019;

INSERT INTO wydatki (data, kwota, kategoria, opis, kto, komentarz) VALUES ('2019-04-29', 159, 'Edukacja', 'Bonito', 'Olga', 'książki do nauki Pythona');
INSERT INTO przychody (data, kwota, kategoria, kto, komentarz) VALUES ('2019-04-15', 1000, 'Premia', 'Olga', 'premia uznaniowa');

DELETE FROM wydatki WHERE id=37;
DELETE FROM przychody WHERE id=37;

CREATE OR REPLACE VIEW wydatki_Olga AS SELECT kategoria, round(sum(kwota),2) AS suma_wydatkow FROM wydatki WHERE kto = 'Olga' GROUP BY kategoria;
SELECT * FROM wydatki_Olga;

CREATE OR REPLACE VIEW wydatki_mies AS SELECT year(data) AS rok, month(data) AS miesiac, round(sum(kwota),2) AS suma_wydatkow FROM wydatki GROUP BY rok, miesiac ORDER BY rok DESC, miesiac DESC;
SELECT * FROM wydatki_mies;

CREATE OR REPLACE VIEW przychody_mies AS SELECT year(data) AS rok, month(data) AS miesiac, round(sum(kwota),2) AS suma_przychodow FROM przychody GROUP BY rok, miesiac ORDER BY rok DESC, miesiac DESC;
SELECT * FROM przychody_mies;

SELECT w.rok, w.miesiac, ifnull(p.suma_przychodow,0) AS przychody, ifnull(w.suma_wydatkow,0) AS wydatki, ((ifnull(p.suma_przychodow,0))-(ifnull(w.suma_wydatkow,0))) AS roznica
FROM wydatki_mies AS w LEFT JOIN przychody_mies AS p 
ON w.rok = p.rok AND w.miesiac = p.miesiac 
GROUP BY w.rok, w.miesiac
ORDER BY w.rok DESC, w.miesiac DESC;