import pygame
import constantes
from nivel import Level
from platforma import LIMITE, MAYONESA, ENEMY, SACHET, VERSION_LARGA, Plataforma, BEBIDAS, PlataformaConMovimiento

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
                  [MAYONESA, 500, 355],
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
                  [VERSION_LARGA, 10350, 150],
                  [LIMITE, 9860, 300],
                  [MAYONESA, 11550, 180],
                  [MAYONESA, 12050, 280],
                  [MAYONESA, 12500, 350],
                  [MAYONESA, 13000, 180],
                  [MAYONESA, 13450, 250],
                  [MAYONESA, 13950, 270],
                  [MAYONESA, 14900, 350],
                  [MAYONESA, 15400, 260],
                  [MAYONESA, 15850, 260],
                  [MAYONESA, 16700, 140],
                  [MAYONESA, 17200, 170],
                  [MAYONESA, 17650, 420],
                  [MAYONESA, 19550,170],
                  [MAYONESA, 20050, 170],
                  [MAYONESA, 20550, 380],
                  [MAYONESA, 21000, 270],
                  [VERSION_LARGA, 21500, 260],
                  [MAYONESA, 22118, 180],
                  [MAYONESA, 22618, 170],
                  [VERSION_LARGA, 23118, 190],
                  [MAYONESA, 23718, 240],
                  [LIMITE, 23218, 300],
                  [MAYONESA, 24218, 250],
                  [MAYONESA, 24718, 180],
                  [MAYONESA, 25218, 234],
                  [MAYONESA, 25718, 290]]
                  

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
                                [MAYONESA, 14450, 180,14450,14450,150, 450, 0, 2],
                                [MAYONESA, 16250, 170,16250,16250,150, 450, 0, 2],
                                [MAYONESA, 18600, 280,18100,19050,280, 280, 2, 0]]
         
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
                      [SACHET, 3000, 28],
                      [SACHET, 7800, 9],
                      [SACHET, 9800, 11],
                      [SACHET, 12550, 220],
                      [SACHET, 15000, 300],
                      [SACHET, 17750, 100],
                      [SACHET, 22000, 500],
                      [SACHET, 23218, 90],
                      [SACHET, 24218, 160]]
        
        for plataforma in nivel_puntos:
            bloque = Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_puntos.add(bloque)
            
        #Lista de enemigos (solo del principio del nivel dado que no eran necesarios)  
        nivel_enemigos=[[ENEMY, 500, 300, 300, 700, 200, 200, 2, 0],
                        [ENEMY, 900, 205, 700, 1050, 345, 345,2, 0],
                        [ENEMY, 1658, 100, 1658,1658,100, 100, 0,0],
                        [ENEMY, 3598, 478, 3500,3798, 478,478,2 ,0],
                        [ENEMY, 4700, 80, 4700, 5000, 80, 80, 2, 0]]
              
        
        
        
        
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