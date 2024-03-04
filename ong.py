#definidas funciones factorial y productoria, a traves de sentencias iterativas.
def factorial(num):
  i=num-1
  fac=num
  while i>0 :
      fac=fac*i
      i-=1
      
  return fac

def productoria(lista):
    prod=1
    for i in lista:
        prod=i*prod
 
    return prod
     
#funcion calcular que desde distintos argumentos recibe en kwargs  
def calcular(**kwargs):
    for k,v in kwargs.items():# recorre el kwargs sobre los argumentos de palabra clave
        if k.startswith('fact_'):# verifica si la clave comienza con 'fact_' para identificar los factoriales
            num = v
            print(f"El factorial de {num} es {factorial(num)}")
        elif k.startswith('prod_'):# verifica si la clave comienza con 'prod_' para la productoria
            lista = v
            print(f"La productoria de {lista} es {productoria(lista)}")
        else: 
            print(f"No se pudo procesar el argumento: {k}")# si la clave no comienza ni con 'fact_' ni con 'prod_' imprime este texto.
            
calcular( prod_1 = [4,6,7,4,3],fact_1 = 5, fact_2 = 6,fact_3=10)