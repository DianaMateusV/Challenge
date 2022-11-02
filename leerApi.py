#Leer datos del api

from urllib.request import urlopen
import json
url = "http://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios"

response = urlopen(url)
#print(response.read())

data = json.loads(response.read())
#print(data)
#colores= []
for i in data:
    print(i)
    #print(i["color_favorito"])
    #if i["color_favorito"] not in colores:
     #   colores.append(i["color_favorito"])
      #  print(colores)
    #break