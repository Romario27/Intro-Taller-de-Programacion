def elimina_3(num):
    if isinstance(num,int):
        return elimina_3_aux(num,0,0)
    else:
        return "Debe ser entero"

def elimina_3_aux(num,nuevo,cont):
    if num==0:
        return nuevo
    else:
        if (num%10)%3==0 and num%10!=0:
            return elimina_3_aux(num//10,nuevo,cont)
        else:
            return elimina_3_aux(num//10,nuevo+(num%10)*(10**cont),cont+1)

#-----------------------------------------------------------------------------------

def pares(lista):
    if isinstance(lista,list):
        print ("Pares:",pares_aux(lista,len(lista),0,[]))
        print ("Impares:",impares_aux(lista,len(lista),0,[]))
    else:
        return "Error, Debe ser una lista"

def pares_aux(lista,largo,indice,pares):
    if indice==largo:
        return pares 
    elif isinstance (lista[indice],list):
        return (pares_aux(lista[indice],len(lista[indice]),0,pares)) + pares_aux(lista,largo,indice+1,[])
    else:
        if lista[indice]%2==0:
            return pares_aux(lista,largo,indice+1,pares+[lista[indice]])
        else:
            return pares_aux(lista,largo,indice+1,pares,)

def impares_aux(lista,largo,indice,impares):
    if indice==largo:
        return impares 
    elif isinstance (lista[indice],list):
        return (impares_aux(lista[indice],len(lista[indice]),0,impares)) + impares_aux(lista,largo,indice+1,[])
    else:
        if lista[indice]%2!=0:
            return impares_aux(lista,largo,indice+1,impares+[lista[indice]])
        else:
            return impares_aux(lista,largo,indice+1,impares,)


