import mysql.connector

yhteys = mysql.connector.connect(
         host='localhost',
         database='flight_game',
         user='root',
         password='Sukram260106',
         autocommit=True
         )

icao_koodi = input("Syötä lentoaseman ICAO-koodi: ").upper().strip()

kursori = yhteys.cursor()

sql = "SELECT name, municipality FROM airport WHERE ident = %s"
kursori.execute(sql, (icao_koodi,))

tulos = kursori.fetchone()

if tulos:
    kentta_nimi = tulos[0]
    kunta = tulos[1]
    print(f"Lentokenttä: {kentta_nimi}")
    print(f"Sijaintikunta: {kunta}")
else:
    print(f"Lentoasemaa ICAO-koodilla '{icao_koodi}' ei löytynyt.")

yhteys.close()