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
     
def calcular(fact_1,prod_1,fact_2):
    print(f"El factorial de {fact_1} es {factorial(fact_1)}")
    print(f"La productoria de {prod_1} es {productoria(prod_1)}")
    print(f"El factorial de {fact_2} es {factorial(fact_2)}")

calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)