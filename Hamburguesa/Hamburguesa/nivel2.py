import pygame
import constantes
from platforma import LIMITE, BANDEJA, ENEMY, SACHET, SACHET2, Plataforma, PlataformaConMovimiento
from nivel import Level

#Clase que define el segundo nivel.

class Level_02(Level):
    ''' Clase que define el primer nivel.
    Se debe definir el fondo, las plataformas y los enemigos que aparezcan.'''

    def __init__(self, jugador):
        """ Metodo que crea el nivel 2 """

        # Se llama al metodo del padre constructor.
        Level.__init__(self, jugador)
        
        #Cargamos la imagen de fondo.
        self.fondo = pygame.image.load("imagenes/fondo2.png").convert()
        self.fondo.set_colorkey(constantes.BLANCO2)
        self.limite_nivel = -37486
        self.limit_nivel_suelo=590

        # Lista con los bloques de plataformas, indicando la ubicacion x,y y el tipo 
        nivel = [ [BANDEJA, 450, 355],
                  [BANDEJA, 900, 260],
                  [BANDEJA, 2000,220],
                  [BANDEJA, 2480, 220],
                  [BANDEJA, 2950,120],
                  [BANDEJA, 4650, 120],
                  [BANDEJA, 5300, 95],
                  [BANDEJA, 5750, 95],
                  [BANDEJA, 6500, 95],
                  [BANDEJA, 7100, 95],
                  [BANDEJA, 7800, 95],
                  [BANDEJA, 9300, 90],
                  [BANDEJA, 9700, 90],
                  [BANDEJA, 10350, 150],
                  [BANDEJA, 11550, 180],
                  [BANDEJA, 12050, 280],
                  [BANDEJA, 12500, 350],
                  [BANDEJA, 13000, 180],
                  [BANDEJA, 13450, 250],
                  [BANDEJA, 13950, 270],
                  [BANDEJA, 14375, 190],
                  [BANDEJA, 15200, 260],
                  [BANDEJA, 15850, 260],
                  [BANDEJA, 16600, 140],
                  [BANDEJA, 17050, 170],
                  [BANDEJA, 17698, 200],
                  [BANDEJA, 18050, 420],
                  [BANDEJA, 19250,170],
                  [BANDEJA, 19800, 260],
                  [BANDEJA, 20200, 170],
                  [BANDEJA, 20550, 380],
                  [BANDEJA, 21000, 270],
                  [BANDEJA, 21500, 260],
                  [BANDEJA, 22118, 180],
                  [BANDEJA, 22618, 170],
                  [BANDEJA, 23118, 190],
                  [BANDEJA, 23718, 240],
                  [BANDEJA, 24218, 250],
                  [BANDEJA, 24718, 180]]

        # Se busca en la lista anterior creada y se le agregan las plataformas al jugador.
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add(bloque)


        nivel_movimiento = [[BANDEJA, 1250, 220, 1150, 1650, 220, 220, 2, 0],
                            [BANDEJA, 3600, 250, 3600, 3600, 150, 450, 0, 2],
                            [BANDEJA, 4100, 120, 3900, 4300, 120, 120, 2, 0],
                            [BANDEJA, 7460, 201, 7460, 7460, 200, 450, 0, 2],
                            [BANDEJA, 8250, 90, 8250, 8900, 90, 90, 2, 0],
                            [BANDEJA, 10900, 350,10600,10600,150, 450, 0, 2],
                            [BANDEJA, 16250, 170,16250,16250,150, 450, 0, 2],
                            [BANDEJA, 18600, 280,18300,18750,280, 280, 2, 0]]
        
        for platforma in nivel_movimiento:
            bloque = PlataformaConMovimiento(platforma[0])
            bloque.rect.x = platforma[1]
            bloque.rect.y = platforma[2]
            bloque.limite_izquierdo = platforma[3]
            bloque.limite_derecho = platforma[4]
            bloque.limite_superior = platforma[5]
            bloque.limite_inferior = platforma[6]
            bloque.mover_x = platforma[7]
            bloque.mover_y = platforma[8]
            bloque.jugador = self.jugador
            bloque.nivel = self
            self.lista_plataformas.add(bloque)