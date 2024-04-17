import sys

import  pygame

import Constants
from Jugador import Jugador
from Pilota import Pilota

pygame.init()

finestreJoc = pygame.display.set_mode(Constants.ConstantsMides.MARGES_ESCENARI)

rellotge = pygame.time.Clock()

jugador1 = Jugador(10,150,(0,0,255),15,60,5);
jugador2 = Jugador(575,150,(255,0,0),15,60,5);

pilota = Pilota(120,150,2,2,(255,255,0),10,10);
gameOver = False


def PintaObjectes():

    finestreJoc.fill(Constants.ConstantsMides.ConstantsColors.BlAU)
    pygame.draw.rect(finestreJoc,Constants.ConstantsMides.ConstantsColors.VERD,(Constants.ConstantsMides.AMPLA_ESCENARI, Constants.ConstantsMides.ALSADA_ESCENARI))

    pygame.draw.rect(finestreJoc,jugador1.color,(jugador1.posX, jugador1.posY, jugador1.midaX, jugador1.midaY))
    pygame.draw.rect(finestreJoc, jugador2.color, (jugador2.posX, jugador2.posY, jugador2.midaX, jugador2.midaY))

    pygame.draw.rect(finestreJoc,pilota.color,(pilota.posicion_x,pilota.posicion_y,pilota.midas_x,pilota.midas_y))


def manejar_movimiento(jugador, tecla_arriba, tecla_abajo):
    keys = pygame.key.get_pressed()
    if keys[tecla_arriba]:
        jugador.posY = max(jugador.posY - jugador.velocidad, 20)
    elif keys[tecla_abajo]:
        limite_abajo = Constants.ConstantsMides.MARGES_ESCENARI[1] - jugador.midaY - 20
        jugador.posY = min(jugador.posY + jugador.velocidad, limite_abajo)



def DetectaEvents():
    manejar_movimiento(jugador1, pygame.K_w, pygame.K_s)
    manejar_movimiento(jugador2, pygame.K_UP, pygame.K_DOWN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()




while  not gameOver:

    PintaObjectes()

    DetectaEvents()

    rellotge.tick(30)
    pygame.display.update()