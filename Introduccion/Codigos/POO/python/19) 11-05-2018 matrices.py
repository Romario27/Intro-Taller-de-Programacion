class Matriz:
    def __init__(self):
        pass
    def construccion_matriz(self, num):
        return self.construccion_matriz_aux(num,[],[])

    def construccion_matriz_aux(self,num,matriz,temp):
        if len(matriz)==num and len(matriz[0])==num:
            return matriz
        elif len(temp)==num:
            return self.construccion_matriz_aux(num,matriz+[temp],[])
        elif len(temp)<num and len(matriz)==0 or len(matriz)==num-1:
            return self.construccion_matriz_aux(num,matriz,temp+["*"])
        elif len(temp)<num and len(temp)==0 or len(temp)==num-1:
            return self.construccion_matriz_aux(num,matriz,temp+["*"])
        elif len(temp)<num:
            return self.construccion_matriz_aux(num,matriz,temp+[0])
        elif len(temp)==0 and len(matriz)==1 or len(temp)==num-1:
            return self.construccion_matriz_aux(num,matriz,temp+["*"])

