import sys
precios = {'Notebook'        : 700000,
           'Teclado'         : 25000,
           'Mouse'           : 12000,
           'Monitor'         : 250000,
           'Escritorio'      : 135000,
           'Tarjeta de Video': 1500000}

def filtrar(dic,umbral,condicion):
    if condicion == "menor":
     diccionario = { k:v for k,v in dic.items() if v < umbral}
     lista= (diccionario.keys())
     print(f'Los productos menores al umbral son: {",".join(lista)}.')
    elif condicion == "mayor" or condicion == "":
     diccionario = { k:v for k,v in dic.items() if v > umbral}
     lista= list(diccionario.keys())
     print(f'Los productos mayores al umbral son: {",".join(lista)}.')
    else:
     print("Lo sentimos, no es una operación válida")
  
if len(sys.argv)>2:
    condicion = str(sys.argv[2])
else:
    condicion = "mayor"  
   
filtrar(precios,int(sys.argv[1]),condicion)
           