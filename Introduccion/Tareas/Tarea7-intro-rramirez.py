def validacion(matrizA,matrizB):
    if isinstance(matrizA,list) and isinstance(matrizA,list):
        if len(matrizA)==len(matrizB[0]):
            return suma(matrizA,matrizB,0,0,0,0,[],[])
        else:
            print ("Debe introducir matrices correctas")
    else:
        print("Debe intorducir matrices")

def suma(matrizA,matrizB,cont2,pos1,pos2,result,temp,nueva):
    if cont2==len(matrizB):
        return suma(matrizA,matrizB,0,pos1,pos2+1,0,temp+[result],nueva)
    elif len(temp)==len(matrizB[0]):  
        return suma(matrizA,matrizB,0,pos1+1,0,0,[],nueva+[temp])
    elif len(nueva)==len(matrizA) and len(nueva[0])==len(matrizB[0]):
        print (nueva)
    else:
        x=matrizA[pos1][cont2]
        y=matrizB[cont2][pos2]
        return suma(matrizA,matrizB,(cont2)+1,pos1,pos2,(result+(x*y)),temp,nueva)
    
        
