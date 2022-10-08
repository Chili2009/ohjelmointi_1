import mysql.connector
from geopy import distance

link = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='Lentopeli',
    user='root',
    password='1234',
    autocommit=True
    )

planetype = 'helicopter'
max_range = 0
emissions = 0
location = "EFHK"
places = []
airports = []


sql = 'select co2_g_km, max_distance from planetype where type = "' + planetype + '"'
bookmark = link.cursor()
bookmark.execute(sql)

response = bookmark.fetchall()

for r in response:
    max_range = r[1]
    emissions = r[0]

def list_it(dist, location):

    get1 = 'select latitude_deg, longitude_deg from airport where gps_code ="' + location + '"'
    bookmark.execute(get1)

    reply = bookmark.fetchall()

    for l in reply:
        loc1 = l

    get_all = 'select gps_code, latitude_deg, longitude_deg from airport'
    bookmark.execute(get_all)

    reply2 = bookmark.fetchall()

    for n in reply2:
        loc2 = (n[1], n[2])
        gap = distance.distance(loc1, loc2)

        if gap < dist:
            airports.append(n[0])





print(f'Max etäisyys: {max_range}, päästöt {emissions} g/km lennetty')
list_it(max_range, location)

for n in range(10):
    print(airports[n])
