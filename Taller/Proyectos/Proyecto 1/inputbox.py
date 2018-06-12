import pygame, math, sys, os

RED=255,0,0
bgcolor = pygame.Color("green")
pygame.init()
spriteGroup = pygame.sprite.OrderedUpdates()
textboxGroup = pygame.sprite.OrderedUpdates()
fondo = pygame.image.load("BANDERA.png")
grande=pygame.font.SysFont("Arial",50)

screen = ""


class newTextBox(pygame.sprite.Sprite):
    def __init__(self, text, xpos, ypos, width, case, maxLength, fontSize):
        pygame.sprite.Sprite.__init__(self)
        self.text = ""
        self.width = width
        self.initialText = text
        self.case = case
        self.maxLength = maxLength
        self.boxSize = int(fontSize * 1.7)
        self.image = pygame.Surface((width, self.boxSize))
        self.image.fill((255, 255, 255))
        pygame.draw.rect(self.image, (255, 0, 0), [0, 0, width - 1, self.boxSize - 1], 2)
        self.rect = self.image.get_rect()
        self.fontFace = pygame.font.match_font("Arial")
        self.fontColour = pygame.Color("black")
        self.initialColour = (180, 180, 180)
        self.font = pygame.font.Font(self.fontFace, fontSize)
        self.rect.topleft = [xpos, ypos]
        newSurface = self.font.render(self.initialText, True, self.initialColour)
        self.image.blit(newSurface, [10, 5])

    def update(self, keyevent):
        key = keyevent.key
        unicode = keyevent.unicode
        if key > 31 and key < 127 and (
                self.maxLength == 0 or len(self.text) < self.maxLength):  # only printable characters
            if keyevent.mod == 1 and self.case == 1 and key >= 97 and key <= 122:
                # force lowercase letters
                key -= 32
                self.text += chr(key)
            else:
                # use the unicode char
                self.text += unicode 
      
        self.image.fill((255, 255, 255))
        pygame.draw.rect(self.image, (255, 0, 0), [0, 0, self.width - 1, self.boxSize - 1], 2)
        newSurface = self.font.render(self.text, True, self.fontColour)
        self.image.blit(newSurface, [10, 5])
        updateDisplay()

    def clear(self):
        self.image.fill((255, 255, 255))
        pygame.draw.rect(self.image, (0, 0, 0), [0, 0, self.width - 1, self.boxSize - 1], 2)
        newSurface = self.font.render(self.initialText, True, self.initialColour)
        self.image.blit(newSurface, [10, 5])
        updateDisplay()

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
    textoRect.center=(600/2),(600/2)+desplazamientoY
    screen.blit(textosuperficie,textoRect) 

def screenSize(sizex, sizey, xpos=None, ypos=None, fullscreen=False):
    global bgcolor
    global screen

    
    screen = pygame.display.set_mode([sizex, sizey])
    screen.blit(fondo, (0,0))
    mensaje("Registre el jugador",RED,-100,tamaño="grande")
    mensaje("Precione ENTER para ir al menu",RED,0,tamaño="grande")
    pygame.display.set_caption("Proyecto 1")
    pygame.display.update()

def makeTextBox(xpos, ypos, width, case=0, startingText="Please type here", maxLength=0, fontSize=22):
    thisTextBox = newTextBox(startingText, xpos, ypos, width, case, maxLength, fontSize)
    textboxGroup.add(thisTextBox)
    return thisTextBox


def textBoxInput(textbox, functionToCall=None, args=[]):
    # starts grabbing key inputs, putting into textbox until enter pressed
    textbox.text = ""
    returnVal=None
    while True:
        updateDisplay()
        if functionToCall:
            returnVal = functionToCall(*args)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    textbox.clear()
                    if returnVal:
                        return textbox.text, returnVal
                    else:
                        return textbox.text
##                elif event.key == pygame.K_ESCAPE:
##                    pygame.quit()
##                    sys.exit()
                else:
                    textbox.update(event)
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



def showTextBox(textBoxName):
    textboxGroup.add(textBoxName)
    updateDisplay()

def updateDisplay():
    global bgSurface
    spriteRects = spriteGroup.draw(screen)
    textboxRects = textboxGroup.draw(screen)
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_ESCAPE]):
        pygame.quit()
        sys.exit()





