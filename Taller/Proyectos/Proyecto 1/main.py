import pygame
from pygame.locals import *
from inputbox import *
import sys
from tkinter import *
import time
import threading
import json
global segundos
global Usuarios
global direccion
global direccion1
Usuarios=[]
segundos=80
listaenemigo=[]
direccion="up"
direccion1="up"

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0,255, 0)

class Bloque(pygame.sprite.Sprite):
    def __init__(self, color, width, height,image):
        # Llama a la clase constructor padre (Sprite)
        super().__init__()

        # Crea una imagen del bloque y lo rellena de color.
        # También podríamos usar una imagen guardada en disco.
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load(image)
        #self.image.fill(color)

        self.rect = self.image.get_rect()

#----------------------class jugador-----------------------------
class jugador(pygame.sprite.Sprite):
    global segundos
    def __init__(self,posx,posy,selec1):
        pygame.sprite.Sprite.__init__(self)

        self.autoderecha= pygame.image.load(selec1)
        self.rect=self.autoderecha.get_rect()
##        self.rect.centerx=220
##        self.rect.centery=290

        self.rect.top= posy
        self.rect.left= posx

        self.listaDisparo=[]

        self.velocidad=5
        self.tiempo=segundos

    def movimientoderecha(self,direccion):
        self.velocidad=5
        if direccion=="right":
            self.rect.right+=self.velocidad
            self.tiempo = segundos
            if self.tiempo-segundos>=0.2:
                self.velocidad+=3
                self.rect.right+=self.velocidad
                self.tiempo = segundos

    def movimientoizquierda(self,direccion):
        self.tiempo = segundos
        self.velocidad=5
        if direccion=="left":
            self.rect.right-=self.velocidad
            self.tiempo = segundos
            if self.tiempo-segundos>=0.2:
                self.velocidad+=3
                self.rect.right-=self.velocidad
                self.tiempo = segundos
            

    def movimientoarriba(self,direccion):
        self.velocidad=5
        if direccion=="up":
            self.rect.top-=self.velocidad
            self.tiempo = segundos
            if self.tiempo-segundos>=0.2:
                self.velocidad+=3
                self.rect.top-=self.velocidad
                self.tiempo = segundos

    def movimientoabajo(self,direccion):
        self.velocidad=5
        if direccion=="down":
            self.rect.top+=self.velocidad
            self.tiempo = segundos
            if self.tiempo-segundos>=0.2:
                self.velocidad+=3
                self.rect.top+=self.velocidad
                self.tiempo = segundos

    def disparar(self,x,y,direccion):
        miproyectil=proyectil(x,y,"bala.png",True,direccion)
        self.listaDisparo.append(miproyectil)

    def dibujar (self,superficie,direccion):
        if direccion=="right":
            self.imagencarro=pygame.transform.rotate(self.autoderecha, -90)
              
        if direccion=="left":
            self.imagencarro=pygame.transform.rotate(self.autoderecha, 90)

        if direccion=="up":
            self.imagencarro=self.autoderecha

        if direccion=="down":
            self.imagencarro=pygame.transform.rotate(self.autoderecha, 180)
            
        #self.imagencarro=self.listaimagenes[self.posimagen]
        superficie.blit(self.imagencarro,self.rect)

#----------------------class proyectil-----------------------------
class proyectil(pygame.sprite.Sprite):
    def __init__(self,posx,posy,ruta,personaje,direccion):
        pygame.sprite.Sprite.__init__(self)
        self.proyectil=pygame.image.load(ruta)
        
        self.rect=self.proyectil.get_rect()
        self.velocidadDisparo=7

        self.direccion=direccion

        self.rect.top= posy
        self.rect.left= posx

        self.disparopersonaje=personaje         # es para detectar quien disparo
        
    def trayectoria(self):
        if self.disparopersonaje==True:
            if self.direccion=="up":
                self.rect.top= self.rect.top-self.velocidadDisparo
            elif self.direccion=="down":
                self.rect.top= self.rect.top+self.velocidadDisparo
            elif self.direccion=="left":
                self.rect.left= self.rect.left-self.velocidadDisparo
            elif self.direccion=="right":
                self.rect.left= self.rect.left+self.velocidadDisparo

    def dibujar(self,superficie):
        superficie.blit(self.proyectil,self.rect)

