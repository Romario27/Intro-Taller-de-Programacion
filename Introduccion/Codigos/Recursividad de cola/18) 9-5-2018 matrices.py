# suma los valores de una matriz y saca el promedio

def suma_matriz(matriz):
    if isinstance(matriz,list) and matriz!=[]:
        return matriz_aux(matriz,len(matriz),len(matriz[0]),0,0,0)
    else:
        return "Ingrese Valores validos"


def matriz_aux(matriz,numfila,numcolum,fila, columna,suma):
    if fila==numfila:
        print ("La suma es:", suma)
        print ("El promedio es:",suma/(numfila*numcolum))
    elif columna==numcolum:
        return matriz_aux(matriz,numfila,numcolum,fila+1,0,suma)
    else:
        return matriz_aux(matriz,numfila,numcolum,fila,columna+1,suma+matriz[fila][columna])
    
#-----------------------------------------------------------------------------------------------

#Funcion que transforma una matriz en una matriz traspuesta


def traspuesta(matriz):
    if isinstance(matriz,list) and matriz!=[]:
        return matriz_aux(matriz,len(matriz),len(matriz[0]),0,0,0)
    else:
        return "Ingrese Valores validos"

def traspuesta_aux():
    
    
    
    
