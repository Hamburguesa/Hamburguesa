#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import constantes
from menu import cMenu, EVENT_CHANGE_STATE
import menu
from Boss import BOSS
from nivel1 import Level_01
from nivel2 import Level_02 
from jugador import Player
from time import time


def Play(pantalla,time2, jugador):
    tiempo_comienzo = time() + time2
        
    # Creamos al jugador con la imagen p1_walk.png
    jugador_principal = Player(jugador)
    letraParaPuntos = pygame.font.Font(None, 24)
    letraParaVidas = pygame.font.Font(None, 24)
    letraTiempo = pygame.font.Font(None, 24)
    Jefe_final = BOSS("imagenes/cheff.png")
    
# Creamos todos los niveles del juego
    lista_niveles = []
    #lista_niveles.append(Level_01(jugador_principal))
    lista_niveles.append(Level_02(jugador_principal))
    
# Seteamos cual es el primer nivel.
    numero_del_nivel_actual = 0
    nivel_actual = lista_niveles[numero_del_nivel_actual]
    lista_sprites_activos = pygame.sprite.Group()
    jugador_principal.nivel = nivel_actual
    jugador_principal.rect.x = 200
    jugador_principal.rect.y = constantes.LARGO_PANTALLA - jugador_principal.rect.height - 120
    lista_sprites_activos.add(jugador_principal)
    letraParaMarcador1 = pygame.font.Font(None, 56)
    letraParaMarcador2 = pygame.font.Font(None, 36)
    
    no_aparece_boss = True
    
# Variable booleano que nos avisa cuando el usuario aprieta el botOn salir.
    salir = False
    clock = pygame.time.Clock()
# -------- Loop Principal -----------
    while not salir:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                salir = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    jugador_principal.avanzarr()
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
        # Si el jugador se mueve hacia el fin del nivel cambia el jugador al siguiente nivel.
        current_position = jugador_principal.rect.x + nivel_actual.posicion_jugador_nivel
        if current_position < nivel_actual.limite_nivel:
            jugador_principal.rect.x = 120
            if numero_del_nivel_actual < len(lista_niveles) - 1:
                current_position=0
                pygame.event.wait()
                Jefe_final.kill()
                numero_del_nivel_actual += 1
                nivel_actual = lista_niveles[numero_del_nivel_actual]
                jugador_principal.nivel = nivel_actual
                tiempo_comienzo = time() + time2
                no_aparece_boss = True
                jugador_principal.vidas = jugador_principal.vidas + 5
            else:
                pantalla.fill(constantes.NEGRO)
                texto_gameover3 = letraParaMarcador1.render(u"¡Has Ganado!", 1, constantes.ROJO)
                texto_gameover4 = letraParaMarcador2.render("Presiona cualquier tecla para volver a jugar", 1, constantes.ROJO)
                pantalla.blit(texto_gameover3, [300, 250])
                pantalla.blit(texto_gameover4, [200, 310])
                pygame.display.flip()
                pygame.event.wait()
                main()
                
        #Lo que modifique fue esto, el menu y la funcion play
               
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
        
        LetraMensaje = pygame.font.Font(None, 38)
        El_Mensaje = LetraMensaje.render("El chef se acerca, apurate", 1, constantes.ROJO)
        
        if tiempo_transcurrido < 30 and no_aparece_boss:
                pantalla.blit(El_Mensaje,(330,80))
            
            
        
        if tiempo_transcurrido < 20 and no_aparece_boss:
                Jefe_final.nivel = nivel_actual
                Jefe_final.rect.x = jugador_principal.rect.x - 950 
                Jefe_final.rect.y = constantes.LARGO_PANTALLA - Jefe_final.rect.height 
                Jefe_final.jugador = jugador_principal
                lista_sprites_activos.add(Jefe_final)
                no_aparece_boss = False
        
                
        if current_position < nivel_actual.posicion_bigboss and no_aparece_boss:
                Jefe_final.nivel = nivel_actual
                Jefe_final.rect.x = jugador_principal.rect.x - 950 
                Jefe_final.rect.y = constantes.LARGO_PANTALLA - Jefe_final.rect.height 
                Jefe_final.jugador = jugador_principal
                lista_sprites_activos.add(Jefe_final)
                no_aparece_boss = False
                print current_position
                
        # TODO EL CODIGO PARA DIBUJAR DEBE IR POR ARRIBA DE ESTE COMENTARIO.
        clock.tick(60)
        pygame.display.flip()
        if jugador_principal.vidas == 0 or tiempo_transcurrido == 0:
            pantalla.fill(constantes.NEGRO)
            print current_position
            texto_gameover1 = letraParaMarcador1.render("GAME OVER", 1, constantes.ROJO)
            texto_gameover2 = letraParaMarcador2.render("Presiona cualquier tecla para volver a jugar", 1, constantes.ROJO)
            pantalla.blit(texto_gameover1, [300, 250])
            pantalla.blit(texto_gameover2, [200, 310])
            pygame.display.flip()
            pygame.event.wait()
            main()
            
        pygame.display.flip()
        if jugador_principal.vidas == -1:
            pantalla.fill(constantes.NEGRO)
            print current_position
            texto_gg = letraParaMarcador1.render("HAS GANADO con "+ str(tiempo_transcurrido) + "segundos sobrantes" , 1, constantes.ROJO)
            texto_gameover2 = letraParaMarcador2.render("Presiona cualquier tecla para volver a jugar", 1, constantes.ROJO)
            pantalla.blit(texto_gg, [300, 250])
            pantalla.blit(texto_gameover2)
            pygame.display.flip()
            pygame.event.wait()
            main()
            
            
    # Salgo del juego
    return True
    

