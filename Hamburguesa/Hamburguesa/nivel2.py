import pygame
import constantes
from platforma import LIMITE, MAYONESA, VERSION_LARGA, ENEMY, SACHET, SACHET2, Plataforma, PlataformaConMovimiento
from platforma2 import ENEMY_F
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
        self.posicion_bigboss = -34200
        
        # Lista con los bloques de plataformas, indicando la ubicacion x,y y el tipo 
        nivel = [ [LIMITE, 0, 300],
                  [VERSION_LARGA, 450, 390],
                  [VERSION_LARGA, 1000, 260],
                  [VERSION_LARGA, 2480, 220],
                  [VERSION_LARGA, 2950,120],
                  [VERSION_LARGA, 4650, 120],
                  [MAYONESA, 5300, 95],
                  [VERSION_LARGA, 5750, 145],
                  [MAYONESA, 6500, 155],
                  [MAYONESA, 7100, 178],
                  [MAYONESA, 7800, 185],
                  [MAYONESA, 9300, 90],
                  [MAYONESA, 9700, 90],
                  [VERSION_LARGA, 10350, 150],
                  [MAYONESA, 11550, 180],
                  [MAYONESA, 12050, 280],
                  [VERSION_LARGA, 12500, 350],
                  [MAYONESA, 13000, 180],
                  [MAYONESA, 13450, 250],
                  [MAYONESA, 13950, 270],
                  [VERSION_LARGA, 14375, 190],
                  [MAYONESA, 15200, 260],
                  [MAYONESA, 15850, 260],
                  [MAYONESA, 16600, 140],
                  [MAYONESA, 17050, 170],
                  [MAYONESA, 17698, 200],
                  [MAYONESA, 18050, 420],
                  [VERSION_LARGA, 19250,170],
                  [MAYONESA, 19800, 260],
                  [MAYONESA, 20200, 170],
                  [MAYONESA, 20550, 380],
                  [MAYONESA, 21000, 270],
                  [VERSION_LARGA, 21500, 260],
                  [MAYONESA, 22118, 180],
                  [MAYONESA, 22618, 170],
                  [VERSION_LARGA, 23118, 190],
                  [MAYONESA, 23718, 240],
                  [LIMITE, 37228, 300],
                  [MAYONESA, 24218, 250],
                  [VERSION_LARGA, 24718, 180],
                  [MAYONESA, 25350, 260],
                  [MAYONESA, 25850, 170],
                  [MAYONESA, 26300, 380],
                  [MAYONESA, 26750, 270],
                  [VERSION_LARGA, 27250, 260],
                  [MAYONESA, 27868, 180],
                  [MAYONESA, 28368, 170],
                  [VERSION_LARGA, 28870, 190],
                  [MAYONESA, 29470, 240],
                  [MAYONESA, 29918, 250],
                  [VERSION_LARGA, 31078, 180],
                  [MAYONESA, 31710, 260],
                  [MAYONESA, 32210, 170],
                  [MAYONESA, 32660, 380],
                  [MAYONESA, 33110, 270],
                  [VERSION_LARGA, 33610, 260],
                  [MAYONESA, 34228, 180],
                  [MAYONESA, 34728, 170],
                  [MAYONESA, 35828, 240],
                  [MAYONESA, 36278, 250],
                  [VERSION_LARGA, 36838, 180]]

        # Se busca en la lista anterior creada y se le agregan las plataformas al jugador.
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add(bloque)


        nivel_movimiento = [[VERSION_LARGA, 1450, 220, 1350, 1950, 220, 220, 2, 0],
                            [VERSION_LARGA, 3580, 250, 3600, 3600, 150, 450, 0, 2],
                            [MAYONESA, 4100, 120, 3900, 4300, 120, 120, 2, 0],
                            [MAYONESA, 7460, 201, 7460, 7460, 200, 470, 0, 2],
                            [MAYONESA, 8250, 90, 8250, 8900, 90, 90, 2, 0],
                            [MAYONESA, 10900, 350,10600,10600,150, 470, 0, 2],
                            [MAYONESA, 16250, 170,16250,16250,150, 470, 0, 2],
                            [VERSION_LARGA, 18600, 280,18300,18750,280, 280, 2, 0],
                            [VERSION_LARGA, 35228, 190, 35228, 35228, 190, 440,0,2],
                            [VERSION_LARGA, 30478, 180,30478,30478, 180,440,0,2],
                            ]
        
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
            
            nivel_puntos=[[SACHET, 500, 200],
                          [SACHET, 1500, 160],
                          [SACHET, 3000, 28],
                          [SACHET, 4546, 32],
                          [SACHET, 7800, 9],
                          [SACHET, 8800, 37],
                          [SACHET, 9800, 11],
                          [SACHET, 12550, 220],
                          [SACHET, 15000, 300],
                          [SACHET, 17050, 100],
                          [SACHET, 18550, 120],
                          [SACHET, 21050, 200],
                          [SACHET, 22000, 500],
                          [SACHET, 23218, 90],
                          [SACHET, 24218, 160],
                          [SACHET, 24718, 120],
                          [SACHET, 4546, 32],
                          [SACHET, 7800, 9],
                          [SACHET, 8800, 37],
                          [SACHET, 9800, 11],
                          [SACHET, 12550, 220],
                          [SACHET, 15000, 300],
                          [SACHET, 17050, 100],
                          [SACHET, 18550, 120],
                          [SACHET, 21050, 200],
                          [SACHET, 22000, 500],
                          [SACHET, 23218, 90],
                          [SACHET, 24218, 160],
                          [SACHET, 24718, 120],
                          [SACHET, 26118, 30],
                          [SACHET, 27212, 141],
                          [SACHET, 29740, 60],
                          [SACHET, 30110, 0],
                          [SACHET, 31709, 60],
                          [SACHET, 32144, 100],
                          [SACHET, 33121, 60],
                          [SACHET, 34701, 30],
                          [SACHET, 35102, 30],
                          [SACHET, 35909, 30]]
        
        for plataforma in nivel_puntos:
            bloque = Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_puntos.add(bloque)
            
        nivel_enemigos=[[ENEMY, 500, 330, 450, 650, 315, 320, 1.5,0],
                        [ENEMY, 1000, 210, 1000, 1200, 210, 210,1.5,0],
                        [ENEMY, 3598, 535, 3500,3798,478,478, 1.5,0],
                        [ENEMY, 4700, 65, 4650, 4850, 80, 80, 1.5,0],
                        [ENEMY, 5350, 40, 5300, 5400, 65,65, 1.5, 0],
                        [ENEMY, 7850, 40,7800, 7900, 80, 80, 1.5, 0],
                        [ENEMY, 10400,100,10350,10550,100,100,1.5,0],
                        [ENEMY, 12500,300,12500,12680,300,300,1.5,0],
                        [ENEMY, 14000,535,13500,14100,450,450,2.5,0],
                        [ENEMY_F,15500,300,15400,15700, 300,300,2,0],
                        [ENEMY_F, 16900,30,16900,16900,-100,330,0,2],
                        [ENEMY_F, 18500,60,18500,18500,-60,160,0, 2],
                        [ENEMY, 19550,100,19530,19750,100,100,1.5,0],
                        [ENEMY, 21500, 535,21200,21800,450, 450,2,0],
                        [ENEMY_F,23000,200,23000,23000,-100,550, 0,2],
                        [ENEMY, 4891, 535, 4891, 5191, 478, 478, 1.5, 0],
                        [ENEMY, 6891, 535, 6891, 7191, 478, 478, 1.5, 0],
                        [ENEMY, 8891, 535, 8891, 9191, 478, 478, 1.5, 0],
                        [ENEMY, 10891, 535, 10891, 11191, 478, 478, 1.5, 0],
                        [ENEMY, 12891, 535, 12891, 13191, 478, 478, 1.5, 0],
                        [ENEMY, 14891, 535, 14891, 15191, 478, 478, 1.5, 0],
                        [ENEMY, 16891, 535, 16891, 17191, 478, 478, 1.5, 0],
                        [ENEMY, 18891, 535, 18891, 19191, 478, 478, 1.5, 0],
                        [ENEMY, 20891, 535, 20891, 21191, 478, 478, 1.5, 0],
                        [ENEMY, 22891, 535, 22891, 23191, 478, 478, 1.5, 0],
                        [ENEMY, 24891, 535, 24891, 25191, 478, 478, 1.5, 0],
                        [ENEMY, 26891, 535, 26891, 27191, 478, 478, 1.5, 0],
                        [ENEMY, 28891, 535, 28891, 29191, 478, 478, 1.5, 0],
                        [ENEMY, 30891, 535, 30891, 31191, 478, 478, 1.5, 0],
                        [ENEMY, 32891, 535, 32891, 33191, 478, 478, 1.5, 0],
                        [ENEMY, 34891, 535, 34891, 35191, 478, 478, 1.5, 0]]
        
              
        
        for platforma in nivel_enemigos:
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
            self.lista_enemigos.add(bloque)
            
        nivel_vidas=[[SACHET2, 10001,-5],
                     [SACHET2, 20002,50]]
        
        for plataforma in nivel_vidas:
            bloque = Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_vidas.add(bloque)
            
        """nivel_gg=[[VERSION_LARGA, 24718, 180]]
        
        for plataforma in nivel_gg:
            bloque = Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_gg.add(bloque)"""