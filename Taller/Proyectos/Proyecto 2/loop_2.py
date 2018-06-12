import pygame
from pygame.locals import *
from inputbox import *
import sys
from tkinter import *
import threading, json , time , loop_3
global segundos , minutos , Usuarios
global direccion, direccion1
Usuarios=[]
segundos=00
minutos=3
listaenemigo=[]
direccion="up"
direccion1="up"

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0,255, 0)

#----------------------class jugador-----------------------------
class jugador(pygame.sprite.Sprite):
    global segundos
    def __init__(self,posx,posy,selec1):
        pygame.sprite.Sprite.__init__(self)

        self.autoderecha= pygame.image.load(selec1)
        self.rect=self.autoderecha.get_rect()

        self.rect.top= posy
        self.rect.left= posx

        self.listaDisparo=[]

        self.velocidad=5
        self.tiempo=segundos
        self.puntuacion=0

        self.sonidoDisparo=pygame.mixer.Sound("disparo cañón.wav")
        self.sonidomotor=pygame.mixer.Sound("Auto Acelerando.wav")
        self.sonidomotor.set_volume(0.1)

    def movimientoderecha(self,direccion):
        if direccion=="right":
            self.rect.right+=self.velocidad
            self.sonidomotor.play()

    def movimientoizquierda(self,direccion):
        if direccion=="left":
            self.rect.right-=self.velocidad
            self.sonidomotor.play()
            

    def movimientoarriba(self,direccion):
        if direccion=="up":
            self.rect.top-=self.velocidad
            self.sonidomotor.play()

    def movimientoabajo(self,direccion):
        if direccion=="down":
            self.rect.top+=self.velocidad
            self.sonidomotor.play()

    def disparar(self,x,y,direccion):
        miproyectil=proyectil(x,y,"bala.png",True,direccion)
        self.listaDisparo.append(miproyectil)
        self.sonidoDisparo.play()

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
        global minutos
        minutos=int(minutos)
        while segundos!=0 or minutos!=0:
            if segundos!=0:
                segundos-=1
                time.sleep(1)
            else:
                minutos-=1
                segundos=59
        
#----------------------class oponente-----------------------------

class oponente(pygame.sprite.Sprite):
    def __init__(self,posx,posy,selec1):
        pygame.sprite.Sprite.__init__(self)

        self.auto1= pygame.image.load(selec1)
        self.rect=self.auto1.get_rect()

        self.rect.top= posy
        self.rect.left= posx

        self.mov=5
        self.apunta="down"


    def opone(self,x):
        if self.rect.left==55:
            self.rect.top+=self.mov
            self.apunta="down"
        if self.rect.top==555:
            self.rect.left+=self.mov
            self.apunta="right"
        if self.rect.left==165 and self.rect.top!=20:
            self.rect.top-=self.mov
            self.apunta="up"
        if self.rect.top==300 and self.rect.left!=55 :
            self.rect.left+=self.mov
            self.apunta="right"
        if self.rect.left==555:
            self.rect.top-=self.mov
            self.apunta="up"
        if self.rect.top==20:
            self.rect.left-=self.mov
            self.apunta="left"



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



class Escenario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.ancho_pantalla = 600
        self.alto_pantalla = 600
        self.pantalla = pygame.display.set_mode([self.ancho_pantalla, self.alto_pantalla])
        pygame.display.set_caption("DEATH RACE")

        self.fondo = pygame.image.load("pista2.png").convert_alpha()
        self.roca = pygame.image.load("roca.png").convert_alpha()
        self.rect=self.roca.get_rect()


        self.final= False
        self.r1=pygame.Rect(98,98,405,180)
        self.r2=pygame.Rect(98,278,40,228)
        self.r3=pygame.Rect(240,380,350,210)
        self.rf=pygame.Rect(0,0,600,600)
        self.meta= pygame.Rect(0,230,92,0.01)
        self.reloj = pygame.time.Clock()

        self.peque=pygame.font.SysFont("Times New Roman",40)
        self.media=pygame.font.SysFont("Times New Roman",50)
        self.grande=pygame.font.SysFont("Times New Roman",70)

        self.font=pygame.font.SysFont("Times New Roman",40)
        pygame.key.set_repeat(1,20)


    def objetotexto(self,texto,color,tamaño):
        if tamaño == "pequeño":
            textosuperficie=self.peque.render(texto,True,color)
        if tamaño == "mediano":
            textosuperficie=self.media.render(texto,True,color)
        if tamaño == "grande":
            textosuperficie=self.grande.render(texto,True,color)
        return textosuperficie, textosuperficie.get_rect()


    def mensaje(self,msg,color,desplazamientoY=0,tamaño="pequeño"):
        textosuperficie,textoRect=objetotexto(msg,color,tamaño)
        textoRect.center=(self.ancho_pantalla/2),(self.alto_pantalla/2)+desplazamientoY
        self.pantalla.blit(textosuperficie,textoRect)

    def next_level(self, condicion):
        if condicion==True:
            loop_3.jugar_2()
        else:
            loop_3.jugar_1()



