velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

#funcion promedio
def promedio(lista):
  prom=(sum(lista)/len(lista))
  return prom

#funcion filtrar segun valores mayores al promedio
def filtrar(lista,promedio):
  listaux=[]
  #iteracion para recorrer la lista y guardar en una lista auxiliar los indices de los valores sobre el promedio.
  for i in range(len(lista)):
      if lista[i]>promedio:
          listaux.append(i)
  
  return listaux

print(filtrar(velocidad,promedio(velocidad)))