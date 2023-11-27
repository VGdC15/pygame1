import pygame
from constantesCar import *
from menu import ejecutar_menu

def ejecutar_pantalla_ranking():
    pygame.init()
    screen = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA]) #se crea una ventana
    pygame.display.set_caption("Cars on Road - Verónica Castillo") #título de la ventana

    #fondo de pantalla 
    imagen_fondo = pygame.image.load("programacion/ejercicios/pygame/pantalla_ranking.png")
    imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

    boton_menu_principal = pygame.image.load("programacion/ejercicios/pygame/menu_principal.png")
    boton_menu_principal = pygame.transform.scale(boton_menu_principal, (ANCHO_BOTON, ALTO_BOTON))
    rect_boton_menu_principal = boton_menu_principal.get_rect()
    rect_boton_menu_principal.x = 60
    rect_boton_menu_principal.y = 440

    menu_principal = False
    run = True
    while run:
        #dibuja el fondo en la nueva posición
        screen.blit(imagen_fondo, (0,0))

        #Botones inicio
        screen.blit(boton_menu_principal,rect_boton_menu_principal) 

        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                run = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(evento.pos)
                if rect_boton_menu_principal.collidepoint(posicion_click):
                    menu_principal = True
                    run = False

        pygame.display.flip()

    if menu_principal:
        ejecutar_menu()
