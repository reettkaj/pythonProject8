import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='euch7soo',
         autocommit=True
)

maakoodi = input("Anna maan ISO-koodi: ")

sql = "Select type, count(*) from airport where iso_country ='" + maakoodi + "' group by type";

kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()

if kursori.rowcount > 0:
    for rivi in tulos:
        print(f"Lentoaseman tyyppi: {rivi[0]}, lukumäärä: {rivi[1]}")
