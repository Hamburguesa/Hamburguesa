import pygame
import constantes
from nivel import Level
from platforma import LIMITE, MAYONESA, ENEMY, SACHET, SACHET2, VERSION_LARGA, Plataforma, PlataformaConMovimiento
from platforma2 import ENEMY_F

class Level_01(Level):
    ''' Clase que define el primer nivel.
        Se debe definir el fondo, las plataformas y los enemigos que aparezcan. '''
    
    """ Definicion del nivel 1. """

    def __init__(self, jugador):
        """ Metodo que crea el nivel 1 """

        # Se llama al metodo del padre constructor.
        Level.__init__(self, jugador)

        #Cargamos la imagen de fondo.
        self.fondo = pygame.image.load("imagenes/MesadaFondo.png").convert()
        self.fondo.set_colorkey(constantes.BLANCO)
        self.limite_nivel = -25000
        self.limit_nivel_suelo=550
        self.limit_izquierdo=150

        nivel = [ [LIMITE, 150, 300], 
                  [VERSION_LARGA, 450, 355],
                  [MAYONESA, 900, 260],
                  [VERSION_LARGA, 2000,220],
                  [VERSION_LARGA, 2480, 220],
                  [VERSION_LARGA, 2950,120],
                  [VERSION_LARGA, 4650, 120],
                  [MAYONESA, 5300, 95],
                  [VERSION_LARGA, 5750, 95],
                  [MAYONESA, 6500, 95],
                  [MAYONESA, 7100, 95],
                  [MAYONESA, 7800, 95],
                  [MAYONESA, 9300, 90],
                  [MAYONESA, 9700, 90],
                  [LIMITE, 9860, 300],
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
                  [LIMITE, 17478, 250],
                  [MAYONESA, 18050, 420],
                  [VERSION_LARGA, 19550,170],
                  [MAYONESA, 20150, 170],
                  [MAYONESA, 20550, 380],
                  [MAYONESA, 21000, 270],
                  [VERSION_LARGA, 21500, 260],
                  [MAYONESA, 22118, 180],
                  [MAYONESA, 22618, 170],
                  [VERSION_LARGA, 23118, 190],
                  [MAYONESA, 23718, 240],
                  [LIMITE, 24818, 300],
                  [MAYONESA, 24218, 250],
                  [VERSION_LARGA, 24718, 180]]
                  

        # Se busca en la lista anterior creada y se le agregan las plataformas al nivel.
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add(bloque)



            nivel_movimiento = [[MAYONESA, 1250, 220, 1150, 1650, 220, 220, 2, 0],
                                [MAYONESA, 3600, 250, 3600, 3600, 150, 450, 0, 2],
                                [MAYONESA, 4100, 120, 3900, 4300, 120, 120, 2, 0],
                                [MAYONESA, 7460, 201, 7460, 7460, 200, 450, 0, 2],
                                [MAYONESA, 10900, 350,10600,10600,150, 450, 0, 2],
                                [MAYONESA, 16250, 170,16250,16250,150, 450, 0, 2],
                                [VERSION_LARGA, 18600, 280,18300,19050,280, 280, 2, 0]]
         
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
                      [SACHET, 24718, 120]]
        
        for plataforma in nivel_puntos:
            bloque = Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_puntos.add(bloque)
            
        #Lista de enemigos (solo del principio del nivel dado que no eran necesarios)  
        nivel_enemigos=[[ENEMY, 500, 300, 450, 650, 315, 320, 1.5,0],
                        [ENEMY, 900, 210, 900, 1000, 210, 210,1.5,0],
                        [ENEMY_F,1658,165, 1658,1658,100, 100, 0, 0],
                        [ENEMY, 3598, 478, 3500,3798,478,478, 1.5,0],
                        [ENEMY, 4700, 60, 4650, 4850, 80, 80, 1.5,0],
                        [ENEMY, 5350, 40, 5300, 5400, 65,65, 1.5, 0],
                        [ENEMY, 7850, 40,7800, 7900, 80, 80, 1.5, 0],
                        [ENEMY, 10400,100,10350,10550,100,100,1.5,0],
                        [ENEMY, 12500,300,12500,12680,300,300,1.5,0],
                        [ENEMY, 14000,485,13500,14100,450,450,2.5,0],
                        [ENEMY_F,15500,300,15400,15700, 300,300,2,0],
                        [ENEMY_F, 16900,30,16900,16900,-100,330,0,2],
                        [ENEMY_F, 18500,60,18500,18500,-60,160,0, 2],
                        [ENEMY, 19550,100,19530,19750,100,100,1.5,0],
                        [ENEMY, 21500, 450,21200,21800,450, 450,2,0],
                        [ENEMY_F,23000,200,23000,23000,-100,550, 0,2]]
              
        
        
        
        
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
        
       
        # Se agrega una plataforma en movimiento.
        bloque = PlataformaConMovimiento(MAYONESA)
        bloque.rect.x = 8500
        bloque.rect.y = 90
        bloque.limite_izquierdo = 8250 
        bloque.limite_derecho = 8900
        bloque.mover_x = 2
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)
        
        """bloque = PlataformaConMovimiento(MAYONESA)
        bloque.rect.x = 17650
        bloque.rect.y = 340
        bloque.limite_inferior = 380
        bloque.limite_superior = 280
        bloque.mover_y = 2
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)"""