def revise(num):
    if isinstance(num, int):
        entre0y4= lambda digito: digito <=4
        entre5y9= lambda digito: digito >=5
        return revise_aux(num,entre0y4),revise_aux(num,entre5y9)
    else:
        return "Error"

def revise_aux(num,condicion):
    if num==0:
        return 0
    elif condicion(num%10):
        return 1+ revise_aux(num//10,condicion)
    else:
        return revise_aux(num//10,condicion)


#-----------------------------------------------------------------

def ceros(lista):
    if isinstance(lista,list):
        cero=lambda x:x==0
        return ceros_aux(lista,cero)
    else:
        return "nada"

def ceros_aux(lista,condicion):
    if lista==[]:
        return False
    elif condicion(lista[0]):
        return True
    else:
        return ceros_aux(lista[1:],condicion)

#-----------------------------------------------------------
def positivo(lista):
    if isinstance(lista,list):
        posi=lambda x:x<=0
        return positivo_aux(lista,posi)
    else:
        return "Error"

def positivo_aux(lista,condi):
    if lista==[]:
        return True
    elif condi(lista[0]):
        return False
    else:
        return positivo_aux(lista[1:],condi)
    
#----------------------------------------------------

def paresimpares(num):
    if isinstance(num, int):
        pares= lambda digito: digito%2==0
        impares= lambda digito: digito%2!=0
        print ("Pares:",paresimpares_aux(num,pares),"," "Impares:",paresimpares_aux(num,impares))
    else:
        return "Error"

def paresimpares_aux(num,condicion):
    if num==0:
        return 0
    elif condicion(num%10):
        return 1+ revise_aux(num//10,condicion)
    else:
        return revise_aux(num//10,condicion)
    
#-------------------------------------------------------

def repite(num,lista):
    if isinstance(num, int) and isinstance (lista, list):
        revisa= lambda num,digito: digito==num
        print ("Repite el", num, "," ,repite_aux(num,lista,revisa),"veces")
    else:
        return "Error"

def repite_aux(num,lista,condicion):
    if lista==[]:
        return 0
    elif condicion(num,lista[0]):
        return 1+ repite_aux(num,lista[1:],condicion)
    else:
        return repite_aux(num,lista[1:],condicion)
    

