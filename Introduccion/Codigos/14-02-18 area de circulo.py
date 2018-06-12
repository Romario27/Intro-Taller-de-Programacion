import math
def areacirculo ():
    radio= input ("Digite el valor del radio:")
    radio1= int(radio)
    area=0
    if radio1>0:
        area= math.pi*(radio1**2)
        print ("El valor del area es:", area)
    else:
        return areacirculo()     