def main():
    """ Clase principal en el que se debe ejecutar el juego. """
    pygame.init()

    # Configuramos el alto y largo de la pantalla
    tamanio = [constantes.ANCHO_PANTALLA, constantes.LARGO_PANTALLA]
    pantalla = pygame.display.set_mode(tamanio)
    
    # Sonido principal
    sonido3 = pygame.mixer.Sound("sonidos/FondoSound.wav")
    sonido3.play(-1)
    pygame.display.set_caption("Comida rapida")

    # Imagenes de frente
    Hamburger = pygame.image.load("imagenes/hamburguesafrente.png")
    Papas = pygame.image.load("imagenes/papafritafrente.png")
    
    
    logo = pygame.image.load("imagenes/logo.png").convert()
    logo.set_colorkey(constantes.BLANCO)
    menu_principal = cMenu(10, 30, 75, 35, "vertical", 5, pantalla, [("Jugar", 1, None), ("Historia", 2, None), (u"Créditos", 3, None), (u"Cómo jugar", 7, None), ("Salir", 4, None)])
    menuJugador = cMenu(160, 100, 75, 5, "horizontal", 3, pantalla, [("", 5, Hamburger), ("", 6, Papas), ("Volver", 0, None)])
    historia = cMenu(800, 500, 400, 400, 'horizontal', 1, pantalla, [("Volver", 0, None)])
    creditos = cMenu(800, 500, 630, 348, 'horizontal', 1, pantalla, [("Volver", 0, None)])
    How_to_play = cMenu(800, 500, 630, 348, "horizontal", 1, pantalla, [("Volver", 0, None)])
    Menu_dificultad = cMenu(135, 120, 100, 100, "vertical", 3, pantalla, [(u"Fácil", 8, None), (u"Difícil", 9, None), ("Volver", 1, None)])
    
    menuJugador.set_center(True, True)
    menuJugador.set_alignment("center", "center")
    
    Menu_dificultad.set_center(True, True)
    Menu_dificultad.set_alignment("center", "center")
    
    letraParaCreditos = pygame.font.Font(None, 45)
    estado = 0
    estado_previo = 1
    opcion = []
    salir = False
    
    historiaa = pygame.image.load("imagenes/historia.png").convert()
    historiaa.set_colorkey(constantes.BLANCO)
    textoCreditos1 = letraParaCreditos.render("Utiliza las flechas izquierda y derecha para moverte hacia delante", 1, constantes.BLANCO)
    textoCreditos7 = letraParaCreditos.render("y atras", 1, constantes.BLANCO)
    textoCreditos2 = letraParaCreditos.render("Utiliza la flecha superior para saltar", 1, constantes.BLANCO)
    textoCreditos3 = letraParaCreditos.render("Captura los sachets de mayonesa para sumar puntos", 1, constantes.BLANCO)
    textoCreditos4 = letraParaCreditos.render("Captura los sachets de ketchup para recuperar vidas", 1, constantes.BLANCO)
    textoCreditos5 = letraParaCreditos.render("Esquiva las ratas para no perder vidas", 1, constantes.BLANCO)
    textoCreditos6 = letraParaCreditos.render(u"El chef te persigue, si te atrapa el juego terminará ", 1, constantes.BLANCO)
    CreditosReales1 = letraParaCreditos.render("Historia: Manuel Freire, Antonela Tapia, Fernanda Mayer", 1, constantes.BLANCO)
    CreditosReales3 = letraParaCreditos.render("Fondo de los niveles: Fernanda Mayer", 1, constantes.BLANCO)
    CreditosReales4 = letraParaCreditos.render(u"Personajes: Lucio Méndez, Fernanda Mayer y Agustín Rodríguez", 1, constantes.BLANCO)
    CreditosReales5 = letraParaCreditos.render(u"Programación: Manuel Freire", 1, constantes.BLANCO)
    CreditosReales6 = letraParaCreditos.render("Agradecimientos: Manuel Garrido, Rosario Sosa, Mariana Betervide, ", 1, constantes.BLANCO)
    CreditosReales2 = letraParaCreditos.render(u"Joel Barros, Cinthia Núñez, Mario La Cámera, Patricia Aldaz, Pablo", 1, constantes.BLANCO)
    CreditosReales7 = letraParaCreditos.render(u"Navas y los Rodrigos Pérez", 1, constantes.BLANCO)
    
    while not salir:
        e = pygame.event.wait()
        if estado != estado_previo:
            pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key=0))
            estado_previo = estado

            if estado == 0:
                pantalla.fill(constantes.NEGRO)
                pantalla.blit(logo, (300, 50))
                pygame.display.flip()
            elif estado == 1:
                pantalla.fill(constantes.NEGRO)
                pygame.display.flip()
            elif estado == 2:
                pantalla.fill(constantes.NEGRO)
                pantalla.blit(logo, (200, 50))
                pantalla.blit(historiaa,(200,80))
                pygame.display.flip()
            elif estado == 3:
                pantalla.fill(constantes.NEGRO)
                pantalla.blit(logo, (200, 50))
                pantalla.blit(CreditosReales1, (25, 20))
                pantalla.blit(CreditosReales3, (25, 110))
                pantalla.blit(CreditosReales4, (25, 200))
                pantalla.blit(CreditosReales5, (25, 290))
                pantalla.blit(CreditosReales6, (25, 380))
                pantalla.blit(CreditosReales2, (25, 420))
                pantalla.blit(CreditosReales7, (25, 460))
                pygame.display.flip()
            elif estado == 7:
                pantalla.fill(constantes.NEGRO)
                pantalla.blit(logo, (200, 50))
                pantalla.blit(textoCreditos1, (25, 10))
                pantalla.blit(textoCreditos7, (25, 40))
                pantalla.blit(textoCreditos2, (25, 110))
                pantalla.blit(textoCreditos3, (25, 210))
                pantalla.blit(textoCreditos4, (25, 310))
                pantalla.blit(textoCreditos5, (25, 410))
                pantalla.blit(textoCreditos6, (25, 510))
                pygame.display.flip()
            else:
                pantalla.fill(constantes.NEGRO)
                pygame.display.flip()

        if e.type == pygame.KEYDOWN or e.type == menu.EVENT_CHANGE_STATE:
            if estado == 0:
                opcion, estado = menu_principal.update(e, estado)
            elif estado == 1:
                opcion, estado = menuJugador.update(e, estado)
            elif estado == 2:
                opcion, estado = historia.update(e, estado)
            elif estado == 3:
                opcion, estado = creditos.update(e, estado)
            elif estado == 4:
                salir = True
            elif estado == 5:
                jugador = 1
                opcion, estado = Menu_dificultad.update(e, estado)
            elif estado == 6:
                jugador = 2
                opcion, estado = Menu_dificultad.update(e, estado)
            elif estado == 7:
                opcion, estado = How_to_play.update(e, estado)
            elif estado == 8:
                Play(pantalla, 200, jugador)
            elif estado == 9:
                Play(pantalla, 140, jugador)

        if e.type == pygame.QUIT:
            salir = True
        pygame.display.update(opcion)

    pygame.quit()
         

if __name__ == "__main__":
    main()
