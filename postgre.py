import psycopg2
connection = psycopg2.connect(database="pythonspatial",user="postgres", password="postgres")
cursor = connection.cursor()
cursor.execute("CREATE TABLE art_pieces (id SERIAL PRIMARY KEY, code VARCHAR(255), location GEOMETRY)")
connection.commit()

import requests
url='http://coagisweb.cabq.gov/arcgis/rest/services/public/PublicAr t/MapServer/0/query'
params={"where":"1=1","outFields":"*","outSR":"4326","f":"json"}
r=requests.get(url,params=params)
data=r.json()
data["features"][0] 