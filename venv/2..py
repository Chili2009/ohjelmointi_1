import random
import mysql.connector
# from geopy import distance

def randomcontingent(yhteys):
    sql = "select name from airport order by rand() limit 1;"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result =cursor.fetchall()
    for row in result:
        return row [0]

# tervehdi käyttäjää, kysy nimi, tallenna muistiin tietokantaan

Name = input("Hyvät matkustajat, tervetuloa lennolle!\nEnnen lennolle lähtöä anna nimesi: ")
print("Kiitos, voitte nousta koneeseen.\nNauttikaa lennosta!")

#Lähtökenttä Helsinki-Vantaa (EFHK), päämääräkenttä arvotaan

link = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='Lentopeli',
    user='root',
    password='1234',
    autocommit=True
    )

contingent = randomcontingent(link)

print (f"Lähtöpaikka: Helsinki-Vantaa lentokenttä (EFHK)\nPäämäärä: {contingent}")



