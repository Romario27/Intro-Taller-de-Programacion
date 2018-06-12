def formarLista(num):
    if isinstance (num,int) and num>0:
        return formarLista_aux(num)
    else:
        return "Debe ser un numero entero mayor a cero"

def formarLista_aux(num):
    if num==0:
        return []
    else:
        if (num%10)%2==0 or num%10==0:
            return [num%10] + formarLista_aux(num//10)
        else:
            return formarLista_aux(num//10)

#----------------------------------------------------------------

def palindromo(num):
    if isinstance (num,int) and num>0:
        if palindromo_aux(num,largo(num))==num:
            return True
        else:
            return False
    else:
        return "Debe ser un numero entero mayor a cero"

def palindromo_aux(num,pot):
    if num==0:
        return 0
    else:
        return (num%10)*(10**(pot-1))+ palindromo_aux(num//10,pot-1)


def largo(num):
    if num==0:
        return 0
    else:
        return 1 + largo(num//10)
#-------------------------------------------------------------------------


def contarConsonantes (cadena):
    if isinstance (cadena, str):
        return contarConsonantes_aux(cadena)
    else:
        return "Debe ser un string"

def contarConsonantes_aux(cadena):
    if cadena=='':
        return 0
    else:
        if cadena[0]=='a' or cadena[0]=='e' or cadena[0]=='i' or cadena[0]=='o' or cadena[0]=='u':
            return contarConsonantes_aux(cadena[1:])
        else:
            return 1 + contarConsonantes_aux(cadena[1:])

#---------------------------------------------------------------------------

def intercambiar(lista):
    if isinstance (lista,list):
        return intercambiar_aux(lista)
    else:
        return "Debe ser una lista"

def intercambiar_aux(lista):
    if lista ==[]:
        return []
    else:
        return [lista[1]] + [lista[0]] + intercambiar_aux(lista[2:])