def jugar_2():
    pygame.init()
    escenario=Escenario()
    global direccion ,direccion1
    protagonista=jugador(10,180,"carro.png")
    protagonista1=jugador(10,130,"opo2.png")
    enemigo=oponente(55,180,"opo2.png")
    listaenemigo.append(enemigo)
    enemigo1=oponente(55,130,"opo1.png")
    listaenemigo.append(enemigo1)

    tup=timeup()
    
    salir=False
    global segundos
    global minutos
    hilo= threading.Thread(target=tup.timer,args=())
    hilo.start()
    tiempo = segundos
    
    while not salir:
        if minutos!=0 or segundos!=0:
            hilor1= threading.Thread(target=enemigo.opone(False),args=())
            hilor1.start()
            hilor2= threading.Thread(target=enemigo1.opone(True),args=())
            hilor2.start()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            if minutos==0 and segundos==0:
                protagonista.sonidomotor.fadeout(100)
                protagonista1.sonidomotor.fadeout(100)
                escenario.mensaje("Fin de la partida",NEGRO,-100,tamaño="grande")
                time.sleep(1)
                salir = True
                escenario.next_level(True)
                


            key=pygame.key.get_pressed()
            if key[pygame.K_RIGHT]:
                direccion="right"
                protagonista.movimientoderecha(direccion)
            if key[pygame.K_LEFT]:
                direccion="left"
                protagonista.movimientoizquierda(direccion)
            if key[pygame.K_UP]:
                direccion="up"
                protagonista.movimientoarriba(direccion)
            if key[pygame.K_DOWN]:
                direccion="down"
                protagonista.movimientoabajo(direccion)
            if key[pygame.K_SPACE]:
                     x,y=protagonista.rect.center
                     protagonista.disparar(x,y,direccion)
            if event.type==pygame.KEYUP:
                if event.key==K_RIGHT:
                    protagonista.sonidomotor.fadeout(100)
                if event.key==K_LEFT:
                    protagonista.sonidomotor.fadeout(100)
                if event.key==K_UP:
                    protagonista.sonidomotor.fadeout(100)
                if event.key==K_DOWN:
                    protagonista.sonidomotor.fadeout(100)
    
            key1=pygame.key.get_pressed()
            if key1[pygame.K_d]:
                direccion1="right"
                protagonista1.movimientoderecha(direccion1)
            if key1[pygame.K_a]:
                direccion1="left"
                protagonista1.movimientoizquierda(direccion1)
            if key1[pygame.K_w]:
                direccion1="up"
                protagonista1.movimientoarriba(direccion1)
            if key1[pygame.K_s]:
                direccion1="down"
                protagonista1.movimientoabajo(direccion1)
            if key1[pygame.K_q]:
                     x,y=protagonista1.rect.center
                     protagonista1.disparar(x,y,direccion1)
            if event.type==pygame.KEYUP:
                if event.key==K_d:
                    protagonista1.sonidomotor.fadeout(100)
                if event.key==K_a:
                    protagonista1.sonidomotor.fadeout(100)
                if event.key==K_w:
                    protagonista1.sonidomotor.fadeout(100)
                if event.key==K_s:
                    protagonista1.sonidomotor.fadeout(100)

        #fondo de la pantalla
        pygame.draw.rect(escenario.pantalla,BLANCO, escenario.rf)
        pygame.draw.rect(escenario.pantalla,BLANCO, escenario.r1)
        pygame.draw.rect(escenario.pantalla,BLANCO, escenario.r2)
        pygame.draw.rect(escenario.pantalla,BLANCO, escenario.r3)
        escenario.pantalla.blit(escenario.fondo, (0,0))
        escenario.pantalla.blit(escenario.roca, (500,100))

        if protagonista1.rect.colliderect(escenario.meta):
            protagonista1.puntuacion+=20
            print("2",protagonista1.puntuacion)

        if protagonista.rect.colliderect(escenario.meta):
            protagonista.puntuacion+=20
            print("1",protagonista.puntuacion)

        if segundos!=0:
            if (protagonista.rect.colliderect(escenario.r1) or protagonista.rect.colliderect(escenario.r2) or 
                protagonista.rect.colliderect(escenario.r3)):
                protagonista.velocidad=2
                protagonista.puntuacion-=1
            else:
                protagonista.velocidad=5

        if segundos!=0:
            if (protagonista1.rect.colliderect(escenario.r1) or protagonista1.rect.colliderect(escenario.r2) or 
                protagonista1.rect.colliderect(escenario.r3)):
                protagonista1.velocidad=2
                protagonista1.puntuacion-=1
            else:
                protagonista1.velocidad=5

        if len(protagonista1.listaDisparo)>0:
            for x in protagonista1.listaDisparo:
                x.dibujar(escenario.pantalla)
                x.trayectoria()

        if len(protagonista.listaDisparo)>0:
            for x in protagonista.listaDisparo:
                x.dibujar(escenario.pantalla)
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
        enemigo.dibujar(escenario.pantalla)
        enemigo1.dibujar(escenario.pantalla)
            
        if protagonista.rect.left>= escenario.ancho_pantalla or protagonista.rect.left<0 or protagonista.rect.top>=escenario.alto_pantalla or protagonista.rect.top<0:
            protagonista.sonidomotor.fadeout(100)
            escenario.mensaje("Game Over",NEGRO,-100,tamaño="grande")
            time.sleep(1)
            salir=True
                
        if minutos==0 and segundos==00:
            escenario.mensaje("Fin de la partida",ROJO,-100,tamaño="grande")
            escenario.mensaje("NIVEL 3",ROJO,0,tamaño="grande")
            
        #temporizador
        cronometro=escenario.font.render(str(minutos)+":"+str(segundos),0,(ROJO))
        escenario.pantalla.blit(cronometro,(10,5))
   

        protagonista.dibujar(escenario.pantalla,direccion)
        protagonista1.dibujar(escenario.pantalla,direccion1)
        
        pygame.display.update()
        escenario.reloj.tick(35)
    pygame.display.update()
    pygame.quit()


