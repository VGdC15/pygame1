import pygame
from constantesCar import *

class Carretera:
    def __init__(self):
        self.marcadores = [(95, 0, ANCHO_MARCADOR, ALTO_VENTANA), (395, 0, ANCHO_MARCADOR, ALTO_VENTANA)]
        self.marcador_color = COLOR_AMARILLO
        self.marcadores_dos = [(75, 0, ANCHO_MARCADOR, ALTO_VENTANA), (415, 0, ANCHO_MARCADOR, ALTO_VENTANA)]
        self.marcador_color_dos = COLOR_BLANCO
        self.movimiento_y_marcador = 0

    def actualizar(self, speed):
        self.movimiento_y_marcador += speed * 2
        if self.movimiento_y_marcador >= ALTO_MARCADOR * 2:
            self.movimiento_y_marcador = 0

    def dibujar(self, screen, carriles):
        pygame.draw.rect(screen, COLOR_GRIS, (100, 0, ANCHO_CAMINO, ALTO_VENTANA))
        for i in range(ALTO_MARCADOR * -2, ALTO_VENTANA, ALTO_MARCADOR * 2):
            for carril in carriles:
                pygame.draw.rect(screen, COLOR_BLANCO, (carril + 45, i + self.movimiento_y_marcador, ANCHO_MARCADOR, ALTO_MARCADOR))
        for marcador in self.marcadores:
            pygame.draw.rect(screen, self.marcador_color, marcador)
        for marcador in self.marcadores_dos:
            pygame.draw.rect(screen, self.marcador_color_dos, marcador)

"""import pygame
from constantesCar import *

class Carretera:
    def __init__(self):
        self.marcadores = [(95, 0, ANCHO_MARCADOR, ALTO_VENTANA), (395, 0, ANCHO_MARCADOR, ALTO_VENTANA)]
        self.marcador_color = COLOR_AMARILLO
        self.movimiento_y_marcador = 0

    def cargar_imagen(self, ruta_archivo: str):
        # Cargar la imagen y escalarla
        imagen = pygame.image.load(ruta_archivo)
        imagen = pygame.transform.scale(imagen, (ANCHO_VENTANA, ALTO_VENTANA))
        return imagen

    def actualizar(self, speed): 
        self.movimiento_y_marcador += speed * 2
        if self.movimiento_y_marcador >= ALTO_MARCADOR * 2:
            self.movimiento_y_marcador = 0

    def dibujar(self, screen, carriles):
        pygame.draw.rect(screen, COLOR_GRIS, (100, 0, ANCHO_CAMINO, ALTO_VENTANA))
        for i in range(ALTO_MARCADOR * -2, ALTO_VENTANA, ALTO_MARCADOR * 2):
            for carril in carriles:
                pygame.draw.rect(screen, COLOR_BLANCO, (carril + 45, i + self.movimiento_y_marcador, ANCHO_MARCADOR, ALTO_MARCADOR))

            # Dibujar la imagen de los arbolitos superpuesta
            screen.blit(self.cargar_imagen, (0, i + self.movimiento_y_marcador))

        for marcador in self.marcadores:
            pygame.draw.rect(screen, self.marcador_color, marcador)"""

