import pygame
import constantes
from funciones_spritesheet import SpriteSheet


class BOSS(pygame.sprite.Sprite):
    # -- Atributos
    mover_x = 0
    
    # Estas listas definen todas las imagenes de nuestro jugador.
    jugador_frame_der = []
    
    jugador = None

    # Direccion en la que va el jugador.
    direccion = "R"

    # Lista de sprite con las cosas que nos podemos chocar.
    nivel = None
    
    def __init__(self,ruta):
        """ __Funcion constructor__ 
            Aca en donde se debe cargar el sprite sheet del jugador.
            Se debe cargar los sprite con movimiento hacia la izquierda y hacia la derecha.
        """

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet(ruta)
        
        # Carga de todos los sprite de la imagen hacia la derecha.
        imagen = sprite_sheet.obtener_imagen(0, 0, 250, 600,constantes.BLANCO)
        self.jugador_frame_der.append(imagen)
        imagen = sprite_sheet.obtener_imagen(280, 0, 280, 600,constantes.BLANCO)
        self.jugador_frame_der.append(imagen)
        imagen = sprite_sheet.obtener_imagen(560, 0, 280, 600,constantes.BLANCO)
        self.jugador_frame_der.append(imagen)
        imagen = sprite_sheet.obtener_imagen(873, 0, 280, 600,constantes.BLANCO)
        self.jugador_frame_der.append(imagen)
        imagen = sprite_sheet.obtener_imagen(1185, 0, 285, 600,constantes.BLANCO)
        self.jugador_frame_der.append(imagen)      

        # Seteamos con que sprite comenzar
        self.image = self.jugador_frame_der[0]


        self.rect = self.image.get_rect()


    def update(self):
        """ Metodo que actualiza la posicion del jugador. """

        # Movimientos Izquierda/Derecha
        self.rect.x += self.mover_x
        pos = self.rect.x 
        if self.direccion == "R":
            frame = (pos // 30) % len(self.jugador_frame_der)
            self.image = self.jugador_frame_der[frame]

        # Verficiamos si colisionamos con algo mientras avanzamos
        lista_de_bloques_colisionados = pygame.sprite.spritecollide(self, self.nivel.lista_plataformas, False)
        for block in lista_de_bloques_colisionados:
            if self.mover_x > 0:
                block.kill()
            elif self.mover_x < 0:
                block.kill()

        
        # Verificamos si coalisionamos con un punto
        lista_de_puntos = pygame.sprite.spritecollide(self, self.nivel.lista_puntos, False)
        for un_punto in lista_de_puntos:
            un_punto.kill()
            
        # Verificamos si coalisionamos con un enemigo
        lista_de_enemigos = pygame.sprite.spritecollide(self, self.nivel.lista_enemigos, False)
        for un_enemigo in lista_de_enemigos:
            un_enemigo.kill()
        
        # Verificamos si coalisionamos con una vida
        lista_de_vidas = pygame.sprite.spritecollide(self, self.nivel.lista_vidas, False)
        for una_vida in lista_de_vidas:
            una_vida.kill()
            
        hit = pygame.sprite.collide_rect(self, self.jugador)
        if hit:
            self.jugador.vidas = 0
        

    def avanzar(self):
        """ Se llama cuando movemos hacia la der. """
        
        self.mover_x = 1
        self.direccion = "R"

        
        