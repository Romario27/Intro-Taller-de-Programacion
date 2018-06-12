def ordenar(lista):
    if isinstance(lista,list):
        return ordenar_aux(lista,0,0)
    else:
        return "Debe ingresar una lista"

def ordenar_aux(lista,indice1,indice2):
    if indice2==len(lista)-1:
        return lista
    elif indice1==len(lista)-1:
        return ordenar_aux(lista,0,indice2+1)
    if lista[indice1]>lista[indice1+1]:
        aux=lista[indice1]
        lista[indice1]=lista[indice1+1]
        lista[indice1+1]=aux
        return ordenar_aux(lista,indice1+1,indice2)
    else:
        return ordenar_aux(lista,indice1+1,indice2)

#-------------------------------------------------------------

def suma_matriz(num,matriz):
    if isinstance(matriz,list) and matriz!=[] and isinstance (num,int):
        return matriz_aux(num,matriz,len(matriz),len(matriz[0]),0,0)
    else:
        return "Ingrese Valores validos"

def matriz_aux(num,matriz,numfilas,numcolumnas,fila, columna):
    if fila==numfilas:
        return matriz
    elif columna==numcolumnas:
        return matriz_aux(num,matriz,numfilas,numcolumna,fila+1,0)
    else:
        return matriz_aux(num,matriz[fila][columna]+num,numfilas,numcolumna,fila,columna+1)

