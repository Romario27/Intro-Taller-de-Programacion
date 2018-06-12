#---------------tarea 3 intro, solo minimo----------------------------------
def minmax(lista):
    if isinstance(lista,list):
        print ("El valor minimo de la lista es:", minimo_aux(lista),"y", "El valor maximo de la lista es:", maximo_aux(lista))
    else:
        return "Error. debe ingresar una lista"


def minimo_aux(lista):
    if len(lista)!=1:
        if lista[0]<lista[1]:
            #lista.remove(lista[1])
            return minimo_aux([lista[0]]+lista[2:])
        else:
            #lista.remove(lista[0])
            return minimo_aux(lista[1:])
    else:
        return lista[0]


def maximo_aux(lista):
    if len(lista)!=1:
        if lista[0]>lista[1]:
            #lista.remove(lista[1])
            return maximo_aux([lista[0]]+lista[2:])
        else:
            #lista.remove(lista[0])
            return maximo_aux(lista[1:])
    else:
        return lista[0]
#-------------------------tarea 3 intro----------------------------------
import math
def suma(lista):
    if isinstance(lista,list):
        return suma_aux(lista)
    else:
        return "Error. debe ingresar una lista"

def suma_aux(lista):
    if lista==[]:
        return 0
    else:
        return math.sqrt(lista[0]) + suma_aux(lista[1:])
