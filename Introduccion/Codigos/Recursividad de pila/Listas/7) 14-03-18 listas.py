#--------------------------tarea de intro----------------------------------
def suma(lista):
    if isinstance(lista,list):
        return suma_aux(lista)
    else:
        return "Error. debe ingresar una lista"

def suma_aux(lista):
    if lista==[]:
        return 0
    else:
        return lista[0]+suma_aux(lista[1:])

#-----------------solo pares es tarea de intro-------------------------------------

def sumapares_impares(lista):
    if isinstance(lista,list):
        print( "La suma de los pares es:",sumapares_aux(lista), "y", "La suma de los impares es",sumaimpares_aux(lista))
    else:
        return "Error. debe ingresar una lista"
    
def sumapares_aux(lista):
    if lista==[]:
        return 0
    else:
        if lista[0]%2==0:
            return lista[0]+sumapares_aux(lista[1:])
        else:
            return sumapares_aux(lista[1:])

def sumaimpares_aux(lista):
    if lista==[]:
        return 0
    else:
        if lista[0]%2!=0:
            return lista[0]+sumaimpares_aux(lista[1:])
        else:
            return sumaimpares_aux(lista[1:])
    
#--------------------------------tarea de taller-------------------------------
def ceros(lista):
    if isinstance(lista,list):
        return ceros_aux(lista)
    else:
        return "Error. debe ingresar una lista"
def ceros_aux(lista):
    if lista==[]:
        return False
    else:
        if lista[0]==0:
            return True
        else:
            return ceros_aux(lista[1:])

#-------------------------------------------------------------
def positivos(lista):
    if isinstance(lista,list):
        return positivos_aux(lista)
    else:
        return "Error. debe ingresar una lista"

def positivos_aux(lista):
    if lista==[]:
        return True
    else:
        if lista[0]<0:
            return False
        else:
            return positivos_aux(lista[1:])
#-----------------------------tarea de taller------------------------

def eliminar(lista,dig):
    if isinstance(lista,list) and isinstance(dig,int):
        return eliminar_aux(lista,dig)
    else:
        return "Error. debe ingresar una lista"

def eliminar_aux(lista,dig):
    if lista==[]:
        return []
    else:
        if lista[0]==dig:
            return eliminar_aux(lista[1:],dig)
        else:
            return [lista[0]]+ eliminar_aux(lista[1:],dig)

