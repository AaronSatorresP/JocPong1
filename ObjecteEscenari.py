import pygame.draw


class ObjecteEscenari:
    def __init__(self,posX,posY, color,midaX,midaY):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.midaX = midaX
        self.midaY=midaY

    def Pinta(self,finestra):
        pygame.draw.rect(finestra, self.color,(self.posX, self.posY, self.midaX, self.midaY))