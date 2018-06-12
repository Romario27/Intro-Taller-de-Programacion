#Programa que determina si un numero es primo

def primo (num):
    #num=int(input("Digite el numero:"))
    if isinstance (num,int):
        if num==0 or num==1:
            print ("El valor es un numero especial")
        else:
            return primo_aux (num,num-1) 
    else:
        print ("El numero debe ser entero")

def primo_aux(num,x):
    if x==1:
        print ("El numero es primo")
    elif num%x==0:
        return "El numero es compuesto"
    else:
        return primo_aux(num,x-1)
        

#----------------------------------------------------------------------

def potencia():
    num=int(input("digite el numero"))
    if isinstance(num,int) and num>=0:
        return potencia_aux(num)
    else:
        return "error"

def potencia_aux(num):
    if num==0:
        print (2**num, end = " ")
    else:
        print (2**num, end =" ")
        return potencia_aux(num-1)

#---------------------------------------------------------------------
