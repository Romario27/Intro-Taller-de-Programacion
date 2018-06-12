# crear una funcion para determinar cuantos digitos pares tiene un numero.
#Recuerde crear la funcion de validacion para que sea un numero entero.
# Verificar que todos los digitos del numero se encuentran entre 0 y 4

import time as t

def pares_impares ():
      num=int(input("Digite el numero a evaluar:"))
      if isinstance(num ,int) and (num>0):
            print( "La cantidad de pares son:",pares_aux(num),",", "La cantidad de impares son:", impares_aux(num),",", "Los digitos del numero evaluado se encuentran entre 0 y 4:",validacion(num))
      else:
            print("¡Error!. Debe ser un numero mayor a cero y entero")
            t.sleep(1)
            return pares_impares()

def pares_aux (num):
      if num!=0:
            if (num%10)%2==0:
                  return 1+pares_aux (num//10)
            else:
                  return pares_aux(num//10)
      else:
            return 0

def impares_aux (num):
      if num!=0:
            if (num%10)%2!=0:
                  return 1+impares_aux (num//10)
            else:
                  return impares_aux(num//10)
      else:
            return 0

def validacion(num):
      if num!=0:
            if (num%10)>=0 and (num%10)<=4:
                  return validacion(num//10)
            else:
                  return False
      else:
            return True

#--------------------------------------------------------------------------
#Calcula el factorial de un numero 
def factorial (num):
      num1=abs(num)
      if num!=0:
            return num1 * factorial (num1-1)
      else:
            return 1

