import pygame
import constantes
from nivel import Level
from platforma import LIMITE, MAYONESA, VERSION_LARGA, MOVIMIENTO, Plataforma, PlataformaConMovimiento

class Level_01(Level):
    ''' Clase que define el primer nivel.
        Se debe definir el fondo, las plataformas y los enemigos que aparezcan. '''
    
    """ Definicion del nivel 1. """

    def __init__(self, jugador):
        """ Metodo que crea el nivel 1 """

        # Se llama al metodo del padre constructor.
        Level.__init__(self, jugador)

        #Cargamos la imagen de fondo.
        self.fondo = pygame.image.load("imagenes/MesadaFONDO.png").convert()
        self.fondo.set_colorkey(constantes.BLANCO)
        self.limite_nivel = -12000
        self.limit_nivel_suelo=500
        self.limit_izquierdo=130

        nivel = [ [LIMITE, 50, 250], 
                  [MAYONESA, 500, 315],
                  [MAYONESA, 900, 260],
                  [LIMITE, 1700,250],
                  [VERSION_LARGA, 2000,220],
                  [VERSION_LARGA, 2480, 220],
                  [VERSION_LARGA, 2950,120],
                  [LIMITE,3340,250],
                  [MOVIMIENTO, 4100, 120],
                  [MAYONESA, 4522, 195],
                  [MAYONESA, 4950, 120],
                  [LIMITE, 5400, 250],
                  [MAYONESA, 5500, 95],
                  [MAYONESA, 6000, 95],
                  [MAYONESA,6500, 95],
                  [MAYONESA, 7100,95],
                  [LIMITE,7450,280],
                  [MAYONESA,7800,95]]
                  

        # Se busca en la lista anterior creada y se le agregan las plataformas al nivel.
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add(bloque)



            nivel_movimiento = [[MAYONESA, 1250, 220, 1150, 1650, 220, 220, 2, 0 ],
                                [MAYONESA,3600, 250, 3600, 3600, 150, 400, 0, 2  ],
                                [MAYONESA, 7460, 201, 7460, 7460, 200, 450, 0, 2],
                                [MAYONESA,8500, 90, 8250, 8900, 280, 280, 2.5, 0]]
        
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
        
       
        """# Se agrega una plataforma en movimiento.
        bloque = PlataformaConMovimiento(MAYONESA)
        bloque.rect.x = 1250
        bloque.rect.y = 220
        bloque.limite_izquierdo = 1150
        bloque.limite_derecho = 1650
        bloque.mover_x = 2
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)
        
        bloque = PlataformaConMovimiento(MAYONESA)
        bloque.rect.x = 3600
        bloque.rect.y = 250
        bloque.limite_inferior = 400
        bloque.limite_superior = 150
        bloque.mover_y = 1
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)"""
        
        




