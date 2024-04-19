
class Pilota:

    velocitat:5
    midas_x:10
    midas_y:10

    def __init__(self, posicion_x,posicion_y,velocitat_x,velocitat_y,color,midas_x,midas_y):

        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.velocitat_x = velocitat_x
        self.velocitat_y = velocitat_y
        self.color = color
        self.midas_x = midas_x
        self.midas_y = midas_y

    def moure(self):
        self.posicion_x += self.velocitat_x
        self.posicion_y += self.velocitat_y

    def rebota_vora(self, ample_escena, alt_escena, jugador1, jugador2):
        if self.posicion_x <= jugador1.posX + jugador1.midaX or self.posicion_x >= jugador2.posX - self.midas_x:
            # Verificar si hay un jugador detrás de la pelota
            if self.posicion_x <= jugador1.posX + jugador1.midaX and self.velocitat_x < 0:
                self.velocitat_x = -self.velocitat_x
            elif self.posicion_x >= jugador2.posX - self.midas_x and self.velocitat_x > 0:
                self.velocitat_x = -self.velocitat_x
            else:
                # Si no hay jugador detrás de la pelota, reposicionar la pelota al centro de la pantalla
                self.posicion_x = ample_escena // 2
                self.posicion_y = alt_escena // 2

