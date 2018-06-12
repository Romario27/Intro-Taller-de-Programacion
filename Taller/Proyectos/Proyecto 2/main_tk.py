from tkinter import *
import random
import os
import json
import loop_1
global Usuarios
Usuarios=[]

windowA=Tk()
windowA.title("DEATH RACE")
windowA.minsize(600,600)
windowA.resizable(width=False, height=False) #hace q la persona no pueda editar
windowA.geometry("400x400+200+150")  #coordenadas y tamaño de la ventana

def esconder(ventanaA, ventanaB):
    ventanaA.deiconify()
    ventanaB.withdraw()

def Registrar():
    def registro_nombre():
        global Usuarios
        texto=e.get()
        print(texto)
        Usuarios+=[{"nombre":texto,"puntaje":0}]
        datos = json.dumps(Usuarios)
        f=open("Usuarios.json","w")
        f.write(datos)
        f.close()
        mietiqueta2= Label(ventanaB,text="Usuario Registrado").pack()
    
    

    windowA.withdraw()
    ventanaB=Tk()  # crea una ventana secundaria
    ventanaB.title("DEATH RACE")
    ventanaB.maxsize(600,600)
    ventanaB.geometry("600x600+300+225")
    ventanaB.resizable(width=False, height=False)
    boton_menu=Button(ventanaB, width=8, height=2,
                  command=lambda:esconder(windowA, ventanaB),text="MENU")
    boton_menu.place(x=270,y=500)
    #nombre= StringVar()
    #Entrada=Entry(ventanaB)#.place(x=230,y=100)
    e = Entry(ventanaB,width=20)
    e.pack(side=RIGHT, expand=YES)#, fill=X)
    e.focus_set()
    #print(Entrada.get())
    boton_registrar=Button(ventanaB, width=15, height=2,
                    command=registro_nombre,text="Registrar Usuario",font=("Arial",15),fg="white",bg="black")
    boton_registrar.place(x=210,y=350)


def ver_puntajes():
    windowA.withdraw()
    ventanaD=Tk()  # crea una ventana secundaria
    ventanaD.title("DEATH RACE")
    ventanaD.maxsize(600,600)
    ventanaD.geometry("600x600+300+225")
    ventanaD.resizable(width=False, height=False)
    boton_menu=Button(ventanaD, width=8, height=2,
                  command=lambda:esconder(windowA, ventanaD),text="MENU")
    datos=open("Usuarios.json","r")
    info=json.load(datos)
    datos.close()
    for usuario in info:
        print("-",usuario["nombre"])
        print(usuario["puntaje"])
        mietiqueta2= Label(ventanaD,text=usuario["nombre"]).pack()
        mietiqueta1= Label(ventanaD,text=usuario["puntaje"]).pack()
    boton_menu.place(x=270,y=500)




def Escojer():
    windowA.withdraw()
    ventanaC=Tk()  # crea una ventana secundaria
    ventanaC.title("DEATH RACE")
    ventanaC.maxsize(600,600)
    ventanaC.geometry("600x600+300+225")
    ventanaC.resizable(width=False, height=False)
    boton_menu=Button(ventanaC, width=8, height=2,
                  command=lambda:esconder(windowA, ventanaC),text="MENU")
    boton_menu.place(x=270,y=500)
    #boton=Button(ventanaB,text="Registrar",command=registro_nombre,fg="white",bg="black").pack()
    boton_1jugador=Button(ventanaC, width=15, height=2,command=lambda:jugar(ventanaC,False),text="1 Jugador",fg="white",bg="black")
    boton_1jugador.place(x=250,y=100)

    boton_multijugador=Button(ventanaC, width=15, height=2,command=lambda:jugar(ventanaC,True),text="2 Jugadores",fg="white",bg="black")
    boton_multijugador.place(x=250,y=200)


"""
pygame
Cuando presionen ESC
# Matar pygame
self.windowA.deiconify()
"""

def jugar(ventanaC,selec):
    if selec==True:
        ventanaC.withdraw()
        loop_1.jugar_2()
    else:
        ventanaC.withdraw()
        loop_1.jugar_1()

def salir(ventanaA):
    ventanaA.withdraw()

titulo= Label(windowA,text="DEATH RACE",font=("Arial",50)).pack()
boton_Registro=Button(windowA, width=8, height=2,command=Registrar,text="Registrar")
boton_Registro.place(x=50,y=450)
boton_jugar=Button(windowA, width=8, height=2,command=Escojer,text="Jugar")
boton_jugar.place(x=270,y=450)
boton_Puntajes=Button(windowA, width=8, height=2,command=ver_puntajes,text="Puntajes")
boton_Puntajes.place(x=480,y=450)
boton_salir=Button(windowA, width=8, height=2,command=lambda:salir(windowA),text="Salir")
boton_salir.place(x=270,y=520)


windowA.mainloop()