#----------------------class time-----------------------------

class timeup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
    def timer(self):
        global segundos
        segundos=int(segundos)
        m=0
        if segundos!=0:
            segundos= segundos-1
            time.sleep(1)
            x=timeup()
            return x.timer()

    def conteo(self):
        global n
        if n!=0:
            n=n-1
            time.sleep(1)
            print(n)
            return conteo(self)
        else:
            n="GO!"

#----------------------class registro-----------------------------
class registro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


    def pantalla1(self):
        def texto():
            mitexto=ment.get()
            mietiqueta2= Label(mGui,text=mitexto).pack()
            return mitexto
        
        mGui=Tk()
        ment= StringVar()
        #mGui.minsize(largo,ancho)
        mGui.geometry("600x600+500+300")
        mGui.title("proyecto")


        mietiqueta=Label(mGui,text="My Label").pack()
        boton=Button(mGui,text="ok",command=texto(),fg="red",bg="blue").pack()
        Entrada=Entry(mGui,textvariable=ment).pack()

        
#----------------------class oponente-----------------------------

class oponente(pygame.sprite.Sprite):
    def __init__(self,posx,posy,selec1):
        pygame.sprite.Sprite.__init__(self)

        self.auto1= pygame.image.load(selec1)
        self.rect=self.auto1.get_rect()

        self.rect.top= posy
        self.rect.left= posx

        self.mov=5
        self.apunta="up"


    def opone(self,x):
        if self.rect.left==170:
            self.rect.top-=self.mov
            self.apunta="up"
            if self.rect.top==65:
                self.rect.left+=1
        if self.rect.top==65:
            self.rect.left-=self.mov
            self.apunta="left"
            if self.rect.left==56:
                self.rect.top+=1
        if self.rect.left==56:
            self.rect.top+=self.mov
            self.apunta="down"
            if self.rect.top==516:
                self.rect.left+=1
        if self.rect.top==516:
            self.rect.left+=self.mov
            self.apunta="right"
            if self.rect.left==527:
                self.rect.top+=1
        if self.rect.left==527:
            self.rect.top-=self.mov
            self.apunta="up"
            if self.rect.top==67:
                self.rect.left+=1
        if self.rect.top==67:
            self.rect.left-=self.mov
            self.apunta="left"
            if self.rect.left==288:
                self.rect.top+=1
        if self.rect.left==288:
            self.rect.top+=self.mov
            self.apunta="down"
            if self.rect.top==208:
                self.rect.left+=1
        if self.rect.top==208:
            self.rect.left+=self.mov
            self.apunta="right"
            if self.rect.left==434:
                self.rect.top+=1
        if self.rect.left==434:
            self.rect.top+=self.mov
            self.apunta="down"
            if self.rect.top==404:
                self.rect.left+=1
        if self.rect.top==404:
            self.rect.left-=self.mov
            self.apunta="left"
            if self.rect.left==170:
                self.rect.top+=1



    def dibujar (self,superficie):
        if self.apunta=="right":
            self.imagenauto1=pygame.transform.rotate(self.auto1, -90)
              
        if self.apunta=="left":
            self.imagenauto1=pygame.transform.rotate(self.auto1, 90)

        if self.apunta=="up":
            self.imagenauto1=self.auto1

        if self.apunta=="down":
            self.imagenauto1=pygame.transform.rotate(self.auto1, 180)
            
        superficie.blit(self.imagenauto1,self.rect)
        
#----------------------class imprimir-----------------------------
    
class imprimir():
    def __init__(self):
        pass
    def registro_nombre(self,nombre,punt):
        global Usuarios
        Usuarios+=[{"nombre":nombre,"puntaje":punt}]
        datos = json.dumps(Usuarios)
        f=open("Usuarios.json","w")
        f.write(datos)
        f.close()



pygame.init()



# Establecemos el largo y alto de la pantalla
ancho_pantalla = 600
alto_pantalla = 600
pantalla = pygame.display.set_mode([ancho_pantalla, alto_pantalla])
pygame.display.set_caption("Proyecto #1")

