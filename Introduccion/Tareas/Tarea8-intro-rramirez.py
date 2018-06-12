class binaria_busq:
    def __init__(self):
        pass

    def busqueda(self,num,lista):
        temp=lista[len(lista)//2]
        cont=len(lista)//2
        while num!=temp:
            if temp<num:
                if len(lista)==1:
                    print (False)
                    break
                else:
                    lista=lista[cont:]
                    temp=lista[len(lista)//2]
                    cont=len(lista)//2
            else:
                lista=lista[:cont]
                temp=lista[len(lista)//2]
                cont=len(lista)//2
        if num==temp:
            print (True)


##El profesor me dio permiso de hacerlo con ciclo while
