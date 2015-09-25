import pygame

import constantes
from menu import cMenu, EVENT_CHANGE_STATE
import menu
from Boss import BOSS
from nivel1 import Level_01
from nivel2 import Level_02 

from jugador import Player
from time import time


def Play(pantalla,jugador):
    tiempo_comienzo = time() +100
    
    # Creamos al jugador con la imagen p1_walk.png
    jugador_principal = Player("imagenes/movimientos hamburger.png")
    letraParaPuntos = pygame.font.Font(None, 24)
    letraParaVidas = pygame.font.Font(None, 24)
    letraTiempo = pygame.font.Font(None, 24)
    Jefe_final = BOSS("imagenes/chef.png")
    
# Creamos todos los niveles del juego
    lista_niveles = []
    lista_niveles.append(Level_01(jugador_principal))
    lista_niveles.append(Level_02(jugador_principal))
    
    lista_niveles.append(Level_01(Jefe_final))
    
# Seteamos cual es el primer nivel.
    numero_del_nivel_actual = 0
    nivel_actual = lista_niveles[numero_del_nivel_actual]
    lista_sprites_activos = pygame.sprite.Group()
    jugador_principal.nivel = nivel_actual
    jugador_principal.rect.x = 700
    jugador_principal.rect.y = constantes.LARGO_PANTALLA - jugador_principal.rect.height - 120
    lista_sprites_activos.add(jugador_principal)
    letraParaMarcador1 = pygame.font.Font(None, 56)
    letraParaMarcador2 = pygame.font.Font(None, 36)
    
    Jefe_final.nivel = lista_niveles[0]
    Jefe_final.rect.x = -3000
    Jefe_final.rect.y = constantes.LARGO_PANTALLA - Jefe_final.rect.height 
    Jefe_final.jugador = jugador_principal
    lista_sprites_activos.add(Jefe_final)
    
#Variable booleano que nos avisa cuando el usuario aprieta el botOn salir.
    salir = False
    clock = pygame.time.Clock()
# -------- Loop Principal -----------
    while not salir:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                salir = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    jugador_principal.retroceder()
                if evento.key == pygame.K_RIGHT:
                    jugador_principal.avanzar()
                if evento.key == pygame.K_UP:
                    jugador_principal.saltar()
                if evento.key == pygame.K_ESCAPE:
                    salir = True
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT and jugador_principal.mover_x < 0:
                    jugador_principal.parar()
                if evento.key == pygame.K_RIGHT and jugador_principal.mover_x > 0:
                    jugador_principal.parar()
            
        Jefe_final.avanzar()
        
        # Actualiza todo el jugador
        lista_sprites_activos.update()
        # Actualiza los elementos del nivel
        nivel_actual.update()
        # Si el jugador se acarca hacia el lado derecho mueve el mundo hacia la izquierda (-x)
        if jugador_principal.rect.x >= 500:
            diff = jugador_principal.rect.x - 500
            jugador_principal.rect.x = 500
            nivel_actual.avance_nivel(-diff)
        # Si el jugador se acarca hacia el lado izquierda mueve el mundo hacia la derecha (-x)
        if jugador_principal.rect.x <= 120:
            diff = 120 - jugador_principal.rect.x
            jugador_principal.rect.x = 120
            nivel_actual.avance_nivel(diff)
        #Si el jugador se mueve hacia el fin del nivel cambia el jugador al siguiente nivel.
        current_position = jugador_principal.rect.x + nivel_actual.posicion_jugador_nivel
        if current_position < nivel_actual.limite_nivel:
            jugador_principal.rect.x = 120
            if numero_del_nivel_actual < len(lista_niveles) - 1:
                numero_del_nivel_actual += 1
                nivel_actual = lista_niveles[numero_del_nivel_actual]
                jugador_principal.nivel = nivel_actual
        # TODO EL CODIGO PARA DIBUJAR DEBE IR DEBAJO DE ESTE COMENTARIO.
        nivel_actual.draw(pantalla)
        lista_sprites_activos.draw(pantalla)
        
        textoPuntos = letraParaPuntos.render("Puntos: " + str(jugador_principal.puntos), 1, constantes.NEGRO)
        pantalla.blit(textoPuntos, (10, 10))
        
        textoVidas = letraParaVidas.render("Vidas: " + str(jugador_principal.vidas), 1, constantes.NEGRO)
        pantalla.blit(textoVidas, (900, 10))
        
        tiempo_transcurrido = int(tiempo_comienzo - time())
        textoTiempo = letraTiempo.render("Tiempo: " + str(tiempo_transcurrido), 1, constantes.NEGRO)
        pantalla.blit(textoTiempo, (300, 10))
        # TODO EL CODIGO PARA DIBUJAR DEBE IR POR ARRIBA DE ESTE COMENTARIO.
        clock.tick(60)
        pygame.display.flip()
        if jugador_principal.vidas == 0 or tiempo_transcurrido == 0:
            pantalla.fill(constantes.NEGRO)
            texto_gameover1 = letraParaMarcador1.render("GAME OVER", 1, constantes.ROJO)
            texto_gameover2 = letraParaMarcador2.render("Presione cualquier tecla para volver a jugar", 1, constantes.ROJO)
            pantalla.blit(texto_gameover1, [300, 250])
            pantalla.blit(texto_gameover2, [200, 310])
            pygame.display.flip()
            pygame.event.wait()
            main()
            
    #Salgo del juego
    return True
    

