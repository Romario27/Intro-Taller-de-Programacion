class Operaciones:
    def __init__(self):
        pass

    def contar (self):
        num=int(input("ingrese el numero:"))
        cont=0
        while num!=0:
            cont+=1
            num=num//10
        print("Tiene",cont,"digitos")


    def ordenar(self,lista):
        ind1=0
        ind2=1

        while ind2<len(lista):
            if lista [ind1]<lista[ind2]:
                ind1+=1
                ind2+=1
            else:
                lista=lista[ind1:]+lista[ind2]+lista[ind1]+lista[:ind2]
                ind1=0
                ind2=1
        print(lista)


    
    
    def multi(self,matriz1,matriz2):
        numfilas=len(matriz1)
        numcolumnas=len(matriz1[0])
        cont1=0
        cont2=0
        nueva=[]
        temp=[]
        suma=0
        cont3=0
        for i in matriz1:
            for j in matriz1:
                for m in matriz1[cont3]:
                    suma+=m*matriz2[cont1][cont2]
                    cont1+=1
                temp+=[suma]
                cont1=0
                cont2+=1
                suma=0
            nueva+=[temp]
            temp=[]
            cont3+=1
            cont2=0
        print("El resultado de la nueva matriz es:", nueva)
                
