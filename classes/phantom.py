import random
import pygame
import pygame_gui
import pygame_gui.ui_manager
from settings import *
import time

class Phantom:
    def __init__(self, screen):
        self.WIDTH_PHANTOM = 40
        self.HEIGHT_PHANTOM = 40
        self.x_phantom = 300
        self.y_phantom = 300
        self.color = Colors.WHITE
        self.screen = screen
        self.walking = True
        self.last_move_time = time.time()
        self.last_direction = None        
        self.image = pygame.image.load("images/phantom.png")

    def update(self):
        current_time = time.time()
        if current_time - self.last_move_time > 0.5:
            self.walk()
            self.last_move_time = current_time        
    
    def show_phantom(self):
        self.screen.blit(self.image, (self.x_phantom, self.y_phantom))
    
    def walk(self):
        opposite = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}
        directions = ['up', 'down', 'left', 'right']

        if self.last_direction:
            directions.remove(opposite[self.last_direction])

        random.shuffle(directions)

        for direction in directions:
            if direction == 'up' and self.y_phantom - 40 >= 0:
                self.y_phantom -= 40
                self.last_direction = direction
                break
            elif direction == 'down' and self.y_phantom + 40 <= self.screen.get_height() - self.HEIGHT_PHANTOM:
                self.y_phantom += 40
                self.last_direction = direction
                break
            elif direction == 'left' and self.x_phantom - 40 >= 0:
                self.x_phantom -= 40
                self.last_direction = direction
                break
            elif direction == 'right' and self.x_phantom + 40 <= self.screen.get_width() - self.WIDTH_PHANTOM:
                self.x_phantom += 40
                self.last_direction = direction
                break

            
    def damage(self):
        pass
    
    