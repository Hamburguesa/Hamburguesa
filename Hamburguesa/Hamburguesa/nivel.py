import pygame

import constantes

class Level():
    """ Super-Clase generica usada para definir los niveles del juego. 
        Se debe crear una clase hija para cada nivel."""

    # Lista de todos los sprites utilizados en todos los niveles.  
    lista_plataformas = None
    lista_enemigos = None
    lista_puntos = None
    lista_vidas = None
    #lista_gg = None

    # Imagen de fondo
    fondo = None

    # Valor numerico de que tan lejos avanzo nuestro jugador en el nivel
    posicion_jugador_nivel = 0
    posicion_bigboss = 0
    limite_nivel = -1000
    limit_nivel_suelo=0
    limit_izquierdo=0 

    def __init__(self, jugador):
        """ Constructor. Se le debe pasar al jugador para saber sobre que nivel esta. """
        self.lista_plataformas = pygame.sprite.Group()
        self.lista_enemigos = pygame.sprite.Group()
        self.lista_puntos = pygame.sprite.Group()
        self.lista_vidas = pygame.sprite.Group()
        #self.lista_gg = pygame.sprite.Group()
        self.jugador = jugador


    def update(self):
        """ Actualizar todo sobre el nivel """
        self.lista_plataformas.update()
        self.lista_enemigos.update()
        self.lista_puntos.update()
        self.lista_vidas
        #self.lista_gg = pygame.sprite.Group()
    def draw(self, pantalla):
        """ Dibujamos todo sobre el nivel. """

        # Se debe dibujar el fondo.
        pantalla.fill(constantes.NEGRO)
        pantalla.blit(self.fondo,(self.posicion_jugador_nivel // 3,0))

        # Se dibujan todos los sprite que se cargaron.
        self.lista_plataformas.draw(pantalla)
        self.lista_enemigos.draw(pantalla)
        self.lista_puntos.draw(pantalla)
        self.lista_vidas.draw(pantalla)
        #self.lista_gg.draw(pantalla)

    def avance_nivel(self, avance_x):
        """ Cuando el usuario se mueve de izquierda/derecha se debe mover el nivel """

        self.posicion_jugador_nivel += avance_x

        for plataforma in self.lista_plataformas:
            plataforma.rect.x += avance_x

        for enemigo in self.lista_enemigos:
            enemigo.rect.x += avance_x
            
        for comidas in self.lista_puntos:
            comidas.rect.x+=avance_x
            
        for vidas in self.lista_vidas:
            vidas.rect.x+=avance_x
            
        #for gg in self.lista_gg:
            #gg.rect.x+=avance_x