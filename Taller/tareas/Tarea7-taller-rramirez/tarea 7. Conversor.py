def validacion(num):
    if num==0:
        return True
    elif num%10==0 or num%10==1:
        return validacion(num//10)
    else:
        return False
    
def convercion(num):
    if isinstance (num,int) and validacion(num)==True:
        return binario_decimal(num,0)
    elif isinstance (num,int) and validacion(num)==False:
        return decimal_binario (num,0)
    else:
        return "Debe ingresar un numero entero"


def binario_decimal(num,x):
    if num==0:
        return 0
    else:
        return ((2**x)*(num%10))+ binario_decimal(num//10,x+1)


def decimal_binario(num,x):
    if num==1:
        return num*(10**x)
    else:
        m=num%2
        num=int(num/2)
        return m*(10**x) + decimal_binario(num,x+1)
    
    
