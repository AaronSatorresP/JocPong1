import sys

import  pygame

import Constants
from Jugador import Jugador
from Pilota import Pilota

pygame.init()

finestreJoc = pygame.display.set_mode(Constants.Constants.ConstantsMides.MARGES_ESCENARI)

rellotge = pygame.time.Clock()

jugador1 = Jugador(Constants.Constants.ConstantsJugadores.X_INICIAL_JUGADOR1,
                    Constants.Constants.ConstantsJugadores.Y_INICIAL_JUGADOR1,
                    Constants.Constants.ConstantsJugadores.COLOR_JUGADOR1,
                    Constants.Constants.ConstantsJugadores.RADIO_JUGADOR1,
                    Constants.Constants.ConstantsJugadores.ALTURA_JUGADOR1,
                    Constants.Constants.ConstantsJugadores.VELOCIDAD_JUGADOR1)

jugador2 = Jugador(Constants.Constants.ConstantsJugadores.X_INICIAL_JUGADOR2,
                    Constants.Constants.ConstantsJugadores.Y_INICIAL_JUGADOR2,
                    Constants.Constants.ConstantsJugadores.COLOR_JUGADOR2,
                    Constants.Constants.ConstantsJugadores.RADIO_JUGADOR2,
                    Constants.Constants.ConstantsJugadores.ALTURA_JUGADOR2,
                    Constants.Constants.ConstantsJugadores.VELOCIDAD_JUGADOR2)

fontText = pygame.font.SysFont("monospace", 35)

pilota = Pilota(320,50,2,2,(255,255,0),10,10,(2,2));


gameOver = False


def PintaObjectes():

    finestreJoc.fill(Constants.Constants.ConstantsColors.BlAU)
    pygame.draw.rect(finestreJoc,Constants.Constants.ConstantsColors.VERD,(Constants.Constants.ConstantsMides.AMPLA_ESCENARI, Constants.Constants.ConstantsMides.ALSADA_ESCENARI))

    jugador1.Pinta(finestreJoc)
    jugador2.Pinta(finestreJoc)
    pilota.PintaPilota(finestreJoc)

    textJugador1 = "Jugador 1: " + str(jugador1.puntos)
    textJugador2 = "Jugador 2: " + str(jugador2.puntos)

    etiquetaJugador1 = fontText.render(textJugador1, 1, (255, 255, 255))
    etiquetaJugador2 = fontText.render(textJugador2, 1, (255, 255, 255))

    finestreJoc.blit(etiquetaJugador1, (10, 10))
    finestreJoc.blit(etiquetaJugador2, (Constants.Constants.ConstantsMides.AMPLA_ESCENARI[0] - -270, 10))
def manejar_movimiento(jugador, tecla_arriba, tecla_abajo):
    keys = pygame.key.get_pressed()
    if keys[tecla_arriba]:
        jugador.posY = max(jugador.posY - jugador.velocidad, 20)
    elif keys[tecla_abajo]:
        limite_abajo = Constants.Constants.ConstantsMides.MARGES_ESCENARI[1] - jugador.midaY - 20
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
    # Mover la pelota
    pilota.moure()

    # Verifica si la pilota rebota en las vores
    pilota.rebota_vora(Constants.Constants.ConstantsMides.AMPLA_ESCENARI, Constants.Constants.ConstantsMides.ALSADA_ESCENARI, jugador1,jugador2)


    rellotge.tick(30)
    pygame.display.update()