def jugar_1():
    pygame.init()
    escenario=Escenario()
    global direccion
    protagonista=jugador(10,180,"carro.png")
    enemigo=oponente(55,180,"opo2.png")
    listaenemigo.append(enemigo)
    enemigo1=oponente(55,130,"opo1.png")
    listaenemigo.append(enemigo1)

    tup=timeup()
    
    salir=False
    global segundos
    global minutos
    hilo= threading.Thread(target=tup.timer,args=())
    hilo.start()
    tiempo = segundos
    
    while not salir:
        if minutos!=0 or segundos!=0:
            hilor1= threading.Thread(target=enemigo.opone(False),args=())
            hilor1.start()
            hilor2= threading.Thread(target=enemigo1.opone(True),args=())
            hilor2.start()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            if minutos==0 and segundos==0:
                protagonista.sonidomotor.fadeout(100)
                escenario.mensaje("Fin de la partida",NEGRO,-100,tamaño="grande")
                time.sleep(1)
                salir = True
                escenario.next_level(False)
                


            key=pygame.key.get_pressed()
            if key[pygame.K_RIGHT]:
                direccion="right"
                protagonista.movimientoderecha(direccion)
            if key[pygame.K_LEFT]:
                direccion="left"
                protagonista.movimientoizquierda(direccion)
            if key[pygame.K_UP]:
                direccion="up"
                protagonista.movimientoarriba(direccion)
            if key[pygame.K_DOWN]:
                direccion="down"
                protagonista.movimientoabajo(direccion)
            if key[pygame.K_SPACE]:
                x,y=protagonista.rect.center
                protagonista.disparar(x,y,direccion)
            if event.type==pygame.KEYUP:
                if event.key==K_RIGHT:
                    protagonista.sonidomotor.fadeout(100)
                if event.key==K_LEFT:
                    protagonista.sonidomotor.fadeout(100)
                if event.key==K_UP:
                    protagonista.sonidomotor.fadeout(100)
                if event.key==K_DOWN:
                    protagonista.sonidomotor.fadeout(100)
    

        #fondo de la pantalla
        pygame.draw.rect(escenario.pantalla,BLANCO, escenario.rf)
        pygame.draw.rect(escenario.pantalla,BLANCO, escenario.r1)
        pygame.draw.rect(escenario.pantalla,BLANCO, escenario.r2)
        pygame.draw.rect(escenario.pantalla,BLANCO, escenario.r3)
        escenario.pantalla.blit(escenario.fondo, (0,0))
        escenario.pantalla.blit(escenario.roca, (500,100))

        if protagonista.rect.colliderect(escenario.meta):
            protagonista.puntuacion+=20
            print("1",protagonista.puntuacion)


        if segundos!=0:
            if (protagonista.rect.colliderect(escenario.r1) or protagonista.rect.colliderect(escenario.r2) or 
                protagonista.rect.colliderect(escenario.r3)):
                protagonista.velocidad=2
                protagonista.puntuacion-=1
            else:
                protagonista.velocidad=5

        if len(protagonista.listaDisparo)>0:
            for x in protagonista.listaDisparo:
                x.dibujar(escenario.pantalla)
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
        enemigo.dibujar(escenario.pantalla)
        enemigo1.dibujar(escenario.pantalla)
            
        if protagonista.rect.left>= escenario.ancho_pantalla or protagonista.rect.left<0 or protagonista.rect.top>=escenario.alto_pantalla or protagonista.rect.top<0:
            protagonista.sonidomotor.fadeout(100)
            escenario.mensaje("Game Over",NEGRO,-100,tamaño="grande")
            time.sleep(1)
            salir=True
                
        if minutos==0 and segundos==00:
            escenario.mensaje("NIVEL 3",ROJO,0,tamaño="grande")
            escenario.mensaje("Fin de la partida",ROJO,-100,tamaño="grande")
            
        #temporizador
        cronometro=escenario.font.render(str(minutos)+":"+str(segundos),0,(ROJO))
        escenario.pantalla.blit(cronometro,(10,5))
   

        protagonista.dibujar(escenario.pantalla,direccion)
        
        pygame.display.update()
        escenario.reloj.tick(35)
    pygame.display.update()
    pygame.quit()