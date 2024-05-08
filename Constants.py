from ObjecteEscenari import ObjecteEscenari


class Constants(ObjecteEscenari):
    class ConstantsMides:

        MARGES_ESCENARI = (600, 400)
        AMPLA_ESCENARI = (0,20)
        ALSADA_ESCENARI = (MARGES_ESCENARI[0],MARGES_ESCENARI[1]-40)

    class ConstantsColors:
        VERD = (0, 255, 0)
        BlAU = (0, 0, 255)

    class ConstantsJugadores:
        X_INICIAL_JUGADOR1 = 10
        Y_INICIAL_JUGADOR1 = 150
        COLOR_JUGADOR1 = (0, 0, 255)
        RADIO_JUGADOR1 = 15
        ALTURA_JUGADOR1 = 60
        VELOCIDAD_JUGADOR1 = 5

        X_INICIAL_JUGADOR2 = 575
        Y_INICIAL_JUGADOR2 = 150
        COLOR_JUGADOR2 = (255, 0, 0)
        RADIO_JUGADOR2 = 15
        ALTURA_JUGADOR2 = 60
        VELOCIDAD_JUGADOR2 = 5