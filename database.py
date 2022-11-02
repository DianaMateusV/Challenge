import sqlite3

 ##Conexion de bases de datos
conn = sqlite3.connect('conexion/dbMercado.db')
c = conn.cursor()
def create_table():
 ## c.execute("CREATE TABLE IF NOT EXISTS Clientes(unix REAL, fecha TEXT, palabraclave TEXT, valor REAL)")
  c.execute("CREATE TABLE IF NOT EXISTS Clientes(fec_alta TEXT, user_name TEXT, codigo_zip TEXT, credit_card_num TEXT, credit_card_ccv REAL, cuenta_numero REAL, direccion TEXT, geo_latitud TEXT, geo_longitud TEXT, color_favorito TEXT, foto_dni TEXT, ip TEXT, auto TEXT, auto_modelo REAL, auto_tipo TEXT, auto_color TEXT, cantidad_compras_realizadas REAL, avatar TEXT, fec_birthday TEXT,id REAL)")
 


##Ingreso de datos
#""""
def data_entry():
 #c.execute("INSERT INTO Clientes VALUES(00001,'2018-02-12 16:50:39','Python',6)")
 c.execute("INSERT INTO Clientes VALUES('2021-04-04T07:00:50.276Z','Filomena.Collins','17919-7207','6393-0943-6424-5954',131,58757891,'Mitchell Bypass','-88.3967','-70.5628','black','http://placeimg.com/640/480','218.204.159.251','Cadillac Volt',1,'Coupe','Jaguar PT Cruiser',84978,'https://cdn.fakercloud.com/avatars/muringa_128.jpg','2022-03-28T21:18:02.439Z',1)")
 
 conn.commit()
 c.close()
 conn.close()
#"""


create_table()
data_entry()