import mysql.connector

def haeKentta(icao):
    sql = "select name, municipality from airport"
    sql += " where ident = '" + icao + "'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentoaseman nimi {rivi[0]}, kunta: {rivi[1]}")
    else:
        print("Emme löytäneet ICAO-koodillasi yhtään lentoasemaa.")

    return
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='euch7soo',
         autocommit=True
         )

koodi = input("Anna kentän ICAO-koodi: ")
haeKentta(koodi)
