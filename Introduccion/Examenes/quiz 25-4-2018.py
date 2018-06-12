def mayores(num,lista):
    if isinstance(lista,list) and isinstance(num,int):
        return mayores_aux(num,lista,0,0)
    else:
        return "Debe insertar valores validos"

def mayores_aux(num,lista,indice,contador):
    if indice==len(lista):
        return contador    
    else:
        if lista[indice]>num:
            return mayores_aux(num,lista,indice+1,contador+1)
        else:
            return mayores_aux(num,lista,indice+1,contador)
