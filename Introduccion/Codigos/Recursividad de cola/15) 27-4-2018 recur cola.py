def busqueda(num, lista):
    if isinstance(lista,list)and isinstance (num,int):
        return busqueda_aux(num,lista,0)
    else:
        return "Debe insertar valores validos"

def busqueda_aux(num,lista,indice):
    if indice==len(lista):
        return False
    else:
        if num==lista[indice]:
            return True
        else:
            return busqueda_aux(num,lista,indice+1)

#-----------------------------------------------------------    

def lineal(num, lista):
    if isinstance(lista,list)and isinstance (num,int):
        return lineal_aux(num,lista)
    else:
        return "Debe insertar valores validos"

def lineal_aux(num,lista):
    if lista==[]:
        return False
    else:
        if num==lista[0]:
            return True
        else:
            return lineal_aux(num,lista[1:])
#-----------------------------------------------------------


def busq_binaria(num, lista):
    if isinstance(lista,list)and isinstance (num,int):
        return busq_binaria_aux(num,lista,len(lista)//2)
    else:
        return "Debe insertar valores validos"

def busq_binaria_aux(num,lista,indice):
    if lista==[]: 
        return False
    elif lista[indice]==num:
        return True
    elif lista[indice]<num:
        return busq_binaria_aux(num,lista[(indice)+1:],len(lista[:indice])//2)
    else:
        return busq_binaria_aux(num,lista[:indice],len(lista[:indice])//2)
