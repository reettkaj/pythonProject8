import mysql.connector
import geopy.distance

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='euch7soo',
         autocommit=True
)

icao = input("Anna lentokentän 1 icao-koodi: ")
sql = "Select latitude_deg, longitude,deg from airport where ident = '" + icao + "'"
kurosri = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchone()

latitude = tulos[0]
longitude = tulos[1]

airport1 = (latitude, longitude)

icao = input("Anna lentokentän 2 icao-koodi: ")
sql = "Select latitude_deg, longitude from airport where ident = '" + icao + "'"
kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchone()
latitude = tulos[0]
longitude = tulos[1]
airport2 = (latitude, longitude)

etaisyys = geopy.distance.distance(airport1, airport2).km

print(f"Lentokenttien välinen etäisyys on {etäisyys:.0f} km.")