def main():
    """ Clase principal en el que se debe ejecutar el juego. """
    pygame.init()

    # Configuramos el alto y largo de la pantalla
    tamanio = [constantes.ANCHO_PANTALLA, constantes.LARGO_PANTALLA]
    pantalla = pygame.display.set_mode(tamanio)
    
    #Sonido principal
    sonido3 = pygame.mixer.Sound("sonidos/FondoSound.wav")
    sonido3.play(-1)
    pygame.display.set_caption("Comida rapida")
    
    menu_principal = cMenu(10,50,50,39,"vertical",4,pantalla,[("Jugar",1,None),("Historia",2,None),("Creditos",3,None),("Salir",4,None)])
    menuJugador = cMenu(30, 350, 100, 5, "horizontal", 3, pantalla, [("Hamburguesa",5, None),("Papa Frita",6,None),("Volver",0,None)])
    historia = cMenu (800,500, 400, 400, 'horizontal',1,pantalla,[("Volver", 0, None)])
    creditos = cMenu (800,500, 630, 348, 'horizontal',1,pantalla,[("Volver", 0, None)])
    
    menuJugador.set_center(True, True)
    menuJugador.set_alignment("center", "center")

    estado = 0
    estado_previo = 1
    opcion = []
    salir = False
    logo = pygame.image.load("imagenes/logo.png").convert()
    logo.set_colorkey(constantes.BLANCO)
    
    
    while (not salir):
        e = pygame.event.wait()
        
        if estado != estado_previo:
            pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key = 0))
            estado_previo = estado
        
        if e.type == pygame.KEYDOWN or e.type == menu.EVENT_CHANGE_STATE:
            if estado == 0:
                opcion, estado = menu_principal.update(e,estado)
                pantalla.blit(logo,(250,20)) 
                pygame.display.flip()
            
            elif estado == 1:
                pantalla.fill(constantes.NEGRO)
                opcion, estado = menuJugador.update(e, estado)
                pygame.display.flip()

            elif estado == 2:
                pantalla.fill(constantes.NEGRO)
                opcion, estado = historia.update(e, estado)
                pygame.display.flip()

            elif estado == 3:
                pantalla.fill(constantes.NEGRO)
                opcion, estado = creditos.update(e, estado)
                pygame.display.flip()
            
            elif estado == 4:
                salir=True
            
            elif estado == 5:
                jugador = 1
                Play(pantalla, jugador)
            
            elif estado == 6:
                jugador = 2
                Play(pantalla, jugador)
            
            
        if e.type == pygame.QUIT:
            salir = True
            
        pygame.display.update(opcion)

        
    pygame.quit()

    

if __name__ == "__main__":
    main()
