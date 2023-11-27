import pygame
from logica_inicial import Juego
from constantesCar import *
from menu import ejecutar_menu




def ejecutar_nivel(rutas_enemigos, color_fondo, tiempo_nivel):
    # Crear una instancia del juego
    juego = Juego()

    # Cambiar el color de fondo
    juego.cambiar_color_fondo(color_fondo)

    # Establecer rutas_enemigos antes de ejecutar el juego
    juego.rutas_enemigos = rutas_enemigos

    # Ejecutar el juego y ajustar el tiempo del nivel
    juego.ejecutar_juego(tiempo_nivel=tiempo_nivel)

"""def cargar_niveles(nivel: int):
    nivel_completado = False

    if nivel == 1:
        nivel_uno_rutas_enemigos = ['programacion\ejercicios\pygame\carVerde.png', 'programacion\ejercicios\pygame\camioneta.png', 'programacion\ejercicios\pygame\carAmarillo.png', 'programacion\ejercicios\pygame\carPremio.png']
        nivel_completado = ejecutar_nivel(nivel_uno_rutas_enemigos, COLOR_VERDE, 60)
    elif nivel == 2:
        nivel_dos_rutas_enemigos = ['programacion\ejercicios\pygame\carVerde.png', 'programacion\ejercicios\pygame\camioneta.png', 'programacion\ejercicios\pygame\carAmarillo.png', 'programacion\ejercicios\pygame\camion.png']
        nivel_completado = ejecutar_nivel(nivel_dos_rutas_enemigos, COLOR_CYAN, 70)
    elif nivel == 3:
        nivel_tres_rutas_enemigos = ['programacion\ejercicios\pygame\car_fire.png', 'programacion\ejercicios\pygame\carPremio.png', 'programacion\ejercicios\pygame\sanidad.png', 'programacion\ejercicios\pygame\camion.png']
        nivel_completado = ejecutar_nivel(nivel_tres_rutas_enemigos, COLOR_PURPURA, 500)
    
    return nivel_completado"""

def cargar_niveles(nivel: int):
    nivel_completado = False

    if nivel == 1:
        nivel_uno_rutas_enemigos = ['programacion/ejercicios/pygame/carVerde.png', 'programacion/ejercicios/pygame/camioneta.png', 'programacion/ejercicios/pygame/carAmarillo.png', 'programacion/ejercicios/pygame/carPremio.png']
        nivel_completado = ejecutar_menu(nivel_uno_rutas_enemigos, COLOR_VERDE, 60)
    elif nivel == 2:
        nivel_dos_rutas_enemigos = ['programacion/ejercicios/pygame/carVerde.png', 'programacion/ejercicios/pygame/camioneta.png', 'programacion/ejercicios/pygame/carAmarillo.png', 'programacion/ejercicios/pygame/camion.png']
        nivel_completado = ejecutar_menu(nivel_dos_rutas_enemigos, COLOR_CYAN, 70)
    elif nivel == 3:
        nivel_tres_rutas_enemigos = ['programacion/ejercicios/pygame/car_fire.png', 'programacion/ejercicios/pygame/carPremio.png', 'programacion/ejercicios/pygame/sanidad.png', 'programacion/ejercicios/pygame/camion.png']
        nivel_completado = ejecutar_menu(nivel_tres_rutas_enemigos, COLOR_PURPURA, 500)
    
    return nivel_completado



