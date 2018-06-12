def may_men(lista):
    if isinstance(lista,list):
        print ("Mayor:",may(lista,1,lista[0],len(lista)),
               ",", "Menor:",men(lista,1,lista[0],len(lista)))
    else:
        return "Debe insertar una lista"

def may(lista,indice,result,largo):
    if indice==largo:
        return result    
    else:
        if result>lista[indice]:
            return may(lista,indice+1,result,largo)
        else:
            return may(lista,indice+1,lista[indice],largo)
    
def men(lista,indice,result,largo):
    if indice==largo:
        return result    
    else:
        if result<lista[indice]:
            return men(lista,indice+1,result,largo)
        else:
            return men(lista,indice+1,lista[indice],largo)

#------------------------------------------------------------------------

def may_men_1(lista):
    if isinstance(lista,list):
        print ("Mayor:",may_1(lista[1:],lista[0]),
               ",", "Menor:",men_1(lista[1:],lista[0]))
    else:
        return "Debe insertar una lista"

def may_1(lista,result):
    if lista==[]:
        return result    
    else:
        if result>lista[0]:
            return may_1(lista[1:],result)
        else:
            return may_1(lista[1:],lista[0])
    
def men_1(lista,result):
    if lista==[]:
        return result    
    else:
        if result<lista[0]:
            return men_1(lista[1:],result)
        else:
            return men_1(lista[1:],lista[0])
            
