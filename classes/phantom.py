import random
import pygame
import pygame_gui
import pygame_gui.ui_manager
from settings import *
import time
from .maze import Maze

class Phantom:
    def __init__(self, screen, maze, start_x, start_y):
        self.WIDTH_PHANTOM = 40
        self.HEIGHT_PHANTOM = 40
        self.x_phantom = start_x
        self.y_phantom = start_y
        self.color = Colors.WHITE
        self.screen = screen
        self.walking = True
        self.last_move_time = time.time()
        self.last_direction = None        
        self.image = pygame.image.load("images/phantom.png")
        self.maze = maze.maze  


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
            new_x = self.x_phantom
            new_y = self.y_phantom

            if direction == 'up':
                new_y -= 40
            elif direction == 'down':
                new_y += 40
            elif direction == 'left':
                new_x -= 40
            elif direction == 'right':
                new_x += 40

            new_rect = pygame.Rect(new_x, new_y, self.WIDTH_PHANTOM, self.HEIGHT_PHANTOM)

            # Verifica se colide com alguma parede
            collision = False
            for wall in self.maze:
                if new_rect.colliderect(wall):
                    collision = True
                    break

            if not collision:
                self.x_phantom = new_x
                self.y_phantom = new_y
                self.last_direction = direction
                break  # achou uma direção válida, para de tentar
            
    def damage(self, player, game):
        phantom = pygame.Rect(self.x_phantom, self.y_phantom, self.WIDTH_PHANTOM, self.HEIGHT_PHANTOM)
        if phantom.colliderect(player.player_rect):
            game.reset()
            player.damage()
            print('Levou Dano, vida atual', player.life)                   
            player.x_player = 480
            player.y_player = 337
    
    