import pygame

from ObjecteEscenari import ObjecteEscenari


class Jugador(ObjecteEscenari):
    def __init__(self,posX,posY,color,midaX,midaY,velocidad):
        self.posX = posX
        self.posY = posY
        self.midaX = midaX
        self.midaY = midaY
        self.color = color
        self.velocidad = velocidad

    def PintaJugador1(self,finestreJoc):
        pygame.draw.rect(finestreJoc, self.color, (self.posX, self.posY, self.midaX, self.midaY))

    def PintaJugador2(self,finestreJoc):
        pygame.draw.rect(finestreJoc, self.color, (self.posX, self.posY, self.midaX, self.midaY))
