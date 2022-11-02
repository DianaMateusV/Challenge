import sqlite3
import json
#import pip._vendor.requests
import requests
from time import gmtime, strftime
#from urllib.request import urlopen
#from pprint import pprint
#url = "http://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios"
#response = urlopen(url)
#data = json.loads(response.read())


#import psycopg2

#acceso al servicio web de USUARIOS
r = requests.get('http://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios')
usuariosRec = r.json()

print("variable usuariosRec:",usuariosRec)

 ##Conexion de bases de datos
#conexión a la base de datos
try:
    conn = sqlite3.connect('conexion/dbMercado.db')
   
except:
    print ("I am unable to connect to the database")


print ("I am able to connect to the database")
c = conn.cursor()
#c.executemany("INSERT into Clientes(fec_alta, user_name, codigo_zip, credit_card_num, credit_card_ccv, cuenta_numero, direccion, geo_latitud, geo_longitud, color_favorito, foto_dni, ip, auto, auto_modelo, auto_tipo, auto_color, cantidad_compras_realizadas, avatar, fec_birthday, id) VALUES (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)",usuariosRec['usuarios'])
#c.executemany("INSERT into Clientes(fec_alta,user_name,codigo_zip,credit_card_num,credit_card_ccv,cuenta_numero,direccion,geo_latitud,geo_longitud,color_favorito,foto_dni,ip,auto,auto_modelo,auto_tipo,auto_color,cantidad_compras_realizadas,avatar,fec_birthday,id) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",usuariosRec)

#c.executemany("INSERT into Clientes(fec_alta,id) VALUES (%(fec_alta)s,%(id)s)", usuariosRec)
#c.executemany("INSERT into Clientes(fec_alta,id) VALUES (%(fec_alta)s,%(id)s)",int(usuariosRec['usuarios'])

c.executemany("INSERT into Clientes(fec_alta,user_name,codigo_zip,credit_card_num,credit_card_ccv,cuenta_numero,direccion,geo_latitud,geo_longitud,color_favorito,foto_dni,ip,auto,auto_modelo,auto_tipo,auto_color,cantidad_compras_realizadas,avatar,fec_birthday,id) VALUES (%(fec_alta)s,%(user_name)s, %(codigo_zip)s,%(credit_card_num)s,credit_card_ccv,cuenta_numero,%(direccion)s,%(geo_latitud)s,%(geo_longitud)s,%(color_favorito)s,%(foto_dni)s,%(ip)s,%(auto)s,%(auto_modelo)s,%(auto_tipo)s,%(auto_color)s,cantidad_compras_realizadas,%(avatar)s,%(fec_birthday)s,id)",usuariosRec['usuarios'])

conn.commit()
c.close()
