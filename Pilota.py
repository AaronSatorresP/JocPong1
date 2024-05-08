import pygame

from ObjecteEscenari import ObjecteEscenari


class Pilota(ObjecteEscenari):

    def __init__(self, posicion_x, posicion_y, velocitat_x, velocitat_y, color, midas_x, midas_y, velocidad_inicial):
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.velocitat_x = velocitat_x
        self.velocitat_y = velocitat_y
        self.color = color
        self.midas_x = midas_x
        self.midas_y = midas_y
        self.velocidad_inicial = velocidad_inicial
    def PintaPilota(self,finestreJoc):
        pygame.draw.rect(finestreJoc, self.color,(self.posicion_x, self.posicion_y, self.midas_x, self.midas_y))


    def moure(self):
        self.posicion_x += self.velocitat_x
        self.posicion_y += self.velocitat_y

    def rebota_vora(self, ample_escena, alt_escena, jugador1, jugador2):
        if self.posicion_x <= jugador1.posX + jugador1.midaX or self.posicion_x >= jugador2.posX - self.midas_x:
            if (self.posicion_x <= jugador1.posX + jugador1.midaX and self.velocitat_x < 0) or \
                    (self.posicion_x >= jugador2.posX - self.midas_x and self.velocitat_x > 0):
                if jugador1.posY <= self.posicion_y <= jugador1.posY + jugador1.midaY or \
                        jugador2.posY <= self.posicion_y <= jugador2.posY + jugador2.midaY:
                    self.velocitat_x = -self.velocitat_x
                    self.aumentar_velocidad()
                else:
                    self.reiniciar_velocidad()
                    self.reiniciar_posicion(ample_escena, alt_escena)
        elif self.posicion_y <= 0 or self.posicion_y >= alt_escena[1] - self.midas_y:
            self.velocitat_y = -self.velocitat_y
            if self.posicion_y <= 0:
                self.posicion_y = 0
            elif self.posicion_y >= alt_escena[1] - self.midas_y:
                self.posicion_y = alt_escena[1] - self.midas_y

    def aumentar_velocidad(self):
        self.velocitat_x *= 1.1
        self.velocitat_y *= 1.1

    def reiniciar_velocidad(self):
        self.velocitat_x = self.velocidad_inicial[0]
        self.velocitat_y = self.velocidad_inicial[1]

    def reiniciar_posicion(self, ample_escena, alt_escena):
        self.posicion_x = ample_escena[0] // 2
        self.posicion_y = alt_escena[1] // 2
