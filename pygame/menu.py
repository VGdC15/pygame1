import pygame
from constantesCar import *
from logica_inicial import Juego
from funcion import *



def ejecutar_menu(ranking:list):
    iniciales = "" 

    pygame.init()
    screen = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA])
    pygame.display.set_caption("Cars on Road - Verónica Castillo")

    imagen_fondo = pygame.image.load("programacion/ejercicios/pygame/menu.png")
    imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

    boton_start = pygame.image.load("programacion/ejercicios/pygame/start.png")
    boton_start = pygame.transform.scale(boton_start, (ANCHO_BOTON, ALTO_BOTON))
    rect_boton_start = boton_start.get_rect()
    rect_boton_start.x = 50
    rect_boton_start.y = 350

    boton_ranking = pygame.image.load("programacion/ejercicios/pygame/score.png")
    boton_ranking = pygame.transform.scale(boton_ranking, (ANCHO_BOTON, ALTO_BOTON))
    rect_boton_ranking = boton_ranking.get_rect()
    rect_boton_ranking.x = 50
    rect_boton_ranking.y = 400

    # Campo de texto para ingresar iniciales
    pygame.draw.rect(imagen_fondo, COLOR_BLANCO, (75, 320, 350, 40))  # Rectángulo blanco para el campo de texto
    # Mostrar el fin del juego   
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render('Ingrese sus iniciales:', True, COLOR_NEGRO)
    imagen_fondo.blit(text, (80, 310))

    start = False
    ranking_boton = False
    run = True

    while run:
        screen.blit(imagen_fondo, (0, 0))
        screen.blit(boton_start, rect_boton_start)
        screen.blit(boton_ranking, rect_boton_ranking)

        font = pygame.font.Font(pygame.font.get_default_font(), 24)
        text_ingreso = font.render(iniciales, True, COLOR_NEGRO)      
        imagen_fondo.blit(text_ingreso, (80, 325))  

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(evento.pos)
                if rect_boton_start.collidepoint(posicion_click):
                    start = True
                    run = False
                elif rect_boton_ranking.collidepoint(posicion_click):
                    ranking_boton = True
                    run = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    iniciales = iniciales[0:-1]
                elif evento.key == pygame.K_RETURN:
                    name = iniciales
                else:
                    iniciales += evento.unicode

        if start:
            nivel_actual = 1
            #puntaje_acumulado = 0  # Inicializa el puntaje acumulado
            while nivel_actual <= 3:
                tiempo_nivel = obtener_tiempo_nivel(nivel_actual)
                print(f"Iniciando nivel {nivel_actual}, tiempo: {tiempo_nivel} segundos")

                # Pasar el puntaje acumulado al cargar_niveles
                nivel_completado= cargar_niveles(nivel_actual, tiempo_nivel)

                if nivel_completado:
                    print(f"Nivel {nivel_actual} completado")
                    nivel_actual += 1
                else:
                    print(f"Nivel {nivel_actual} no completado, saliendo del bucle")
                    break
      
        elif ranking_boton:
            ejecutar_pantalla_ranking(ranking)
              

        pygame.display.flip()

    pygame.quit()


def ejecutar_pantalla_ranking(ranking:list):
    pygame.init()

    screen = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA])
    pygame.display.set_caption("Cars on Road - Verónica Castillo")

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
        screen.blit(imagen_fondo, (0, 0))
        screen.blit(boton_menu_principal, rect_boton_menu_principal)

        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                run = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(evento.pos)
                if rect_boton_menu_principal.collidepoint(posicion_click):
                    menu_principal = True
                    run = False
            
            #font = pygame.font.Font(pygame.font.get_default_font(), 16)
        
        font_data = pygame.font.SysFont('Bauhaus 93', 30)
        for i in range(len(ranking)):
            texto_name = font_data.render(ranking[i]["name"], True, COLOR_NEGRO)
            imagen_fondo.blit(texto_name, (200, 320 + i * 60))

            texto_score = font_data.render(str(ranking[i]["score"]), True, COLOR_NEGRO)
            imagen_fondo.blit(texto_score, (200, 320 + i * 60))
            
        pygame.display.flip()
                
    if menu_principal:
        ejecutar_menu(ranking)


def ejecutar_nivel(rutas_enemigos, color_fondo, tiempo_nivel):
    # Crea una instancia del juego
    juego = Juego()

    # Cambia el color de fondo
    juego.cambiar_color_fondo(color_fondo)

    # Establece rutas_enemigos antes de ejecutar el juego
    juego.rutas_enemigos = rutas_enemigos

    # Ejecuta el juego y ajustar el tiempo del nivel
    nivel_completado = juego.ejecutar_juego(tiempo_nivel)
    return nivel_completado

def cargar_niveles(nivel: int, tiempo_nivel: int):
    rutas_enemigos = []
    color_fondo = None

    if nivel == 1:
        rutas_enemigos = ['programacion/ejercicios/pygame/carVerde.png', 'programacion/ejercicios/pygame/camioneta.png', 'programacion/ejercicios/pygame/carAmarillo.png', 'programacion/ejercicios/pygame/carPremio.png']
        color_fondo = COLOR_VERDE
    elif nivel == 2:
        rutas_enemigos = ['programacion/ejercicios/pygame/carVerde.png', 'programacion/ejercicios/pygame/camioneta.png', 'programacion/ejercicios/pygame/carAmarillo.png', 'programacion/ejercicios/pygame/camion.png']
        color_fondo = COLOR_CYAN
    elif nivel == 3:
        rutas_enemigos = ['programacion/ejercicios/pygame/car_fire.png', 'programacion/ejercicios/pygame/carPremio.png', 'programacion/ejercicios/pygame/sanidad.png', 'programacion/ejercicios/pygame/camion.png']
        color_fondo = COLOR_PURPURA

    # Ejecutar el nivel y pasar el puntaje acumulado
    nivel = ejecutar_nivel(rutas_enemigos, color_fondo, tiempo_nivel)
 
    return nivel
    

def obtener_tiempo_nivel(nivel: int):
    if nivel == 1:
        return 20
    elif nivel == 2:
        return 30
    elif nivel == 3:
        return 40
    return 0 

if __name__ == "__main__":
    puntaje_acumulado = ejecutar_menu()