fondo = pygame.image.load("pista.png").convert_alpha()
menu = pygame.image.load("fondo menu.png").convert_alpha()


final= False
r1=pygame.Rect(0,0,600,600)
reloj = pygame.time.Clock()

peque=pygame.font.SysFont("Times New Roman",40)
media=pygame.font.SysFont("Times New Roman",50)
grande=pygame.font.SysFont("Times New Roman",70)

font=pygame.font.SysFont("Times New Roman",40)
pygame.key.set_repeat(1,20)
vel=4
##direccion="up" 
##direccion1="up"




 
def objetotexto(texto,color,tamaño):
    if tamaño == "pequeño":
        textosuperficie=peque.render(texto,True,color)
    if tamaño == "mediano":
        textosuperficie=media.render(texto,True,color)
    if tamaño == "grande":
        textosuperficie=grande.render(texto,True,color)
    return textosuperficie, textosuperficie.get_rect()


def mensaje(msg,color,desplazamientoY=0,tamaño="pequeño"):
    textosuperficie,textoRect=objetotexto(msg,color,tamaño)
    textoRect.center=(ancho_pantalla/2),(alto_pantalla/2)+desplazamientoY
    pantalla.blit(textosuperficie,textoRect)


    
def introduccion():
    introjuego=True


#bucle principal
while not final:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            final = True

        if event.type == pygame.QUIT:
            introjuego=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                escoger_usuario()
                introjuego = False
            if event.key==pygame.K_SPACE:
                registro_usuario()
                introjuego = False
            if event.key==pygame.K_ESCAPE:
                final = True
        pantalla.blit(menu, (0,0))
        mensaje("DEATH RACE",NEGRO,-250,tamaño="grande")
        mensaje("Precione Enter para empezar",NEGRO,200,tamaño="pequeño")
        mensaje("Precione Space para registrar un usuario",NEGRO,240,tamaño="pequeño")
        mensaje("Precione ESC para salir del juego",NEGRO,280,tamaño="pequeño")
        pygame.display.update()
        reloj.tick(15)

        def registro_usuario():
            R=imprimir()
            retroceso=True
            regis=registro()
            while retroceso:
                for event in pygame.event.get():
