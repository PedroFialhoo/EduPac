import pygame

class Heart:
    def __init__(self, screen):
        self.screen = screen
        self.heart_full = pygame.image.load("images/heart.png") 
        self.heart_empty = pygame.image.load("images/heart2.png")
        self.WIDTH_HEART= 40
        self.HEIGHT_HEART = 40

    def draw(self, life, max_life=3):
        for i in range(max_life):
            x = 800 + i * (self.WIDTH_HEART + 10)
            y = 10
            if i < life:
                self.screen.blit(self.heart_full, (x, y))
            else:
                self.screen.blit(self.heart_empty, (x, y))
