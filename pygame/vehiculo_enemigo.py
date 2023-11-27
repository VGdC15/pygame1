import pygame
import random
from vehiculo import Vehiculo
from constantesCar import *

class VehiculoEnemigo(Vehiculo):
    
    def __init__(self, x, y, rutas_enemigos, scale=1.2):
        super().__init__(self.obtener_imagen_aleatoria(rutas_enemigos), x, y, scale)
        
    def obtener_imagen_aleatoria(self, rutas_enemigos):
        nombre_archivo = random.choice(rutas_enemigos)
        return pygame.image.load(nombre_archivo)
    
    def mover_vehiculo(self, speed):
        self.rect.y += speed

    def actualizar(self, speed, score):
        self.mover_vehiculo(speed)
        
        # Quitar el vehículo una vez que sale de la pantalla
        if self.rect.top >= ALTO_VENTANA:
            self.kill()           
            # Sumar a la puntuación
            score += 10
        return score