##                    regis.pantalla1()
                        if event.type == pygame.QUIT:
                            retroceso=False
                        if retroceso ==True:
                            
                            screenSize(600,600)
                            wordBox = makeTextBox(150, 80, 300, 0, "Registre el Usuario", 10, 24)
                            showTextBox(wordBox)
                            entry = textBoxInput(wordBox)
                            R.registro_nombre(entry,0)
                            
                        if event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_RETURN:
                                print(Usuarios)
                                introduccion()
                                retroceso = False
            
                pygame.display.update()
                reloj.tick(15)

        def escoger_usuario():
            salir1=True
            while salir1:
                if Usuarios==[]:
                    for event in pygame.event.get():
                        if event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_RETURN:
                                time.sleep(1)
                                introduccion()
                                salir1 = False
                    pantalla.fill(BLANCO)
                    mensaje("No hay usuarios registrados",VERDE,-100,tamaño="mediano")
                    pygame.display.update()
                else:
                    for event in pygame.event.get():
                        if event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_RETURN:
                                for usuario in Usuarios:
                                    print("al",usuario)
                    
                                  
                                mensaje1=media.render(usuario["nombre"],1,NEGRO)
                                pantalla.blit(mensaje1,(15,150))
                                time.sleep(2)
                                gameloop() 
                                salir1=False
                    pantalla.fill(BLANCO)
                    mensaje("Seleccione el usuario",ROJO,-250,tamaño="mediano")
                    mensaje("a utilizar",ROJO,-200,tamaño="mediano")
                    pygame.display.update()

        def gameloop():
            global direccion
            global direccion1
            

            protagonista=jugador(200,280,"carro.png")
            protagonista1=jugador(170,330,"opo2.png")
            enemigo=oponente(170,280,"opo1.png")
            listaenemigo.append(enemigo)
            enemigo1=oponente(170,330,"opo2.png")
            listaenemigo.append(enemigo1)

            tup=timeup()
            
            salir=False
            global segundos
            hilo= threading.Thread(target=tup.timer,args=())
            hilo.start()
            tiempo = segundos
            
            while not salir:
                if segundos!=0:
                    hilor1= threading.Thread(target=enemigo.opone(False),args=())
                    hilor1.start()
                    hilor2= threading.Thread(target=enemigo1.opone(True),args=())
                    hilor2.start()

                for event in pygame.event.get():                    
                    if event.type == pygame.QUIT:
                        salir = True
                    elif segundos==0:
                        mensaje("Fin de la partida",NEGRO,-100,tamaño="grande")
                        time.sleep(1)
                        salir = True
                        introduccion()

   
                    if event.type==pygame.KEYDOWN:
                        if event.key==K_RIGHT:
                            direccion="right"
                            protagonista.movimientoderecha(direccion)

                        elif event.key==K_LEFT:
                            direccion="left"
                            protagonista.movimientoizquierda(direccion)

                        elif event.key==K_UP:
                            direccion="up"
                            protagonista.movimientoarriba(direccion)

                        elif event.key==K_DOWN:
                            direccion="down"
                            protagonista.movimientoabajo(direccion)
                        elif event.key==K_SPACE:
                            x,y=protagonista.rect.center
                            protagonista.disparar(x,y,direccion)



                    if event.type==pygame.KEYDOWN:
                        if event.key==K_d:
                            direccion1="right"
                            protagonista1.movimientoderecha(direccion1)

                        elif event.key==K_a:
                            direccion1="left"
                            protagonista1.movimientoizquierda(direccion1)

                        elif event.key==K_w:
                            direccion1="up"
                            protagonista1.movimientoarriba(direccion1)

                        elif event.key==K_s:
                            direccion1="down"
                            protagonista1.movimientoabajo(direccion1)
                        elif event.key==K_q:
                            x,y=protagonista1.rect.center
                            protagonista1.disparar(x,y,direccion1)

                #fondo de la pantalla
                pygame.draw.rect(pantalla,BLANCO, r1)
                pantalla.blit(fondo, (0,0))

                if protagonista.rect.colliderect(r1):
                    protagonista.velocidad=0

                if len(protagonista1.listaDisparo)>0:
                    for x in protagonista1.listaDisparo:
                        x.dibujar(pantalla)
                        x.trayectoria()

                if len(protagonista.listaDisparo)>0:
                    for x in protagonista.listaDisparo:
                        x.dibujar(pantalla)
                        x.trayectoria()

                        if x.rect.top<0:                    #delimita a dnd se quiere eliminar el proyectil una ves salido de la pantalla
                            protagonista.listaDisparo.remove(x)

                        elif x.rect.top>600:                    #delimita a dnd se quiere eliminar el proyectil una ves salido de la pantalla
                            protagonista.listaDisparo.remove(x)

                        elif x.rect.left<0:                    #delimita a dnd se quiere eliminar el proyectil una ves salido de la pantalla
                            protagonista.listaDisparo.remove(x)

                        elif x.rect.left>600:                    #delimita a dnd se quiere eliminar el proyectil una ves salido de la pantalla
                            protagonista.listaDisparo.remove(x)

##                        else:
##                            for enemigo in listaenemigo:                codigo para las coliciones
##                                if x.rect.colliderect(enemigo.rect):
##                                    listaenemigo.remove(enemigo)
##                                    protagonista.listaDisparo.remove(x)
                            
                #protagonista.dibujar(pantalla)
                enemigo.dibujar(pantalla)
                enemigo1.dibujar(pantalla)
                    
                if protagonista.rect.left>= ancho_pantalla or protagonista.rect.left<0 or protagonista.rect.top>=alto_pantalla or protagonista.rect.top<0:
                    mensaje("Game Over",NEGRO,-100,tamaño="grande")
                    time.sleep(1)
                    salir=True
                        
                if segundos==0:
                    mensaje("Fin de la partida",NEGRO,-100,tamaño="grande")
                    
                #temporizador
                cronometro=font.render("00:"+str(segundos),0,(ROJO))
                pantalla.blit(cronometro,(10,5))
           

                protagonista.dibujar(pantalla,direccion)
                protagonista1.dibujar(pantalla,direccion1)
                
                pygame.display.update()
                reloj.tick(35)
            
    
pygame.display.update()
pygame.quit()
