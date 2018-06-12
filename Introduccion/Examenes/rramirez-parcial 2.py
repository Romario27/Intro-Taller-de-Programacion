#1)
def invertir (lista):
    if isinstance(lista,list):
        return invertir_aux(lista
    else:
        return "debe ingresar una lista"

def invertir_aux(lista):

#----------------------------------------------------

#2.1


def consecutivos(matriz):
    if isinstance(matriz,list) and len(matriz)==len(matriz[0]):
        return consecutivos_aux(matriz,len(matriz),1,0,0)
    else:
        return "debe ingresar una matriz correcta"

def consecutivos_aux(matriz,num,ind,contcolum,contfila):
    if ind==(num**2)+1:
        return True
    elif contcolum==len(matriz):
        if contfila==num-1:
            return False
        else:
            return consecutivos_aux(matriz,num,ind,0,contfila+1)
    elif ind==matriz[contcolum][contfila]:
        return consecutivos_aux(matriz,num,ind+1,0,0)
    else:
        return consecutivos_aux(matriz,num,ind,contcolum+1,contfila)

#------------------------------------------------------------------------------

#2.2

def es_magico(matriz):
    if isinstance(matriz,list) and len(matriz)==len(matriz[0]):
        if suma_fila(matriz)

def suma_fila(matriz,result,cont):


#*-------------------------------------------------------------------------


def rotar(matriz):
    if isinstance(matriz,list):
        return rotar_aux(matriz,[],[],len(matriz),len(matriz[0]))
    else:
        return "debe ingresar una matriz"


def rotar_aux(lista,nueva,temp,fila,columna):
    if len(nueva)==len(matriz[0]):
        return nueva
    elif

        
            
                
                 
