import pygame
import constantes
from nivel import Level
from platforma import LIMITE, MAYONESA, SACHET, VERSION_LARGA, Plataforma, PlataformaConMovimiento

class Level_01(Level):
    ''' Clase que define el primer nivel.
        Se debe definir el fondo, las plataformas y los enemigos que aparezcan. '''
    
    """ Definicion del nivel 1. """

    def __init__(self, jugador):
        """ Metodo que crea el nivel 1 """

        # Se llama al metodo del padre constructor.
        Level.__init__(self, jugador)

        #Cargamos la imagen de fondo.
        self.fondo = pygame.image.load("imagenes/MesadaFFondo.png").convert()
        #self.fondo.set_colorkey(constantes.BLANCO)
        self.limite_nivel = -25000
        self.limit_nivel_suelo=550
        self.limit_izquierdo=150

        nivel = [ [LIMITE, 50, 300], 
                  [MAYONESA, 500, 355],
                  [MAYONESA, 900, 260],
                  [LIMITE, 1700,300],
                  [VERSION_LARGA, 2000,220],
                  [VERSION_LARGA, 2480, 220],
                  [VERSION_LARGA, 2950,120],
                  [LIMITE, 3340,300],
                  [MAYONESA, 4522, 195],
                  [MAYONESA, 4950, 120],
                  [LIMITE, 5400, 300],
                  [MAYONESA, 5500, 95],
                  [MAYONESA, 6000, 95],
                  [MAYONESA, 6500, 95],
                  [MAYONESA, 7100, 95],
                  [LIMITE, 7450, 300],
                  [MAYONESA, 7800, 95],
                  [LIMITE, 8361, 300],
                  [MAYONESA, 9300, 90],
                  [MAYONESA, 9700, 90],
                  [MAYONESA, 10100, 150],
                  [LIMITE, 10514, 300],
                  [MAYONESA, 11100, 250],
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
                  [MAYONESA, 17650, 340],
                  [MAYONESA, 19550,170],
                  [MAYONESA, 20050, 170],
                  [MAYONESA, 20550, 380],
                  [MAYONESA, 21000, 270],
                  [VERSION_LARGA, 21500, 260],
                  [MAYONESA, 22118, 180],
                  [MAYONESA, 22618, 170],
                  [VERSION_LARGA, 23118, 190],
                  [MAYONESA, 23718, 240],
                  [LIMITE, 23218, 300]]
                  

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
                                [MAYONESA, 10600, 350,10600,10600,150, 450, 0, 2],
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
        """
        bloque = PlataformaConMovimiento(MAYONESA)
        bloque.rect.x = 3600
        bloque.rect.y = 250
        bloque.limite_inferior = 400
        bloque.limite_superior = 150
        bloque.mover_y = 1
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)"""
        
        




