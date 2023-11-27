import pygame

"""class Vehiculo(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        image_scale = 45 / image.get_rect().width
        nuevo_ancho = image.get_rect().width * image_scale
        nuevo_alto = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (int(nuevo_ancho), int(nuevo_alto)))
        
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        
class PlayerCar(Vehiculo):
    
    def __init__(self, x, y):
        image = pygame.image.load('programacion\ejercicios\pygame\PlayerCar.png')
        super().__init__(image, x, y)"""

class Vehiculo(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y, scale=1.0):
        pygame.sprite.Sprite.__init__(self)
        
        nuevo_ancho = int(image.get_rect().width * scale)
        nuevo_alto = int(image.get_rect().height * scale)
        self.image = pygame.transform.scale(image, (nuevo_ancho, nuevo_alto))
        
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        
class PlayerCar(Vehiculo):
    
    def __init__(self, x, y, scale=1.0):  # Añadir un argumento de escala
        image = pygame.image.load('programacion\ejercicios\pygame\PlayerCar.png')
        super().__init__(image, x, y, scale)  # Pasar la escala a la superclase