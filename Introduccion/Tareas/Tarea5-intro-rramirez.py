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
