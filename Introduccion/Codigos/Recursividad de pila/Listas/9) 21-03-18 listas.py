def primo (num):
    #num=int(input("Digite el numero:"))
    if isinstance (num,int) and num>0:
        if num==0 or num==1:
            return True
        else:
            return primo_aux (num,num-1) 
    else:
        print ("Hay un valor dentro de la lista que es invalido:", num)

def primo_aux(num,x):
    if x==1:
        return True
    elif num%x==0:
        return False
    else:
        return primo_aux(num,x-1)

def val_primo(lista):
    if isinstance(lista,list):
        return val_primo_aux(lista)
    else:
        return "Error. debe ingresar una lista"

def val_primo_aux(lista):
    if lista==[]:
        return []
    else:
        if primo(lista[0])!=True:
            return val_primo_aux(lista[1:])
        else:
            return [lista[0]]+val_primo_aux(lista[1:])
    
