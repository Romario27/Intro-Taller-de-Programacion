class sumando:
    def __init__(self):
        pass
    
    def ingrese(self):
        temp=True
        suma=0
        while temp:
            num=int(input("ingrese el numero:"))
            suma+=num
            if num==0:
                temp=False
                print("la suma final es:",suma)
        
