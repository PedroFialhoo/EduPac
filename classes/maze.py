import pygame
from settings import Colors
class Maze:
    def __init__(self, screen):
        self.maze = [
    # Bordas externas (topo, base, esquerda, direita)
    pygame.Rect(0, 75, 1000, 10),   # topo
    pygame.Rect(0, 790, 1000, 10),   # base
    pygame.Rect(0, 75, 10, 720),   # esquerda
    pygame.Rect(990, 75, 10, 720),   # direita

    # Paredes internas adaptadas proporcionalmente
     # Parte superior 
    pygame.Rect(100, 175, 270, 10),
    pygame.Rect(630, 175, 270, 10),
    pygame.Rect(100, 175, 10, 220),
    pygame.Rect(900, 175, 10, 220),

    pygame.Rect(250, 270, 150, 10),
    pygame.Rect(600, 270, 150, 10),

    # Corredores laterais 
    pygame.Rect(100, 500, 200, 10),
    pygame.Rect(700, 500, 200, 10),
    pygame.Rect(100, 500, 10, 200),
    pygame.Rect(900, 500, 10, 200),

    # Centro horizontal
    pygame.Rect(300, 400, 400, 10),
    pygame.Rect(500, 400, 10, 300),

    # Parte inferior
    pygame.Rect(250, 600, 150, 10),
    pygame.Rect(600, 600, 150, 10),
    pygame.Rect(250, 600, 10, 100),
    pygame.Rect(750, 600, 10, 100),

    pygame.Rect(400, 700, 200, 10),
]

        self.screen = screen
    
    def draw_maze(self):
        for barrier in self.maze:
            pygame.draw.rect(self.screen, Colors.BLUE, barrier)