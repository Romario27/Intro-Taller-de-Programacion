class Invertir:
    def __init__(self):
        pass    #es como decir que pase

    def invertido(self,lista):
        if isinstance(lista,list):
            return self.invertido_aux(lista)
        else:
            return "Error. debe ingresar una lista"

    def invertido_aux(self,lista):
        if lista==[]:
            return []
        else:
            return [lista[-1]]+self.invertido_aux(lista[:-1])
