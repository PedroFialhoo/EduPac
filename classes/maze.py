import pygame
from settings import Colors
class Maze:
    def __init__(self, screen):
        self.maze = [
    # Bordas externas (topo, base, esquerda, direita)
    pygame.Rect(0, 100, 1000, 10),   # topo
    pygame.Rect(0, 790, 1000, 10),   # base
    pygame.Rect(0, 100, 10, 700),   # esquerda
    pygame.Rect(990, 100, 10, 700),   # direita

    # Paredes internas adaptadas proporcionalmente
     # ▓▓▓▓ Parte superior ▓▓▓▓
    pygame.Rect(100, 150, 200, 10),
    pygame.Rect(700, 150, 200, 10),
    pygame.Rect(100, 150, 10, 150),
    pygame.Rect(900, 150, 10, 150),

    pygame.Rect(250, 200, 150, 10),
    pygame.Rect(600, 200, 150, 10),

    # ▓▓▓▓ Corredores laterais ▓▓▓▓
    pygame.Rect(100, 350, 200, 10),
    pygame.Rect(700, 350, 200, 10),
    pygame.Rect(100, 350, 10, 200),
    pygame.Rect(900, 350, 10, 200),

    # ▓▓▓▓ Centro horizontal ▓▓▓▓
    pygame.Rect(300, 400, 400, 10),

    # ▓▓▓▓ Jaula dos fantasmas ▓▓▓▓
    pygame.Rect(430, 410, 10, 80),
    pygame.Rect(560, 410, 10, 80),
    pygame.Rect(430, 490, 140, 10),
    #pygame.Rect(430, 410, 140, 10),

    # ▓▓▓▓ Acesso à jaula ▓▓▓▓
    #pygame.Rect(495, 490, 10, 30),

    # ▓▓▓▓ Parte inferior ▓▓▓▓
    pygame.Rect(250, 600, 150, 10),
    pygame.Rect(600, 600, 150, 10),
    pygame.Rect(250, 600, 10, 100),
    pygame.Rect(750, 600, 10, 100),

    pygame.Rect(400, 700, 200, 10),

    # ▓▓▓▓ Entradas invisíveis (teleport) ▓▓▓▓
    pygame.Rect(0, 440, 70, 10),      # entrada esquerda
    pygame.Rect(930, 440, 70, 10),    # entrada direita
]

        self.screen = screen
    
    def draw_maze(self):
        for barrier in self.maze:
            pygame.draw.rect(self.screen, Colors.BLUE, barrier)