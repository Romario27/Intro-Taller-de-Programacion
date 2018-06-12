def suma_digitos(num):
      if num==0: #rojo
            return 0
      else:  #verde
            return num%10+suma_digitos(num//10)
#------------------------------------------------------

#Entrada: es un numero entero
#Restricciones: es un entero positivo mayor a cero
# Salida: suma de los digitos

def suma_digitos1(num):
      if isinstance (num,int) and (num>0):
            return suma_digitos_aux(num)
      else:
            return "Error"
def suma_digitos_aux(num):
      if (num==0):
            return 0
      else:
            return num%10 + suma_digitos_aux(num//10)

#--------------------------------------------------------

#Dado un numero, determine su longitud(numero de digitos)
#Entrada: es un numero entero
#Restricciones: es un entero positivo mayor a cero
#Salida: suma de los digitos


def largo(num):
      if isinstance(num,int) and (num>0):
            return largo_aux (num)
      else:
            return "Error"

def largo_aux(num):
      if num==0:
            return 0
      else:
            return 1 + largo_aux(num//10)

#---------------------------------------------------------------------------------

def aparece(num,dig):
      if isinstance (num,int) and isinstance (dig,int) and (num>0) and (dig>=0) and (dig<=9):
            return aparece_aux(num,dig)
      else:
            return "Error"
      
def aparece_aux(num, dig):
      if num!=0:
            if num%10==dig:
                  return 1+aparece_aux ((num//10),(dig))
            else:
                  return aparece_aux (num//10,dig)
      else:
            return 0
            
